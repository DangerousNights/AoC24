#Part1
import re

with open("day3/input.txt", "r") as f:
    input_text = f.read()

t = re.findall(r'mul\(\d\d?\d?,\d\d?\d?\)', input_text)

def mul(mul_str):
    num1 = int(mul_str[4:mul_str.find(',')])
    num2 = int(mul_str[mul_str.find(',')+1:-1])
    return num1 * num2

total = 0

for mul_str in t:
    total += mul(mul_str)

print(total)

#Part2

pointer = 0
mul_dict = {}

for mul_str in t:
    k = input_text.find(mul_str, pointer)
    pointer = k
    mul_dict[k] = mul_str

dn = re.compile(r'don\'t\(\)')
d = re.compile(r'do\(\)')

dont_ranges = []
pointer = 0

for i in range(len(re.findall(r'don\'t\(\)', input_text))):
    if dn.search(input_text, pointer) is None:
        break
    if d.search(input_text, dn.search(input_text, pointer).end()) is None:
        end = len(input_text)
    else:
        end = d.search(input_text, dn.search(input_text, pointer).end()).start()
    dont_ranges.append([dn.search(input_text, pointer).start(), end])
    pointer = end

total_2 = 0

for k,v in mul_dict.items():
    temp = mul(v)
    for r in dont_ranges:
        if r[0] < k < r[1]:
            temp = 0
    total_2 += temp

print(total_2)