# print 10 result links
def print_result_links(list, workbook):
    output_list = list[0:10]
    for result in output_list:
        print(workbook.active.cell(row=result+1, column=2).value)