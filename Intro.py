import customtkinter as CTk
from tkinter import *
from tkinter import messagebox



janela = CTk.CTk()

    
class Application():
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()
       
    def tema(self):
        CTk.set_appearance_mode("dark")
        CTk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("900x500")
        janela.title("sistema de login")
   
        janela.resizable(False, False)

    def tela_login(self):

        label_tt = CTk.CTkLabel(master=janela, text= "*-*", font=("Roboto", 18), text_color="#00B0F0"). place(x=10, y=10)


        #frame
        login_frame = CTk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        #widgets dentro da frane de tela do login
        label = CTk.CTkLabel(master=login_frame, text='Faça o Login', font = ('Roboto', 35, 'bold'), text_color= ('white') )
        label.place(x=25, y=5)

        username_entry1 = CTk.CTkEntry(master=login_frame, placeholder_text="Nome de usuario", width=300, font=("Roboto", 14)).place(x=25, y=105)
        username_label1 = CTk.CTkLabel(master=login_frame, text="*O campo nome de usario e de carater obrigatorio.", text_color="green", font =("Roboto", 12)). place(x=25, y= 135)

        password_entry2 = CTk.CTkEntry(master=login_frame, placeholder_text="Senha de usuario", width=300, font=("Roboto", 14), show="*").place(x=25, y=175)
        password_label2 = CTk.CTkLabel(master=login_frame, text="*O campo nome de senha e de carater obrigatorio.", text_color="green", font =("Roboto", 12)). place(x=25, y= 205)

        Checkbox = CTk.CTkCheckBox(master= login_frame, text="Lembrar-se de min sempre").place(x=25, y=235)

        def login():
            messagebox.showinfo(title="Estado do Login", message="Login feito com sucesso")

            pass
        login_button = CTk.CTkButton(master=login_frame, text="login", width=300, command=login).place(x=25, y=285)

        register_span = CTk.CTkLabel(master=login_frame, text="Se não tenha uma conta").place(x=25, y=325)

        def tela_cadastro():
            #remover frame de login
            login_frame.pack_forget()

            #criando a tela de cadastro de usuarios            
            cd_frame = CTk.CTkFrame(master=janela, width=350, height=396)
            cd_frame.pack(side=RIGHT)

            label = CTk.CTkLabel(master=cd_frame, text='Faça o seu cadastro', font = ('Roboto', 20, 'bold'), text_color= ('white') )
            label.place(x=25, y=5)  

            span = CTk.CTkLabel(master=cd_frame, text="Por favor complete todos seus dados corretamente", font=("Roboto", 12), text_color="gray").place(x=25, y=50)          

            username_entry1 = CTk.CTkEntry(master=cd_frame, placeholder_text="Nome de usuario", width=300, font=("Roboto", 14)).place(x=25, y=105)

            email_entry1 = CTk.CTkEntry(master=cd_frame, placeholder_text="E-mail de usuario", width=300, font=("Roboto", 14)).place(x=25, y=145)

            password_entry1 = CTk.CTkEntry(master=cd_frame, placeholder_text="Senha de usuario", width=300, font=("Roboto", 14), show="*").place(x=25, y=185)

            cPassword_entry1 = CTk.CTkEntry(master=cd_frame, placeholder_text="Comfirma sua senha", width=300, font=("Roboto", 14), show="*").place(x=25, y=225)

            Checkbox = CTk.CTkCheckBox(master= cd_frame, text="Aceitar os Termos e Politicas").place(x=25, y=265)


            def back():
                #Removendo o frame de cadastro
                cd_frame.pack_forget()

                #Devolvendo o frame de login
                login_frame.pack(side=RIGHT)

 
            back_button = CTk.CTkButton(master=cd_frame, text="VOLTAR", width=145, fg_color="gray", hover_color="#202020", command=back).place(x=25, y=300)

            def save_user():
                msg = messagebox.showinfo(title="Estado do Cadastro", message="Muito bem usuario foi cadastrado com sucesso.")
                pass
            save_button = CTk.CTkButton(master=cd_frame, text="CADASTRAR", width=145, fg_color="green", hover_color="#014B105", command=save_user).place(x=180, y=300)



        cadastro_button = CTk.CTkButton(master=login_frame, text="Cadastra-se", width=150, fg_color="green", hover_color="#2D9334", command=tela_cadastro).place(x=175, y=325)




Application()