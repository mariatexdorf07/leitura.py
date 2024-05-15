escolha = input("escolha entre a e b")

while escolha != 'p1' and escolha != 'p2':
    print("Escolha só uma!!")
    escolha = input("escolha entre a e b: ")
if escolha == 'b':
    print("escolheu b")
else:
    print("escolheu a")

