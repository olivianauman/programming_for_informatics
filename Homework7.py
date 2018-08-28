#Olivia Nauman
#Homework 7 

#import the string library so we can use it later
import string

#this function reads in the file contents of the dictionary
def read_dictionary_file(filename):
    #encode to latin-1 because spanish dict has more words than english
    #open for reading
    f = open(filename,'r', encoding = 'latin-1')
    #split the contents of the file into each pair of english-spanish
    lineList = f.read().splitlines()
    #close the file
    f.close()
    return lineList

#this function makes a dictionary with the english word as a key and spanish word as the value
def make_dictionary(lineList):
    #the dictionaries start empty
    etos_dictionary = {}
    stoe_dictionary = {}
    #for every line in the file, split the english and spanish words apart at the comma and make the english word the key and the spanish word the value
    for line in lineList:
        translation = line.split(',')
        #this makes the English to Spanish dictionary
        etos_dictionary[translation[0]] = translation[1]
        #this makes the Spanish to English dictionary
        stoe_dictionary[translation[1]] = translation[0]
    return etos_dictionary, stoe_dictionary

#you are given a file with either english, spanish, or a mix of both sentences. Open this file for reading.
def read_sentences_file(filename):
    f = open(filename, 'r')
    #punctuation is a variable equal to all punctuation elements in the string library
    punctuation = string.punctuation
    #read the file contents
    file_sentences = f.read()
    #make a transformation to replace punctuation with a blank space
    file_no_punct = str.maketrans(punctuation, ' '*len(punctuation))
    #apply the transformation to the file contents
    file_no_punct_2 = file_sentences.translate(file_no_punct)
    #make the file contents (with no punctuation) lowercase and split it into a list of the sentences
    final_file = file_no_punct_2.lower().splitlines()
    #close the file
    f.close()
    return  final_file

#convert all of the sentences from that file into the opposite language using the dictionaries made earlier. If a word appears in neither dictionary, leave it as is. 
def convert_sentences(final_file,stoe_dictionary,etos_dictionary):
    #start with an empty string to add to 
    translation_string =""
    #For every sentence in the list of sentences
    for sentence in final_file:
        #make it look a bit nicer by adding a new line after each sentence
        translation_string += "\n"
        #for every word in the sentence (without the white space)
        for word in sentence.split():
            #if the word is in spanish, find the equivalent in english from the span-eng dictionary and add the english version to the string of words and a space after
            if word in stoe_dictionary:
                translation_string += stoe_dictionary[word] + " "
            #if the word is in english, find the equivalent in spanish from the eng-span dictionary and add the spanish version to the string of words and a space after
            elif word in etos_dictionary:
                translation_string += etos_dictionary[word] + " "
            #if the word isn't in either dictionary, just keep the word as is! (and add a space after)
            else:
                translation_string += word + " "
    #return the translated file    
    return translation_string
                    
filecontents = read_dictionary_file('english_spanish.csv')
eng_to_sp_dict, sp_to_eng_dict = make_dictionary(filecontents)   
sentences = read_sentences_file('to_translate.txt')            
translated_sentences = convert_sentences(sentences, sp_to_eng_dict, eng_to_sp_dict)     
print(translated_sentences)
  