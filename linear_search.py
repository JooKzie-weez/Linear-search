array = [432,543432,756,345,5786354,756,234,76,342,76,24,76,423,76]

search_term = int(input("please input a search term, "))
Found = False
index = 0

while index < len(array) and Found == False:
    if array[index] == search_term:
        Found = True
    else:
        index = index + 1

    if Found == True:
        print("item was found at", index)
    else:
        print("item not found")

