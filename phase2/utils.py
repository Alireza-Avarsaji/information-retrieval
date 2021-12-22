# print 10 result links
import itertools

# ? print result links
def print_result_links(list, workbook):
    output_list = list[0:10]
    for result in output_list:
        print( workbook.active.cell(row=result+1, column=2).value)
        print(workbook.active.cell(row=result + 1, column=3).value)

# ? sort score list by index
def sort_score_list_by_index(score_list):
    li = []
    for i in range(len(score_list)):
        li.append([score_list[i], i])
    li.sort()
    sort_index = []
    for x in li:
        sort_index.append(x[1])
    return sort_index[::-1]



# ? make champion list from scored inverted index
def make_champion_list(list):
        inverted_index = list
        champion = {}
        for word in inverted_index:
            champion[word] = []
            champion[word].append({})
            for doc in inverted_index[word][0]:
                champion[word][0][doc] = inverted_index[word][0][doc][1]
            champion[word][0] = sort_dictionary(champion[word][0])
            champion[word][0] = dict(itertools.islice(champion[word][0].items(), 0, 4))
        return champion


# ? sorts a dictionary
def sort_dictionary(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1],reverse=True))