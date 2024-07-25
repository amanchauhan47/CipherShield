#!/usr/bin/python3

import string
import random

def encrypt_message(plain_text, chars_list, key):
    if len(chars_list) == len(key):
        cipher_text = ""
        for letter in plain_text:
            if letter in chars_list:
                index = chars_list.index(letter)
                cipher_text += key[index]
            else:
                cipher_text += letter  # If the character is not in chars_list, keep it unchanged
        return cipher_text
    else:
        print("Invalid key length.")

chars_list = string.ascii_letters + string.digits + string.punctuation + " "

plain_txt = input("Enter the message to encrypt: ")
key = input("Enter the key to encrypt the message: ")

cipher = encrypt_message(plain_txt, chars_list, key)

print(f"\nOriginal message:  {plain_txt}")
print(f"Encrypted message: {cipher}")

