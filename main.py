import openpyxl

from normalizer import NormalizeHandler
from utils import print_result_links

file = "IR1_7k_news.xlsx"

def get_query():
    query = input("what are you looking for?  ")
    query = query.strip()
    query = normalizer.stop_words(normalizer.remove_punctuation(query))
    return query


def single_word_result(query):
    doc_list = []
    result = positional_index[query[0]]
    for doc in result[1]:
        doc_list.append(doc)
    return doc_list
    # for i in doc_list:
    #     print(workbook.active.cell(row=i+1, column=2).value)



def by_word_result(query):
    result = []
    doc_list_1 = positional_index[query[0]][1]
    doc_list_2 = positional_index[query[1]][1]
    for doc1 in doc_list_1:
        for doc2 in doc_list_2:
            if doc1 == doc2:
                for i in doc_list_1[doc1]:
                    if i+1 in doc_list_2[doc2]:
                         result.append(doc1)
    result = list(set(result))
    return result

def multi_word_result(query):
    sec_1 = by_word_result(query[0:2])
    sec_2 = by_word_result(query[1:3])
    result = list(set(sec_1).intersection(sec_2))
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
                print_result_links(by_word_result(query), workbook)
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
# normalizer.base_normalizer()
# normalizer.write_in_file()
positional_index = normalizer.read_from_file("indexed_data.pkl")
main()