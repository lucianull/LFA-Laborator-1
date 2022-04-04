import read_module

def ValidDFA(input_file):
    Sigma, Starting_States, Final_States, DFA, States = read_module.Read(input_file)
    if len(Starting_States) > 1:
        return 0
    Freq = {}
    for x in Sigma:
        Freq[x] = 0
    for x in DFA.items():
        if x[0] not in States:
            return 0
        for y in x[1].items():
            if y[0] not in States:
                return 0
            for z in y[1]:
                if z not in Sigma:
                    return 0
                Freq[z] = 1
        for x in Sigma:
            if Freq[x] != 1:
                return 0
            Freq[x] = 0
    return 1

def Run(input_file):
    if ValidDFA(input_file) == 0:
        print("DFA-ul nu este valid")
    else:
        print("DFA-ul este valid")

if __name__ == "__main__":
    input_file = "dfa_config_file"
    Run(input_file)
