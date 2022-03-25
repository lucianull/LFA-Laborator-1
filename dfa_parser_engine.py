import read_module
from stack import Stack

def ValidDFA(input_file):
    Sigma, Starting_States, Final_States, DFA, States = read_module.Read(input_file)
    if len(Starting_States) > 1:
        return 0
    for x in DFA.items():
        if x[0] not in States:
            return 0
        for y in x[1].items():
            if y[0] not in States:
                return 0
            if y[1] not in Sigma:
                return 0
    stack = Stack()
    freq = [0 for i in range(len(States))]
    freq[0] = 1
    stack.push(Starting_States[0])
    while stack.size() > 0:
        top = stack.top()
        stack.pop()
        if top in Final_States:
            return 1
        if top in DFA:
            for x in DFA[top].keys():
                if freq[x] == 0:
                    stack.push(x)
                    freq[x] = 1
    return 0

def Run(input_file):
    if ValidDFA(input_file) == 0:
        print("DFA-ul nu este valid")
    else:
        print("DFA-ul este valid")

if __name__ == "__main__":
    input_file = "dfa_config_file"
    Run(input_file)
