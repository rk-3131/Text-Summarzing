import argparse
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

def main():
    argRecieved = parser_method()
    # This will get us the reference of the arguements recieved whenever we use the command line interface to enter the name and length of the file
    text = file_input(argRecieved.Filepath)
    # This line will be used to give input to the file. The file is given as input after taking it from command line interface
    updated_text = remove_extra(text)
    # Extra symbols such as \t \n along with any other symbols will be removed in this step
    tokenized_sentence, tokenized_words = tokenizer_method(updated_text)
    # Sentence and the words will be tokenized after above methods. For words tokenization we have to remove even the punctuation along with the stopwords. After all this two sentence and words are returned after the tokenization in two separate variables
    get_rank_of_sentence = score_tokens(tokenized_words, tokenized_sentence)
    # This method is used to get the rank of each sentence based on the occurence of each word in the frequency distrubution of the words available.
    print(final_summarize(get_rank_of_sentence,argRecieved.length, tokenized_sentence))
    # This methods returns final summary of the text after all the proccessing and ranking of the sentences. It is used to get the list of the lenghts which are larger based on the key supplied to it.



def parser_method():
    parser = argparse.ArgumentParser()
    parser.add_argument("Filepath", help="Enter the file name in same directory")
    parser.add_argument("-l","--length", default=4, help="What is number of sentence")
    args = parser.parse_args()
    return args
    '''
    This method is used for the purpose of creating arguments in the command line interface.
    Whatever the arguments that we want to get into the program can be passed by this feature.
    Here we have added the filepath arguments which actually makes program able to take arguments as the name of the file in the same directory so that it can be used in the file to get the input
    '''

def file_input(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print("Error occured as follows",e)
    '''
    Here we have used a method to get a file as input.
    The file has been taken as the f in the section for the default purpose of reading.
    try and catch block are also added in the code so as if there is any exception then they can be handled by the try and catch block easily
    '''

def remove_extra(data):
    replace = {
        ord("\t") : " ",
        ord("\n") : " ",
        ord("\f") : " ",
        ord("\r") : None
    }
    return data.translate(replace)
    '''
    This method named as remove extra will be used to replace the extra symbols from the code.
    The ord method in python returns us the ASCII code for the given letter, here \n will be returned by the ord method as the respective ASCII number. 
    replace dictionary will assign the blank spaced and None character to respective characters
    At the end translate method will return the replaced character by the given blank spaces thus reducing the code overhead
    '''

def tokenizer_method(data):
    stop_words = set(stopwords.words("english") + list(punctuation))
    all_words = word_tokenize(data.lower())
    for words in all_words:
        if words in stop_words:
            all_words.remove(words)

    return sent_tokenize(data), all_words

    '''
    This is the method which is used to make tokens from the given input file
    There are two main types of the tokens word tokens and sentence tokens 
    words tokenizer divide the whole block of text into single single words and simillarly the sentence tokenizer tokenizes the whole text data into group of sentences.
    Here we have added stopwords which are basically words which dont affect the meaning even after their removal. They can be "and, or, etc"
    Here we have prepared a list all_words such that we have removed the stopwords from them and we have returned the list along with the list of all the sentece after tokenizatin
    '''

def score_tokens(word_tokens, sent_tokens):
    word_frequency = FreqDist(word_tokens)
    rank = defaultdict(int)
    for i, sent in enumerate(sent_tokens):
        for words in word_tokenize(sent.lower()):
            if words in word_frequency:
                rank[i] += word_frequency[words]

    return rank

    '''
    Above method is used to give each sentence a rank based on each of the occurence of the word according to word frequency of occurence
    This code defines a function called "score_tokens" that takes in two arguments: a list of sentence tokens (sent_tokens) and a list of word tokens (word_tokens).
    It first creates a frequency distribution of the word tokens using the FreqDist() function from the Natural Language Toolkit (NLTK) library.
    Then it initializes a default dictionary (rank) with integer values.
    It then iterates through the list of sentence tokens, tokenizing each sentence into individual words (using word_tokenize() function) and lowercasing each word.
    For each word in the sentence, if the word is present in the frequency distribution of word tokens, the rank of the corresponding sentence is incremented by the frequency of the word.
    Finally, it returns the rank dictionary, which assigns a score to each sentence based on the frequency of the words in the word_tokens list. 
    '''

def final_summarize(rank, length, sentence):
    if (int(length) > len(sentence)):
        print("You have requested more number of summarizes sentence than that of the actual sentences in the original data.")
        return ""
        '''
        If length of the asked sentence in the code is greater than that of the original number of sentences in the sentences then it will print the message and function will return empty string.
        '''

    else:
        indices = nlargest(int(length), rank, key=rank.get)
        final_summary = [sentence[j] for j in indices]

        return " ".join(final_summary)

        '''
        Above else statement is useful for the purpose of summarizing final text
        Here we have used the method nlargest to extract the largest elements from the rank based on the values in the dictionary specified by key = rank.get
        In simple words it returns list of the length key from the ranks that corresponds to largest value
        After that we have created empty list 
        The list final_summary will be fulled by the corresponding number of the element in the sentence list
        Finally it is returned
        '''

if __name__ == '__main__':
    main()
        
