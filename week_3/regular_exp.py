log = 'July 31 07:51:48 my computer bad_process[12345]: ERROR Performing package upgrade'
index = log.index("[")
print(log[index + 1:index + 6])
#12345
import re
log = 'July 31 07:51:48 my computer bad_process[12345]: ERROR Performing package upgrade'
regex = r"\[(d+)\]"
result = re.search(regex, log)
print(result[1])
#12345

import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

import re
result = re.search(r"aza", 'plaza')
print(result)
#<re.Match object; span=(2, 5), match='aza'>
result = re.search(r"aza", 'bazaar')
print(result)
#<re.Match object; span=(1, 4), match='aza'>
result = re.search(r"aza", 'maze')
print(result)
None
print(re.search(r'^x', 'xenon'))     
#<re.Match object; span=(0, 1), match='x'>
print(re.search(r'p.ng', 'penguin'))
#<re.Match object; span=(0, 4), match='peng'>
print(re.search(r'p.ng', 'clapping'))
#<re.Match object; span=(4, 8), match='ping'>
print(re.search(r'p.ng', 'sponge'))
#<re.Match object; span=(1, 5), match='pong'>
print(re.search(r'p.ng', 'Pangaea', re.IGNORECASE))
#<re.Match object; span=(0, 4), match='Pang'>
