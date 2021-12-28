# TimeInPC - v1

Program to monitor time spended in PC

Simple program that uses a function to capture the datime.now when executed.

The datetime taked is added to a empty list called 'data'. When the list reach lenght == 2, it subtract the data[1] from data[0] to get the time between two function execution (supposly the time spended in pc), that it also added to 'data'.

So, when 'data' get those three information (entrance and exit hour, and time between each other), it write them to a csv file, then clean 'data'.

I pretend to do some upgrades, as monitor hardware activit (so as i dont need to execute a function, because i may forget to do, and than my program fails) and create a 'assistive touch' as Apple's Siri.

v1 - Just backend

Next version: simple UI




