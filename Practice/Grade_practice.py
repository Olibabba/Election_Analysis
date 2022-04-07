#what is the score?
score=int(input("What is your test score?"))

#Determine the grade.
if score >= 90:
    print('YOU GOT AN A!!!')
else:
    if score >= 80:
        print('Your grade is a B! Not bad!')
    else:
        if score >= 70:
            print('Your grade is a C. And that\'s ok')
        else:
            if score >= 60:
                print('Your grade is a D. Do better.')
            else:
                print('YOU\'RE FAILING!')

#Determine the Grade Better
if score >= 90:
    print('YOU GOT AN A!!!')
elif score >= 80:
    print('Your grade is a B! Not bad!')
elif score >= 70:
    print('Your grade is a C. And that\'s ok')
elif score >= 60:
    print('Your grade is a D. Do better.')
elif:
    print('You\re failing')
