from customtkinter import *
from tkinter import messagebox, END

root = CTk()
root.geometry('500x250')
root.resizable(False, False)
root.title('Conversor de Comprimento')
root.iconbitmap('icone.ico')
root._set_appearance_mode('system')


def converter():
    try:
        opcao1 = optionmenu1.get()
        opcao2 = optionmenu2.get()
        if opcao1 == 'Centímetros' and opcao2 == 'Metros':
            float(entry2.get())
            resu = float(entry1.get()) / 100
            labelresu.configure(root, text=f'{resu:.2f}')
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry1.focus()
        elif opcao1 == 'Centímetros' and opcao2 == 'Quilômetros':
            float(entry2.get())
            resu = float(entry1.get()) / 100000
            labelresu.configure(root, text=f'{resu:.2f}')
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry1.focus()
        elif opcao1 == 'Metros' and opcao2 == 'Centímetros':
            float(entry2.get())
            resu = float(entry1.get()) * 100
            labelresu.configure(root, text=f'{resu:.2f}')
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry1.focus()
        elif opcao1 == 'Metros' and opcao2 == 'Quilômetros':
            float(entry2.get())
            resu = float(entry1.get()) / 1000
            labelresu.configure(root, text=f'{resu:.2f}')
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry1.focus()
        elif opcao1 == 'Quilômetros' and opcao2 == 'Centímetros':
            float(entry2.get())
            resu = float(entry1.get()) * 100000
            labelresu.configure(root, text=f'{resu:.2f}')
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry1.focus()
        elif opcao1 == 'Quilômetros' and opcao2 == 'Metros':
            float(entry2.get())
            resu = float(entry1.get()) * 1000
            labelresu.configure(root, text=f'{resu:.2f}')
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry1.focus()
        elif entry1.get() == '' or entry2.get() == '':
            messagebox.showerror(title='Erro!', message='Os campos devem ser '
                                                        'preenchidos com '
                                                        'valores numéricos')
    except ValueError:
        messagebox.showerror(title='Erro!', message='Os campos devem ser '
                                                    'preenchidos com valores '
                                                    'numéricos')


labelresu = CTkLabel(root, text='', font=('Arial', 15, 'bold'),
                     width=120, anchor='center')
labelresu.place(relx=0.39, rely=0.65)

optionmenu1 = CTkOptionMenu(root, values=['Centímetros', 'Metros',
                                          'Quilômetros'],
                            anchor='center',
                            font=('Arial', 15, 'bold'))
optionmenu1.place(relx=0.05, rely=0.05)

entry1 = CTkEntry(root, width=60, justify='center')
entry1.place(relx=0.12, rely=0.18)

labelseta = CTkLabel(root, text='→', font=('Arial', 40, 'bold'))
labelseta.place(relx=0.47, rely=0.05)

optionmenu2 = CTkOptionMenu(root, values=['Centímetros', 'Metros',
                                          'Quilômetros'],
                            anchor='center',
                            font=('Arial', 15, 'bold'))
optionmenu2.place(relx=0.67, rely=0.05)

entry2 = CTkEntry(root, width=60, justify='center')
entry2.place(relx=0.74, rely=0.18)

botao = CTkButton(root, text='Converter', font=('Arial', 15, 'bold'),
                  command=converter)
botao.place(relx=0.37, rely=0.42)

root.mainloop()
