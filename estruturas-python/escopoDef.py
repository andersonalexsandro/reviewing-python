variavel = "valor"

def func():
    print(variavel)

def func2():
    variavel = "outro valor"
    print(variavel)

func()
func2()

def func3():
    global variavel 
    variavel = "valor final"
    print(variavel)

func3()
