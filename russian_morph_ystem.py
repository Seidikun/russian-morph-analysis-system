# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 23:06:18 2019

@author: seidi
"""

import  pymorphy2
from nltk import word_tokenize
from googletrans import Translator

morph = pymorphy2.MorphAnalyzer()
translator = Translator()

# Lets's make a function that does it

def phrase_analysis(phrase):
    
    translation = translator.translate(phrase,src='ru',dest='en')
    print('_'*80)
    print('origin:     ', phrase)
    print('translation:',translation.text)
    print('_'*80)

    tokens = word_tokenize(phrase)
    run = True
    while run == True:    
      
      print('0 - EXIT')
      for i in range(1,len(tokens)+1):
        print(i,'-',tokens[i-1])
      choice = input('Enter a number to run morphological analysis:')
      if choice == '0':
        run = False
      else:
        token = tokens[int(choice) - 1]
        a = morph.parse(token)[0]
        print(' word:       ',a.word,'\n',
              'translation:',translator.translate(token, src='ru',dest='en').text,'\n',
              'tag:        ',a.tag,'\n',
              'normal_form:',a.normal_form,'\n',
              'score:      ',a.score,'\n')
        input("Press Enter to continue...")
        print('_'*80)
        
      
phrase = 'кто хочет много знать, тому надо мало спать'
phrase_analysis(phrase)