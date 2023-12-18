# HOUARI Houssam - RATSIMBAZAFY Armence - INT4

import os
import string


# gets the names of the presidents out of the files name
def last_name_file(s, docu):
    last_names = []

    for file in docu:

        name_without_digits = ''.join(char for char in file if not char.isdigit())

        if len(name_without_digits) >= 15:
            last_name = name_without_digits[11:-4]
            last_names.append(last_name)

    return last_names


# removal of every doublon
def remove_dupli(docu):
    nodupli = []

    for i in docu:
        if i not in nodupli:
            nodupli.append(i)

    return nodupli


# association of every president's first and last's name
def associate_names(first_names, last_names, result):
    for i in range(len(first_names)):
        full_name = first_names[i] + " " + last_names[i]
        result.append(full_name)
    return result


# transform every uppercase into lower case character
def lowercase(text):
    return ''.join(lowercased_char for lowercased_char in text.lower())


# removes every ponctuation in the text
def no_punctuation(text):
    allowed_chars = set(string.ascii_letters + string.digits + 'àâæçéèêëîïôœùûüÿ')

    text_without_punctuation = ''.join(char if char in allowed_chars else ' ' for char in text)
    return text_without_punctuation


speeches = "speeches-20231123"
info = os.listdir(speeches)

presidents = []
l_names = []
f_names = ["Jacques", "Valéry", "François", "Emmanuel", "François", "Nicolas"]

l_names = last_name_file(l_names, info)
l_names = remove_dupli(l_names)

print(associate_names(f_names, l_names, presidents))


# give all the texts without no punctuations and with uppercase
def cleaned_text(text):
    for file in info:
        with open("speeches-20231123/" + file, "r", encoding="utf-8") as f1:
            content = f1.read()

        cleaned_content = no_punctuation(lowercase(content))

        with open("cleaned_" + file, "w") as f2:
            f2.write(cleaned_content)
        print(cleaned_content, "\n")
speeches="cleaned"
cleaned_text(speeches)


from math import log10
import os
def TF(text : str) -> dict:
    """
    Gives the number of occurrences of every word in a text

    IN:
        text (str): line of text
    OUT:
        dict_occurrence (collection): dictionary with a word as a key and the number of occurrences in a file as a value
    """
    dict_occurrence = {}
    text_list = text.split(" ")
    for word in text_list:
        if word in dict_occurrence.keys():
            dict_occurrence[word] += 1
        else:
            dict_occurrence[word] = 1
    return dict_occurrence


def IDF(directory_name : str) -> dict:

    mattress = []
    for filename in os.listdir(directory_name):
        list_words = []
        file = open(directory_name + "/" + filename, "r")
        line = file.readline().split(" ")
        for word in line:
            if word not in list_words:
                list_words.append(word)
        mattress.append(list_words)
        file.close()


    dict_idf = {}
    for list in mattress:
        for word in list:
            if word in dict_idf.keys():
                dict_idf[word] += 1
            else:
                dict_idf[word] = 1
    for value in dict_idf.keys():
        dict_idf[value] = log10(len(mattress) / dict_idf[value])  # gives a high value to rare words and a low value to common words
    print("ok",dict_idf)



def TF_IDF(directory_name : str) -> tuple:
    IDF_values = IDF(directory_name)
    final_matrix = []
    list_words = []
    for word in IDF_values.keys():
        list_words.append(word)
        final_matrix.append([IDF_values[word]])

    nb_file = 1
    for line in final_matrix:
        for filename in os.listdir(directory_name)[1:]:
            line.append(line[-1])
            nb_file += 1

    column = 0
    for filename in os.listdir(directory_name):
        with open("./cleaned/" + filename, "r", encoding="utf-8") as file:
            tf_collection = TF(file.readline())
            for index in range(len(list_words)):
                if list_words[index] in tf_collection.keys():
                    final_matrix[index][column] *= tf_collection[
                        list_words[index]]  # multiplication of IDF by the TF of the word

                else:
                    final_matrix[index][column] *= 0

        column += 1
    print(final_matrix, list_words)





#Fonction 6



#cleaned_content = no_punctuation(lowercase(content))
print(IDF("./cleaned"))
cleaned = 'cleaned'