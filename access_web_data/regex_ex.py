import re
hand = open('regex_sum_1452554.txt')
lst = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    if len(x) > 0:
        lst.extend(x)
#change the original string x in lst into int
lst = [int(x) for x in lst]
print(sum(lst))
