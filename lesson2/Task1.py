Enterlean= input("Enter your list: ").split(' ')
search = input("Enter element: ")
score = 0 
for element in Enterlean:
    if search == element:
        score += 1
print(score)