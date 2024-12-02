# Part1
import csv

input_data = []

with open("day2/input.csv", "r") as f:
    r = csv.reader(f)
    for row in r:
        report = []
        for item in row:
            if item != "":
                report.append(int(item))

        input_data.append(report)

output = []
for row in input_data:
    for i in range(len(row)):
        if i == 0:
            continue
        elif i == 1:
            check = row[i] - row[0]
            if abs(check) > 3 or check == 0:
                output.append("unsafe")
                break
            if row[i] > row[0]:
                increasing = True
            elif row[i] == row[0]:
                output.append("unsafe")
                break
            elif row[i] < row[0]:
                increasing = False
        else:
            check = row[i] - row[i - 1]
            if abs(check) > 3 or check == 0:
                output.append("unsafe")
                break
            elif (check > 0 and increasing is False) or (check < 0 and increasing is True):
                output.append("unsafe")
                break
            elif i == len(row) - 1:
                output.append("safe")
            else:
                continue

print(output.count("safe"))

# part2
output = []
def check_report(row, recur=True):
    difs = []
    for i in range(len(row)):
        if i == 0:
            continue
        else:
            difs.append(row[i] - row[i-1])
    negs = sum(n<0 for n in difs)
    pos = sum(n>0 for n in difs)
    zeroes = sum(n==0 for n in difs)
    magnitude = sum(abs(n)>3 for n in difs)
    if min([negs, pos]) + zeroes + magnitude == 0:
        return 0
    if recur:
        for i in range(len(row)):
            temp = row.copy()
            temp.pop(i)
            result = check_report(temp, recur=False)
            if result == 0:
                return 0
    return min([negs, pos]) + zeroes + magnitude


for row in input_data:
    output.append(check_report(row))

print(output.count(0))