# to reverse a string in python

def reverse_string(string2):

    for i in range(len(string2) - 1, -1, -1):
        print(string2[i], end="")


def reverse_string3(string2):
    return ''.join(reversed(string2))


# fastest possible way in python to reverse a string
def reverse_string2(string2):
    return string2[::-1]


string = "Hi My name is Harshit"
print(reverse_string3(string))
