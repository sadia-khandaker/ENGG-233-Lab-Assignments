province = input('Please enter your province two letter abbreviation (ex. AB for Alberta)):').upper()
income = float (input("Please enter your taxable(gross) income:"))

if province == 'AB':
    if income<= 40000:
         tax = 0.25
    elif income <= 80000:
        tax = 0.32
    elif income <= 120000:
        tax = 0.36
    else:
        tax = 0.39
elif province == 'SK' or province =='ON':
    if income <= 40000:
        tax = 0.25
    elif income <= 60000:
         tax = 0.30
    elif income <= 80000:
        tax = 0.35
    elif income <= 100000:
        tax = 0.40
    elif income <= 120000:
        tax = 0.45
    else:
        tax = 0.50    
elif province == 'BC':
    if income <= 20000:
        tax = 0.20
    elif income <= 35000:
        tax = 0.225
    elif income <= 50000:
        tax = 0.30
    elif income <= 65000:
        tax = 0.325
    elif income <= 80000:
        tax = 0.365
    elif income <= 100000:
        tax = 0.395
    elif income <= 120000:
            tax = 0.41
    else:
            tax = 0.44
else:
        print('Invalid input')

print('Province:', province)
print('Gross Income:', income)
print('Tax rate:', tax)
print('Tax Amount:',(tax*income))
print('Net Income:',(income - income * tax))