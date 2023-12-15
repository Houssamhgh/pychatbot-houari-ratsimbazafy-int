
import os
import string

def last_name_file(s, docu):
    last_names = []

    for file in docu:

        name_without_digits = ''.join(char for char in file if not char.isdigit())

        if len(name_without_digits) >= 15:
            last_name = name_without_digits[11:-4]
            last_names.append(last_name)

    return last_names

def remove_dupli(docu):
    nodupli = []

    for i in docu:
        if i not in nodupli:
            nodupli.append(i)

    return nodupli

def associate_names(first_names, last_names, result):
    for i in range(len(first_names)):
        full_name = first_names[i] + " " + last_names[i]
        result.append(full_name)
    return result

def lowercase(text):
    return ''.join(lowercased_char for lowercased_char in text.lower())


def no_punctuation(text):
    allowed_chars = set(string.ascii_letters + string.digits + 'àâæçéèêëîïôœùûüÿ')

    text_without_punctuation = ''.join(char if char in allowed_chars else ' ' for char in text)
    return text_without_punctuation

def tfre(x):
    terms = {}
    for word in x:
        i = 0
        while i < len(terms) and word != terms[i][0]:
            i += 1
        if i < len(terms):
            terms[i][1] += 1
    return terms

speeches = "speeches-20231123"
info = os.listdir(speeches)

presidents = []
l_names =[]
f_names =["Jacques","Valéry","François","Emmanuel","François","Nicolas"]


l_names = last_name_file(l_names, info)
l_names = remove_dupli(l_names)

print(associate_names(f_names, l_names, presidents))

for file in info:
    with open("speeches-20231123/" + file, "r", encoding="utf-8") as f1:
        content = f1.read()


    cleaned_content = no_punctuation(lowercase(content))

    with open("cleaned_" + file, "w") as f2:
        f2.write(cleaned_content)
        print(cleaned_content,"\n")

import re
from contextlib import redirect_stdout
from io import StringIO

def token_to_sentence(str):
    f = StringIO()
    with redirect_stdout(f):
        regex_of_sentence = re.findall('([\w\s]{0,})[^\w\s]', str)
        regex_of_sentence = [x for x in regex_of_sentence if x != '']
        for i in regex_of_sentence:
            print(i)
        first_step_to_sentence = (f.getvalue()).split('\n')
    g = StringIO()
    with redirect_stdout(g):
        for i in first_step_to_sentence:
            try:
                regex_to_clear_sentence = re.search('\s([\w\s]{0,})', i)
                print(regex_to_clear_sentence.group(1))
            except:
                print(i)
        sentence = (g.getvalue()).split('\n')
    return sentence

def token_to_words(str):
    f = StringIO()
    with redirect_stdout(f):
        for i in str:
            regex_of_word = re.findall('([\w]{0,})', i)
            regex_of_word = [x for x in regex_of_word if x != '']
            for word in regex_of_word:
                print(regex_of_word)
        words = (f.getvalue()).split('\n')

def convert_to_words(str):
    sentences = token_to_sentence(str)
    for i in sentences:
        word = token_to_words(i)
    return word

def compare_list_of_words__to_another_list_of_words(from_strA, to_strB):
        fromA = list(set(from_strA))
        for word_to_match in fromA:
            totalB = len(to_strB)
            number_of_match = (to_strB).count(word_to_match)
            data = str((((to_strB).count(word_to_match))/totalB)*100)
            print('words: -- ' + word_to_match + ' --' + '\n'
            '       number of match    : ' + number_of_match + ' from ' + str(totalB) + '\n'
            '       percent of match   : ' + data + ' percent')





from tkinter import *
import datetime

root_of_chatbot = Tk()

def sending():
    sending = "Me : " +e.get()
    txt.insert(END, "\n"+sending)

    if 'Bonjour' or 'Salut' or 'Bonsoir' or 'Coucou' in e.get():
        txt.insert(END, "\n"+"Your CHATBOT : Salut!, Comment pourrais-je t'aider ? ")


    e.delete(0, END)



txt = Text(root_of_chatbot)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root_of_chatbot, width=100)
e.grid(row=1, column=0)
Send = Button(root_of_chatbot, text="Send",command=sending).grid(row=1, column=1)
root_of_chatbot.title("Your CHATBOT")
root_of_chatbot.mainloop()
