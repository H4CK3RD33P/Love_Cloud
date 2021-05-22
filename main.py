#MODULE IMPORTS
import pyfiglet
import wordcloud
import numpy as np
import matplotlib.pyplot as plt
import os

#USER INTERACTION

print(pyfiglet.figlet_format("Love Cloud",font="slant"))
print(pyfiglet.figlet_format("By Subhodeep Sarkar",font="digital"))

#TEXT GENERATION

word_list = []
print("Enter all the words you want to : )")
print("To finish, type X and hit enter")

counter = 0

while True:
    word = input(f"{counter+1}: ")
    if word == "X":
        break
    word_list.append(word)
    counter+=1

if counter==1:
    print(f"Added {counter} word")
else:
    print(f"Added {counter} words")

text = " ".join(word_list)

path = os.getcwd()
font_path = os.path.join(path,"hb.ttf")
mask_path = os.path.join(path,"romeo.jpg")


