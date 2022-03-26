import read_module

def Word_Accept(Word, Starting_States, Final_States, DFA):
    Word = list(Word)
    State = Starting_States[0]
    for letter in Word:
        for x in DFA[State].items():
            if letter == x[1]:
                State = x[0]
    if State in Final_States:
        print("Cuvantul este acceptat")
    else:
        print("Cuvantul nu este acceptat")

def Run(input_file):
    Sigma, Starting_States, Final_States, DFA, States = read_module.Read(input_file)
    Word = input("Introduceti cuvantul: ")
    Word_Accept(Word, Starting_States, Final_States, DFA)

if __name__ == "__main__":
    Run("dfa_config_file")