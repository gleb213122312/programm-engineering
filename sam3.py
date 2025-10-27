import re

text = open("input_4.txt", encoding="utf-8").read()
letters = re.findall(r"[A-Za-z]", text)
words = re.findall(r"[A-Za-z]+", text)
lines = text.splitlines()

print("Input file contains:")
print(len(letters), "letters")
print(len(words), "words")
print(len(lines), "lines")