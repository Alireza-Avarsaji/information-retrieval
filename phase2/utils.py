# print 10 result links
def print_result_links(list, workbook):
    output_list = list[0:10]
    for result in output_list:
        print( workbook.active.cell(row=result+1, column=2).value)


def sort_score_list_by_index(score_list):
    li = []
    for i in range(len(score_list)):
        li.append([score_list[i], i])
    li.sort()
    sort_index = []
    for x in li:
        sort_index.append(x[1])
    return sort_index[::-1]
