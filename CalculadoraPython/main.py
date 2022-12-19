import operator
from functools import partial
from tkinter import *


Numeros = []
Operadores = []
operacoes = {
    "+": operator.add,
    "-": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "^": operator.xor,
    "√": operator.sub
}
def mostrar_calculo(*args):
    if len(label_text.get()) >= 26:
        return None
    elif args:
        temp = label_text.get()
        temp += f'{args[0]} '
        label_text.set(temp)


TK = Tk()
TK.config(width=600,height=400,bg="#111111")




label_text = StringVar()
LABEL = Label(textvariable=label_text, font=("Ubuntu Medium",24,"normal"), width=26, height=2,anchor='e')
LABEL.config(fg="black",bg="DARKGREEN",highlightthickness=0)
LABEL.grid(row=0,column=0,columnspan=4)




NUMERO_1 = Button(text="1",width=6,height=3,bg="#434242",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0,command=partial(mostrar_calculo,'1'))
NUMERO_1.grid(row=4,column=0)

NUMERO_2 = Button(text="2",width=6,height=3,bg="#434242",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0,command=partial(mostrar_calculo,'2'))
NUMERO_2.grid(row=4,column=1)

NUMERO_3 = Button(text="3",width=6,height=3,bg="#434242",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0,command=partial(mostrar_calculo,'3'))
NUMERO_3.grid(row=4,column=2)

NUMERO_4 = Button(text="4",width=6,height=3,bg="#434242",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0,command=partial(mostrar_calculo,'4'))
NUMERO_4.grid(row=3,column=0)

NUMERO_5 = Button(text="5",width=6,height=3,bg="#434242",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0,command=partial(mostrar_calculo,'5'))
NUMERO_5.grid(row=3,column=1)

NUMERO_6 = Button(text="6",width=6,height=3,bg="#434242",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0,command=partial(mostrar_calculo,'6'))
NUMERO_6.grid(row=3,column=2)

NUMERO_7 = Button(text="7",width=6,height=3,bg="#434242",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0,command=partial(mostrar_calculo,'7'))
NUMERO_7.grid(row=2,column=0)

NUMERO_8 = Button(text="8",width=6,height=3,bg="#434242",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0,command=partial(mostrar_calculo,'8'))
NUMERO_8.grid(row=2,column=1)

NUMERO_9 = Button(text="9",width=6,height=3,bg="#434242",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0,command=partial(mostrar_calculo,'9'))
NUMERO_9.grid(row=2,column=2)

NUMERO_0 = Button(text="0",width=6,height=3,bg="#434242",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0,command=partial(mostrar_calculo,'0'))
NUMERO_0.grid(row=5,column=1)

MOSTRAR_RESULTADO = Button(text="=",width=6,height=3,bg="#CC0000",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0)
MOSTRAR_RESULTADO.grid(row=5,column=3)




SOMA = Button(text="+",width=6,height=3,bg="#22A39F",font=("Ubuntu Medium",24,"normal"),command=partial(mostrar_calculo,'+'))
SOMA.grid(row=1,column=3)

SUBTRACAO = Button(text="-",width=6,height=3,bg="#22A39F",font=("Ubuntu Medium",24,"normal"),command=partial(mostrar_calculo,'-'))
SUBTRACAO.grid(row=2,column=3)

MULTIPLICACAO = Button(text="×",width=6,height=3,bg="#22A39F",font=("Ubuntu Medium",24,"normal"),command=partial(mostrar_calculo,'×'))
MULTIPLICACAO.grid(row=3,column=3)

DIVISAO = Button(text="÷",width=6,height=3,bg="#22A39F",font=("Ubuntu Medium",24,"normal"),command=partial(mostrar_calculo,'÷'))
DIVISAO.grid(row=4,column=3)

MODULO = Button(text="%",width=6,height=3,bg="#22A39F",font=("Ubuntu Medium",24,"normal"),command=partial(mostrar_calculo,'%'))
MODULO.grid(row=1,column=0)

RAIZ = Button(text="√",width=6,height=3,bg="#22A39F",font=("Ubuntu Medium",24,"normal"),command=partial(mostrar_calculo,'√'))
RAIZ.grid(row=1,column=1)

POTENCIA = Button(text="^",width=6,height=3,bg="#22A39F",font=("Ubuntu Medium",24,"normal"),command=partial(mostrar_calculo,'^'))
POTENCIA.grid(row=1,column=2)




TK.mainloop()