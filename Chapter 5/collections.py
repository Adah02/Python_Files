from collections import Counter

def word_count(sentence):
    words = Counter(sentence.split())
    for word, count in sorted(words.items()):
        print(f'{word>12} {count}')


sentence = input("Enter a sentence: ")