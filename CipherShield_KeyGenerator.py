#!/usr/bin/python3

import string
import random

# Generate a random symmetric key
random_string = string.ascii_letters + string.digits + string.punctuation + " "
random_list = list(random_string)
random.shuffle(random_list)
key = ''.join(random_list)  # Join or Convert the list into a string

# Print the symmetric key
print(f"Your symmetric key is: '{key}'\n")

# Save the key to a file
try:
    with open("symmetric_key.txt", "w") as file:
        file.write(key)
    print("Saved to 'symmetric_key.txt'.")
except IOError as e:
    print(f"Error saving to file: {e}")

# Print instructions for the user
print("\nThis program generates a random key every time, so make sure not to lose this key.")
print("Otherwise, you will not be able to decrypt your message.")
