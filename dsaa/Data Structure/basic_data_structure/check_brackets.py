# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    #text = sys.stdin.read()
    for j in range(1, 55):
        path = './Programming-Assignment-1/check_brackets_in_code/tests/'
        if j < 10:
            path += '0' + str(j)
        else:
            path += str(j)
        with open(path, 'r') as f:
            text = f.readline()
            flag = 0
            opening_brackets_stack = []
            for i, next in enumerate(text):
                if next == '(' or next == '[' or next == '{':
                    # Process opening bracket, write your code here
                    opening_brackets_stack.append(Bracket(next, i))
                    continue
                if next == ')' or next == ']' or next == '}':
                    # Process closing bracket, write your code here
                    if len(opening_brackets_stack) == 0:
                        flag = 1
                        break
                    brac = opening_brackets_stack.pop()
                    if brac.Match(next) == False:
                        break
            # Printing answer, write your code here
            re = ''
            if i < len(text)-1 or flag == 1:
                #print (i+1)
                re = str(i+1)
            elif len(opening_brackets_stack) != 0:
                #print(opening_brackets_stack[0].position + 1)
                re = str(opening_brackets_stack[0].position + 1)
            else:
                re = 'Success'
                #print("Success")
            patha = path + '.a'
            with open(patha, 'r') as a:
                an = a.readline().strip()
            if an == re:
                print ('ok', j)
            else:
                print(an, re, j)
'''
The key word "return" which should be used only in a function in
Python Programming language. if you use it in a loop or else, it could
pop out the error "return outside functiond"
'''
