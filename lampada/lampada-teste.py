from tkinter import *
from tkinter import ttk
import os
yes = ['yes', 'sim', 'y', 's', "True", "true"]
no = ['no', 'nao', 'n', 'não', "false", "False"]

#classe lampada
class Lampada:
    

    contagem = 3
    lampadatual =''
    def __init__(self, nome , voltagem, cor, ligada):
        self.nome = nome
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = ligada
        
        
    @classmethod
    def ver_categoria(cls):
        print(cls)


    def liga(self):
        self.ligada = True
        #print("Ligada")
        Lampada.ver_lampada(self)
    def desliga(self):
        self.ligada = False
        #print("Desligada")
        Lampada.ver_lampada(self)
    def ver_lampada(self):
        os.system('cls' or 'clear')
        print(self.__class__.__name__)
        valores = vars(self)
        for i in valores.values():
            print("\n", i)
        
    def criar_lampada(self):
        print("ok")
        
        nome = "lampada{}".format(Lampada.contagem)
        voltagem = input("qual a voltagem da lampada? ")
        cor = input("qual a cor da lampada? ")
        if input("a lampada está ligada? ") in yes:
            ligada = True
        else:
            ligada = False
        #ligada = input("a lampada está ligada? ")
        newlampname = "lampada{}".format(Lampada.contagem)
        newlampname = Lampada(nome, voltagem, cor, ligada)
        Lampada.ver_lampada(newlampname)
        Lampada.contagem += 1
    
        lampadatual.clear()
        lampadatual.append(newlampname)

        lampadatual[0].ver_lampada()
        return(lampadatual)
           
#lampadas padrão
lampada0 = Lampada("lampada0",110, 'branca', True)
lampada1 = Lampada("lampada1",110, 'branca', True)
lampada2 = Lampada("lampada2",220, 'amarela', False)


lampadas = [lampada0, lampada1, lampada2]


#asdasdsa
def escolher_lampada():
    for i in lampadas:
        print(i.nome)
    print('\n')
    lampadatual.clear()
    lampadatual.append(eval(input("Qual lampada você quer ver? ")))
    lampadatual[0].ver_lampada()
    return(lampadatual)


lampadatual = [lampada1]



def iniciar_programa():
    
    if input('quer escolher uma lampada?') in yes:
        escolher_lampada()
    
    elif input('quer fazer uma lampada?') in yes:
        lampadatual[0].criar_lampada() 
    else:
        print('Certo, sem lampada então')

## GUI


root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

#row 0
ttk.Label(frm, text="Lampada!").grid(column=2, row=0)
ttk.Label(frm, text="").grid(column=2, row=1)
ttk.Label(frm, text="").grid(column=2, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=9)
#row 3
iniciar_programa()

ttk.Button(frm, text="ligar lampada", command=lampadatual[0].liga).grid(column=1, row=3)
ttk.Button(frm, text="desligar lampada", command=lampadatual[0].desliga).grid(column=2, row=3)
ttk.Label(frm, text="").grid(column=2, row=6)
ttk.Label(frm, text="").grid(column=2, row=5)
ttk.Label(frm, text="").grid(column=2, row=6)
ttk.Label(frm, text="").grid(column=2, row=7)
ttk.Label(frm, text="").grid(column=2, row=8)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=9)

ttk.Button(frm, text="escolher_lampada", command=escolher_lampada).grid(column=4, row=3)
#loop end
root.mainloop()

#input("Press enter to exit;")



















"""
def criar_lampada(string):
    fazer_lampada = input('quer fazer uma lampada?') 
    if fazer_lampada == "y":
        print("ok")
        globals[(vars(Lampada(input("voltagem"), input("cor"), input("ligada"))))] = string
        print(ver_lampada(string))
    elif fazer_lampada == "n":
        print('Certo, sem lampada então')

    elif fazer_lampada != "n" and "y":
        print('era y/s, mas ok')

"""
