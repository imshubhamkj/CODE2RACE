#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse(sentence):
    #Put in a tab
    tab = sentence.split(" ")
    reverseTab = []
    a = ""
    #reverse the tab
    for i in range(len(tab)-1, -1, -1):
        reverseTab.append(tab[i])
    #create the string
    for j in reverseTab:
        a = a + j + ' '
    return str(a)


if __name__ == "__main__":
    sentence = raw_input("Enter a string : ")
    newSentence = reverse(sentence)
    print(newSentence)

