#HOUARI Houssam - RATSIMBAZAFY Armence - INT4

import os
import string


#opening and get access to all the president's speeches
def list_of_files(directory, extension):
    files_names = []

    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
        return files_names
# Call of the function
directory = "./speeches-20231123"
files_names = list_of_files(directory, "txt")
print(list_of_files("./speeches-20231123", "txt")


# gets the names of the presidents out of the files name
def last_name_file(docu):
    last_names = []

    for file in docu:

        name_without_digits = ''.join(char for char in file if not char.isdigit())

        if len(name_without_digits) >= 15:
            last_names = name_without_digits[11:-4]
            last_names.append(last_name)

    return last_names
print(last_name_file(last_names))


#removal of every doublon
def remove_dupli(docu):

    nodupli = []

    for i in docu:
        if i not in nodupli:
            nodupli.append(i)

    return nodupli
print(remove_dupli())


#association of every president's first and last's name
def associate_names(first_names, last_names, result):
    for i in range(len(first_names)):
        full_name = first_names[i] + " " + last_names[i]
        result.append(full_name)
    return result
print(associate_names())


#transform every uppercase into lower case character
def lowercase(text):
    return ''.join(lowercased_char for lowercased_char in text.lower())
print(lowercase(text))



#removes every ponctuation in the text
def no_punctuation(text):
    allowed_chars = set(string.ascii_letters + string.digits + 'àâæçéèêëîïôœùûüÿ')

    text_without_punctuation = ''.join(char if char in allowed_chars else ' ' for char in text)
    return text_without_punctuation


#counts the occurrence of a word in a text
def term_fre(x):
    terms = {}
    for word in x:
        i = 0
        while i < len(terms) and word != terms[i][0]:
            i += 1
        if i < len(terms):
            terms[i][1] += 1
    return terms
print(term_fre()) #we weren't sure of how to write the analysis of all the files

speeches = "speeches-20231123"
info = os.listdir(speeches)

presidents = []
l_names = []
f_names = ["Jacques", "Valéry", "François", "Emmanuel", "François", "Nicolas"]


l_names = last_name_file(l_names)
l_names = remove_dupli(l_names)

print(associate_names(f_names, l_names, presidents))

for file in info:
    with open("speeches-20231123/" + file, "r", encoding="utf-8") as f1:
        content = f1.read()

    cleaned_content = no_punctuation(lowercase(content))

    with open("cleaned_" + file, "w") as f2:
        f2.write(cleaned_content)


#start of tf-idf
#counts the occurrence of a word in a text
def term_fre(text):
    terms = {}
    for word in text:
        i = 0
        while i < len(terms) and word != terms[i][0]:
            i += 1
        if i < len(terms):
            terms[i][1] += 1
    return terms
print(term_fre()) #we weren't sure of how to write the analysis of all the files

#we tried to search for some methods on the internet on how to find the idf, but yeah


# definition of the text to analyze
directory = "./speeches-20231123"
files_names = list_of_files(directory, "txt")
print(list_of_files("./speeches-20231123"',' "txt")
text = "list_of_files("./new_speeches-20231123", "txt")"

# Séparez le texte en tokens à l'aide de word_tokenize


#afichage des tokens et score idf de chaque mots sous formes de dictionnaires
for token, score in tf_scores.items():
    print(f"Token: {token}, TF-IDF: {score}")
# and we stopped here because we couldn't go further 
