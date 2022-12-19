import re
from math import sqrt
from functools import partial
from tkinter import *

OPERADORES = ['×','^','+','%','÷','-','/','sqrt(']

def mostrar_calculo(*args):
    if any(TELA_CALCULADORA.get().endswith(operators) for operators in OPERADORES) or not TELA_CALCULADORA.get():
        try:
            int(args[0])
            temp = TELA_CALCULADORA.get()
            temp += f'{args[0]}'
            TELA_CALCULADORA.set(temp)
            return
        except ValueError:
            return
    elif args:
        EQUACAO = TELA_CALCULADORA.get()
        if args[0] == 'sqrt(' and EQUACAO:
            TEMP = re.findall('[+-/×/÷/sqrt(/%/^()]|\d+', TELA_CALCULADORA.get())
            TEMP2 = TEMP.pop()
            EQUACAO = ''.join(TEMP)
            EQUACAO += f'sqrt({TEMP2})'
            TELA_CALCULADORA.set(EQUACAO)
            return
        EQUACAO += f'{args[0]}'
        TELA_CALCULADORA.set(EQUACAO)


def resultado():
    EQUACAO_TEXTO = TELA_CALCULADORA.get().replace('×', '*').replace('÷', '/').replace('^', '**')
    eval(f'TELA_CALCULADORA.set({EQUACAO_TEXTO})')
    if len(TELA_CALCULADORA.get()) >= 26:
        try:
            TAMANHO_DO_RESULTADO = len(TELA_CALCULADORA.get()) - 4
            RESULTADO_SIMPLIFICADO = TELA_CALCULADORA.get()[0:4] + f'e{TAMANHO_DO_RESULTADO}'
            TELA_CALCULADORA.set(RESULTADO_SIMPLIFICADO)
        except ValueError:
            TELA_CALCULADORA.set(EQUACAO_TEXTO)
        return None
    return EQUACAO_TEXTO


JANELA_PRINCIPAL = Tk()
JANELA_PRINCIPAL.config(width=600, height=400, bg="#111111")



TELA_CALCULADORA = StringVar()
LABEL = Label(textvariable=TELA_CALCULADORA, font=("Ubuntu Medium", 24, "normal"), width=26, height=2, anchor='e')
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

MOSTRAR_RESULTADO = Button(text="=",width=6,height=3,bg="#CC0000",font=("Ubuntu Medium",24,"normal"),fg="white",highlightthickness=0,command=resultado)
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

RAIZ = Button(text="√",width=6,height=3,bg="#22A39F",font=("Ubuntu Medium",24,"normal"),command=partial(mostrar_calculo,'sqrt('))
RAIZ.grid(row=1,column=1)

POTENCIA = Button(text="^",width=6,height=3,bg="#22A39F",font=("Ubuntu Medium",24,"normal"),command=partial(mostrar_calculo,'^'))
POTENCIA.grid(row=1,column=2)




JANELA_PRINCIPAL.mainloop()