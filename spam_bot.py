from pynput.keyboard import Key, Controller
import time
import argparse

keyboard = Controller()

def send_message(message, repetitions):
    time.sleep(5) # Time in seconds you have until it starts typing. Change it if you want other cooldown

    # Checking if the message is a number not
    if message.isnumeric(): 
        for i in range(1, int(message) + 1):
            keyboard.type(str(i))
            keyboard.press(Key.enter)
    else:
        for _ in range(repetitions):
            keyboard.type(message)
            keyboard.press(Key.enter)

def main():
    parser = argparse.ArgumentParser(
        description='Spam a message using pynput')
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
