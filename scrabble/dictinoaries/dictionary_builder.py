# TODO find a way to clean word as a wrapper


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






