telefonlista = {}

def insertnumber(inp):
    splitted = inp.split(' ', 1)
    namn = splitted[0]
    nummer = splitted[1]

    return namn, nummer

for i in range(3):
        formatedUserInput = insertnumber(input('ange namn och telefonnummer: '))
        if formatedUserInput[0] in telefonlista:
            print('finns redan')
        else:
            telefonlista[formatedUserInput[0]] = formatedUserInput[1]

print(telefonlista)

for key, value in telefonlista.items():
    print (key, value)

while True:
    searchName = input('skriv namn att soka efter: ')
    if searchName in telefonlista:
        print(f'{searchName} har telefonnummer {telefonlista[searchName]}')
    else:
        print(searchName, 'fanns inte')


        print('hello')
