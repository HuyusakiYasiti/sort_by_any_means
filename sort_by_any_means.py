def main():

    MAXIMUM_LENGTH = 4


    temporaryList = list(range(MAXIMUM_LENGTH))

    indexsList = list()


    print(temporaryList)


    while len(temporaryList) != 0:

        n = temporaryList.pop(0)

        indexsList.append(IndexRequest(n, indexsList, MAXIMUM_LENGTH))


    temporaryList = SortAsOrdered(indexsList, MAXIMUM_LENGTH)

    print(temporaryList)


    temporaryList.sort()

    print(temporaryList)








def IndexRequest(value, answers, length):

    possibleNumbers = list()

    choice = str()


    for number in range(length):

        if number not in answers:

            possibleNumbers.append(number)


    for suitable in possibleNumbers:

        choice = choice + "{}, ".format(suitable)


    choice = choice.rstrip(", ")





    while True:

        print("What is the index of '{}'?".format(value))


        answer = input("Choose from {}.: ".format(choice))

        try:

            answer = int(answer)

        except ValueError:

            print("please input positive integer value.")

            continue


        if answer not in possibleNumbers:

            print("'{}' is invalid number.".format(answer))

            continue


        break




    return answer








def SortAsOrdered(orders, length):

    orderedGoods=list(0 for x in range(length))


    for i, order in enumerate(orders):

        orderedGoods.insert(order, i)

        del orderedGoods[order + 1]


    return orderedGoods







if __name__ == "__main__":

    main()

