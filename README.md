# AUTO-SPAM

This script allows you to send a message multiple times using pyautogui. 
You can specify the message you want to send and the number of times it
will be sent. If the message is a number, it will send a sequence of numbers
from 1 to the specified number. If the message is not numeric, it will be sent
as-is


# Spam examples
Default spam message (5 times)
python `spam_bot.py` --mesage 'Sample Text'

Spam a message 10 times
>python spam_bot.py --message 'Sample Text' --reps 10

Using a number to spam
>python spam_bot.py --message 100
