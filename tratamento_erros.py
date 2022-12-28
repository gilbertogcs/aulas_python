import pdb
#lib para pausar o codigo

x= [1,2,3]
y = 2
z = 10

print(z + y)

print('')
print(999*'-')

#nessa linha o pdb faz a pausa para verificar as variaveis
# caso queira continuar digie C
# caso queira sair digite Q
pdb.set_trace()
print(x + z)