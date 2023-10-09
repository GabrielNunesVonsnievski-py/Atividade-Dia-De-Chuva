x0 = [0,1,2]
x1 = [0,1,2]
x2 = [0,1,2]

while True:
    print(x0)
    print(x1)
    print(x2)

    linha = input(f"Escolha qual a linha que você quer do X (x0,x1,x2): ")
    coluna = int(input(f"Escolha qual a coluna que você quer do X : "))

    if linha == "x0":
        x0[coluna] = "X"
    elif linha == "x1":
        x1[coluna] = "X"
    elif linha == "x2":
        x2[coluna] = "X"

    print("-------------")   
    print(x0)
    print(x1)
    print(x2)
    print("-------------")
    

    linha = input(f"Escolha qual a linha que você quer do O (x0,x1,x2): ")
    coluna = int(input(f"Escolha qual a coluna que você quer do O : "))

    if linha == "x0":
        x0[coluna] = "O"
    elif linha == "x1":
        x1[coluna] = "O"
    elif linha == "x2":
        x2[coluna] = "O"
    
    print("-------------")
    print(x0)
    print(x1)
    print(x2)
    print("-------------")

    def verifica(x0,x1,x2):
        if x0[0] == "X" and x0[1] == "X" and x0[2] == "X":
            print("X é o vencedor!!")
        elif x1[0] == "X" and x1[1] == "X" and x1[2] == "X":
            print("X é o vencedor!!")
        elif x2[0] == "X" and x2[1] == "X" and x2[2] == "X":
            print("X é o vencedor!!")
        elif x1[0] == "X" and x1[1] == "X" and x1[2] == "X":
            print("X é o vencedor!!")
        elif x0[0] == "X" and x1[0] == "X" and x1[0] == "X":
            print("X é o vencedor!!")
        elif x0[1] == "X" and x1[1] == "X" and x1[1] == "X":
            print("X é o vencedor!!")
        elif x0[2] == "X" and x1[2] == "X" and x1[2] == "X":
            print("X é o vencedor!!")
        elif x0[0] == "X" and x1[1] == "X" and x2[2] == "X":
            print("X é o vencedor!!")
        elif x0[2] == "X" and x1[1] == "X" and x2[0] == "X":
            print("X é o vencedor!!")
        elif x0[0] == "O" and x0[1] == "O" and x0[2] == "O":
            print("O é o vencedor!!")
        elif x1[0] == "O" and x1[1] == "O" and x1[2] == "O":
            print("X é o vencedor!!")
        elif x2[0] == "O" and x2[1] == "O" and x2[2] == "O":
            print("O é o vencedor!!")
        elif x1[0] == "O" and x1[1] == "O" and x1[2] == "O":
            print("O é o vencedor!!")
        elif x0[0] == "O" and x1[0] == "O" and x1[0] == "O":
            print("O é o vencedor!!")
        elif x0[1] == "O" and x1[1] == "O" and x1[1] == "O":
            print("O é o vencedor!!")
        elif x0[2] == "O" and x1[2] == "O" and x1[2] == "O":
            print("O é o vencedor!!")
        elif x0[0] == "O" and x1[1] == "O" and x2[2] == "O":
            print("O é o vencedor!!")
        elif x0[2] == "O" and x1[1] == "O" and x2[0] == "O":
            print("O é o vencedor!!")
            
        
        

        