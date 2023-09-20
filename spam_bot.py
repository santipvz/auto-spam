import pyautogui
import time
import argparse

def send_message(message, repetitions):
    time.sleep(5) # Time in seconds you have until it starts typing. Change it if you want other cooldown

    # Checking if the message is a number not
    if message.isnumeric(): 
        for i in range(1, int(message) + 1):
            pyautogui.typewrite(str(i))
            pyautogui.press('enter')
    else:
        for _ in range(repetitions):
            pyautogui.typewrite(message)
            pyautogui.press('enter')

def main():
    parser = argparse.ArgumentParser(
        description='Spam a message using pyautogui',
        epilog= '''
        This script allows you to send a message multiple times using pyautogui. 
        You can specify the message you want to send and the number of times it
        will be sent. If the message is a number, it will send a sequence of numbers
        from 1 to the specified number. If the message is not numeric, it will be sent
        as-is.
        ''')
    # Setting help messages
    parser.add_argument('--message', required=True, help='The message you want to send (between ' ')')
    parser.add_argument('--reps', type=int, default=5, help='Number of times the message will be sent (default: 5)')

    args = parser.parse_args()

    message = args.message
    repetitions = args.reps

    # Checking if number of repetitions is greater than zero
    if repetitions <= 0:
        print('The number of repetitions must be greater than zero.')
    else:
        # Sending the message if everything went allright
        send_message(message, repetitions)

if __name__ == '__main__':
    main()
