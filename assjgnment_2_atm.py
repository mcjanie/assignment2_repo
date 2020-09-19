"""
The following program is designed to determine the user's pin code.
"""
if __name__ == '__main__':

    valid_pin = '1234'
    attempt = 0
    while attempt < 3:
        pin_code = input('Please enter your 4-digit PIN:')
        attempt += 1
        if pin_code == valid_pin:
            print('PIN accepted!')
            break
        if pin_code != valid_pin and attempt == 2:
            print(f'Incorrect PIN. Please try again. You have {3 - attempt}\
 attmept remaining.')
        if pin_code != valid_pin and attempt != 2:
            print(f'Incorrect PIN. Please try again. You have {3 - attempt}\
 attempts remaining.')
        if attempt == 3 and pin_code != valid_pin:
            print("For security purposes, your account has been locked.")
            break
