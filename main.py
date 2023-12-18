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


from collections import Counter
import string


# other method to get the occurence of a word
def count_word_occurrences(text):
    # ''counts the number of times a word is present in a text''
    words = text.split()
    word_counts = Counter(words)
    return word_counts





import math
from collections import Counter

def computation_tf(document):
    # Utiliser Counter pour compter le nombre d'occurrences de chaque mot dans le document
    occurrences_mots = Counter(document.split())

    # Calculer le TF pour chaque mot
    tf_resultat = {mot: occurrences / len(document.split()) for mot, occurrences in occurrences_mots.items()}
    print("hh",tf_resultat)
    return tf_resultat

with open ("./cleaned/cleaned_Nomination_Chirac1.txt", "r") as file:
    computation_tf(file.readline())

# document_exemple = collection_documents_exemple[0]


def computation_idf(collection_documents, mot):
    # total number of elements in the collection
    nb_documents_total = len(collection_documents)

    # cber of docs couting the word
    nb_documents_contenant_mot = sum(1 for doc in collection_documents if mot in doc)

    # compuation of the idf
    idf = math.log(10)(nb_documents_total / (1 + nb_documents_contenant_mot))

    return idf


tf_resultat = computation_tf('cleaned')
print("TF pour chaque mot dans le document :", tf_resultat)
for mot, tf_score in tf_resultat.items():
    print(f"{mot}: {tf_score:.0f}")

# calculation of each word's idf in the texts
idf_resultats = {}
collection_documents = str('cleaned')
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
#liste_exemple = [[1, 2, 3],
                 #[4, 5, 6],
                 #[7, 8, 9]]

#vecteur_resultat = liste_en_vecteur(liste_exemple)

#print("Liste d'origine :\n", liste_exemple)
#print("\nVecteur résultat :", vecteur_resultat)

import os
import math
from collections import Counter


def calculer_tfidf_matrix(directory):
    # Step 1: Tokenize the documents and build a vocabulary
    vocabulaire = set()
    texts = []

    # Read the content of each file in the directory
    for file_name in os.listdir(directory):
        with open(os.path.join(directory, file_name), 'r',) as f:
            texts.append(f.read())

    # Tokenize each document
    for text in texts:
        words = text.lower().split()
        vocabulaire.update(words)

    vocabulaire = list(vocabulaire)
    vocabulaire.sort()

    # Step 2: Calculate the Term Frequencies (TF) for each document
    tf_matrix = []
    for text in texts:
        words = text.lower().split()
        tf_vector = [words.count(word) for word in vocabulaire]
        tf_matrix.append(tf_vector)

    # Step 3: Calculate the Document Frequencies (DF) for each term
    df_vector = [sum(1 for tf_vector in tf_matrix if tf_vector[i] > 0) for i in range(len(vocabulaire))]

    # Step 4: Calculate the Inverse Document Frequencies (IDF)
    idf_vector = [math.log(len(texts) / df) for df in df_vector]

    # Step 5: Calculate the TF-IDF matrix
    tfidf_matrix = []
    for tf_vector in tf_matrix:
        tfidf_vector = [tf * idf for tf, idf in zip(tf_vector, idf_vector)]
        tfidf_matrix.append(tfidf_vector)

    # Print the TF-IDF matrix and feature names
    print("Matrice TF-IDF :")
    for row in tfidf_matrix:
        print(row)
    print("\nNoms des mots:")
    print(vocabulaire)

    return tfidf_matrix, vocabulaire







#Fonction 6
def display_least_important_words(tfidf_matrix):
    least_important_words = []
    for i in tfidf_matrix:
        for tf_idf_score in i:
            # Check if the TF-IDF score is 0 in all documents
            if tf_idf_score == 0:
                least_important_words.append(tf_idf_score)
                print(least_important_words)

speeches_directory = "./cleaned"
tfidf_matrix = calculer_tfidf_matrix(speeches_directory)
display_least_important_words(tfidf_matrix)



#Fonction 7
def display_highest_tfidf_words(tf_idf_matrix):
    highest_tfidf_words = set()

    for document in tf_idf_matrix:
        for tf_idf_score in document:
            # Check if any individual TF-IDF score is greater than 0
            if tf_idf_score > 0:
                highest_tfidf_words.add(tf_idf_score)

    print("Words with TF-IDF Score:", highest_tfidf_words)

# Example usage:
speeches_directory = "./cleaned"
tf_idf_matrix, _ = calculer_tfidf_matrix(speeches_directory)
display_highest_tfidf_words(tf_idf_matrix)



#questions fonctions
# question
def calculate_tf_idf_matrix_with_presidents(directory, president_names, idf_scores):

    tf_idf_matrix = []

    for file_name, president in zip(os.listdir(os.path.join(directory)), president_names):
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
#speeches_directory = "./cleaned"
#president_names = ['Chirac', 'Giscard d\'Estaing', 'Hollande', 'Mitterrand', 'Macron', 'Sarkozy']
#tf_idf_matrix = calculate_tf_idf_matrix_with_presidents(speeches_directory, president_names)
#most_repeated_words_by_president(tf_idf_matrix, 'Chirac')

# Fonction 9

def calculate_tf_idf_matrix_with_target_word(directory, president_names, target_word):

    tf_idf_matrix = []

    for file_name, president in zip(os.listdir(os.path.join(directory)), president_names):
        file_path = os.path.join(directory, file_name)

        with open(file_path, 'r') as file:
            content = file.read()



        tf_idf_scores = {}
#for word, tf in word_occurrences.items():


    cleaned_content = no_punctuation(lowercase(content))

    with open("cleaned_" + file, "w") as f2:
        f2.write(cleaned_content)
        print(cleaned_content, "\n")

cleaned = 'cleaned'