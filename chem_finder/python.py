import pandas as pd

chem_df = pd.read_csv('upload/reagentes.csv')

def checar(reagente):
    if (reagente in chem_df['Material de química'].values) or (reagente in chem_df['Fórmula'].values):
        print("O reagente está presente na tabela. \n\n")
    else:
        print("O reagente não está presente na tabela. \n\n")
        
    if(input("quer checar outro?")=="sim"):
        checar(input("Qual o nome do outro reagente?\n\n"))
        
checar(input("Qual o nome do reagente? \n\n"))