import json
# difflib a library that does the job of finding the match ###
from difflib import get_close_matches


data = json.load(open("data.json"))


def get_def(word):
    word = word.lower()
    if word in data:
        return data[word]
    # if user entered "texas" this will check for "Texas" as well.
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:  # in case user enters words like USA or NATO
        return data[word.upper()]
    # cutoff return high match
    elif len(get_close_matches(word, data.keys(), cutoff=.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N for no: " %
                   get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return 'This word doesn\'t exist!, Please double check it'
        else:
            return "We didnt understand your entry."
    else:
        return 'This word doesn\'t exist!, Please double check it'


word = input('Enter a word: ')

output = get_def(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
