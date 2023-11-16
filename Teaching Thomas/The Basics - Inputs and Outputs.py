#   The basics: Input and Output
#
#   Where do we get input and output:
#   In python, you'll be talking to the machine with through the "shell", which is just
#   where the code will output stuff to and go to for input from you.
#   The shell can only recieve and send text, and without it, you would have no idea if
#   your code worked or not.
#
#
#
#   How do you send an output:
#   Sending an output is as easy as writing the print() command, whatever you put inside
#   the brackets, will be evaluated, then turned into text and sent to the screen.
#   The print command is pretty much the only way you can see data from your script, so
#   it's vital that you learn how to use well if you want to save yourself a lot of
#   hassle.
#
#   //This isnt the basics//
#   The print command has 2 main modes, the default mode evaluates everything inside it
#   then turns it all into text and outputs, but the second mode uses formatting, if
#   you put a variable inside curly brackets {} in this mode the variable will be treat
#   as text from the beginning, removing the need to use str() on it.
#   To use the formatting mode, simply put a "f" at the beginning of the print statement
#   for instance, if x = "And this is a formatted variable" and y = 10
#   print(f"This is a string {x} {y}") would output
#   "This is a string And this is a formatted variable 10"
#   //End of the non-basic stuff//
#
#
#
#   How to get inputs:
#   Getting input from the user is almost as important as displaying an output to them,
#   you can get input from the user with the input() command, however it's important that
#   you remember to assign this input to a variable, or else the input will just be
#   recieved and not saved anywhere, which can still be usefull sometimes, but you can save
#   the input by instead using x = input(), which will save whatever you input to the
#   variable x.
#   This still isnt very usefull though, since you user can't tell what they're supposed to
#   be inputting, you can fix this by treating the input() command like the print command
#   and putting text or variable inside it's brackets, when you do this, the input() will
#   also output whatever's inside it, so you can tell the user exactly what you want them
#   to input
#
#
#
#   Below i've attached some example code, which should help you get to understand exactly
#   how inputs and outputs work, feel free to tamper with the code and try to get it do
#   something intresting

x = input("Hi, please enter something: ")
print(x)
y = input("Please input another thing: ")
print(x, y)
print(f"Even if you inputted numbers, this will still join them to the text {x} {y}")
print("")
input("You can use empty inputs to wait for a user to read something, press enter to continue")
print(input(input("Please ask a question: ")))