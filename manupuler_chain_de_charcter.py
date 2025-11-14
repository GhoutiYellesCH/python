def operate(list_of_strings):
    list_of_strings.append("new string")
    print("A new string has been added to the end of the list.")
    for item in list_of_strings:
        print(item)

  
    list_of_strings.insert(0,"another string")
    print("Another string has been added to the beginning of the list.")
    for item in list_of_strings:
        print(item)

    index = int(input("give the index for deleting the element"))
    list_of_strings.pop(index)
    print("the indexit element was removed")
    for item in list_of_strings:
        print(item)

    list_of_strings.sort()
    print("The list has been sorted alphabetically.")
    for item in list_of_strings:
        print(item)

    list_of_strings.reverse()
    print("The order of the list has been reversed.")
    for item in list_of_strings:
        print(item)

    while len(list_of_strings) > 2:
        print("Element at index", len(list_of_strings) - 1, "has been removed.")
        list_of_strings.pop()

    for item in list_of_strings:
        print(item)

    return list_of_strings 

list_of_strings = ["hello world","cool world","jhon ammond", "networkshunk"]
print(list_of_strings)
operate(list_of_strings)