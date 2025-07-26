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

emailpattern = re.findall(r"[a-z]+[0-9]*@gmail*yahoomail.com*", email)
print(emailpattern)


# Define a class
class Town:
    def __init__(self, name, x, y, mayor):
        self.name = name
        self.x = x
        self.y = y
        self.mayor = mayor

# Create an empty list
towns = list()

# Append instances of the class to the list
towns.append(Town("Lagos", 6.5244, 3.3792, "John Doe"))
towns.append(Town("Abuja", 9.0765, 7.3986, "Jane Smith"))

# Accessing the appended objects
for town in towns:
    print(f"Town: {town.name}, Mayor: {town.mayor}")
