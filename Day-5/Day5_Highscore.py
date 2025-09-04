student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
Total_sum = 0
for value in student_scores:
    Total_sum += value
print(Total_sum)
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

#BuzzFizz

for number in range(1,101):
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    
    else:
        print(number)
