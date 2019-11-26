from DocumentGenerator import *

if __name__ == '__main__':
    fp = input("Enter filename: ")
    dc = DocumentGenerator(fp)
    while dc == None:
        fp = input("Enter another filename: ")
        dc = DocumentGenerator(fp)
    file1 = open("generated.txt", "w")
    wc = int(input("Enter word count: "))
    file1.write(dc.generateDocument(wc))
    file1.close()
