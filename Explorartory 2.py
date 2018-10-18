def countPositive(numbers):
    positiveCount = 0
    for number in numbers:
        if number > 0:
            positiveCount += 1
    return positiveCount


input_num = input("Enter a list of numbers comma seprated:")
#list_num = [12,-34,54,-12,2334,34,-323,23,-23]
#str_num = '1233435423232'
if type(input_num) == list:
    print 'We are searching in the list_num'
    print 'Total positive numbers in the list are:',countPositive(input_num)
else:
    raise TypeError('This is not a list')
