# HOUARI Houssam - RATSIMBAZAFY Armence - INT4

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
print(list_of_files("./speeches-20231123", "txt"))

# gets the names of the presidents out of the files name
def last_name_file(s,docu):
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


speeches = "./speeches-20231123"
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


from collections import Counter
import string


# other method to get the occurence of a word
def count_occurrences_word(text):
    occurrences_mots = Counter(text)
    text = {}
    return occurrences_mots

    # display the results of the occurences
    for mot, occurrences in text.items():
        print({mot}, {occurrences})

import math
from collections import Counter

def computation_tf(document):
    # Utiliser Counter pour compter le nombre d'occurrences de chaque mot dans le document
    occurrences_mots = Counter(document.split())

    # Calculer le TF pour chaque mot
    tf_resultat = {mot: occurrences / len(document.split()) for mot, occurrences in occurrences_mots.items()}

    return tf_resultat


# document_exemple = collection_documents_exemple[0]


def computation_idf(collection_documents, mot):
    # total number of elements in the collection
    nb_documents_total = len(collection_documents)

    # cber of docs couting the word
    nb_documents_contenant_mot = sum(1 for doc in collection_documents if mot in doc)

    # compuation of the idf
    idf = math.log(nb_documents_total / (1 + nb_documents_contenant_mot))

    return idf

# example
# collection_documents_exemple = [text]

#document_exemple = collection_documents_exemple[0]

# calculation of every word's tf in the text
tf_resultats = computation_tf(collection_documents)
print("TF pour chaque mot dans le document :", tf_resultats)
for mot, tf_score in tf_resultats.items():
    print(f"{mot}: {tf_score:.0f}")

# calculation of each word's idf in the texts
idf_resultats = {}
for mot in set(collection_documents.split()):
    idf_resultats[mot] = computation_idf(collection_documents, mot)

print("\nIDF pour chaque mot dans la collection de documents :")
for mot, idf_score in idf_resultats.items():
    print(f"{mot}: {idf_score:.0f}")


# changing the matrice into a vector
    def liste_en_vecteur(liste):
        # Utiliser une liste en compréhension pour aplatir la liste de listes
        vecteur_resultat = [element for sous_liste in liste for element in sous_liste]

        return vecteur_resultat

    # Exemple d'utilisation :
    liste_exemple = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]

    vecteur_resultat = liste_en_vecteur(liste_exemple)

    print("Liste d'origine :\n", liste_exemple)
    print("\nVecteur résultat :", vecteur_resultat)

    def calculer_tfidf_matrix(texts):

        # Exemple d'utilisation :
            textes_exemple = [
            "Ceci est un exemple de texte.",
            "Un autre exemple de texte.",
            "Encore un exemple pour illustrer."
            ]

    # Calculer la matrice TF-IDF et les noms de mots
    tfidf_matrix, noms_mots = calculer_tfidf_matrix(textes_exemple)

    # Afficher la matrice TF-IDF
    print("Matrice TF-IDF :")
    print(tfidf_matrix.toarray())

    # Afficher les noms de mots
    print("\nNoms de mots :")
    print(noms_mots)


#Fonction 6
def display_least_important_words(tf_idf_matrix):
    least_important_words = set()

    # Iterate over each word in the TF-IDF matrix
    for document in tf_idf_matrix:
        for word, tf_idf_score in document.items():
            # Check if the TF-IDF score is 0 in all documents
            if tf_idf_score == 0:
                least_important_words.add(word)

    # Display the list of least important words
    print("Least Important Words:", least_important_words)

speeches_directory = "./cleaned"
tf_idf_matrix = calculate_tf_idf_matrix(speeches_directory)
display_least_important_words(tf_idf_matrix)

#Fonction 7
def display_highest_tfidf_words(tf_idf_matrix):
    highest_tfidf_words = {}

    for document in tf_idf_matrix:
        # Find the word(s) with the highest TF-IDF score in the document
        max_tfidf_word = max(document, key=document.get)
        max_tfidf_score = document[max_tfidf_word]

        # Add the word(s) and their score to the result dictionary
        highest_tfidf_words[max_tfidf_word] = max_tfidf_score

    print("Word(s) with Highest TF-IDF Score:", highest_tfidf_words)

speeches_directory = "./cleaned"
tf_idf_matrix = calculate_tf_idf_matrix(speeches_directory)
display_highest_tfidf_words(tf_idf_matrix)



#questions fonctions
# question
def calculate_tf_idf_matrix_with_presidents(directory, president_names):

    tf_idf_matrix = []

    for file_name, president in zip(file_names, president_names):
        file_path = os.path.join(directory, file_name)

        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        word_occurrences = count_word_occurrences(content)

        tf_idf_scores = {}
        for word, tf in word_occurrences.items():
            tf_idf_scores[word] = tf * idf_scores.get(word, 0)

        tf_idf_matrix.append({'president': president, 'tf_idf_scores': tf_idf_scores})

    return tf_idf_matrix

# Fonction 8.1
def most_repeated_words_by_president(tf_idf_matrix, president_name):
    president_documents = [doc['tf_idf_scores'] for doc in tf_idf_matrix if doc['president'] == president_name]

    if not president_documents:
        print(f"No documents found for President {president_name}")
        return

    combined_scores = {}
    for document in president_documents:
        for word, tf_idf_score in document.items():
            combined_scores[word] = combined_scores.get(word, 0) + tf_idf_score

    most_repeated_word = max(combined_scores, key=combined_scores.get)
    most_repeated_score = combined_scores[most_repeated_word]

    print(f"Most Repeated Word(s) by President {president_name}:")
    print(f"Word: {most_repeated_word}, TF-IDF Score: {most_repeated_score}")

# Example usage:
speeches_directory = "./cleaned"
president_names = ['Chirac', 'Giscard d\'Estaing', 'Hollande', 'Mitterrand', 'Macron', 'Sarkozy']
tf_idf_matrix = calculate_tf_idf_matrix_with_presidents(speeches_directory, president_names)
most_repeated_words_by_president(tf_idf_matrix, 'Chirac')

# Fonction 9

def calculate_tf_idf_matrix_with_target_word(directory, president_names, target_word):

    tf_idf_matrix = []

    for file_name, president in zip(file_names, president_names):
        file_path = os.path.join(directory, file_name)

        with open(file_path, 'r') as file:
            content = file.read()

        word_occurrences = count_word_occurrences(content)

        tf_idf_scores = {}
#for word, tf in word_occurrences.items():


    cleaned_content = no_punctuation(lowercase(content))

    with open("cleaned_" + file, "w") as f2:
        f2.write(cleaned_content)
        print(cleaned_content, "\n")
