'''
This is a python script for determine the data format using
regular expression and external third party python library.

Identifiable data columns includes:
    Phone Number
    DOB
    Email address
    Person Name
    Location (Country, city)
    SSN
    Credit Card Number
    ZipCode

Currently, support csv file that doesn't not have meta data.
Can be extend to streamming data and NoSQL data later.\

Input: String data

if alphabetic:
	match Person Name
    match Location
    default unknowfield
else:
    match Email
	match DOB
	match Phone Number
	match Credit Card Number
	match SSN
	match Zipcode
	defalt unknowfield
'''

import csv
import re
from collections import Counter

names = {
    'PER': "Person Name",
    'LOC': "Location",
    'UNK': "unknowfield",
    'EMA': "Email",
    'DOB': "DOB",
    'PHO': "Phone Number",
    'CRE': "Credit Card Number",
    'SSN': "SSN",
    'ZIP': "Zipcode"
}

# This defines the regular expression, column name for each field
regEXP = {
    'EMA': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    'DOB': r'\d{1,2}[\-\/]\d{1,2}[\-\/]\d{2,4}',
    'PHO': r'\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*',
    'CRE': r'(?:\d[ -]*?){13,16}',
    'SSN': r'(?!\b(\d)\1+-(\d)\1+-(\d)\1+\b)(?!123-45-6789|219-09-9999|078-05-1120)(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}',
    'ZIP': r'[0-9]{5}(?:-[0-9]{4})?'
}

# This defines the order we are going to check
regName = ['EMA', 'DOB', 'PHO', 'CRE', 'SSN', 'ZIP']


def readFirst10LineFromCSV(filepath, linelimit):
    with open("Pattern_recog_data.csv") as csvfile:

        reader = csv.reader(csvfile, delimiter=',')
        data = []
        i = 0
        for row in reader:
            if i < linelimit:
                i += 1
                assert len(row) == 15
                data.append(row)
            else:
                break
    return data





def predict_type(item):
    if item.isalpha():
        return 'PER'
    else:
        for type_name in regName:
            regexpstr = regEXP[type_name] + r'$'
            pattern = re.compile(regexpstr)
            match = pattern.match(item.strip())
            if match is not None:
                return type_name
    return 'UNK'



def vote(col):
    '''

    return the majority label in this col
    :param col: a list of strings
    :return:
    '''
    counter = Counter(col)
    return (counter.most_common(1)[0][0], counter.most_common(1)[0][1]*1./len(col))


if __name__ == "__main__":

    linelimit = 10  # only read the first 10 line
    data = readFirst10LineFromCSV("Pattern_recog_data.csv", linelimit)
    n = len(data)  # num_rows
    m = len(data[0])  # num_cols

    data_pred = []
    for row in data:
        row_pred = []
        for item in row:
            pred = predict_type(item)
            row_pred.append(pred)
            data_pred.append(row_pred)

    headerstr = "id,first_name,last_name,Address,Zipcode,City,Country,Phone,Date of Birth,Gender,Credit Card No,Social Security No,University Education,Email,Comment"
    header = headerstr.split(",")

    final_pred = []
    for j in range(m):
        col = [data_pred[i][j] for i in range(n)]
        print "%15s" % header[j], col
        final_pred += [vote(col)]
    print "final_pred\n", final_pred


    