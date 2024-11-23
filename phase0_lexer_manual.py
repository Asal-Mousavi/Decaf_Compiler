import pandas as pd

class Token:
    def __init__(self, number, type_name, final_state):
        self.number = number
        self.final_state = final_state
        self.type_name = type_name

    def __str__(self):
        return self.type_name


def tokenize(input_string, dfa,line):
    count = 0
    input_string += " "
    state = 0
    word = ""
    for char in input_string:
        count += 1
        word += char
        index = index_of_alpha(char)
        if index < 0:
            print("syntax error on " + word
                  + f" in line %i character %i" %(line,count) )
            word =""
            continue

        state = int(dfa[int(state)][index + 1])
        if states[state].final_state:
            print(f"< %s , %s >" % (word, states[state]))
            word = ""



def index_of_alpha(char):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_=+)(0 "
    if char in alpha:
        return alpha.index(char)
    else :
        return -1

def check_comment(text):
    if text[:2] == "//":
        return True
    else:
        return False

# main code
df = pd.read_csv('TABLE1.csv')
df = df.to_numpy()
states = list()

for s in df[:, 0]:
    fs = False
    title = str(s)
    if s < 6:
        fs = True
        if s == 0:
            title = "Start"
            fs = False
        elif s == 1:
            title = "KW"
        elif s == 2:
            title = "ID"
        elif s == 3:
            title = "OP"
        elif s == 4:
            title = "INT"
        else:
            title = "Trap"
    states.append(Token(s, title, fs))

with open("decaf.txt") as file:
    count_line = 0
    for line in file:
        count_line += 1
        text = line.strip()
        if(check_comment(text)):
            continue
        tokenize(text, df, count_line)

file.close()

#text = input("Enter your TEXT: ")



