"""
Spam Bot
"""

import time
import argparse
from pynput.keyboard import Key, Controller

keyboard = Controller()

def send_message(message, repetitions) -> None:
    """
    Sends a specified message a given number of times with a delay in between.

    Args:
        message (str): The message you want to send.
        repetitions (int): Number of times the message will be sent.

    Returns:
        None
    """
    time.sleep(2) # Time cooldown, change if you want to

    # Checking if the message is a number or not
    if message.isnumeric():
        for i in range(1, int(message) + 1):
            keyboard.type(str(i))
            keyboard.press(Key.enter)
    else:
        for _ in range(repetitions):
            keyboard.type(message)
            keyboard.press(Key.enter)

def main() -> None:
    """
    Main function to parse command line arguments and initiate the message sending.

    Args:
        None

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        description='Spam a message using pynput')
    # Setting help messages
    parser.add_argument('--message', '-m',
                        required=True,
                        help='The message you want to send (between single quotes)')

    parser.add_argument('--reps', '-r',
                        type=int,
                        default=5,
                        help='Number of times the message will be sent (default: 5)')

    args = parser.parse_args()

    message = args.message
    repetitions = args.reps

    # Checking if the number of repetitions is greater than zero
    if repetitions <= 0:
        print('The number of repetitions must be greater than zero.')
    else:
        # Sending the message if everything went alright
        send_message(message, repetitions)

if __name__ == '__main__':
    main()
