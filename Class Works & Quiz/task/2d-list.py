"""
def values_in_elements():
    list = [[4, 6, 8, 2], [8, 3, 2, 5], [7, 1, 5]]
    for index, number in enumerate(list):
        for index_value, value in enumerate(number):
            print(value)

dictionary = {"name": "John", "age": 25, "height": 70, "weight": 100}
for key, value in dictionary.items():
    print(key, value)

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)
print("\n",dictionary["age"])

del dictionary["age"]
print(dictionary)
"""

def numbers_in_words(number):
    number_to_word= {1:"One",
                  2:"Two",
                  3:"Three",
                  4:"Four",
                  5:"Five",
                  6:"Six",
                  7:"Seven",
                  8:"Eight",
                  9:"Nine",
                  10:"Ten",
                  11:"Eleven",
                  12:"Twelve",
                  13:"Thirteen",
                  14:"Fourteen",
                  15:"Fifteen",
                  16:"Sixteen",
                  17:"Seventeen",
                  18:"Eighteen",
                  19:"Nineteen",
                  20:"Twenty"
                  }

    return number_to_word.get(number, "Not available now")

number = int(input("Enter a number: "))

print(f"Number {number} in word is {numbers_in_words(number)}")