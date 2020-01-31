'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?'''

def IsPandigital(list_new):
    result = False
    set_new = set(list_new)
    if len(list_new) == len(set_new) and (set_new == {1,2,3,4,5,6,7,8,9} or set_new == {'1','2','3','4','5','6','7','8','9'}) :
        result = True
    return result

def PandigitalMultiples():
    n = 1
    answer = []
    while n != 9876:
        final_number = ''
        for i in range(1, 10):
            final_number += str(n*i)
            if len(final_number) > 9:
                break
            if IsPandigital(list(final_number)):
                answer.append(final_number)
                break
        n += 1
    answer = [int(i) for i in answer] 
    return max(answer)

final = PandigitalMultiples()
print(final)