import json
from difflib import get_close_matches

def translate(word):
    data = json.load(open("dictionary_data.json"))
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean %s instead?" %get_close_matches(word, data.keys())[0])
        decide = input("Press 'y' for yes or 'n' for no: ")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("Invalid Input")
        else:
            return("You have entered wrong input please enter just y or n: ")
    else:
        print("Invalid Input")

if __name__ == "__main__":
    x = "y"
    while x == "y":
        word = input("\nEnter the word you want to search: ")
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
        x = input("\nEnter 'y' to seach again or press any other key to end session: ") 
