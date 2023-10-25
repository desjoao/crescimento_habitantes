#Lista 4 - Exercício 8

ano=0
A = 5000000
B = 7000000
while B>=A:
    A+=A*0.03
    B+=B*0.02
    ano+=1
print(f'Levará {ano} anos para que o estado A tenha mais habitantes que o país B')
