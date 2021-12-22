from collections import OrderedDict

from normalizer import NormalizeHandler
import openpyxl
import math
from utils import print_result_links, sort_score_list_by_index, make_champion_list

file = "IR1_7k_news.xlsx"

# ? get user query
def get_query():
    query = input("what are you looking for?  ")
    query = query.strip()
    query = normalizer.stem(normalizer.stop_words(normalizer.remove_punctuation(query)))
    return query

# ? calculate score of docs for a term
def weight_term_doc(term):
    dft = len(inverted_index[term][0])
    for doc in inverted_index[term][0]:
     score = math.log10(inverted_index[term][0][doc][0] + 1)*math.log10(7562/dft)
     score_list[doc] += score


# ? update score list by champion list
def champion_weight_term_doc(term, champion_list):
    for doc in champion_list[term][0]:
        score_list[doc] += champion_list[term][0][doc]


# ? adds score to inverted index
def add_score_to_inverted_index(inverted_index):
    temp = inverted_index
    for term in temp:
        dft = len(inverted_index[term][0])
        for doc in inverted_index[term][0]:
            score = math.log10(inverted_index[term][0][doc][0] + 1) * math.log10(7562 / dft)
            temp[term][0][doc].append(score)
    return temp



def main():
    while(True):
        query = get_query()
        for term in query:
            weight_term_doc(term)
        print_result_links(sort_score_list_by_index(score_list),workbook)
        # print(inverted_index)


def main_part2():
    champion_list = make_champion_list(add_score_to_inverted_index(inverted_index))
    while(True):
        query = get_query()
        for term in query:
            count = len(query)
            champion_weight_term_doc(term,champion_list)
        print_result_links(sort_score_list_by_index(score_list),workbook)



############################################################
# main block of code
normalizer = NormalizeHandler(file)
workbook = openpyxl.load_workbook(file)
# inverted_index = normalizer.base_normalizer()
# normalizer.write_in_file(inverted_index)
inverted_index = normalizer.read_from_file("indexed_data.pkl")
score_list = [0] * len(inverted_index)
# main()
main_part2()
############################################################


# inverted index with score
# print(make_champion_list(add_score_to_inverted_index(inverted_index)))
