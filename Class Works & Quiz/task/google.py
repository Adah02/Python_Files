def google_word(word):
    items = {alpha.lower():word.lower().count(alpha) for alpha in word}
    return items

def word_count(word):
    google = {}
    alpha = ''
    for item in word:
        alpha += item
    for letter in alpha:
        google[letter.lower()] = alpha.lower().count(letter)

    return google


print('First method:',google_word("GOogle"))
print('Second method:',word_count("Google"))