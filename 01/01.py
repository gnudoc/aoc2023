from sys import argv
data = open(argv[1]).read().strip()
sum = 0
for line in data.split('\n'):
    sum_digits = []
    for count,val in enumerate(line):
        if val.isdigit():
           sum_digits.append(val)
    print(sum_digits)
    sum += int(sum_digits[0] + sum_digits[-1])
print(sum)
            
