def vowels_filter_upgrade(word):
    vowels = "AEIOU"
    word = word.upper()
    word_without_vowels = ""
    for letter in word:
        if letter == vowels[0]:
            continue
        elif letter == vowels[1]:
            continue
        elif letter == vowels[2]:
            continue
        elif letter == vowels[3]:
            continue
        elif letter == vowels[4]:
            continue
        else:
            word_without_vowels += letter
    print(word_without_vowels)


word = input("Enter a word: ")
vowels_filter_upgrade(word)
