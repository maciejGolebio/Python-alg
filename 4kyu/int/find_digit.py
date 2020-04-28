"""
Task from codewars.com

To give credit where credit is due: This problem was taken from the ACMICPC-Northwest Regional Programming Contest. Thank you problem writers.

You are helping an archaeologist decipher some runes. He knows that this ancient society used a Base 10 system, and that they never start a number with a leading zero. He's figured out most of the digits as well as a few operators, but he needs your help to figure out the rest.

The professor will give you a simple math expression, of the form

[number][op][number]=[number]
He has converted all of the runes he knows into digits. The only operators he knows are addition (+),subtraction(-), and multiplication (*), so those are the only ones that will appear. Each number will be in the range from -1000000 to 1000000, and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s. If there are ?s in an expression, they represent a digit rune that the professor doesn't know (never an operator, and never a leading -). All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the other given digits in the expression. No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.

Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works, give the lowest one. If no digit works, well, that's bad news for the professor - it means that he's got some of his runes wrong. output -1 in that case.

Complete the method to solve the expression to find the value of the unknown rune. The method takes a string as a paramater repressenting the expression and will return an int value representing the unknown rune or -1 if no such rune exists.


"""


def arr_to_int(arr):
    s = ''.join(map(str, arr))
    return int(s)


def prepare_eq_site(eq_site: str) -> list:
    lst = []
    tmp: str = ''
    for i in eq_site:
        if i != '+' and i != '*' and i != '-':
            tmp += i
            # print(i)
        else:
            print(tmp)
            lst.append(tmp)
            lst.append(i)
            tmp = ''
    lst.append(tmp)
    return lst


def solve_runes(runes: str):
    eq = runes.replace('--', '+').split("=")
    left = eq[0]
    right = eq[1]
    #
    # l_4 = eval(left.replace('?', str(4)))
    # r_4 = eval(right.replace('?', str(4)))
    # old = l_4 - r_4
    # if old == 0:
    #     return 4
    # l_5 = eval(left.replace('?', str(5)))
    # r_5 = eval(right.replace('?', str(5)))
    # new = l_5 - r_5
    # if new == 0:
    #     return 5
    # r = None
    # if new < old:
    #     r = range(0, 4)
    # else:
    #     r = range(6, 10)
    #
    # for i in r:
    #     if eval(left.replace('?', str(i))) == eval(right.replace('?', str(i))):
    #         return i
    #
    # return -1
    for i in (range(10)):
        print(right.replace('?', str(i)))
        print(str(i))
        if eval(left.replace('?', str(i))) == eval(right.replace('?', str(i))) != 0:
            return i
    return -1


result = solve_runes('?*11=??')
print(result)
