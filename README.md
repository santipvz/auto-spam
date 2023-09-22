# AUTO-SPAM

This script allows you to send a message multiple times using pyautogui. 
You can specify the message you want to send and the number of times it
will be sent. If the message is a number, it will send a sequence of numbers
from 1 to the specified number. If the message is not numeric, it will be sent
as-is (if repetitions not specified, default repetitions are 5).

## Usage
For this script, we are using the library `pyautogui` so we need to install it first through our _OS_ console.

>Command for instalation <pre><code>pip install pyautogui</code></pre>

If it doesn't work you can try these other options:

### Linux / macOS
<pre><code>python3 -m pip install pyautogui</code></pre>
</code></pre>

### Windows
<pre><code>py -m pip install pyautogui</code></pre>
</code></pre>

After installing the library, you can finally use this script.
All you need to do is open your console on the same directory where you saved the _`spam_bot.py`_ and use the commands you can see below on Spam examples.

![Example command on _Visual Studio Code_ console on Windows](https://github.com/santipvz/auto-spam/assets/114695520/7fbc8db2-8bba-4448-a1f4-a2d820dc733a)

## Spam examples

* Default spam message (5 times) 
    <pre><code>python spam_bot.py --mesage 'Sample Text'</code></pre>
    </code></pre>

* Spam a message 10 times 
    <pre><code>python spam_bot.py --message 'Sample Text' --reps 10</code></pre>
    </code></pre>

* Using a number to spam 
    <pre><code>python spam_bot.py --message 100</code></pre>
    </code></pre>
