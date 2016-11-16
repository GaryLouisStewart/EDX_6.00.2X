List = [('Gold', 10, 500), ('Silver', 5, 200), ('Diamond', 2, 2000), ('Platinum', 20, 1000)]
aList = sorted(List, key =  lambda x : x[2]) # sort the list above

def plunder(aList, c):
    aList[-1] = list(aList[-1])
    i = aList[-1]
    r = 0
    if c > 0 and i[1] != 0:
        c -= 1
        i[1] -=1
        r += 1
        return plunder(aList, c-r)
    elif c == 0:
        pass
        print('Done')
    else:
        return plunder(aList[:-1], c-r)

plunder(aList, 10)
print(plunder(aList, 100))