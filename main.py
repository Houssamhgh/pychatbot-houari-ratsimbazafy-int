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



from math import log10
import os
def TF(text : str):
    """
    Gives the number of occurrences of every word in a text

    IN:
        text (str): line of text
    OUT:
        dict_occurrence (collection): dictionary with a word as a key and the number of occurrences in a file as a value
    """


    text_list = text.split()

    list = []
    list_name = []
    for word in text_list:
        list.append([word, 0])
        list_name.append(word)

    for word in text_list:
        if word in list_name:
            for i in range(len(list)):
                if word == list[i][0]:
                    list[i][1] += 1

    return list


def IDF(directory_name : str) :

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

    final = []
    for i, j in dict_idf.items():
        final.append([i,j])

    #print("idf score: ",final)
    return final



def TF_IDF(directory_name : str) :
    IDF_values = IDF(directory_name) #introduire la valeur d'idf
    final_matrix = []
    list_words = []
    for i in range(len(IDF_values)):
        list_words.append(IDF_values[i][0])
        final_matrix.append(IDF_values[i])
    final = []
    for i in range(len(final_matrix)):
        final.append([final_matrix[i],0])
    column = 0

    for filename in os.listdir(directory_name):
        with open("./cleaned/" + filename, "r") as file:
            tf_collection = TF(file.readline())
            tf_name = []

            for i in range(len(tf_collection)):
                tf_name.append(tf_collection[i][0])
            for index in range(len(final_matrix)):

                for index in range(len(final_matrix)):
                    if list_words[index] in tf_name:
                        for i in range(len(tf_collection)):
                            if list_words[index] == tf_collection[i][0]:

                                final[index][column] = final_matrix[index][1] * tf_collection[i][1]
                        else:
                            final[index][column] = final_matrix[index][1] * 0

        column += 1
    return final

print(TF_IDF("cleaned"))


def tokenisation_question(chaine_caractere):
    new_chaine = cleaned(chaine_caractere)
    tab = tableau_chaine_caractere(new_chaine)
    return tab


def scalaire(tab1, tab2):
    resultat = sum(i * j for i, j in zip(tab1, tab2))
    return resultat


def calcul_similarite(tfidf_question, tfidf_document, correspondance_question, correspondance_liste):
    tfidf_question_aligned = [0] * len(correspondance_liste)
    for i, mot in enumerate(correspondance_liste):
        mot_str = str(mot)
        if mot_str in correspondance_question:
            index_mot_question = correspondance_question.index(mot_str)
            tfidf_question_aligned[i] = tfidf_question[index_mot_question]

    dot_product = sum(q * d for q, d in zip(tfidf_question_aligned, tfidf_document))
    norm_question = sum(q ** 2 for q in tfidf_question_aligned) ** 0.5
    norm_document = sum(d ** 2 for d in tfidf_document) ** 0.5

    if norm_question == 0 or norm_document == 0:
        return 0

    cos_sim = dot_product / (norm_question * norm_document)
    return cos_sim


def matrice_tfidf_Vecteur(directory):
    matrice = []
    tab_fichiers = list_of_files(directory)
    nb_fichiers = len(tab_fichiers)

    for i, fichier_nom in enumerate(tab_fichiers):
        with open(os.path.join(directory, fichier_nom), "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                enleve = tableau_chaine_caractere(ligne)
                mots_comptes = set()
                for mot in enleve:
                    mot = mot.strip()
                    if mot not in mots_comptes:
                        if mot not in tfidf_dict:
                            tfidf_dict[mot] = [0.0] * nb_fichiers

                        # Calcule le score TF
                        tf = TF(os.path.join(directory, fichier_nom), mot)

                        # Calcule le score IDF
                        somme = sum(presence(os.path.join(directory, tab_fichiers[j]), mot) for j in range(nb_fichiers))
                        if somme != 0:
                            score_idf = round(math.log10(nb_fichiers / somme), 3)  # vérifiée
                        else:
                            score_idf = 0.0

                        # Calcule le score TF-IDF
                        tfidf = round(tf * score_idf, 3)

                        tfidf_dict[mot][i] = tfidf
                        mots_comptes.add(mot)

    for mot in tfidf_dict:
        matrice.append(tfidf_dict[mot])

    return matrice


def scorequestion(question, matrice):
    MatriceQuestion = []

    directory = "./speeches/Cleaned/"

    question = tokenisation_question(question)

    tab_fichiers = list_of_files(directory)

    # Pour chaque mot dans la matrice (chaque ligne représente un mot)

    for i in range(len(matrice)):

        mot = matrice[i][0]

        if mot in question:

            TF = TFliste(question, mot)

            scores_idf = matrice[i][1:]

            tfidf_scores = [TF * idf for idf in scores_idf]

            MatriceQuestion.append(tfidf_scores)

        else:

            MatriceQuestion.append([0.0] * nb_fichiers)

    return MatriceQuestion




