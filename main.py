file = open("calories.txt","r")
calorie = []
calorieCounter = 0
    
for line in file:
    if line != "\n":
        calorieCounter += int(line.strip("\n"))
    elif calorieCounter > 0:
        calorie.append(calorieCounter)
        calorieCounter = 0

print(max(calorie))