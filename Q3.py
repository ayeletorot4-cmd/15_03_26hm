#Exercise 3 – Group numbers by sign
def group_numbers(nums: list) -> dict:
    '''

    :param nums: list of numbers
    :return: dictionary with keys:
             "positive", "negative", "zero"
             and lists of numbers for each category
    '''
    dict_ = {"positive":[], "negative":[], "zero":[]}

    for num in nums:
        if num > 0:
            dict_["positive"].append(num)
        elif  num < 0:
            dict_["negative"].append(num)
        else:
            dict_["zero"].append(num)

    return dict_

nums=[4, -2, 0, 7, -5, 3]
print(group_numbers(nums))