def google_word(word):
    items = {alpha:word.count(alpha) for alpha in word}
    return items

def word_count(word):
    google = {}
    alpha = ''
    for item in word:
        alpha += (item + ' ')
    for letter in alpha.split():
        google[letter] = alpha.count(letter)

    return google


print(word_count("google"))