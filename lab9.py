def caesar_cipher(text, shift):

    cipher = ''
    for char in text:
        is_upper = char.isupper()

        if not char.isalpha():
            cipher += char
            continue

        char_upper = char.upper()
        code = ord(char_upper) + shift

        if code > ord('Z'):
            code -= 26

        if is_upper:
            cipher += chr(code)
        else:
            cipher += chr(code + 32)
    return cipher


def main():
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (1-25): "))

    if not 1 <= shift <= 25:
        print("Invalid shift value.")
        return

    cipher = caesar_cipher(text, shift)
    print(cipher)


if __name__ == "__main__":
    main()
