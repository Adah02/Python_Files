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
        return self.hour

    @hour.setter
    def hour(self, value):
        if 0 > value > 23:
            raise ValueError('hour must be between 0 and 23')
        self.hour = value

    @property
    def minute(self):
        return self.minute

    @minute.setter
    def minute(self, value):
        if 0 > value > 59:
            raise ValueError('minute must be between 0 and 59')
        self.minute = value

    @property
    def second(self):
        return self.second

    @second.setter
    def second(self, value):
        if 0 > value > 59:
            raise ValueError('second must be between 0 and 59')
        self.second = value
