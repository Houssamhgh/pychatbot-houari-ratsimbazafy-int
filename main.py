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
        list[i]: list with a word as a key and the number of occurrences in a file as a value
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



def TF_IDF(directory_name):
    # Obtaining the values of TF_IDF
    idf_values = IDF(directory_name)
    idf_dict = dict(idf_values)

    # Dictionnary to stock the total frequency of each word
    total_tf = {}

    # Go through each file and calculate TF frequencies
    for filename in os.listdir(directory_name):
        file_path = os.path.join(directory_name, filename)
        with open(file_path, 'r') as file:
            content = file.read()
            tf_scores = TF(content)

            # Add the TF frequencies for each word
            for word, count in tf_scores:
                if word in total_tf:
                    total_tf[word] += count
                else:
                    total_tf[word] = count

    #Calculate TF-IDF scores by multiplying cumulative TF by IDF
    tf_idf_scores = [[word, tf * idf_dict.get(word, 0)] for word, tf in total_tf.items()]

    return tf_idf_scores

# HOUARI Houssam - RATSIMBAZAFY Armence - INT4----------------------PART II---------------------------------------------------
def tokenization_of_question(qst):
    """Takes a question as a string in parameter and returns a cleaned version of it as a list of words (lowercase and with no punctuation), thus tokenizing the question."""
    qst = str(qst)
    txt = qst

    txt1 = ''
    punc = (',', "'", ";", ':', '!', '?', '-', '_', '(', ')', '/', '.')#removing ponctuation from the questions

    for word in txt:
        for char in word:
            if char not in punc:
                txt1 += char
            else:
                txt1 += ' '
    txt = txt1

    # putting the letters into lower case
    text1 = ''
    for word in txt:
        for letter in word:
            if 64 < ord(letter) and ord(letter) < 91 :
                text1 += chr(ord(letter) + 32)
            else:
                text1 += letter
    txt = text1
    lquest = txt.split()

    return lquest




import os


tfidf_dict = {}  # Initialize the tfidf_dict


def tableau_chaine_caractere(ligne):
    # devide the lines by using spaces between each word
    return ligne.split()

def tableau_chaine_caractere(ligne):
    # same here
    return ligne.split()



def TFliste(question, mot):
    # Calculate the frequency of a word in the question
    mots = question.split()
    return mots.count(mot) / len(mots)

def list_of_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]



def scalaire(tab1, tab2):
    resultat = sum(i * j for i, j in zip(tab1, tab2))
    return resultat

def calculate_similarity(tfidf_question, tfidf_document, correspondance_question, correspondance_list):  #Calculating similarity
    tfidf_question_aligned = [0] * len(correspondance_list)
    for i, mot in enumerate(correspondance_list):
        mot_str = str(mot)
        if mot_str in correspondance_question:
            index_mot_question = correspondance_question.index(mot_str)
            tfidf_question_aligned[i] = tfidf_question[index_mot_question]
#calculate the similarities by using the cosin
    dot_product = sum(q * d for q, d in zip(tfidf_question_aligned, tfidf_document))
    norm_question = sum(q ** 2 for q in tfidf_question_aligned) ** 0.5
    norm_document = sum(d ** 2 for d in tfidf_document) ** 0.5

    if norm_question == 0 or norm_document == 0:
        return 0

    cos_sim = dot_product / (norm_question * norm_document)
    return cos_sim
#we have troubles runing this function in our program
def matrice_tfidf_Vecteur(directory): #fiding the vector of the matrix tf idf
    tfidf_matrix = {}
    for fichier_nom in os.listdir(directory):
        file_path = os.path.join(directory, fichier_nom) #
        with open(file_path, 'r') as file:
            content = file.read()
            tfidf_matrix[fichier_nom] = TF(content)
    return tfidf_matrix

#also this function

def trouver_phrase_dans_document(mots_question, document):
    with open(document, 'r') as file:
        content = file.read()

    for mot in mots_question:
        start_index = content.find(mot)
        if start_index != -1:
            start_phrase = content.rfind('.', 0, start_index) + 1
            end_phrase = content.find('.', start_index)
            return content[start_phrase:end_phrase].strip()

    return "Mot non trouvé dans le document."


def obtenir_chemin_fichier_pertinent(mots_question):

    import os
    import random

    dossier_cleaned = './cleaned'  # Remplacement par le chemin réel du dossier
    fichiers = os.listdir(dossier_cleaned)
    fichiers = [f for f in fichiers if os.path.isfile(os.path.join(dossier_cleaned, f))]

    if fichiers:
        fichier_choisi = random.choice(fichiers)
        chemin_fichier_pertinent = os.path.join(dossier_cleaned, fichier_choisi)
        return chemin_fichier_pertinent
    else:
        return None
def handle_question(question):
    mots_question = tokenization_of_question(question)
    document_pertinent = obtenir_chemin_fichier_pertinent(mots_question)

    if document_pertinent:
        reponse = trouver_phrase_dans_document(mots_question, document_pertinent)
        return reponse
    else:
        return "Aucun document pertinent trouvé."

#Calculating the most relevant document
def scorequestion(question, matrice):
    MatriceQuestion = []
    directory = "./Cleaned/"
    question = tokenization_of_question(question)
    tab_fichiers = list_of_files(directory)
    nb_fichiers = len(tab_fichiers)

    for i in range(len(matrice)):
        mot = matrice[i][0]
        if mot in question:
            TF_score = TFliste(question, mot)
            scores_idf = matrice[i][1:]
            tfidf_scores = [TF_score * idf for idf in scores_idf]
            MatriceQuestion.append(tfidf_scores)
        else:
            MatriceQuestion.append([0.0] * nb_fichiers)

    return MatriceQuestion



def generer_reponse(question, document):   #generate an answer from the previous functions (troubles to make the function work)
    mots_question = tokenization_of_question(question)
    tf_idf_question = TF_IDF(mots_question)

    mot_cle = max(tf_idf_question, key=tf_idf_question.get)

    reponse = trouver_phrase_dans_document(mot_cle, document)
    return reponse

#the answer does not correspond to our needs but its close enough to our question







def main():
    print("================================================\n"
          "[   Hello ! Je suis Votre ChatBot Personnel    ]\n"
          "[      Comment puis-je vous etre utile ?       ]\n"
          "================================================\n")

    while True:
        user_input = input("\nN'hésitez pas à me poser votre question!, si vous voulez annuler, tapez 'quitter' pour sortir : ")
        if user_input.lower() == 'quitter':
            print("J'espere vous revoir bientot !")
            break
        else:
            response = handle_question(user_input)
            print("Réponse :", response)


print(main())