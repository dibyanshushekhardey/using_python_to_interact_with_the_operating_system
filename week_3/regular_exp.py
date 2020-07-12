#date 11 july 2020
>>log = 'July 31 07:51:48 my computer bad_process[12345]: ERROR Performing package upgrade'
>>index = log.index("[")
>>print(log[index + 1:index + 6])
12345
>>import re
>>log = 'July 31 07:51:48 my computer bad_process[12345]: ERROR Performing package upgrade'
>>regex = r"\[(d+)\]"
>>result = re.search(regex, log)
>>print(result[1])
12345

>>import re
>>def check_aei (text):
...  result = re.search(r"a.e.i", text)
...  return result != None

>>print(check_aei("academia")) # True
>>print(check_aei("aerial")) # False
>>print(check_aei("paramedic")) # True

>>import re
>>result = re.search(r"aza", 'plaza')
>>print(result)
<re.Match object; span=(2, 5), match='aza'>
>>result = re.search(r"aza", 'bazaar')
>>print(result)
<re.Match object; span=(1, 4), match='aza'>
>>result = re.search(r"aza", 'maze')
>>print(result)
None
# use of ^ to check the character at the beginning of the script
>>print(re.search(r'^x', 'xenon'))     
<re.Match object; span=(0, 1), match='x'>
>>print(re.search(r'p.ng', 'penguin'))
<re.Match object; span=(0, 4), match='peng'>
>>print(re.search(r'p.ng', 'clapping'))
<re.Match object; span=(4, 8), match='ping'>
>>print(re.search(r'p.ng', 'sponge'))
<re.Match object; span=(1, 5), match='pong'>
>>print(re.search(r'p.ng', 'Pangaea', re.IGNORECASE))
<re.Match object; span=(0, 4), match='Pang'>

# date 13 july 2020
>>import re
>>print(re.search(r"[Pp]ython", "Python"))
<re.Match object; span=(0, 6), match='Python'>
>>print(re.search(r"[a-z]way", "The end of the highway"))
<re.Match object; span=(18, 22), match='hway'>
>>print(re.search(r"[a-z]way", "What a way to go"))
None
>>print(re.search("cloud[a-zA-Z0-9]", "cloud"))
None
>>print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
<re.Match object; span=(0, 6), match='cloudy'>
>>print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces"))
<re.Match object; span=(4, 5), match=' '>
>>print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces"))
None
>>rint(re.search(r"cat|dog", "I like cats"))
<re.Match object; span=(7, 10), match='cat'>
>>print(re.search(r"cat|dog", "I like dogs."))
<re.Match object; span=(7, 10), match='dog'>
>>print(re.search(r"cat|dog", "I like dogs and cats."))
<re.Match object; span=(7, 10), match='dog'>
>>print(re.findall(r"cat|dog", "I like both dogs and cats."))
['dog', 'cat']
print(re.search(r'[Pp]ython', 'Python'))
<re.Match object; span=(0, 6), match='Python'>
>>> # to search any character between a - z
>>> print(re.search(r'Py.*n', 'Pygmalion'))
<re.Match object; span=(0, 9), match='Pygmalion'>
>>> print(re.search(r'Py.*n', 'Python Programming'))
<re.Match object; span=(0, 17), match='Python Programmin'>
>>> print(re.search(r'Py[a-z]*n', 'Pygmalion'))
<re.Match object; span=(0, 9), match='Pygmalion'>
>>> print(re.search(r'Py[a-z]*n', 'Pyg'))
None
>>> # egrep character + checks oneor more character before it
>>> print(re.search(r'o+l+', 'goldfish'))
<re.Match object; span=(1, 3), match='ol'>
>>> print(re.search(r'o+l+', 'woooly'))
<re.Match object; span=(1, 5), match='oool'>
>>> print(re.search(r'o+l+', 'boil'))
None
>>> print(re.search(r'p?each', 'To each their own'))
<re.Match object; span=(3, 7), match='each'>
>>> print(re.search(r'p?each', 'I like peaches'))
<re.Match object; span=(7, 12), match='peach'>
>>> # use of escape character
>>> print(re.search(r'\.com', 'welcome'))
None
>>> print(re.search(r'\.com', 'mydomain.com'))
<re.Match object; span=(8, 12), match='.com'>
>>> # \w matches alphanumeric character
>>> print(re.search(r'\w*', 'This is an example'))
<re.Match object; span=(0, 4), match='This'>
>>> print(re.search(r'\w*', 'This_is_another_example'))
<re.Match object; span=(0, 23), match='This_is_another_example'>
