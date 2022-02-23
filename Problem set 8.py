import random
from textwrap import indent 

# Making a fraud multiplication 
def fraudMulti(number):
    wrong_num = random.randint(0,3)
    table = [i*number for i in range(1,11)]
    table[wrong_num] += wrong_num

    return table

if __name__ == '__main__':
    ask = int(input('Enter the number you want multiplication of = '))
    check = fraudMulti(ask)
    print(check)
    index = 0
    ans = 0
    for j in range(1,11):
        if ask*j == check[index]:
            index += 1
        else :
            ans = index

    print(ans)