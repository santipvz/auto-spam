# AUTO-SPAM

This script allows you to send a message multiple times using pyautogui. 
You can specify the message you want to send and the number of times it
will be sent. If the message is a number, it will send a sequence of numbers
from 1 to the specified number. If the message is not numeric, it will be sent
as-is (if repetitions not specified, default repetitions are 5).


# Spam examples

Default spam message (5 times) 
<pre><code>python spam_bot.py --mesage 'Sample Text'</code></pre>
</code></pre>

Spam a message 10 times 
<pre><code>python spam_bot.py --message 'Sample Text' --reps 10</code></pre>
</code></pre>

Using a number to spam 
<pre><code>python spam_bot.py --message 100</code></pre>
</code></pre>
