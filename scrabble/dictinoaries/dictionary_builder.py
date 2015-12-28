

def clean_word_stream(word_stream):
    for word in word_stream:
        if not word:
            continue
        word = str(word).strip().upper()
        if not word.isalpha():
            continue
        yield word


def build_model(file_name, make_func):
    with open(file_name) as f:
        model = make_func(clean_word_stream(f))
    return model


if __name__ == '__main__':
    from scrubble.dictinoaries.dictionary_2_sqllite import Dictionary
    file_name = 'data/huge.txt'
    m = build_model(file_name, Dictionary.make)
    assert 'CAT' in m





