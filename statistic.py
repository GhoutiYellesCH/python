def statistics(numbers):
    sum = 0
    max_value = 0  
    total = 0
    pairlist = []
    for number in numbers:
        if number%2==0:
            pairlist.append(number)
        if number > max_value: 
            max_value = number 
        sum += number 
        total += 1 
    average = sum / total 
    print("the sum is :",sum)
    print("the avrege is :",average)
    print("the max value is :", max_value)
    return pairlist
        
numbers = [1,2,3,4,5]

pairlist = []
pairlist = statistics(numbers)

for n in pairlist:
    print(n)