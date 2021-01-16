import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")


data = pd.read_csv(r"/home/van/Documents/matplotlib_corey_shafer/data/data.csv")
ids = data["Responder_id"]
lang_reponses = data["LanguagesWorkedWith"]

# intantiate counter to count how many times a language appear
language_counter = Counter()

for reponse in lang_reponses:
    language_counter.update(reponse.split(";"))

# read the info in list or in array-like format to input in plot
languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# to show the most popularity at the top of chart
languages.reverse()
popularity.reverse()

# barh is stand for horizontal bar (having too many value)
plt.barh(languages, popularity)

# parameter in barh is the same but the label x is now y
plt.title("Most Popular Languages")
plt.xlabel("People Who uses")

plt.tight_layout()

plt.show()
