import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))

while (1):
    word = input("Enter a word")
    word = word.lower()
    best_ratio = 0.8
    list_words = []
    for w in data.keys():
        if SequenceMatcher(None, word, w).ratio() >= best_ratio:
            # print(w)
            list_words.append(w)

    list_words = get_close_matches(word, list_words)

    if len(list_words) > 0:
        print(list_words)
        print((data[list_words[0]][0]))
    else:
        print("Word not present in the dictionary")

    option = input("Do you wish to continue? Y/N")
    if option.lower() == 'n':
        break
