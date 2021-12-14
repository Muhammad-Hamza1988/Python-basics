user = int(input('Please enter the Number:  '))
if user % 2 != 0:    print('Weird')
elif user % 2 == 0 and user in range(2, 6):    print('Not Weird')
elif user % 2 == 0 and user in range(6, 21):    print('Weird')
elif user % 2 == 0 and user > 20:    print('Not Weird')
    

