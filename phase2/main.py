from collections import OrderedDict

from normalizer import NormalizeHandler
import openpyxl
import math

from utils import print_result_links, sort_score_list_by_index

file = "IR1_7k_news.xlsx"







def get_query():
    query = input("what are you looking for?  ")
    query = query.strip()
    query = normalizer.stem(normalizer.stop_words(normalizer.remove_punctuation(query)))
    return query


def weight_term_doc(term):
    dft = len(inverted_index[term][0])
    print(dft)
    for doc in inverted_index[term][0]:
     score = math.log10(inverted_index[term][0][doc][0] + 1)*math.log10(7562/dft)
     score_list[doc] += score



# def weight_term_query(term, query):


def main():
    query = get_query()
    for term in query:
        weight_term_doc(term)
    print_result_links(sort_score_list_by_index(score_list),workbook)



normalizer = NormalizeHandler(file)
workbook = openpyxl.load_workbook(file)
# normalizer.base_normalizer()
# normalizer.write_in_file()
inverted_index = normalizer.read_from_file("indexed_data.pkl")
score_list = [0] * len(inverted_index)
main()