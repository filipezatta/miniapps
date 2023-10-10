from tkinter import *
from tkinter import ttk
import os

#classe lampada
class Lampada:
    

    
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
        print("Ligada")
    def desliga(self):
        self.ligada = False
        print("Desligada")
    def esta_ligada(self):
        if self.ligada == True:
            print("Ligada")
        else:
            print("Desligada")
    def ver_lampada(self):
        os.system('cls')
        print(self.__class__.__name__)
        valores = vars(self)
        for i in valores.values():
            print("\n", i)
        
    def criar_lampada(self):
        fazer_lampada = input('quer fazer uma lampada?') 
        if fazer_lampada == "y":
            print("ok")
            nome = input("qual o nome da lampada?")
            voltagem = input("qual a voltagem da lampada?")
            cor = input("qual a cor da lampada?")
            ligada = input("a lampada está ligada?")
            nome = Lampada(nome, voltagem, cor, ligada)

        elif fazer_lampada == "n":
            print('Certo, sem lampada então')

        elif fazer_lampada != "n" and "y":
            print('era y/n, mas ok')
           



#lampadas padrão
lampada0 = Lampada("lampada0",110, 'branca', True)
lampada1 = (vars(Lampada("lampada1",110, 'branca', True)))
lampada2 = (vars(Lampada("lampada2",220, 'amarela', False)))


## GUI

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
#row 0
ttk.Label(frm, text="Lampada!").grid(column=2, row=0)
#row 3
ttk.Button(frm, text="ligar lampada", command=lampada0.liga).grid(column=1, row=3)
ttk.Button(frm, text="desligar lampada", command=lampada0.desliga).grid(column=2, row=3)
ttk.Button(frm, text="ver status", command=lampada0.esta_ligada).grid(column=3, row=3)
#row 4
ttk.Button(frm, text="ver lampada", command=lampada0.ver_lampada).grid(column=1, row=4)
ttk.Button(frm, text="criar_lampada", command=lampada0.criar_lampada).grid(column=2, row=4) #arrumar
ttk.Button(frm, text="placeholder", command=Lampada.ver_categoria).grid(column=3, row=4)
#row 5
ttk.Button(frm, text="Clear", command=os.system('cls')).grid(column=1, row=5) #arrumar
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=5)

#loop end
root.mainloop()


    
input("Press enter to exit;")



















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
