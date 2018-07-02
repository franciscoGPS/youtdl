import csv
def make_ids_table(file_name, array):
    ipdb.set_trace()
    with open(file_name+".csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(array)