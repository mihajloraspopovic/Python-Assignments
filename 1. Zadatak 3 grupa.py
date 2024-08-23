def get_words_ends_with_letter(text, letter):
    sentences = text.split('.')
    result = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        words = sentence.split()
        filtered_words = [word for word in words if word.endswith(letter)]

        if filtered_words:
            result.append((tuple(filtered_words), len(filtered_words)))

    return result

text = "Print only the words that end with the chosen letter in those sentences. Example can contains one or more sentences."
letter = "s"
print(get_words_ends_with_letter(text, letter))

