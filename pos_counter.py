#requires download of NLTK in Python
import os
import nltk
from nltk.corpus import *
import string

def main():
    # modify path for where files are on machine
    path = "/Users/EMWork/Desktop/Boston University/EVL/Map Lemon Analysis/Participant Texts/Men"
    for text_file in os.listdir(path):
        if '.txt' in text_file:
            print("We are in " + text_file)
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            my_file = os.path.join(THIS_FOLDER, text_file)
            f = open(my_file, 'r+')
            raw = f.read()

            # tags all words with corresponding part-of-speech in user's text file choice
            tokens = nltk.word_tokenize(raw)
            tagged_corpus = nltk.pos_tag(tokens)
            update_corpus = ""

            count_adj = 0
            count_noun = 0
            count_prep = 0
            count_propnoun = 0
            count_prpnoun = 0
            count_prpsnoun = 0
            count_adv = 0
            count_verb = 0
            count_chad = 0

            for i in range(len(tagged_corpus)):
                if (str.lower(tagged_corpus[i][0]) == 'chad'):
                    count_chad += 1
                if ('JJ' in tagged_corpus[i]) or ('JJR' in tagged_corpus[i]) or ('JJS' in tagged_corpus[i]):
                    count_adj += 1
                elif ('NN' in tagged_corpus[i]) or ('NNS' in tagged_corpus[i]):
                    count_noun += 1
                elif ('IN' in tagged_corpus[i]):
                    count_prep += 1
                elif ('NNP' in tagged_corpus[i]) or ('NNPS' in tagged_corpus[i]):
                    count_propnoun += 1
                elif ('PRP' in tagged_corpus[i]):
                    count_prpnoun += 1
                elif ('PRP$' in tagged_corpus[i]):
                    count_prpsnoun += 1
                elif ('RB' in tagged_corpus[i]) or ('RBR' in tagged_corpus[i]) or ('RBS' in tagged_corpus[i]):
                    count_adv += 1
                elif ('VB' in tagged_corpus[i]) or ('VBD' in tagged_corpus[i]) or ('VBG' in tagged_corpus[i]) or ('VBN' in tagged_corpus[i]) or ('VBP' in tagged_corpus[i]) or ('VBZ' in tagged_corpus[i]):
                    count_verb += 1

            update_corpus += "Adjectives: " + str(count_adj) + "\n" + \
                "Nouns: " + str(count_noun) + "\n" + \
                    "Prepositions: " + str(count_prep) + "\n" + \
                        "Proper Nouns: " + str(count_propnoun) + "\n" + \
                            "Personal Pronouns: " + str(count_prpnoun) + "\n" + \
                                "Possessive Pronouns: " + str(count_prpsnoun) + "\n" + \
                                    "Adverbs: " + str(count_adv) + "\n" + \
                                        "Verbs: " + str(count_verb) + "\n" + \
                                            "Chads: " + str(count_chad)

            f = open(str(input("Enter filename for which you want the data text to be exported (with .txt): \n")), "w")
            f.write(update_corpus)

while True:
    answer = input("Run the 'POS Counter ML' program? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye.")
        break
