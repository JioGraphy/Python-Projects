numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break  # Exit the loop when num is 3
    if num == 2:
        continue  # Skip the iteration when num is 2
    print(num)
else:
    print("Loop completed without encountering a break statement")
