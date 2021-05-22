#MODULE IMPORTS
import pyfiglet
import wordcloud
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

#USER INTERACTION

print(pyfiglet.figlet_format("Love Cloud",font="slant"))
print(pyfiglet.figlet_format("By Subhodeep Sarkar",font="digital"))

#TEXT GENERATION

word_list = []
print("Enter all the words you want to :)")
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

print("Please wait while your Love Cloud is being created! :)")

text = " ".join(word_list)

path = os.getcwd()
font_path = os.path.join(path,"hb.ttf")
mask_path = os.path.join(path,"romeo.jpg")

mask_image = np.array(Image.open(mask_path))

wc = wordcloud.WordCloud(
                   mask=mask_image, background_color="white",
                   max_words=1000, max_font_size=256, min_font_size=5,colormap='rainbow',
                   random_state=42, width=600,
                   height=400,contour_width=0.2, repeat=True,font_path=font_path).generate(text)

plt.imshow(wc,interpolation='bilinear')
plt.title('Love makes life perfect!')
plt.axis('off')
plt.show()