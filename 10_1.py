
def word_in_word(word1, word2):
    n = 0
    for i in word1:
        n = word2.find(i, n, len(word2))
        if n == -1:
            return "No"
    return "Yes"

print(word_in_word("dog", "ddjadssgsl"))