# TODO реализовать функцию
def get_sentences_list(text):
    sentences = text.split('.')
    cleaned_sentences = []
    for sentence in sentences:
        cleaned_sentence = sentence.strip()
        if cleaned_sentence:
            cleaned_sentences.append(cleaned_sentence)
    return cleaned_sentences


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
