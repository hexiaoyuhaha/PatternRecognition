from collections import Counter
from nltk.tag import StanfordNERTagger


nerTagger = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')


def findType(item):
    '''

    :param item: could be Michelle,Gray,7627 Glacier Hill Pass, Raleigh,United States
    :return:
    '''
    ners = getNER(item.split())
    print ners
    tags = [a[1] for a in ners]
    counter = Counter(tags)
    return counter.most_common(1)[0][0]



def getNER(words):
    '''
    return name entities tags for words
    :param words: list of words
    :return: list of (word, name_entities) tuple
    '''
    return nerTagger.tag(words)


if __name__ == '__main__':

    corpus = []
    doc1 = "the quick brown fox jumps over the lazy dog"
    doc2 = "What is the airspeed of an unladen swallow ?"
    doc3 = "Rami Eid is studying at Stony Brook University in NY New York"


    # print 'ner', getNER(doc3.split())
    # ner [(u'Rami', u'PERSON'), (u'Eid', u'PERSON'), (u'is', u'O'),
    # (u'studying', u'O'), (u'at', u'O'), (u'Stony', u'ORGANIZATION'),
    # (u'Brook', u'ORGANIZATION'), (u'University', u'ORGANIZATION'),
    # (u'in', u'O'), (u'NY', u'LOCATION'), (u'New', u'LOCATION'), (u'York', u'LOCATION')]

    # print findType('Michelle')
    # print findType('Fort Myers')
    print findType('506 Buena Vista Alley')
    print findType('United States')
    print findType('Fort Myers')
    print findType('William Paterson University')
    print findType('Brook University')

'''
             id [u'O', u'O', u'O', u'O', u'O', u'O', u'O', u'O', u'O', u'O']
     first_name [u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON']
      last_name [u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON']
        Address [u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON']
        Zipcode ['ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP']
           City [u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON']
        Country [u'LOCATION', u'LOCATION', u'LOCATION', u'LOCATION', u'LOCATION', u'LOCATION', u'LOCATION', u'LOCATION', u'LOCATION', u'LOCATION']
          Phone ['PHO', 'PHO', 'PHO', 'PHO', 'PHO', 'PHO', 'PHO', 'PHO', 'PHO', 'PHO']
  Date of Birth ['DOB', 'DOB', 'DOB', 'DOB', 'DOB', 'DOB', 'DOB', 'DOB', 'DOB', 'DOB']
         Gender ['SEX', 'SEX', 'SEX', 'SEX', 'SEX', 'SEX', 'SEX', 'SEX', 'SEX', 'SEX']
 Credit Card No ['CRE', 'CRE', 'CRE', 'CRE', 'CRE', 'CRE', 'CRE', 'CRE', 'CRE', 'CRE']
Social Security No ['SSN', 'SSN', 'SSN', 'SSN', 'SSN', 'SSN', 'SSN', 'SSN', 'SSN', 'SSN']
University Education [u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON', u'PERSON']
          Email ['EMA', 'EMA', 'EMA', 'EMA', 'EMA', 'EMA', 'EMA', 'EMA', 'EMA', 'EMA']
        Comment [u'O', u'O', u'O', u'O', u'O', u'O', u'O', u'O', u'O', u'O']
final_pred
[(u'O', 1.0), (u'PERSON', 1.0), (u'PERSON', 1.0), (u'PERSON', 1.0), ('ZIP', 1.0), (u'PERSON', 1.0), (u'LOCATION', 1.0), ('PHO', 1.0), ('DOB', 1.0), (u'O', 1.0), ('CRE', 1.0), ('SSN', 1.0), (u'PERSON', 1.0), ('EMA', 1.0), (u'O', 1.0)]



             id ['UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK']
     first_name ['UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK']
      last_name ['UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK']
        Address ['UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK']
        Zipcode ['ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP', 'ZIP']
           City ['UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK']
        Country ['UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK']
          Phone ['PHO', 'PHO', 'PHO', 'PHO', 'PHO', 'PHO', 'PHO', 'PHO', 'PHO', 'PHO']
  Date of Birth ['DOB', 'DOB', 'DOB', 'DOB', 'DOB', 'DOB', 'DOB', 'DOB', 'DOB', 'DOB']
         Gender ['SEX', 'SEX', 'SEX', 'SEX', 'SEX', 'SEX', 'SEX', 'SEX', 'SEX', 'SEX']
 Credit Card No ['CRE', 'CRE', 'CRE', 'CRE', 'CRE', 'CRE', 'CRE', 'CRE', 'CRE', 'CRE']
Social Security No ['SSN', 'SSN', 'SSN', 'SSN', 'SSN', 'SSN', 'SSN', 'SSN', 'SSN', 'SSN']
University Education ['UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK']
          Email ['EMA', 'EMA', 'EMA', 'EMA', 'EMA', 'EMA', 'EMA', 'EMA', 'EMA', 'EMA']
        Comment ['UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK']
final_pred
[('UNK', 1.0), ('UNK', 1.0), ('UNK', 1.0), ('UNK', 1.0), ('ZIP', 1.0), ('UNK', 1.0), ('UNK', 1.0), ('PHO', 1.0), ('DOB', 1.0), ('SEX', 1.0), ('CRE', 1.0), ('SSN', 1.0), ('UNK', 1.0), ('EMA', 1.0), ('UNK', 1.0)]

'''