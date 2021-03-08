# -*- coding: utf-8 -*-
from email.message import EmailMessage
import smtplib
import config as cfg
from time import sleep

class EnviarEmail():

    #iniciando o construtor
    def __init__(self,destinatario,mensagem,anexo):
        self.destinatario = destinatario
        self.mensagem = mensagem
        self.anexo = anexo
        print(mensagem)

    #iniciando função de envio
    def enviar(self):
        #instanciando a framework e definindo valores de envio
        msg = EmailMessage()
        msg['Subject'] = 'CV'
        msg['From'] = cfg.usuario
        msg['To'] = self.destinatario
        msg.set_content(self.mensagem)

        #lendo anexo para envio
        with open(self.anexo,'rb') as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype = 'application', subtype ='octet-stream', filename = file_name)

        #configurando servidor SMTP
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:
            smtp.ehlo()
            #inicando tls
            smtp.starttls()
            smtp.ehlo()

            #realizando login
            smtp.login(cfg.usuario,cfg.senha) 

            #enviando email
            smtp.send_message(msg)


class main():

    anexo = input("digite o endereço e o nome do arquivo que sera enviado em anexo com sua extensão \n ex: 'documentos/CV.pdf'")
    # abrindo arquivo com a lista de contatos
    f = open('contatos.txt', 'r')
    
    for email in f:

        #instanciando a classe EnviarEmail
        newEmail = EnviarEmail(email,open("mensagem.txt", "r").read(),"anexo")
        #iniciando a função enviar
        newEmail.enviar()
        print(f'email enviado para {email}')
        sleep(5)




