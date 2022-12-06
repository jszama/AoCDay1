file = open("calories.txt","r")
calorie = []
calorieCounter = 0
    
for line in file:
    if line != "\n":
        calorieCounter += int(line.strip("\n"))
    elif calorieCounter > 0:
        calorie.append(calorieCounter)
        calorieCounter = 0

# Highest calorie value
print(max(calorie))

# Top 3 calorie values added together
top1 = calorie.index(max(calorie))
top1val = max(calorie)
calorie.pop(top1)
top1 = calorie.index(max(calorie))
top2val = max(calorie)
calorie.pop(top1)
top1 = calorie.index(max(calorie))
top3val = max(calorie)
print(top1val+top2val+top3val)