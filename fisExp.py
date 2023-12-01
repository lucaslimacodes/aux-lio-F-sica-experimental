from sympy import *
#definindo os simbolos
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
d = Symbol('d')
e = Symbol('e')
#f será a função
g = Symbol('g')
h = Symbol('h')
i = Symbol('i')
j = Symbol('j')
k = Symbol('k')
l = Symbol('l')
m = Symbol('m')
n = Symbol('n')
o = Symbol('o')
p = Symbol('p')
q = Symbol('q')
r = Symbol('r')
s = Symbol('a')
t = Symbol('t')
u = Symbol('u')
v = Symbol('v')
w = Symbol('w')
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# função que retorna o erro propagado
def erroPropagado(f, variaveis, valores, erros):
    resultado = 0
    
    for i in range(0, len(variaveis)):
        func = diff(f,variaveis[i])
        for j in range(0, len(valores)):
            func = func.subs(variaveis[j], valores[j])
        resultado+= (N(func)*erros[i])**2
    
    return sqrt(resultado)

#função que retorna a média dos dados
def media(dados):
    resultado = 0
    for i in dados:
        resultado+=i
    return resultado/len(dados)

#função que retorna a média dos quadrados
def media_dos_quadrados(dados):
    resultado = 0
    for i in dados:
        resultado+=i**2
    return resultado/len(dados)

#função que retorna o desvio padrão dos dados
def desvio_padrao(dados):
    return sqrt(media_dos_quadrados(dados) - media(dados)**2)


#escreva aqui a função da qual queira achar o erro
f = m*(v**2)/2

#escreva aqui as variáveis
variaveis = [m,v]

#escreva aqui os valores das variáveis(em ordem)
valores = [10,10]

#escreva aqui os valores dos erros das variáveis(em ordem)
erros = [0.5, 0.2]


print(erroPropagado(f, variaveis, valores, erros))

#insira os dados para calcular média ou desvio padrão
dados = [1,2,3,4,5,6]

print(media(dados))
print(desvio_padrao(dados))