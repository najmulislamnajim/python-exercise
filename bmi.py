weight=float(input('Enter your weight in kilogram (kg) : '))
height=float(input('Enter your height in feet (ft) : '))
bmi=weight/((height*0.3048)**2)
rbmi=round(bmi,2)
print(f'Your BMI is {rbmi}!')
if rbmi<18.5:
    print('Your are Underweight!')
elif rbmi<25.0:
    print('Congratulations! You are Normal.')
else:
    print('You are Overweight!')