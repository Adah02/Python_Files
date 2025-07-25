import re

text = "0123282 Mentality defines a man in most cases"
link = """http://power/rerdWEr Mentality defines a man in most cases """

# pattern1 = re.findall(r"[^abc]+", text) #Anything other than abc
# #print(pattern1)
#
# pattern = re.compile(r"[A-Za-z]+")  #For printing alphabets in a given string
# match = pattern.findall(text)
# #print(match)
#
# pattern2 = re.compile(r"[^0-9]+")  #For printing things that are not numbers in strings
# match1 = pattern2.findall(text)
#print(match1)

# patterns = re.compile(r"([a-z]+)(://)([a-z]+/[a-zA-Z]+)", re.IGNORECASE)
# matches = patterns.finditer(link)
#
# for match in matches:
#     print(match.group(0),"\n", match.group(1),"\n", match.group(2),"\n", match.group(3))

phoneNumber = "123-456-7890"

pattern_ = re.findall(r"(\d{3}-\d{3}-\d{4})", phoneNumber)
# matches = pattern_.findall(phoneNumber)

print(pattern_)

sentence = "Alice!! is a Lady"

patterns_ = re.findall(r"([A-Z][a-z]+)", sentence)
print(patterns_)

pattern_ = re.findall(r"(\w+)", sentence)
print(pattern_)

email = "adah02@gmail.com"

emailpattern = re.findall(r"[a-z]+[0-9]*@[a-z]+mail.com", email)
print(emailpattern)
