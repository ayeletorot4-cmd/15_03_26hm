#Exercise 1 – Group words by length
from collections import defaultdict

words=["apple","banana","kiwi","grape","melon","pear"]
def group_words_by_length(words: list) -> dict:
    '''

    :param words: list of words
    :return: dict { <length>: [list of words with that length] }
    '''
    dict_={}
    for word in words:
        length=len(word)
        if length not in dict_:
           dict_[length]=[]
        dict_[length].append(word)
    return dict_
print(group_words_by_length(words))