import random
import re
import os.path
from collections import defaultdict


#line is a string
def tokenize(line):
    t = line.lower()
    t = t.strip()
    #t = t.encode('utf-8').strip()
    words = re.findall(r"[\w']+|[.,!?;]", t)
    return words

class DocumentGenerator:
    def __init__(self, filename):
        textstring = ''
        self.dictionary = defaultdict(list)
        with open(filename, 'r', encoding='utf8', errors= 'ignore') as f:
            texts = f.readlines()
            textstring = ' '.join(texts)
        tokens = tokenize(textstring)
        
        for i in range(len(tokens) - 1):
            self.dictionary[tokens[i]].append(tokens[i+1])
        #print(self.dictionary)

    def generateNextWord(self, word):
        if word not in self.dictionary.keys() or len(self.dictionary[word]) == 0:
            return "."
        return random.choice(self.dictionary[word])

    def generateDocument(self, length):
        words = []
        curr = self.generateNextWord(".")
        words.append(curr)
        for i in range(length - 1):
            curr = self.generateNextWord(curr)
            if curr in "!?.,;":
                last = words.pop()
                last = last+curr
                words.append(last)
            else:
                words.append(curr)
        return " ".join(words)
