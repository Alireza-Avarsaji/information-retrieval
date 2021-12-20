from __future__ import unicode_literals
import pickle
import openpyxl
from hazm import *

class NormalizeHandler:
    tokenized_list = []
    file = ''
    normalizer = Normalizer()
    stemmer = Stemmer()
    pos_index = {}
    panctuations = [
        "]",
        "[",
        "}",
        "{",
        "؛",
        ":",
        "«",
        "»",
        ">",
        "<",
        "؟",
        "!",
        "٬",
        "﷼",
        "٪",
        "×",
        "،",
        "*",
        ")",
        "(",
        "-",
        "ـ",
        "-",
        "=",
        "+",
        "|",
        "`",
        "~",
        ".",
        ".",
        "»",
        "«"
    ]

    stopWords = [
       "از",
       "با",
       "تا",
       "آن",
       "این",
       "برای",
       "و",
       "در",
       "اما",
       "است",
       "شد",
       "شده",
       "که",
       "آمد",
       "مانند",
       "به",
       "حتی",
       "کرد",
        "را",
       "چه",
       "چند",
       "باشد",
       "یا",
       "یعنی"
    ]

    def __init__(self, file):
        self.file = file


    def remove_punctuation(self, row):
        normalized = self.normalizer.normalize(row)
        for punc in self.panctuations:
            normalized = normalized.replace(punc, '')
        return word_tokenize(normalized)


    def stop_words(self, token_list):
       x = token_list
       for stop in self.stopWords:
           for token in token_list:
              if stop == token:
                  x.remove(stop)
       return x


    def stem(self, token_list):
        list = token_list
        for token in list:
            list[list.index(token)] = self.stemmer.stem(token)
        return list


    def base_normalizer(self):
       index = 0
       for row in openpyxl.load_workbook(self.file).active.iter_rows():
           curr_doc_token_list = self.stem(self.stop_words(self.remove_punctuation(row[0].value)))
           for pos, token in enumerate \
                       (curr_doc_token_list):
               if token in self.pos_index:
                   if index in self.pos_index[token][0]:
                       self.pos_index[token][0][index][0] += 1

                   else:
                       self.pos_index[token][0][index] = [1]
               else:
                   self.pos_index[token] = []
                   self.pos_index[token].append({})
                   self.pos_index[token][0][index] = [1]
           index += 1


    def write_in_file(self):
        file = open("indexed_data.pkl", "wb")
        pickle.dump(self.pos_index, file)
        file.close()


    def read_from_file(self, file):
        filee = open(file, 'rb')
        data = pickle.load(filee)
        return data