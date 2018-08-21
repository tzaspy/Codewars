def getCount(inputStr):
    num_vowels = 0

    # your code here
    num_vowels= len(filter(lambda v: v in ['a','e','i','o','u'] ,inputStr))

    return num_vowels
