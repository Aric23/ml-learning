def num(ch):
    return ch**2

def apply_to_all(func, *items):
    new = []
    for i in items:
        i = num(i)
        new.append(i)    

        
    return new

print(apply_to_all(num, 10, 30, 50, 3 ,5))

def num1(ch):
    if ch == "Yes":
        return True
    else:
        return False

def apply_to_all1(func, *items):
    new = []
    for i in items:
        if num1(i):
            new.append(i)    

        
    return new

print(apply_to_all1(num, "No", "Yes", "No", "Yes","No"))


def make_repeater(i):
    def repeat(b):
        return print(b * i)
    return repeat

repeat_3 = make_repeater(3)
print(repeat_3("ha"))


def make_repeater1(i):
    i+1
    def repeat(b):
        return print(b * i)
    return repeat

repeat_3 = make_repeater1(3)
print(repeat_3(4))