from turtle import*

Screen() #tela   #Dica! lembrar do "S" maiúsculo, como "Screen" e naum "screen"


shoturtle() #demonstrar tartaruga
hideturtle() #ocultar tartaruga/ esconder

shape("circle") #formato       #arrow / turtle / square / triangle / classic

forward() #para frente      #forward(valor) somente número real
backward() #para trás        #backward(valor) somente número real

goto() ou setposition() #definir posição      #goto(valor,valor) valor é um par de números cartesianos tal que "0,0"

degrees() #graus
radians() #radiano

right() #para direita      #right(valor) verificar o valor do ângulo para virar para direita
left() #para esquerda      #left(valor)  verificar o valor do ângulo para virar para esquerda

pendown() #para riscar (abaixe a caneta)
penup() #para não riscar (levante a caneta)

pensize() ou width() #largura do traço     #pensize(valor) valor deve ser um número positivo

speed() #rapidez/ velocidade

pencolor() #cor da caneta             #pencolor([valor])   valor pode ser uma str "red", "green", ou "#56326"
fillcolor() #cor do preenchimento     #pencolor([valor])   uma tupla rgb(100, 200, 300) = três números inteiros representando rgb
bgcolor() #cor da tela inteira        #bgcolor("color")


title() #título acima da tela         #title("Ex: Ball")  pode descrever qualquer o título só lembrando que esse título é fora da tela


clear() #limpando a tela
reset() #começando tudo novamente

#preenchendo um desenho
fill(True)#antes de começar o desenho e...
fill(False) #...depois terminá-lo

home() #levando no (0,0)

#não seriam a mesma coisa entre eles ???

done() #feito


#...


#e demais conceitos....
