#!/usr/bin/python3

import string
import random

def decrypt_message(cipher_text, chars_list, key):
    if len(chars_list) == len(key):
        plain_text = ""
        for letter in cipher_text:
            if letter in key:
                index = key.index(letter)
                plain_text += chars_list[index]
            else:
                plain_text += letter  # If the character is not in key, keep it unchanged
        return plain_text
    else:
        print("Invalid key length.")
        exit()


chars_list = string.ascii_letters + string.digits + string.punctuation + " "

cipher = input("Enter the cipher to decrypt: ")
key = input("Enter the key to decrypt the message: ")

plain_txt = decrypt_message(cipher, chars_list, key)

print(f"\nEncrypted message: {cipher}")
print(f"Original message:  {plain_txt}")


