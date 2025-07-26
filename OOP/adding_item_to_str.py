def add_item_to_str(letters, domant):
    #for adding a string to sentence or word
    word = []
    word += letters
    item = "ce"
    if (len(word)) % 2 == 0:
        word.insert((len(word) //2), item)
    else:
        word.append(item)
    return "".join(word)

print(add_item_to_str('letter', ""))


def display_asterisks(func):
    def wrapper(*args, **kwargs):
        print('*' * 15)
        return func(*args, **kwargs)
        print('*' * 15)
    return wrapper


@display_asterisks
def display_name(name):
    print(name)

display_name('joyce')


class TimeWithProperties:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self.hours

    @hour.setter
    def hour(self, value):
        if 0 > value > 23:
            raise ValueError('hour must be between 0 and 23')
        self.hours = value

    @property
    def minute(self):
        return self.minutes

    @minute.setter
    def minute(self, value):
        if 0 > value > 59:
            raise ValueError('minute must be between 0 and 59')
        self.minutes = value

    @property
    def second(self):
        return self.seconds

    @second.setter
    def second(self, value):
        if 0 > value > 59:
            raise ValueError('second must be between 0 and 59')
        self.seconds = value

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

time = TimeWithProperties(6, 45, 49)
# time.hour(7)
# time.minute(5)
# time.second(6)
print(time)