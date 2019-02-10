#TASK1

import string

def file_read():
    """Reads a file and prints the words in the file"""
    fin=open("book.txt")
    count=0
    for line in fin:
        line = line.replace("-", " ")
        word=line.split()
        for item in word:
            item=item.strip(string.punctuation + string.whitespace)
            item=item.lower()
            print(item)
    return 0
    
print(file_read())

____________________________________________________________________

#TASK2

import string

def read_file(book):
    """Reads the given file, counts words and returns the dictionary"""
    d = dict()
    count = 0
    file = open(book)
    for line in book:
        line = line.replace("-"," ")
        words = line.split()
        for i in words:
            i = i.strip(string.punctuation + string.whitespace)
            i = i.lower()
            d[i] = d.get(i,0)+1
            count = count + 1
    return count,d

def print_dic(d):
    """Prints the histogram of dictionary"""
    print(len(d))
    for k,v in d.items():
        print(k,v)

def diff_words(d):
    diff_words = dict()
    for key in d.keys():
        if key not in diff_words:
            diff_words[key] = "none"
    return diff_words

def diff_words(d):
    """Prints the different words used in file"""
    dict_words=dict()
    for key in d.keys():
        if key not in dict_words:
            dict_words[key]="none"
    return dict_words

def compare_books(d1,d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def vocab(d1,d2):
    """Returns which book has more number of vocabulary"""
    if len(d1) > len(d2):
        return "Book 1"
    elif len(d2) > len(d1):
        return "Book 2"
    else:
        return None

count1,d1 = file_read("book1.txt")
print ("Total no. of words in book1: ",count1)
print_dict (d1)
dict_words = diff_words (d1)
print_dict (dict_words)
count2,d2 = file_read("book2.txt")
print ("Total no. of words in book2: ",count2)
d1md2 = compare_books(d1,d2)
d2md1 = compare_books(d2,d1)
print ("Best book with more vocabulary is: ",vocab(d1,d2))

____________________________________________________________________

#TASK3

import string

def file_read(filename):
    """Reads a file and counts the words frequency and total word count"""
    fin=open(filename)
    count=0
    d=dict()
    for line in fin:
        line=line.replace("-"," ")
        word=line.split()
        for item in word:
            item=item.strip(string.punctuation + string.whitespace)
            item=item.lower()
            d[item]=d.get(item,0)+1
            count=count+1
    return count,d

def print_dict(d):
    """Prints the histogram dictionary"""
    list1=list()
    for key,value in d.items():
        list1.append((value,key))
    list1.sort(reverse=True)
    for word,value in list1[:20]:
        print(word, value, sep='\t')

count1,d1=file_read("prideandprejudice.txt")
print("Total no of words in book1 is ",count1)
print_dict(d1)

_____________________________________________________________________

#TASK4

import string

def file_read(filename):
    """Reads a file and return the words as a list"""
    fin=open(filename)
    word_list=list()
    for line in fin:
        line=line.strip()
        word_list.append(line)
    return word_list

def file_read1(filename):
    """Reads a file and counts the words frequency and total word count"""
    fin=open(filename)
    d=dict()
    for line in fin:
        line=line.replace("-"," ")
        word=line.split()
        for item in word:
            item=item.strip(string.punctuation + string.whitespace)
            item=item.lower()
            d[item]=d.get(item,0)+1
    return d

def compare_books(word_list,d1):
    res = list()
    for key in d1:
        if key not in word_list:
            res.append(key)
    return res

word_list=file_read("words.txt")
d=file_read1("prideandprejudice.txt")
res=compare_books(word_list,d)
print(res)

_____________________________________________________________________

#TASK5

from __future__ import print_function, division

import sys
import string
import matplotlib.pyplot as plt

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist
def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1


def rank_freq(hist):
    """Returns a list of (rank, freq) tuples.

    hist: map from word to frequency

    returns: list of (rank, freq) tuples
    """
    # sort the list of frequencies in decreasing order
    freqs = list(hist.values())
    freqs.sort(reverse=True)

    # enumerate the ranks and frequencies
    rf = [(r+1, f) for r, f in enumerate(freqs)]
    return rf


def print_ranks(hist):
    """Prints the rank vs. frequency data.

    hist: map from word to frequency
    """
    for r, f in rank_freq(hist):
        print(r, f)


def plot_ranks(hist, scale='log'):
    """Plots frequency vs. rank.

    hist: map from word to frequency
    scale: string 'linear' or 'log'
    """
    t = rank_freq(hist)
    rs, fs = zip(*t)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=3)
    plt.show()


def main(script, filename='emma.txt', flag='plot'):
    hist = process_file(filename, skip_header=True)

    # either print the results or plot them
    if flag == 'print':
        print_ranks(hist)
    elif flag == 'plot':
        plot_ranks(hist)
    else:
        print('Usage: zipf.py filename [print|plot]')


if __name__ == '__main__':
    main(*sys.argv)

_____________________________________________________________________

#TASK6

import os
def walk(dirname):    
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)        
        if os.path.isfile(path):
            print(path)        
        else:            
            walk(path)

walk(os.getcwd())

_____________________________________________________________________

#TASK7

import string
def removepattern(word):
    punc = string.punctuation
    string = ""
    for p in punc:
        string = word.strip()
        string = word.replace(p,'')
    return string

def read(filename1,filename2):
     try:
        master = open(filename1,"r")
        slave = open(filename2,"w")
        for ma in master:
            new = removepattern(ma)
            slave.write(ma)
        print("File write operation completed successfully :-)")
     except:
        print("Oops something went wrong!!!")


x = input("Enter master file for copy operation:")
y = input("Enter slave file:")
read(x,y)

_____________________________________________________________________

#TASK8


import hashlib
import os


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

PATH = os.getenv("HOME")
def findfile(extension):
    for root, subFolder, files in os.walk(PATH):
        for item in files:
            if item.endswith("."+ str(extension)):
                fileNamePath = str(os.path.join(root,item))
                print(fileNamePath," ",md5(fileNamePath))


x = input("enter file extension for search operation:")
findfile(x)

_____________________________________________________________________
