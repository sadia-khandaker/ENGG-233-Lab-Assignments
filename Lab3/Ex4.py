mortgagetype = input('Enter the type of mortgage (open/closed): ').lower()

termduration = input('Enter term duration (1,3, or 5): ')



if mortgagetype == 'open':

    if termduration == '1':

        print('The mortgage rate for the given input is 7.10%')

    elif termduration == '3':

        print('The mortgage rate for the given input is 7.50%')

    elif termduration == '5':

        print('The mortgage rate is unavailable for the given input')

    else:

        print('Invalid Term Duration')

elif mortgagetype == 'closed':

    if termduration == '1':

        print('The mortgage rate for the given input is 5.30%')

    elif termduration == '3':

        print('The mortgage rate for the given input is 5.00%')

    elif termduration == '5':

        print('The mortgage rate for the given input is 5.75%')

    else:

        print('Invalid Term Duration')

else:

    print('Invalid mortgage type entered.')

