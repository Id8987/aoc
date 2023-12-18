f = open("inputs.txt", "r")


def extract_numbers(tab):
    """
    grab the two digits: tab[0]['number'] and tab['lastElement]['number]

    Parameters:
    - arr (list)
    Ex: [{'startAtIndex': 7, 'number': 1}, {'startAtIndex': 18, 'number': 2}, {'startAtIndex': 12, 'number': 4}]

    Returns:
        an integer : concatenation of first and last digits from tab element'number key
    """
    if tab == []:
        return 0
    elif len(tab) == 1:
        return int(str(tab[0]["number"])*2) 
    else:
        digit_len = len(tab)
        return int(str(tab[0]["number"]) + str(tab[digit_len -1]["number"]))  
     
def quick_sort_for_my_special_tab(tab):
    """
    Quick Sort

    Parameters:
    - arr (list): La liste à trier.

    Returns:
   s    Sorted list
    """
    if len(tab) <= 1:
        return tab
    pivot = tab[len(tab)//2]
    middle = [element for element in tab if element["startAtIndex"] == pivot["startAtIndex"]]
    left = [element for element in tab if element["startAtIndex"] < pivot["startAtIndex"]]
    right = [element for element in tab if element["startAtIndex"] > pivot["startAtIndex"]]
    
    return quick_sort_for_my_special_tab(left)+ middle +quick_sort_for_my_special_tab(right)
  
        
    
def first_and_last(word):
    dictionary = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    digits = []
    
    for j in [1,3,4,5]:
        r = 0
        for i in range(0, len(word)-j+1):
            r = i+j
            if word[i:r] in dictionary.keys():
                # digits.append(dictionary[word[i:r]])
                digits.append({"number":dictionary[word[i:r]], "startAtIndex":i})
            if word[i:r] in ["0","1","2","3","4","5","6","7","8","9"]:
                # print(word[i:r])
                digits.append({"number":int(word[i:r]), "startAtIndex":i})
    return quick_sort_for_my_special_tab(digits)
    
        
def solution():
    """
    Return the sum of all numbers on every word in the iput file

    Parameters:
    - None

    Returns:
    None: integer
    """
    sum = 0
    for word in f:
        sum += extract_numbers(first_and_last(word))
    print(sum)
    return sum

solution()