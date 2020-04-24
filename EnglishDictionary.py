import json                                     #import Libraries
from difflib import get_close_matches

data = json.load(open("data.json"))             #store .json file content to data

def translate(w):
    w = w.lower()                               #convert uppercase word to lowercase
    if w in data:                               #check has inside the .json and return it
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
while True:
    word = input("Enter word: ")    #get user input
    output = translate(word)        #call the function
    if type(output) == list:        #if type is list, list down the content one by one
        for item in output:
            print("> " + item)
    else:
        print(output)

