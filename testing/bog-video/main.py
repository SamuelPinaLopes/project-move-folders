number_inputs = int(input("write the number of inputs: "))
each_line = list()
list_characters = list()
equal = True

for times in range(number_inputs):
    each_line.append(str(input(" -> ")))

for index, lines in enumerate(each_line):
    list_characters = lines.split(' ')
    
    for character in list_characters:
        if int(character) == int(list_characters[0]):
            equal = True
        else:
            equal = False
            break
    print(f"for line {index + 1}, is {equal}")


print(each_line)