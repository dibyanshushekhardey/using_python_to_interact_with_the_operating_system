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
>>> # use of regular expressions in patterns
>>> print(re.serach(r.'A.*a', 'Argentina'))
SyntaxError: invalid syntax
>>> print(re.serach(r'A.*a', 'Argentina'))
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(re.serach(r'A.*a', 'Argentina'))
AttributeError: module 're' has no attribute 'serach'
>>> 
KeyboardInterrupt
>>> print(re.search(r.'A.*a', 'Argentina'))
SyntaxError: invalid syntax
>>> print(re.search(r'A.*a', 'Argentina'))
<re.Match object; span=(0, 9), match='Argentina'>
>>> print(re.search(r'A.*a', 'Azerbaijan'))
<re.Match object; span=(0, 9), match='Azerbaija'>
>>> print(re.search(r'A.*a$', 'Azerbaijan'))
None
>>> print(re.search(r'^A.*$', 'Australia'))
<re.Match object; span=(0, 9), match='Australia'>
>>> pattern = r'^[a-zA-Z_][a-zA-Z0-9]*
SyntaxError: EOL while scanning string literal
>>> pattern = r'^[a-zA-Z_][a-zA-Z0-9]*$'
>>> print(re.search(patter, '_this_is_a_wild_variable_name_'))
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(re.search(patter, '_this_is_a_wild_variable_name_'))
NameError: name 'patter' is not defined
>>> print(re.search(pattern, '_this_is_a_wild_variable_name_'))
None
>>> print(re.search(pattern, '_this_is_a_wild_variable_name'))
None
>>> print(re.search(pattern, '_this_is_a_wild_variable_name_'))
None
>>> pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
>>> print(re.search(pattern, '_this_is_a_wild_variable_name_'))
<re.Match object; span=(0, 30), match='_this_is_a_wild_variable_name_'>
>>> print(re.search(pattern, 'this is not a valid variable here'))
None
>>> print(re.search(pattern, 'my_variable1'))
<re.Match object; span=(0, 12), match='my_variable1'>
>>> print(re.search(pattern, '_this_is_a_wild_variable_name_'))
<re.Match object; span=(0, 30), match='_this_is_a_wild_variable_name_'>
>>> print(re.search(pattern, '1_this_is_a_wild_variable_name_'))
None
>>> result = re.search(r'^(\w*), (\w*)$', 'Lovelace, Ada')
>>> print(result)
<re.Match object; span=(0, 13), match='Lovelace, Ada'>
>>> print(result.groups())
('Lovelace', 'Ada')
>>> print(result[0])
Lovelace, Ada
>>> print(result[1])
Lovelace
>>> print(result[2])
Ada
>>> '{} {}'.format(result[2], result[1])
'Ada Lovelace'
>>> def rearrange_name(name):
	result = re.search(r'^(\w*), (\w*)$', name)
	if result is None:
		return name
	return '{}  {}'.format(result[2], result[1])

>>> rearrange_name("Lovelace, Ada')
	       
SyntaxError: EOL while scanning string literal
>>> rearrange_name('Lovelac, Ada')
'Ada  Lovelac'
>>> rearrange_name('Ritchie, Dennis')
'Dennis  Ritchie'
>>> rearrange_name('Lovelac, Ada.G')
'Lovelac, Ada.G'
>>> def rearrange_name(name):
  result = re.search(r"^(\w*), (\w.*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

>>> name=rearrange_name("Kennedy, John F.")
>>> print(name)
John F. Kennedy
>>> def rearrange_name(name):
  result = re.search(r"^(\w\.-*), (\w\.-*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

>>> name = rearrange_name('Kennedy, John F.')
>>> print(name)
Kennedy, John F.
>>> def rearrange_name(name):
  result = re.search(r"^([\w\.-]*), ([\w\.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

>>> name = rearrange_name('Kennedy, John F.')
>>> print(name)
Kennedy, John F.
>>> print(re.search(r'[a-zA-Z]{5}', 'a ghost'))
<re.Match object; span=(2, 7), match='ghost'>
>>> print(re.search(r'[a-zA-Z]{5}', 'a very scary ghost in a nutty shape'))
<re.Match object; span=(7, 12), match='scary'>
>>> print(re.findall(r'[a-zA-Z]{5}', 'a very scary ghost i na nutty shape'))
['scary', 'ghost', 'nutty', 'shape']
>>> print(re.findall('r\b[a-zA-Z]{5}\b', 'a scary ghost appeared'))
[]
>>> print(re.findall('r\b[a-zA-Z]{5}\b', 'A scary ghost appeared'))
[]
>>> print(re.findall(r'\b[a-zA-Z]{5}\b', 'a scary ghost appeared'))
['scary', 'ghost']
>>> print(re.findall(r'\b[a-zA-Z]{5}\b', 'I really like strawberri'))
[]
>>> print(re.findall(r'\w{5, 10}', 'I really like strawberri'))
[]
>>> print(re.findall(r'\w{5,10}', 'I really like strawberries'))
['really', 'strawberri']
>>> print(re.findall(r'\w{5,}', 'I really like strawberries'))
['really', 'strawberries']
>>> print(re.findall(r's\w{,20}', 'I really like strawberries'))
['strawberries']
>>> def long_words(text):
  pattern = r'\w{7,}'
  result = re.findall(pattern, text)
  return result

>>> print(long_words("I like to drink coffee in the morning.")) # ['morning']
['morning']
>>> print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
['chocolate', 'afternoon']
>>> print(long_words("I never drink tea late at night.")) # []
[]
>>> import re
>>> log = 'July 31 07:51:48 my computer bad_process[12345]: ERROR Performing package upgrade'
>>> regex = r"\[(d+)\]"
>>> result = re.search(regex, log)
>>> print(result)
None
>>> print(result[1])
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    print(result[1])
TypeError: 'NoneType' object is not subscriptable
>>> result = re.search(regex, int(log))
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    result = re.search(regex, int(log))
ValueError: invalid literal for int() with base 10: 'July 31 07:51:48 my computer bad_process[12345]: ERROR Performing package upgrade'
>>> result = re.search(regex, log)
>>> print(result[1])
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    print(result[1])
TypeError: 'NoneType' object is not subscriptable
>>> def extract_pid(log_line):
	regex = r'\[(\d+)]'
	result = re.search(regex, log_line)
	if result is None:
		return ""
	return result[1]

>>> print(extract_pid(log))
12345
>>> print(extract_pid("99 elepj=hants in a a[cage]"))

>>> #splitting and replacing
>>> re.split(r'[.?!]', 'One sentence, Another ome?, and the last one!')
['One sentence, Another ome', ', and the last one', '']
>>> re.split(r'([.?!])', 'One sentence, Another ome?, and the last one!')
['One sentence, Another ome', '?', ', and the last one', '!', '']
>>> re.sub(r'[\w.%+-]+@[\w.-]+', '[REDACTED]', 'Received an email for go_nuts95@my.example.com')
'Received an email for [REDACTED]'
>>> re.sub(r'^([\w .-]*), ([\w .-]*)$', r"2\1", 'Lovelace, Ada')
'2Lovelace'
>>> re.sub(r'^([\w .-]*), ([\w .-]*)$', r"\2\1", 'Lovelace, Ada')
'AdaLovelace'
