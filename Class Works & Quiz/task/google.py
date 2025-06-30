def google_word(word):
    items = {alpha:word.count(alpha) for alpha in word}
    return items

def word_count(word):
    google = []
    for letter in sorted(word):
        google.append(f"{letter}:{word.count(letter)}")

    dict = google
    return dict




print(word_count("google"))