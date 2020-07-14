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
import subprocess
>>> print(subprocess.run('date /t', shell=True))
CompletedProcess(args='date /t', returncode=0)
>>>print(subprocess.run('sleep /t', shell=True))
CompletedProcess(args='sleep /t', returncode=1)
>>> result = subprocess.run('ls /t', shell=True)
>>> print(result.returncode)
1

#obtaining the output of a system command
>>> result = subprocess.run(['host /t', '8.8.8.8'], capture_output=True, shell=True)
>>> print(result.returncode)
1
>>> print(result.stdout)
b''
>>> result = subprocess.run(['rm /t', 'does_not_exist'], capture_output=True, shell=True)
>>> print(result.returncode)
1
>>> print(result.stdout)
b''
>>> print(result.stderr)
b'The system cannot find the path specified.\r\n'

#advanced subprocess management
>>> import os
>>> import subprocess
>>> my_env = os.environ.copy()
>>> my_env['PATH'] = os.pathsep.join(['/opt/myapp/', my_env['PATH']])
>>> result = subprocess.run(['myapp /t'], env=my_env, shell=True)

#processing log files
import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for linw in f:
    if 'CRON" not in line:
      continue
    print(line.strip())
#check.py
>>> import re
>>> pattern = r'USER \((\w+)\)$'
>>> line = 'JUL 6 14:04:01computer.name CRON[29440]: USER (naughty_user)'
>>> result = re.search(pattern, line)
>>> print(result[1])
naughty_user

# making sense of data
>>> usernames = {}
>>> name = "good user"
>>> usernames[name] = usernames.get(name, 0) +1
>>> print(usernames)
{'good user': 1}
>>> usernames[name] = usernames.get(name, 0) + 1
>>> print(usernames)
{'good user': 2}

import re
import sys

logfile = sys.argv[1]
usernames = {}

with opn(logfile) as f:
        for line in f:
                if "CRON" not in line:
                        continue
                pattern = r"USER\((\w+)\)$"
                result = re.search(pattern line)
                if result is None:
                        continue
                name = result[1]
                usernames[name] = usernames.get(name, 0) + 1

