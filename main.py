
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
        print(cleaned_content, "\n")