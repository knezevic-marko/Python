import json

text = """Chose one option:
0) Quit
1) Create
2) Read All
3) Read meanings for 1 word
4) Delete word
5) Delete meaning
6) Update meaning
Input:
"""

with open('dictionary.json', 'r') as openfile:
    dictionary = json.load(openfile)
print(dictionary)

while True:
    option = input(text)

    if option == "0":
        print("QUIT!")
        with open("dictionary.json", "w") as outfile:
            outfile.write(json.dumps(dictionary, indent=4))
        quit()

    elif option == "1":
        k = input("Enter word: ")
        v = input("Enter meaning: ")
        if k not in dictionary:
            dictionary[k] = [v]
        else:
            dictionary[k].append(v)

    elif option == "2":
        print(dictionary)

    elif option == "3":
        word = input("Enter word: ")
        if word in dictionary:
            print(dictionary[word])
        else:
            print("ERROR! Word does not exist!")

    elif option == "4":
        word = input("Enter word for delete: ")
        if word in dictionary:
            del dictionary[word]
            print("Successfuly deleted: " + word)
        else:
            print("ERROR! Word does not exist!")

    elif option == "5":
        word = input("Enter word for update: ")
        if word not in dictionary:
            print("ERROR! Word does not exist!")
            continue
        word_meanings = dictionary[word]
        for i, e in enumerate(word_meanings):
            print(str(i) + ": " + e)
        i = int(input("Enter index to be deleted: "))
        word_meanings.pop(i)
        print("Successfully updated word: " + word)

    elif option == "6":
        word = input("Enter word for update: ")
        if word not in dictionary:
            print("ERROR! Word does not exist!")
            continue
        word_meanings = dictionary[word]
        for i, e in enumerate(word_meanings):
            print(str(i) + ": " + e)
        i = int(input("Enter index to be changed: "))
        w = input("Enter new value: ")
        word_meanings[i] = w
        dictionary[word] = word_meanings
        print("Successfully updated word: " + word)