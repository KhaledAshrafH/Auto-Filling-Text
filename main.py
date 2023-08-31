import nltk
import re
from tkinter import *
from PIL import Image, ImageTk
from AutoFillingGeneral import AutoFilling as generalAF  # (For Bigrams)


# Reading the dataset from one file contains all text files (English & Arabic)
def read_corpus(file_path):
    file = open(file_path, 'r', encoding="utf-8")
    corpus_ = file.read()
    file.close()
    return corpus_


# Auto Filling Text Class by Trigrams Model
class AutoFilling:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.trigrams = {}

    # Tokenization process for text
    def tokenize(self):
        print('Tokenization process running now.')
        self.text = re.sub(r'/W', '', self.text)
        self.tokens = nltk.word_tokenize(self.text)

    # Generate all trigrams and count each word after it
    def generate_trigrams(self):
        if len(self.tokens) > 0:
            print('generating trigrams process running now.')
            for i in range(len(self.tokens)-2):  # take 2 words
                seq_list = self.tokens[i:i+2]
                seq = ""
                for word in seq_list:
                    seq += word
                    seq += " "
                seq = seq.strip()

                # map each 2 words with frequency of third word
                if seq in self.trigrams:
                    self.trigrams[seq][self.tokens[i + 2]] = self.trigrams[seq].get(self.tokens[i + 2], 0) + 1
                else:
                    self.trigrams[seq] = {}
                    self.trigrams[seq][self.tokens[i + 2]] = 1

        # in case of calling this function without tokenization
        else:
            print('You should tokenize the text first! tokenization process running now.')
            self.tokenize()
            self.generate_trigrams()

    # Calculate the probability of each trigram
    def calculate_prob(self):
        if len(self.trigrams) > 0:
            print('probability calculations process running now.')
            for prev_seq in self.trigrams:
                total_prev_cnt = 0.0
                for key in self.trigrams[prev_seq].keys():
                    total_prev_cnt += self.trigrams[prev_seq][key]

                for key in self.trigrams[prev_seq].keys():
                    self.trigrams[prev_seq][key] /= total_prev_cnt
                self.trigrams[prev_seq] = sorted(self.trigrams[prev_seq].items(), key=lambda x: (x[1], x[0]),
                                                 reverse=True)

        # in case of Trigrams not Generated yet!
        else:
            print('You should generating trigrams first!')
            self.generate_trigrams()
            self.calculate_prob()

    # take input and suggest next word after it
    def suggest_next_trigrams(self, str_input):
        res = []
        str_input.strip()
        list_input = str_input.split(" ")
        if len(list_input) >= 2:
            last_2_words = (list_input[-2] + " " + list_input[-1])
            if last_2_words in self.trigrams:
                for i in range(len(self.trigrams[last_2_words])):
                    predicted = self.trigrams[last_2_words][i]
                    res.append(predicted[0])
                    if i == 9:  # to limit number os suggestions
                        break
        else:
            pass
        return res


# --------------------------------The Main---------------------------------------

# Reading English dataset
corpus = read_corpus('10_million_words.txt')  # this file contains 10 million words from 14441 articles

AutoFillingObj = AutoFilling(corpus)  # Generate Trigrams
AutoFillingObj.tokenize()
AutoFillingObj.generate_trigrams()
AutoFillingObj.calculate_prob()

AutoFillingObjBi = generalAF(corpus, 2)  # Generate Bigrams
AutoFillingObjBi.tokenize()
AutoFillingObjBi.generate_ngrams()
AutoFillingObjBi.calculate_prob()

# Reading Arabic dataset (Extra)
corpusAr = read_corpus('2_million_arabic_words.txt')  # this file contains 2 million words from 6499 articles

AutoFillingObjAr = AutoFilling(corpusAr)  # Generate Trigrams
AutoFillingObjAr.tokenize()
AutoFillingObjAr.generate_trigrams()
AutoFillingObjAr.calculate_prob()

AutoFillingObjArBi = generalAF(corpusAr, 2)  # Generate Bigrams
AutoFillingObjArBi.tokenize()
AutoFillingObjArBi.generate_ngrams()
AutoFillingObjArBi.calculate_prob()


# # --------------------------------GUI------------------------------------------

# Track if input entered and suggest result
def auto_filling_suggest(*args):
    # get input from the entry & delete the list box
    str_input = str_entry.get()
    list_box.delete(0, END)
    try:
        input_str = str_input.strip()
        my_list = []
        # if their at least one word
        if len(input_str) > 0:

            # check if english text
            if 'a' <= input_str[0] <= "z" or 'A' <= input_str[0] <= 'Z':
                if ' ' not in input_str:  # if one word apply bigrams
                    my_list = AutoFillingObjBi.suggest_next_ngrams(input_str)
                else:  # if multiple words apply trigrams
                    my_list = AutoFillingObj.suggest_next_trigrams(input_str)

            # check if arabic text
            else:
                if ' ' not in input_str:  # if one word apply bigrams
                    my_list = AutoFillingObjArBi.suggest_next_ngrams(input_str)
                else:  # if multiple words apply trigrams
                    my_list = AutoFillingObjAr.suggest_next_trigrams(input_str)
        else:
            pass

        # show list of suggestions
        for element in my_list:
            element = input_str + " " + element
            list_box.insert(END, element)
            list_box.place(height=9, width=55)
            list_box.listbox_is_showing = True
            list_box.pack(pady=3)
    except KeyError:
        pass


# Select one of the suggestion List
def select_result(event):
    event = event.widget
    text_input.set(event.get(int(event.curselection()[0])))


# these Functions for focus on and out the input entry
def on_enter(e):
    str_entry['border'] = 2


def on_leave(e):
    str_entry['border'] = 0


# Starting of generating Gui
AutoFillingWindow = Tk()
AutoFillingWindow.title("Auto Filling App")
AutoFillingWindow.geometry('650x350')
AutoFillingWindow.resizable(False, False)

img_temp = Image.open("google.png")
img_temp = img_temp.resize((240, 90))
img_temp = ImageTk.PhotoImage(img_temp)
img_label = Label(image=img_temp)
img_label.pack(pady=15)

text_input = StringVar()
str_entry = Entry(AutoFillingWindow, font="Arial", textvariable=text_input, width=41, border=0)
str_entry.pack()
str_entry.bind("<FocusIn>", on_enter)
str_entry.bind("<FocusOut>", on_leave)

list_box = Listbox(AutoFillingWindow, height=9, width=75, border=0)
list_box.place_forget()
list_box.listbox_is_showing = False

list_box.bind('<<ListboxSelect>>', select_result)
text_input.trace('w', auto_filling_suggest)

AutoFillingWindow.mainloop()

# -----------------This code to merge all files in one file--------------------

# # find all the txt files in the dataset folder
# import os
# inputs = []
# for file in os.listdir("../data"):
#     if file.endswith(".txt"):
#         inputs.append(os.path.join("../data/", file))
#
# # concatenate all txt files in a one file
# str = ""
# for fname in inputs:
#     print(fname)
#     with open(fname, 'r', encoding="utf-8") as infile:
#         str += infile.read()
#         str += '\n'
#         l_var = len(str.split())
#         print(l_var)
#         if l_var>10000000: break
#
# file = open('2_million_arabic_words.txt', 'w', encoding="utf-8")
# file.write(str)
# file.close()
# ----------------------------------------------------------------------------
