'''
with open("words1.txt") as file:
    for line in file:
        print(line.upper().strip())
'''

'''
file = open("words1.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)
'''

'''
with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")
'''

'''
# os module imported
>>>import os
# to permanently remove the text file or any file
>>>os.remove("words1.txt")
# to rename a file
>>>os.rename("words1.txt", "wrds.txt")
# to check whether the file exists 
>>>os.path.exists("words.txt")
False
# to get the size of the text file
>>>os.path.getsize("romeo.txt")
169
# to get the time of the file of when it was last modified
>>>os.path.getmtime("romeo.txt")
1591359188.3785102 #this shows the time in seconds from the original windows in the 90s
# to get date time function we import datetime
>>>import datetime
# use of timestamp to get the date time of common calender
>>>timestamp = os.path.getmtime("romeo.txt")
>>>datetime.datetime.fromtimestamp(timestamp) # to get the time and date the file was last modified
datetime.datetime(2020, 6, 5, 17, 43, 8, 378510)
>>>os.path.abspath('romeo.txt') # to get the absolute path of the text file
'C:\\Users\\Hp\\PycharmProjects\\modules\\romeo.txt'
'''

'''
import os
os.listdir("website")
dir = "website"
for name in os.lisdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

"""Output:
website/images is a directory
websilte/index.html is a file
website/favicon.ico is a file"""
'''

