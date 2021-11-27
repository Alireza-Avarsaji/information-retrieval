import openpyxl
from normalizer import NormalizeHandler
from utils import print_result_links
from hazm import *
import matplotlib.pyplot as plt

file = "IR1_7k_news.xlsx"

def get_query():
    query = input("what are you looking for?  ")
    query = query.strip()
    query = normalizer.stem(normalizer.stop_words(normalizer.remove_punctuation(query)))
    return query


def single_word_result(query):
    doc_list = []
    result = positional_index[query[0]]
    for doc in result[1]:
        doc_list.append(doc)
    return doc_list



def by_word_result(query,doc_1,doc_2):
    result = []
    common = []
    doc_list_1 = positional_index[query[doc_1]][1]
    doc_list_2 = positional_index[query[doc_2]][1]
    for doc1 in doc_list_1:
        for doc2 in doc_list_2:
            if doc1 == doc2:
                common.append(doc1)
                for i in doc_list_1[doc1]:
                    if i+(doc_2 - doc_1) in doc_list_2[doc2]:
                         result.append(doc1)

    result = list(set(result))
    common = list(set(common))
    common = list(set(common).difference(set(result)))
    return result, common


def multi_word_result(query):
    sec_1,sec_1_common = by_word_result(query,0,1)
    sec_2,sec_2_common = by_word_result(query,1,2)
    sec_3,sec_3_common = by_word_result(query,0,2)
    result = list(set(sec_1).intersection(sec_2))
    result = list(set(result).intersection(sec_3))
    for w in *sec_1,*sec_2,*sec_3,*sec_1_common,*sec_2_common,*sec_3_common:
        if w not in result:
            result.append(w)
    return result



def main():
    while True:
        query = get_query()
        if len(query) == 1:
            try:
                print_result_links(single_word_result(query), workbook)
            except:
                print('not found:(')
            continue
        if len(query) == 2:
            try:
                result = by_word_result(query,0,1)[0]
                common = by_word_result(query,0,1)[1]
                result = result + common
                print_result_links(result, workbook)
            except:
                print('not found:(')
        else:
            try:
                print_result_links(multi_word_result(query),workbook)
            except:
                print('not found:(')


# build index file and read it
normalizer = NormalizeHandler(file)
workbook = openpyxl.load_workbook(file)
normalizer.base_normalizer()
normalizer.write_in_file()
positional_index = normalizer.read_from_file("indexed_data.pkl")
main()



## zipf chart
# normalizer.base_normalizer_stop_words()
# normalizer.write_in_file()
# positional_index = normalizer.read_from_file("indexed_data.pkl")
# freq_list = []
# for i in positional_index:
#     freq_list.append(positional_index[i][0])
# freq_list.sort(reverse=True)
# freq_list.reverse()
# plt.yscale('log')
# plt.xscale('log')
# plt.plot(freq_list)
# plt.show()


## Heap check
# positional_index = normalizer.read_from_file("indexed_data.pkl")
# total_words = 0
# uniq = len(positional_index)
# for i in positional_index:
#    total_words += positional_index[i][0]
# print(total_words)
# print(uniq)
# plt.plot([101917,201315,302782,448530],[10499,14716,17758,25107])
# plt.plot([101917,201315,302782,448530],[8165,11243,13440,18456])
# plt.show()