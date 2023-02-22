score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

total_score = 0
total_time = 0

for i in range(20):
    subject, time, level = input().split()
    if level != "P":
        total_time += float(time)
        total_score += score[level]*float(time)

print(total_score/total_time)