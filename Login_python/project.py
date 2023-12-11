from tkinter import *
root = Tk()
root.geometry("500x300")
root.title("Calculator")


def getvals():
    print("Aceitar")

#cabeçalho

Label(root, text="Formulário de Registro Python", font="arial 15 bold").grid(row=0, column=3)


#Nome do campo
name = Label(root, text="Nome")
phone = Label(root, text="Tel")
gender = Label(root, text="Gênero")
emergency = Label(root, text="Emergência")
paymentmood = Label(root, text="Modo de Pagamento")

#Campo de informações
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

#Variável para armazenamento de dados
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmoodvalue = StringVar()
checkvalue = IntVar()


#Criando campo de entrada
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmoodentry = Entry(root, textvariable=paymentmoodvalue)

#Packing entry field
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)


#Criando caixa de seleção
checkbtn = Checkbutton(text="Salvar login?", variable = checkvalue)
checkbtn.grid(row = 6, column = 3 )


# Botão de envio
Button(text = "Submit", command = getvals).grid(row = 7, column = 3)

root.mainloop()
