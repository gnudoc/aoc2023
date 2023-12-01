from sys import argv
data = open(argv[1]).read().strip()
sum = 0
for line in data.split('\n'):
    sum_digits = [] # list will contain the numbers as strings eg ['2', '1', '4'] 
    for count,val in enumerate(line):
        if val.isdigit():
           sum_digits.append(val)
        for num,word in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            if line[count:].startswith(word):
                sum_digits.append(str(num+1)) # map the strings to the index, which is the value offset by 1
    print(sum_digits)
    sum += int(sum_digits[0] + sum_digits[-1])
print(sum)

            
