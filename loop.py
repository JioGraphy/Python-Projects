
counter = 0

while counter <= 5:
    print(counter)
    counter += 1
    if counter == 2:
        continue
        print('Skip 2, proceeds to {}'.format(counter))
        
    if counter == 4:
        print('Iteration = {}'.format(counter))
        break
