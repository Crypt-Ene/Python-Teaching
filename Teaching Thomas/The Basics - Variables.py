#   The basics: Variables
#
#
#   What is a variable:
#   A variable is a name that you give a value to, for instance, if you have 10 apples, 
#   you could represent that as a variable, you could say "yourApples = 10" or "x = 10"
#
#   It doesnt matter what the name of the variable is, but it's usually better to stick
#   with a name that makes sense, so that anyone would be able to tell what it might
#   represent at a glance
#
#
#
#   What can be a variable:
#   A variable can have almost anything as it's name or as it's value, you can represent
#   text, numbers, lists of information and even functions as a variable, they are
#   incredibly versitile
#
#   Values in variables have "types" which decide how the computer treats that data, for
#   instance, you can store "4" as either a number or a letter depending on how you want
#   to use it
#
#   if you store it as a letter, you'll treat it as text, which makes it easier to work
#   with when trying to print() something to the screen. Text values are known as
#   "Strings"
#
#   If you treat it as a whole number, the computer will treat it as digit, which means
#   you can perform math with it, like addition, multiplication etc. Whole number values
#   are known as "Integers"
#   
#   You could also treat it as a non-whole number, but you would only need to do that if
#   you actually had a non-whole number, however, these are very important when doing
#   things that need decimal points, like division etc. Non-whole number values are known
#   as "Floats"
#
#   
#
#   The importance of knowing variable types:
#   You can mostly ignore variable types in python because it automatically sets the type
#   of data depending on how it's presented, a string will be in quotations, an integer wont
#   and a float will have a decimal on the end, even if it's .0, however, sometimes you may
#   need to force a type onto a variable, like when getting input from a user, the user
#   cant specify if they want a number to be treated as text or as an integer, so you need
#   to use the "Type's function" to force it for them
#
#   a type function is a function that sets whatever is inside of it to that type, and if
#   it cant, it will raise an error
#   to set something to text, all i have to do is use str(), and put whatever i want to be
#   treat as text inside the brackets
#   For further demonstation, if x = 10, and i want x to be a string, i would write
#   x = str(x), which would set x to the stringified version of itself
#
#   Likewise for integers, to set it's type to a number all i have to do is use int(), and
#   again put whatever i want to become a number inside it. Let's say x = "100"
#   if i want x to be an number instead, i would say x = int(x)
#   However, if x = "One hundred", the program would crash when using int() on it, because it
#   is unable to turn actual letters into numbers.
#
#   With floats, the command is float(), using this on an integer will return the integer
#   with .0 on the end.
#   Notably, using int() on a float doesnt round it, it just cuts off the decimal point, for
#   instance, if i used x = int(9.9), x would equal 9, not 10
#
#   One more command of note is the type() command, which will return the type of whatever value
#   is in it
#
#
#
#   Below i have written some example code which should help demonstrate what exatly variables
#   and types are. Feel free to mess around with the names, values and commands to see if you
#   can do anything intresting
#   

strExample = "10"
intExample = 10
floatExample = 10.0

print(strExample + " This is a string, so it can be added to other strings with a plus symbol " + strExample)
print(strExample, "Strings can also be added using commas, which automatically include spaces for you", strExample)

print(intExample + intExample)
print("Those are integers so i cant add them onto text, instead, they're added together numeriacally")
print("But i can still use str() to treat them as text if i need to", str(intExample + intExample))

print(floatExample)
print("Like an integer, if i want to add it onto a string, i'll need to use str()")
print("It's worth noting though that if you use a float with an int, the result will be treat as a float even if it has no decimal places")

print(type(strExample), type(intExample), type(floatExample))