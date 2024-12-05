#Part1
import csv

rules = []
updates = []

with open("day5/rules.csv", "r") as f1:
    r = csv.reader(f1)
    for row in r:
        rules.append(row)

with open("day5/updates.csv", "r") as f2:
    r = csv.reader(f2)
    for row in r:
        line = []
        for cell in row:
            if cell != "":
                line.append(cell)
        updates.append(line)

def check_update(update, rules):
    applicable_rules = []
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            applicable_rules.append(rule)
    for rule in applicable_rules:
        if update.index(rule[0]) > update.index(rule[1]):
            return ["fail", applicable_rules]
    return update[(len(update)-1)//2]


total = 0

for update in updates:
    u = check_update(update, rules)
    if u[0] == "fail":
        continue
    else:
        total += int(u)

print(total)

#Part2

def fix_update(update, applicable_rules):
    rule_dict = {}
    for rule in applicable_rules:
        if rule[0] in rule_dict.keys():
            rule_dict[rule[0]].append(rule[1])
        else:
            rule_dict[rule[0]] = [rule[1]]
    initial = [k for k in sorted(rule_dict, key=lambda k: len(rule_dict[k]), reverse=True)]
    for k,v in rule_dict.items():
        for val in v:
            if val not in initial:
                initial.append(val)
        if k not in initial:
            initial.insert(k, 0)
        else:
            temp = []
            for val in v:
                temp.append(initial.index(val))
            min_index = min(temp)
            if initial.index(k) > min_index:
                initial.insert(initial.pop(initial.index(k)), max(min_index-1, 0))
    if len(update) != len(initial):
        return "fail length check"
    for item in update:
        if item not in initial:
            return "fail item check"
    return check_update(initial, applicable_rules)


total2 = 0

for update in updates:
    u = check_update(update, rules)
    if u[0] == "fail":
        temp = fix_update(update, u[1])
        total2 += int(temp)

print(total2)