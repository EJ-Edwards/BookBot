def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars



def sort_on(item):
    return item["num"]

text = [
    {"char": "e", "num": 44538},
    {"char": "t", "num": 29493},
    {"char": "a", "num": 25894},
    {"char": "o", "num": 24494},

    {"char": "i", "num": 23927},
    {"char": "n", "num": 23643},
    {"char": "s", "num": 20360},
    {"char": "r", "num": 20079},
    {"char": "h", "num": 19176},
    {"char": "d", "num": 16318},
    {"char": "l", "num": 12306},
    {"char": "m", "num": 10206},
    {"char": "u", "num": 10111},
    {"char": "c", "num": 9011},
    {"char": "f", "num": 8451},
    {"char": "y", "num": 7756},
    {"char": "w", "num": 7450},
    {"char": "p", "num": 5952},
    {"char": "g", "num": 5795},
    {"char": "b", "num": 4868},
    {"char": "v", "num": 3737},
    {"char": "k", "num": 1661},
    {"char": "x", "num": 691},
    {"char": "j", "num": 497},
    {"char": "q", "num": 325},
    {"char": "z", "num": 235},
    {"char": "æ", "num": 28},
    {"char": "â", "num": 8},
    {"char": "ê", "num": 7},
    {"char": "ë", "num": 2},
    {"char": "ô", "num": 1},
]
text.sort(reverse=True, key=sort_on)
print(text)
