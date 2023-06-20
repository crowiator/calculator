

logo = ''' .------------------------------------------,
| .---------------------------------------, |
| | _~_                                   | |
| |  \/  Texas Instruments     T I - 8 6  | |
| | .-----------------------------------, | |
| | |                                   | | |
| | | 1 + 1                             | | |
| | |                                   | | |
| | |                                2  | | |
| | |                                   | | |
| | | 6 * 8                             | | |
| | |                               14  | | |
| | |                                   | | |
| | | _                                 | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | `-----------------------------------' | |
| |                                       | |
| `---------------------------------------' |
|     M1      M2      M3      M4      M5    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  F1 | |  F2 | |  F3 | |  F4 | |  F5 |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|-------.________          ________,--------|
|                `--------'                 |
|                                           |
|          QUIT    MODE        _,-._        |
|  .-----, .-----, .-----,  /\ \_^_/ /\     |
|  | 2nd | | EXIT| | MORE| / /   |   \ \    |
|  `-----' `-----' `-----' |<|   O   |>|    |
|  alpha   LINK x  INS     \ \  _|_  / /    |
|  .-----, .-----, .-----,  \/ / v \ \/     |
|  |ALPHA| |x-VAR| | DEL |     -._,-        |
|  `-----' `-----' `-----'                  |
|  SOLVER  SIMULT  POLY   CATLG-VARS        |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |GRAPH| |TABLE| | PRGM| |CUSTM| |CLEAR|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  10x  A  SIN-1 B COS-1 C TAN-1 D pi   E   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LOG | | SIN | | COS | | TAN | |  ^  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ex   F  x-1  G  [    H  ]    I  CALC J   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LN  | | EE  | |  (  | |  )  | |     |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ./~  K  MATRX L VECTR M CPLX N  MATH O   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | X2  | |  7  | |  8  | |  9  | |  x  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  /_   P  CONS Q  CONV R  STRNG S LIST T   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  ,  | |  4  | |  5  | |  6  | |  -  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  RCL  =  BASE U  TEST V  MEM  W  STAT X   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | STO>| |  1  | |  2  | |  3  | |  +  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  OFF     CHAR Y  :    z  ANS  _  ENTRY    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | ON  | |  0  | |  .  | | (-) | |ENTER|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  -------                                  |
`\                                         /'
  `-._                                 _.-'
      `--.__                     __.--'
            ``----.._____,,---'''

#FUNCTION

#Add
def add(n1, n2):
    return n1 + n2


#Substract
def substract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2





operations = {'+': add,
              '-': substract,
              '*': multiply,
              '/': divide
              }
def calculator():
    start = True
    while start:
        print(logo)
        continue_calculating = True
        number_1 = float(input("What's the first number?: "))
        while continue_calculating:
            for key in operations:
                print(key)
            operation = input("Pick an operation: ")

            number_2 = float(input("What's the second number?: "))
            function = operations[operation]
            result = function(number_1, number_2)
            print(f"{number_1} {operation} {number_2} = {result}")
            choice = input(f" Type 'y' to continue calculating with {result} or type 'n' to start new calculation:")
            if choice == 'y':
                continue_calculating = True
                number_1 = result
            else:
                continue_calculating = False
                start = True
calculator()