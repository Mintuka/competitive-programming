from math import log2, floor
n, l, r = map(int, input().split())
    
def is_one(number, index, count):
    if number <= 1:
        return number
    if count//2 + 1 == index:
        return number%2
    if index > count//2:
        index -= (count//2+1)
    return is_one(number//2, index, count//2)
count = 0
if n <= 1:
    print(n)
    exit(0)
total = 2**(floor(log2(n))+1)-1
    
for index in range(l, r+1, 1):
    count += is_one(n, index, total)
print(count)