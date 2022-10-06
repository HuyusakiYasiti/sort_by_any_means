MAXIMUM = 4

n = int()

temporaryList = list(range(MAXIMUM))
indexsList = list()

def IndexRequest(value, answers):
    choice = str()
    answer = str()

    possibleNumbers = list()

    for number in range(MAXIMUM):
        if number not in answers:
            possibleNumbers.append(number)

    for suitable in possibleNumbers:
        choice = choice + ", {}".format(suitable)
    choice = choice.lstrip(", ")
    print("What is the index of '{}'?".format(value))

    answer = input("Choose from {}.: ".format(choice))

    try:
        answer = int(answer)
    except ValueError:
        print("please input number.")
        answer = IndexRequest(value, answers)
        return answer

    if answer in possibleNumbers:
        return answer
    else:
        print("'{}' is invalid number.".format(answer))
        answer = IndexRequest(value, answers)
        return answer

def SortAsOrdered(orders, i=0, orderedGoods=list(0 for x in range(MAXIMUM))):
    for order in orders:
        orderedGoods.insert(order, i)
        del orderedGoods[order + 1]
        i = i + 1
    return orderedGoods

print(temporaryList)

while len(temporaryList) != 0:
    n = temporaryList.pop(0)
    indexsList.append(IndexRequest(n, indexsList))
temporaryList = SortAsOrdered(indexsList)

print(temporaryList)
temporaryList.sort()
print(temporaryList)
