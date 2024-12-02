#Part1
import csv

left = []
right = []

with open("day1/input.csv", "r") as f:
    r = csv.reader(f)
    for row in r:
        left.append(row[0])
        right.append(row[1])

left.sort()
right.sort()

sum = 0

for i in range(len(left)):
    val = int(left[i]) - int(right[i])
    sum+=abs(val)

print(sum)

#Part2
def counter(operand, target_list):
    sum = 0
    for item in target_list:
        if item == operand:
            sum+=1
    return sum

sim_score = 0

for item in left:
    count = counter(item, right)
    score = count * int(item)
    sim_score += score

print(sim_score)