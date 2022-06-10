from tkinter import *



janela = Tk()

janela.geometry('1200x1000')

def format_cpf(event = None):
    text = cpf2.get().replace(".","").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in[2,5]: new_text += text[index] + "."
        elif index == 8: new_text += text[index] + "-"
        else: new_text += text[index]

    cpf2.delete(0, "end")
    cpf2.insert(0, new_text)

def format_telefone(event = None):
    text = telefone2.get().replace(".","").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in[6]: new_text += text[index] + "-"
        else: new_text += text[index]

    telefone2.delete(0, "end")
    telefone2.insert(0, new_text)
f1 = Frame(janela, highlightbackground='#22E3E0', highlightthickness=2)
f2 = Frame(janela, highlightbackground='#22E3E0', highlightthickness=2)
f3 = Frame(janela, highlightbackground='#22E3E0', highlightthickness=2)
f4 = Frame(janela, highlightbackground='#F40B00', highlightthickness=2)
f5 = Frame(janela, highlightbackground='#22E3E0', highlightthickness=2, bg='#22E3E0')
f6 = Frame(janela, highlightbackground='#22E3E0', highlightthickness=2, borderwidth=100)
f7 = Frame(janela, highlightbackground='#22E3E0', highlightthickness=2, bg='#22E3E0')

def tela():
    f5.grid(row=0, column=0, sticky=NSEW, columnspan=2 , padx=100, pady=100)
    f1.grid(row=1, column=0, sticky=NSEW, pady=15)
    f2.grid(row=1, column=1, sticky=NSEW, pady=15, padx=0)
    f3.grid(row=2, column=0, columnspan=2)
    f4.grid(row=4, column=1, columnspan=2)
    f6.grid_forget()
    f7.grid_forget()

def telo():
    f1.grid_forget()
    f2.grid_forget()
    f3.grid_forget()
    f4.grid_forget()
    f5.grid_forget()
    f6.grid(row=4, column=0, pady=70, padx=250)
    f7.grid(row=3, column=0, sticky=NSEW, columnspan=2, pady=10)

mascVar = IntVar()

cb_masc= Radiobutton(f6, text='masculino',font='ARIAL 20', variable=mascVar, value=0 )

cb_fem= Radiobutton(f6, text='feminino',font='ARIAL 20', variable=mascVar, value=1)

dado = Label(f1, font='Arial 30 ', foreground='#22E3E0', text='DADOS:' )
texto = Label(f5, font='ARIAL 40 italic', foreground='white', text='CADASTRO', bg='#22E3E0', anchor=E, width=23)
nome = Label(f1, font='ARIAL 20 italic', text='Nome:')
nome2 = Entry(f1, font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
cpf = Label(f1, font='ARIAL 20 italic', text='Cpf:')
cpf2 = Entry(f1,font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
cpf2.bind("<KeyRelease>", format_cpf)
pas = Label(f7, font='ARIAL 40 italic', foreground='white', text='LOGIN', bg='#22E3E0', anchor=E, width=23)

data = Label(f1, font='ARIAL 20 italic', text='Data De Nascimento:')
data2 = Entry(f1, font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
telefone = Label(f1, font='ARIAL 20 italic', text='Telefone:')
telefone2 = Entry(f1, font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
telefone2.bind("<KeyRelease>", format_telefone)
endereço = Label(f2, font='ARIAL 30', foreground='#22E3E0', text='Endereço:')
rua = Label(f2, font='ARIAL 20 italic', text='Rua:')
rua2 = Entry(f2, font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
bairro = Label(f2, font='ARIAL 20 italic', text='Bairro:')
bairro2 = Entry(f2, font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
cidade = Label(f2, font='ARIAL 20 italic', text='Cidade:')
cidade2 = Entry(f2, font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
n = Label(f2, font='ARIAL 20 italic', text='N°:' )
n2 = Entry(f2, font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
uf = Label(f2, font='ARIAL 20 italic', text='Uf:' )
uf2 = Entry(f2, font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
registro = Label(f1, font='ARIAL 20 italic', text='Registro:' )
registro2 = Entry(f1, font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
sair= Button(f4, font='ARIAL 20', text='Sair', command=telo)
email = Label(f6, font='ARIAL 20 italic', text='Email:', highlightthickness=2 )
email2 = Entry(f6, font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
senha = Label(f6, font='ARIAL 20 italic', text='Senha:', highlightthickness=2 )
senha2 = Entry(f6, font='ARIAL 20 italic', highlightthickness=2)
senha2 = Entry(f6, show='*',font='ARIAL 20 italic', highlightbackground='#22E3E0', highlightthickness=2)
botao= Button(f6, font='ARIAL 20 italic',text='entrar', highlightbackground='#22E3E0', highlightthickness=2, command=tela)

for linha in range (7):
    janela.grid_columnconfigure(linha, weight=3)

f6.grid(row=4, column=0, pady=70, padx=250)
f7.grid(row=3, column=0, sticky=NSEW, columnspan=2, pady=10)
botao.grid(row=4, column=2)
pas.grid(row=0, column=0, columnspan=2)
email.grid(row=0, column=0, pady=20)
email2.grid(row=0, column=1, pady=20)
senha.grid(row=1, column=0, pady=20)
senha2.grid(row=1, column=1, pady=20)
texto.grid(row=0, column=0, columnspan=2)
dado.grid(row=0, column=0)
nome.grid(row=1, column=0)
nome2.grid(row=1, column=1, pady=5)
cpf.grid(row=2, column=0)
cpf2.grid(row=2, column=1, pady=5)
data.grid(row=3, column=0)
data2.grid(row=3, column=1, pady=5)
telefone.grid(row=4, column=0)
telefone2.grid(row=4, column=1, pady=5)
registro.grid(row=5, column=0)
registro2.grid(row=5, column=1, pady=5)
endereço.grid(row=0, column=2)
rua.grid(row=1, column=2)
rua2.grid(row=1, column=3, pady=5)
bairro.grid(row=2, column=2)
bairro2.grid(row=2, column=3, pady=5)
cidade.grid(row=3, column=2)
cidade2.grid(row=3, column=3, pady=5)
n.grid(row=4, column=2)
n2.grid(row=4, column=3, pady=5)
uf.grid(row=5, column=2)
uf2.grid(row=5, column=3, pady=5)
sair.grid(row=0, column=0)
cb_masc.grid(row=3, column=0)
cb_fem.grid(row=3, column=1)

janela.mainloop()