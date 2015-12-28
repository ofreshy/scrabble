# Use sqllite DB to store the words
from os import path
import sqlite3

CUR_DIR = path.dirname(path.abspath(__file__))


class Dictionary(object):
    @classmethod
    def make(cls, word_stream):
        """
        :param word_stream: clean stream of words to store. case sensitive !
        :return: an instance of this dictionary with the words stored
        """
        word_db_file_location = path.join(path.dirname(CUR_DIR), "temp", "words.sqlite")
        conn = sqlite3.connect(word_db_file_location)
        with conn:
            # Unique will create an index on the column as per
            # https://www.sqlite.org/lang_createtable.html
            conn.executescript('''
                DROP TABLE IF EXISTS Words;
                CREATE TABLE Words (
                    word   TEXT UNIQUE
                );
            ''')
            for word in word_stream:
                conn.execute('''INSERT OR IGNORE INTO Words (word) VALUES ( ? )''', (word, ))

        return cls(conn)

    def __init__(self, conn):
        self._conn = conn

    def __contains__(self, item):
        stmt = "SELECT count(*) FROM Words WHERE word = ?"
        with self._conn:
            result = self._conn.execute(stmt, (item, ))
        return result.fetchone()[0] == 1


# TODO move this to a test class
def test():
    words = ['CAT', 'I', 'TOMORROW']

    model = Dictionary.make(words)

    assert 'CAT' in model
    assert 'I' in model
    assert 'TOMORROW' in model
    assert 'C' not in model

if __name__ == '__main__':
    test()