#importanto tkinter
from tkinter import *
from tkinter import ttk

#cores
cor1 = "#000000"#preto
cor2 = "#ffffff"#branco
cor3 = "#ff7700"#laranja
cor4 = "#1a202e"#azul acinzentado
cor5 = "#5c5c5c"#cinza claro


janela =Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1,column=0)





janela.mainloop()