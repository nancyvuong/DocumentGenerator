# DocumentGenerator

A Python program that reads in a user inputted text file and generates a new text file using the built-in Python dictionary. Each key is a word or a punctuation and each value of the keys are a list of words/punctuation that appears right after every appearance of the key word. For example for the sentence “I see a dog and a cat”, the corresponding value of the “a” key is a list that contains “dog” and “cat”. The generator first chooses a dictionary key (word) at random to include in the new text file. Then it selects a random word from the corresponding list of that key and repeats until the new document has reached the desired word count.

# Instructions
* Have a non-empty text file ready.
* Run main.py and enter in the file path and filename of your text file as well as how many words do you want your new generated text file to be.
* This program will then generate a new text file.

