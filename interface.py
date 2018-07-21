from tkinter import *
from Voz import *
import time
class Application:

    def __init__(self, master=NONE):

        self.speech = Speech()
        #frame texto
        self.frame1 = Frame(master)
        self.frame2 = Frame(master)
        self.frame_buttons1 = Frame(master,pady= 10)
        self.frame_buttons2 = Frame(master,pady =10)

        self.frame1.pack()
        self.frame2.pack(side=BOTTOM)
        self.frame_buttons1.pack(side= BOTTOM)
        self.frame_buttons2.pack(side = BOTTOM)

        #self.rec=0
        self.count=0
        self.escolher_menu=0


        self.msg = Label(self.frame1, text="Clique para falar")
        self.msg["font"] = ("Calibri0","20")
        self.msg.pack ()

        self.comida = Label(self.frame_buttons1, text="Comidas",bg='yellow',borderwidth= 10,width = 25)
        self.comida.pack(side=LEFT)

        self.agua = Label(self.frame_buttons1, text= "Agua",bg ='blue',borderwidth= 10,width = 25)
        self.agua.pack(side= LEFT)

        self.necessidade = Label(self.frame_buttons2,text='Necessidade', bg = 'green',borderwidth= 10,width = 25)
        self.necessidade.pack(side=LEFT)

        self.urgencia = Label(self.frame_buttons2,text='Urgencia', bg = 'red', borderwidth= 10, width = 25)
        self.urgencia.pack(side=LEFT)

        self.start = Button(self.frame2,text='selecionado')
        self.start["font"] = ("Calibri", "9")
        self.start["width"] = 10
        self.start["command"] = self.gra
        self.start.pack ()

    def gra(self):
        self.start.pack_forget()
        self.rec=Label(self.frame2,text='Gravando..',bg = 'red', borderwidth= 10, width = 25)
        self.rec.pack()
        self.frame1.after(5,self.menu_inicial)

    def count_gra(self):
        self.count=self.count+1
        textg = str(self.count) + '-Gravando..'
        self.rec['text'] = textg
        if self.escolher_menu == 'inicial':
            self.frame1.after(5,self.menu_inicial)
        elif self.escolher_menu == 'comida':
            self.frame1.after(5,self.comida_opcoes)
        elif self.escolher_menu == 'voltar_comida':
            self.frame1.after(5,self.voltar_comida)
        elif self.escolher_menu == 'agua':
            self.frame1.after(5,self.voltar_agua)
        elif self.escolher_menu == 'urgencia':
            self.frame1.after(5,self.voltar_urgencia)
        elif self.escolher_menu == 'necessidade':
            self.frame1.after(5,self.necessidade_opcoes)
        elif self.escolher_menu == 'voltar_necessidade':
            self.frame1.after(5,self.voltar_necessidade)


    def menu_inicial(self):
        self.count=0
        x = self.speech.voz()

        if 'comida' in x :
            self.msg['text'] = "Comida"
            self.rec['text'] = 'Gravando..'

            self.tela_comida()
        elif 'urgência' in x :
            self.msg['text'] = "Urgencia"
            self.rec['text'] = 'Gravando..'
            self.tela_urgencia()
        elif 'necessidade' in x :
            self.msg['text'] = "Necessidade"
            self.rec['text'] = 'Gravando..'
            self.tela_necessidade()
        elif 'água' in x :
            self.msg['text'] = "Água"
            self.rec['text'] = 'Gravando..'
            self.tela_agua()
        else:
            self.escolher_menu = 'inicial'
            self.frame1.after(5,self.count_gra)


                #MODULO DA COMIDA
    def tela_comida(self):

        self.count=0
        self.msg['text'] = "Escolha a comida"
        self.frame_buttons1.pack_forget()
        self.frame_buttons2.pack_forget()
        self.banana = Label(self.frame1, text='Banana',bg='yellow',borderwidth= 10,width = 25)
        self.banana.pack(side= LEFT)
        self.maça = Label(self.frame1, text='Maça',bg='yellow',borderwidth= 10,width = 25)
        self.maça.pack(side= LEFT)
        self.frame1.after(5,self.comida_opcoes)


    def comida_opcoes(self):
        x = self.speech.voz()
        verf = True
        #while verf:
        if 'banana' in x:
            self.msg['text']= """Comida Selecionada,fale sair para voltar"""
            self.banana['bg']= 'green'
            self.rec['text'] = 'Gravando..'
            self.count=0
            self.frame1.after(5,self.voltar_comida)
            verf = False
        elif 'maçã' in x:
            self.msg['text']= "Comida Selecionada, fale sair para voltar"
            self.maça['bg']= 'green'
            self.rec['text'] = 'Gravando..'
            self.count=0
            self.frame1.after(5,self.voltar_comida)
            verf = False
        else:
            self.msg['text']= " Comida nao encontrada, fale denovo!"
            self.escolher_menu ='comida'
            self.frame1.after(5,self.count_gra)

    def voltar_comida(self):
        x = self.speech.voz()
        if 'sair' in x :
            self.rec.pack_forget()
            self.banana.pack_forget()
            self.maça.pack_forget()
            self.frame_buttons1.pack(side= BOTTOM)
            self.frame_buttons2.pack(side= BOTTOM)
            self.start.pack(side= BOTTOM)
            self.msg['text']= "Clique para falar"
            return 0
        else:
             self.escolher_menu ='voltar_comida'
             self.frame1.after(5,self.count_gra)

                #MODULO DE AGUA
    def tela_agua(self):

        self.count=0
        self.msg['text'] = "Fale Agua para confirmar"
        self.frame_buttons1.pack_forget()
        self.frame_buttons2.pack_forget()
        self.agua = Label(self.frame1, text='agua',bg='Blue',borderwidth= 10,width = 25)
        self.agua.pack(side= BOTTOM)
        self.frame1.after(5,self.voltar_agua)

    def voltar_agua(self):
        x = self.speech.voz()
        #while True:
        if 'água' in x :
            self.msg['text'] = "Para voltar fale sair"
            self.agua['bg']= 'green'
            self.rec['text']= 'Gravando..'
            self.count=0
            self.frame1.after(5,self.voltar_agua)
        elif 'sair' in x :
            self.rec.pack_forget()
            self.agua.pack_forget()
            self.frame_buttons1.pack(side= BOTTOM)
            self.frame_buttons2.pack(side= BOTTOM)
            self.start.pack(side= BOTTOM)
            self.msg['text']= "Clique para falar"
            return 0
        else:
            self.msg['text'] = "Palavra Nao reconhecida , Fale dnv"
            self.escolher_menu = 'agua'
            self.frame1.after(5,self.count_gra)

            #MODULO URGENCIA

    def tela_urgencia(self):

        self.count=0
        self.msg['text'] = "Necessita de Urgencia!!!!"
        self.frame_buttons1.pack_forget()
        self.frame_buttons2.pack_forget()
        self.urgencia = Label(self.frame1, text='URGENCIA!!',bg='red',borderwidth= 10,width = 25)
        self.urgencia.pack(side= BOTTOM)
        self.frame1.after(5,self.voltar_urgencia)

    def voltar_urgencia(self):
        x = self.speech.voz()
        if 'sair' in x :
            self.rec.pack_forget()
            self.urgencia.pack_forget()
            self.frame_buttons1.pack(side= BOTTOM)
            self.frame_buttons2.pack(side= BOTTOM)
            self.start.pack(side= BOTTOM)
            self.msg['text']= "Clique para falar"
            return 0
        else:
            self.escolher_menu= 'urgencia'
            self.frame1.after(5,self.count_gra)

            #MODULO NECESSIDADE

    def tela_necessidade(self):
        self.count=0
        self.msg['text'] = "Escolha a necessidade"
        self.frame_buttons1.pack_forget()
        self.frame_buttons2.pack_forget()
        self.banheiro = Label(self.frame1, text='Banheiro',bg='yellow',borderwidth= 10,width = 25)
        self.banheiro.pack(side= BOTTOM)
        self.ajuda = Label(self.frame1, text='Ajuda',bg='yellow',borderwidth= 10,width = 25)
        self.ajuda.pack(side= BOTTOM)
        self.frame1.after(5,self.necessidade_opcoes)

    def necessidade_opcoes(self):
        x = self.speech.voz()
        #verf = True
        #while verf:
        if 'banheiro' in x:
            self.msg['text']= "Pedido feito,fale sair para voltar"
            self.banheiro['bg']= 'green'
            self.rec['text'] = 'Gravando..'
            self.count=0
            self.frame1.after(5,self.voltar_necessidade)
            #verf = False
        elif 'ajuda' in x:
            self.msg['text']= "Pedido feito, fale sair para voltar"
            self.ajuda['bg']= 'green'
            self.rec['text'] = 'Gravando..'
            self.count=0
            self.frame1.after(5,self.voltar_necessidade)
            #verf = False
        else:
            self.msg['text']= " necessidade nao encontrada, fale denovo!"
            self.escolher_menu= 'necessidade'
            self.frame1.after(5,self.count_gra)

    def voltar_necessidade(self):
        x = self.speech.voz()
        if 'sair' in x :
            self.rec.pack_forget()
            self.banheiro.pack_forget()
            self.ajuda.pack_forget()
            self.frame_buttons1.pack(side= BOTTOM)
            self.frame_buttons2.pack(side= BOTTOM)
            self.start.pack(side= BOTTOM)
            self.msg['text']= "Clique para falar"
            return 0
        else:
            self.escolher_menu= 'voltar_necessidade'
            self.frame1.after(5,self.count_gra)




root = Tk()
root.geometry("600x400")
Application(root)
root.mainloop()
