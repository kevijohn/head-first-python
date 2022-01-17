# Author: Kevin Johnson
# Created date: JAN 17 2022

vowels = ['a', 'e', 'i', 'o', 'u']
found = []
word = input("Type a word to search for vowels: ")
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)