#Part1
text = []

with open("day4/input.txt", "r") as f:
    for line in f:
        text.append(line.strip())

horizontal = 0
vertical = 0
diagonal = 0

def find_word(line):
    count = 0
    for i in range(len(line)):
        if line[i:i+4] == 'XMAS' or line[i:i+4] == 'SAMX':
            count+=1
    return count


for line in text:
    horizontal += find_word(line)

for i in range(len(text[0])):
    temp = ""
    for t in text:
        temp = temp + t[i]
    vertical += find_word(temp)

def diag_count(text):
    count = 0
    for l in range(len(text)):
        if l+4 <= len(text):
            for i in range(len(text[l])):
                if i+4 <= len(text[l]):
                    temp = text[l][i] + text[l+1][i+1] + text[l+2][i+2] + text[l+3][i+3]
                    if temp == "XMAS" or temp == "SAMX":
                        count+=1
    return count


def diag_count_2(text):
    count = 0
    for l in range(len(text)):
        if l >= 3:
            for i in range(len(text[l])):
                if i+4 <= len(text[l]):
                    temp = text[l][i] + text[l-1][i+1] + text[l-2][i+2] + text[l-3][i+3]
                    if temp == "XMAS" or temp == "SAMX":
                        count+=1
    return count

diagonal = diag_count(text)
diagonal2 = diag_count_2(text)

print(horizontal+vertical+diagonal+diagonal2)

#Part2

def mas_count(text):
    count = 0
    for l in range(len(text)):
        if l + 3 <= len(text):
            for i in range(len(text[l])):
                if i + 3 <= len(text[l]):
                    temp1 = text[l][i] + text[l+1][i+1] + text[l+2][i+2]
                    temp2 = text[l][i+2] + text[l+1][i+1] + text[l+2][i]
                    if (temp1 == "MAS" or temp1 == "SAM") and (temp2 == "MAS" or temp2 == "SAM"):
                        count+=1
    return count
