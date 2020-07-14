def to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


print("Welcome to this time converter")

cont = 'y'
while(cont.lower() == 'y'):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversation? [ y to continue] ")

print("Good Bye!")

>>> import os
>>> print("HOME: " + os.environ.get("HOME", ""))
HOME: C:\Users\Hp
>>> print("SHELL: " + os.environ.get("SHELL", ""))
SHELL: 
>>> print("FRUIT: " + os.environ.get("FRUIT", ""))
FRUIT: 

#Linux executable command
#cat parameters.py
import sys
print(sys.argv)
'''
./paramers.py
out:  ['./parameters.py']
./parameters.py one two three
out: ['./parameters.py', 'one', 'two', 'three']
'''

#wc command 
'''
wc variables.py
out: 7 19 174 variables.py
echo $?
out: 0
''' 
#creating file
import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("New file created\n")
else:
    print("Error, the file {] already exists".format(filename))
    sys.exit(1)

'''
LINUX Command
./create_file.py example
echo $?
out: 0
cat example
out: New File created
./create_file.py example
out: Error, the file example already exits
echo $?
out: 1
'''
