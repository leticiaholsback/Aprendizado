Algoritmo "Capgemini - DIV e MOD"

Var
//real = float
   x,y: inteiro
   w: real

Inicio
x <- 12
y <- 6
w <- x DIV y
//DIV pega apenas o numero inteiro da opera��o , j� o / pega toda a dizima periodica
Escreval (w)

x <- 12
y <- 6
w <- x % y
Escreval (w)
// % mostra o resto da opera��o, ex. saber se o numero � par ou nao

se w % 2 = 0 entao
   Escreval ("Numero PAR")
senao
     Escreval ("Numero Impar")
fimse
Fimalgoritmo
