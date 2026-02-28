subjects = []
total = 0
flag = False
for i in range(4): #getting subjects
    subjects.append(str(input(f'Please enter your subject {i + 1}: ')))

for s in range(len(subjects)): #getting score
    while True: #confirm datatype
        try:
            score = float(input(f'Please enter your score for subject {subjects[s]}: '))
            break
        except ValueError:
            print('Please enter a valid integer between 0 and 100.')
    while True: #confirm range
        if score < 0 or score > 100:
            print("Bullshit, Try again. ")
            score = float(input(f'Please enter your score for subject {subjects[s]}: '))
        else:
            break
    if score < 40:
        print(f'You did not pass since your {subjects[s]}"s score is less than 40.')
        flag = True
        break
    total = total + score

average = total / 4
if average < 60 and flag == False:
    print(f'You did not pass since your GPA({average}) is less than 60.')
elif flag == False:
    print(f'Yay you passed! (Your GPA is {average})')