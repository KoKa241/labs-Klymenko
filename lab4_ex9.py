def vowels_filter(word):
    result = ""
    vowels = "AEIOU"
    word = word.upper()
    for letter in word:
        if letter in vowels:
            continue
        else:
            result += letter
    for letter in result:
        print(letter)


word = input("Enter a word: ")
vowels_filter(word)
