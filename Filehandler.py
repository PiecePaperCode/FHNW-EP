def read_Basisroutine():
    with open('Basisroutine.txt') as file:
        return file.read()

def write_Basisroutine(text):
    with open('Basisroutine.txt', 'w') as file:
        file.write(text)