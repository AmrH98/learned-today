#Finding Numbers in a Haystack
#In this assignment read through and parse a file with text and numbers. extract all the numbers in the file and compute the sum of the numbers.

import re

hay = open("regex_sum_482613.txt")
num = list()
for line in hay:
    line = line.rstrip()
    nums = re.findall('([0-9]+)',line)
    if len(nums) > 0 :
        for n in nums:
            n = float(n)
            num.append(n)
print(sum(num))

#import re
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
