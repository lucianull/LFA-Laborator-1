def Read(input_file):
    inFile = open(input_file)
    Sigma = []
    Starting_State = -1
    Final_States = []
    DFA = {}
    States = []
    Valid = 1
    info_read = 0
    while True:
        line = inFile.readline().rstrip()
        if line == "Sigma:":
            line = inFile.readline().rstrip()
            while line != "End":
                Sigma.append(line.rstrip())
                line = inFile.readline().rstrip()
            info_read += 1
        if line == "States:":
            line = inFile.readline().rstrip()
            while line != "End":
                line = list(line)
                States.append(int(line[0]))
                if len(line) == 4:
                    if line[3] == 'S':
                        if Starting_State != -1:
                            Valid = 0
                        else:
                            Starting_State = int(line[0])
                    else:
                        Final_States.append(int(line[0]))
                line = inFile.readline().rstrip()
            info_read += 1
        if line == "Transitions:":
            line = inFile.readline().rstrip()
            while line != "End":
                line = line.replace(", ", "")
                line = list(line)
                # line = line.split()
                if int(line[0]) not in DFA:
                    DFA[int(line[0])] = {}
                    DFA[int(line[0])][int(line[2])] = line[1]
                else:
                    if int(line[2]) in DFA[int(line[0])] and DFA[int(line[0])][int(line[2])] != line[1]:
                        Valid = 0
                    else:
                        DFA[int(line[0])][int(line[2])] = line[1]
                line = inFile.readline().rstrip()
            info_read += 1
        if info_read == 3:
            break
    for x in DFA.items():
        if x[0] not in States:
            Valid = 0
            break
        for y in x[1].items():
            if y[0] not in States:
                Valid = 0
                break
            if y[1] not in Sigma:
                Valid = 0
                break
    return Sigma, Starting_State, Final_States, DFA, States, Valid

def Word_Accept(Word, Starting_State, Final_States, DFA):
    Word = list(Word)
    State = Starting_State
    for letter in Word:
        for x in DFA[State].items():
            if letter == x[1]:
                State = x[0]
    if State in Final_States:
        print("Cuvantul este acceptat")
    else:
        print("Cuvantul nu este acceptat")

def Run(input_file):
    Sigma, Starting_State, Final_States, DFA, States, Valid = Read(input_file)
    if Valid == 0:
        print("DFA-ul nu este valid")
    else:
        print("DFA-ul este valid")
        Word = input("Introduceti cuvantul: ")
        Word_Accept(Word, Starting_State, Final_States, DFA)

if __name__ == "__main__":
    input_file = "input.txt"
    Run(input_file)
