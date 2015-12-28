"""
Use sqllite DB to store the words
"""

from functools import lru_cache
from os import path
import sqlite3

from scrabble.dictionaries.dictionary_builder import clean_word_stream

CUR_DIR = path.dirname(path.abspath(__file__))


class Dictionary(object):
    @classmethod
    def make(cls, word_stream, db_name="words.sqlite"):
        """
        :param word_stream: clean stream of words to store. case sensitive !
        :param db_name: optional db_name
        :return: an instance of this dictionary with the words stored
        """
        word_db_file_location = path.join(path.dirname(CUR_DIR), "temp", db_name)
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
            for word in clean_word_stream(word_stream):
                conn.execute('''INSERT OR IGNORE INTO Words (word) VALUES ( ? )''', (word, ))

        return cls(conn)

    def __init__(self, conn):
        self._conn = conn

    @lru_cache(2000)
    def __contains__(self, item):
        stmt = "SELECT count(*) FROM Words WHERE word = ?"
        with self._conn:
            result = self._conn.execute(stmt, (item, ))
        return result.fetchone()[0] == 1

    def __len__(self):
        stmt = "SELECT count(*) FROM Words"
        with self._conn:
            result = self._conn.execute(stmt)
        return result.fetchone()[0]

    def __del__(self):
        if self._conn:
            self._conn.close()


if __name__ == "__main__":
    dictionary = Dictionary.make(['CAT'], "test.sqlite")
    assert 'CAT' in dictionary
    assert 'CAT' in dictionary
    assert 'CAT' in dictionary
