f = open("./inputs.txt", "r")

sum = 0
    
def FirstAndLast(word):
    digits = []
    for letter in word:
        if letter.isdigit():
            digits.append(int(letter))
    if digits == []:
        return 0
    elif len(digits) == 1:
        return int(str(digits[0])*2) 
    else:
        digit_len = len(digits)
        return int(str(digits[0]) + str(digits[digit_len -1]))   


def solution():
    for word in f:
        sum += FirstAndLast(word)
    return sum

solution()