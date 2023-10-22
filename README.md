# AUTO-SPAM

This script allows you to send a message multiple times using pynput. 
You can specify the message you want to send and the number of times it
will be sent. If the message is a number, it will send a sequence of numbers
from 1 to the specified number. If the message is not numeric, it will be sent
as-is (if repetitions not specified, default repetitions are 5).

<p align="center">
   <img src="https://github.com/santipvz/auto-spam/actions/workflows/pylint.yml/badge.svg/" alt="Tests">
   <img src="https://img.shields.io/badge/Version-2.0-blue/" alt="Static Badge">
</p>

## Usage
For this script, we are using the library `pynput` so we need to install it first through our _OS_ console.

>Command for instalation <pre><code>pip install pynput</code></pre>

After installing the library, you can finally use this script.
All you need to do is open your console on the same directory where you saved the _`spam_bot.py`_ and use the commands you can see below on Spam examples.

![Example command on _Visual Studio Code_ console on Windows](https://github.com/santipvz/auto-spam/assets/114695520/7fbc8db2-8bba-4448-a1f4-a2d820dc733a "Example command on Visual Studio Code console on Windows")

Once you executed the command on the console, you need to place and click your mouse on the area where you want to send the messages, for example a WhatsApp chat.

## Spam examples
> [!NOTE]
> Remember that in Linux you must use _`python3`_ instead of _`python`_ for the script to work.

* Default spam message (5 times) 
    <pre><code>python spam_bot.py --mesage 'Sample Text'</code></pre>
    </code></pre>

* Spam a message 10 times 
    <pre><code>python spam_bot.py --message 'Sample Text' --reps 10</code></pre>
    </code></pre>

* Using a number to spam 
    <pre><code>python spam_bot.py --message 100</code></pre>
    </code></pre>



> [!WARNING]  
> If you dont set your mouse on the correct place you could make a mess, so make sure that you have everything prepared before spamming someone.
