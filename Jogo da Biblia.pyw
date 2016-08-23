from tkinter import *

# Método de Daniel referente a resposta ----------------
def bt1116_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nDaniel 1:1-6',
                     font='Verdana',
                     height=5,
                     width=25,                    
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)

def bt2116_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nDaniel 1:1-6',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)            
    
        
          

# Método de Daniel referente a pergunta ---------------
def daniel_116():    
        
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
               text="Para que país Daniel foi levado como escravo?",
               font='Verdana',
               height=3,
               bg='FireBrick',
               fg='white').pack(fill=BOTH, expand=1)
    
    b1 = Button(filewin,
                     text="Babilônia",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt1116_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                     text="Egito",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2116_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                     text="Assíria",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2116_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                     text="Israel",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2116_onclick).pack(fill=BOTH, expand=1)

# -------------------------------------------------------------------------------------------------------------
  # Método de tiago referente a resposta 
def bt1514_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nTiago 5:14',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)

def bt2514_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nTiago 5:14',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)
  
# Método de tiago referente a pergunta 
def tiago_514():    
        
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
               text="Com o que devemos ungir os enfermos?",
               font='Verdana',
               height=3,
               bg='FireBrick',
               fg='white').pack(fill=BOTH, expand=1)
    
    b1 = Button(filewin,
                     text="Água",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2514_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                     text="Azeite",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt1514_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                     text="Vinho",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2514_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                     text="Essência",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2514_onclick).pack(fill=BOTH, expand=1)

  
#-------------------------------------------------------------------------------------------------------

# Método de gêneses referente a pergunta 
def geneses_4125():    
        
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
               text="Quem eram os pais de Caim, Abel e Sete?",
               font='Verdana',
               height=3,
               bg='FireBrick',
               fg='white').pack(fill=BOTH, expand=1)
    
    b1 = Button(filewin,
                     text="Isaque e Rebeca",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt24125_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                     text="Davi e Mical",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt24125_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                     text="Adão e Eva",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt14125_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                     text="Maria e Jó",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt24125_onclick).pack(fill=BOTH, expand=1)

# Método de geneses referente a resposta 

def bt14125_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nGênesis 4:1-25',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)

def bt24125_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nGênesis 4:1-25',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)

#-------------------------------------------------------------------------------------------------------
# Método de gêneses referente a pergunta 
def joao_148():    
        
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
               text="Que discípulo Jesus encontrou sob uma figueira?",
               font='Verdana',
               height=3,
               bg='FireBrick',
               fg='white').pack(fill=BOTH, expand=1)
    
    b1 = Button(filewin,
                     text="Natanael",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt1148_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                     text="Mateus",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2148_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                     text="Judas",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2148_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                     text="Zaqueu",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2148_onclick).pack(fill=BOTH, expand=1)

# Método de geneses referente a resposta 

def bt1148_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nJoão 1:48',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)

def bt2148_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nJoão 1:48',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)

#-------------------------------------------------------------------------------------------------------
# Método de atos referente a pergunta 
def atos_182():    
        
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
               text="Quem foi o imperador romano que \nobrigou todos os judeus a saírem de Roma?",
               font='Verdana',
               height=3,
               bg='FireBrick',
               fg='white').pack(fill=BOTH, expand=1)
    
    b1 = Button(filewin,
                     text="Otávio",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2182_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                     text="Augusto",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2182_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                     text="Cláudio",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt1182_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                     text="Constantino",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2182_onclick).pack(fill=BOTH, expand=1)

# Método de geneses referente a resposta 

def bt1182_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nAtos 18:2',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)

def bt2182_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nAtos 18:2',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)

#-------------------------------------------------------------------------------------------------------

# Método de 1ª Samuel referente a pergunta 
def Isamuel_174950():    
        
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
               text="O que Davi utilizou para matar Golias?",
               font='Verdana',
               height=3,
               bg='FireBrick',
               fg='white').pack(fill=BOTH, expand=1)
    
    b1 = Button(filewin,
                     text="Um dardo",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2174950_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                     text="Arco e flecha",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2174950_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                     text="Uma funda",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt1174950_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                     text="Uma pedra",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2174950_onclick).pack(fill=BOTH, expand=1)

# Método de geneses referente a resposta 

def bt1174950_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nI Samuel 17:49-50',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)

def bt2174950_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nI Samuel 17:49-50',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)

#-------------------------------------------------------------------------------------------------------

# Método de 1ª Samuel referente a pergunta 
def lucas_323():    
        
    filewin = Toplevel(janela)
    pergunta = Label(filewin,
               text="Quandos anos tinha Jesus Cristo \nquando comerçou a pregar seu ministério?",
               font='Verdana',
               height=3,
               bg='FireBrick',
               fg='white').pack(fill=BOTH, expand=1)
    
    b1 = Button(filewin,
                     text="Aproximadamente 30 anos",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt1323_onclick).pack(fill=BOTH, expand=1)
    b2 = Button(filewin,
                     text="Aproximadamente 33 anos",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2323_onclick).pack(fill=BOTH, expand=1)
    b3 = Button(filewin,
                     text="Aproximadamente 35 anos",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2323_onclick).pack(fill=BOTH, expand=1)
    b4 = Button(filewin,
                     text="Aproximadamente 32 anos",
                     font='Verdana',
                     height=2,
                     bg='Khaki',
                command=bt2323_onclick).pack(fill=BOTH, expand=1)

# Método de geneses referente a resposta 

def bt1323_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='CERTO A RESPOSTA! \n\nConfira a resposta em \nI Samuel 17:49-50',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='green',
                     fg='white').pack(fill=BOTH, expand=1)

def bt2323_onclick():
    filewin = Toplevel(janela)    

    pergunta = Label(filewin,
                     text='RESPOSTA ERRADA! \n\nVeja a resposta em \nI Samuel 17:49-50',
                     font='Verdana',
                     height=5,
                     width=25,
                     bg='red',
                     fg='white').pack(fill=BOTH, expand=1)

#------------------------------------------------------------------------------------------------------- 
    
class Packing:	
    def __init__(self,instancia):
        
        self.container1=Frame(instancia)
        self.container2=Frame(instancia)
        self.container3=Frame(instancia)
       
        self.container1.pack(expand=1)
        self.container2.pack(expand=1)
        self.container3.pack(expand=1)
      
        Button(self.container1,width=18,height=3,text='Daniel 1:1-6',font='Verdana', bg='FireBrick',fg='white',command=daniel_116).pack(side=RIGHT)
        Button(self.container1,width=18,height=3,text='Atos 18:2',font='Verdana', bg='FireBrick',fg='white',command=atos_182).pack(side=RIGHT)
        Button(self.container1,width=18,height=3,text='Gênesis 4:1-25',font='Verdana',bg='FireBrick',fg='white',command=geneses_4125).pack()
        Button(self.container2,width=18,height=3,text='Tiago 5:14',font='Verdana',bg='FireBrick',fg='white',command=tiago_514).pack(side=LEFT)
        Button(self.container2,width=18,height=3,text='João 1:48',font='Verdana',bg='FireBrick',fg='white',command=joao_148).pack(side=LEFT)
        Button(self.container2,width=18,height=3,text='Lucas 3:23',font='Verdana',bg='FireBrick',fg='white',command=lucas_323).pack(side=LEFT)

        self.b4=Button(self.container3,width=18,height=3,text='Mateus 4:3-4',font='Verdana',bg='FireBrick',fg='white',command=joao_148)
        self.b5=Button(self.container3,width=18,height=3,text='I Samuel 17:49-50',font='Verdana',bg='FireBrick',fg='white',command=Isamuel_174950)
        self.b6=Button(self.container3,width=18,height=3,text='João 4:6-7',font='Verdana',bg='FireBrick',fg='white',command=joao_148)
        
        self.b6.pack(side=RIGHT)
        self.b4.pack(side=RIGHT)
        self.b5.pack(side=RIGHT)        
        

janela = Tk()
Packing(janela)
janela['bg']='white'
janela.title('Conhecendo a Bíblia Com Perguntas e Respostas')
janela.geometry('600x300')
menubar = Menu(janela)
janela.config(menu=menubar)

# ==============================================================
# Método Donothing
def donothing():
    filewin = Toplevel(janela)
    lb0 = Label(filewin, text='Momentos de Buscar Sabedoria e Refletir.',bg='Black',fg='white')
    lb01 = Label(filewin, text='',bg='Black')
    lb02 = Label(filewin, text='',bg='Black')
    lb03 = Label(filewin, text='',bg='Black')
    lb1 = Label(filewin,text='O Evangelho Está Funcionando para Você?',font='Verdana',bg='white',width=80,height=3)
    lb2 = Label(filewin,text='Comece de Onde Está, Seja humilde sempre.',font='Verdana',bg='yellow',width=80,height=3)
    lb3 = Label(filewin,text='Você É Digno de Ser Resgatado Pelo Senhor',font='Verdana',bg='blue',fg='white',width=80,height=3)
    lb4 = Label(filewin,text='Precisamos Reservar Tempo Para Exercer A Fé.',font='Verdana',bg='green',width=80,height=3)
    lb5 = Label(filewin,text='Não Deixe Que Nada Nem Ninguém O Impeça De Ser Vitorioso.',font='Verdana',bg='DarkKhaki',width=80,height=3)
    lb6 = Label(filewin,text='A Oração Em Família Deve Ser Uma Prioridade Inadiável De Sua Vida Diária.',font='Verdana',bg='Maroon',fg='white',width=80,height=3)
    lb7 = Label(filewin,text='“Rejeitar o mal e escolher o bem” (Isaías 7:15).',font='Verdana',bg='Thistle',width=80,height=3)
    lb8 = Label(filewin,text='É importante erguer-nos acima das racionalizações e fazer as melhores escolhas.',font='Verdana',bg='Lime',width=80,height=3)
    lb9 = Label(filewin,text='Quando racionalizamos as escolhas erradas, perdemos as bênçãos que necessitamos.',font='Verdana',bg='SlateGray',width=80,height=3)
    lb10 = Label(filewin,text='A imensidão do universo não mudou de repente, mas nossa \ncapacidade de ver e entender essa verdade mudou drasticamente.',font='Verdana',bg='SteelBlue',width=80,height=3)
    lb11 = Label(filewin,text='Nosso conhecimento prévio pode até parecer tolice para nós porque o que \nantes era tão claro novamente se tornou borrado, embaçado e distante.',fg='white',font='Verdana',bg='Navy',width=80,height=3)
    lb12 = Label(filewin,text='Acaso não temos motivo para encher-nos de gratidão, \nsejam quais forem as circunstâncias em que nos encontremos?',font='Verdana',bg='#00FFFF',width=80,height=3)
    lb13 = Label(filewin,text='E aquele que receber todas as coisas com gratidão será glorificado; e as coisas desta Terra \nser-lhe-ão acrescentadas, mesmo centuplicadas, sim, mais',font='Verdana',bg='SkyBlue',width=80,height=3)

    lb0.pack(side=TOP, fill=X)
    lb01.pack(side=LEFT, fill=Y)
    lb02.pack(side=RIGHT, fill=Y)
    lb03.pack(side=BOTTOM, fill=X)
    lb1.pack(side=TOP,fill=BOTH,expand=1)
    lb2.pack(side=TOP,fill=BOTH,expand=1)
    lb3.pack(side=TOP,fill=BOTH,expand=1)
    lb4.pack(side=TOP,fill=BOTH,expand=1)
    lb5.pack(side=TOP,fill=BOTH,expand=1)
    lb6.pack(side=TOP,fill=BOTH,expand=1)
    lb7.pack(side=TOP,fill=BOTH,expand=1)
    lb8.pack(side=TOP,fill=BOTH,expand=1)
    lb9.pack(side=TOP,fill=BOTH,expand=1)
    lb10.pack(side=TOP,fill=BOTH,expand=1)
    lb11.pack(side=TOP,fill=BOTH,expand=1)
    lb12.pack(side=TOP,fill=BOTH,expand=1)
    lb13.pack(side=TOP,fill=BOTH,expand=1)

def exemplo1():
    filewin = Toplevel(janela)
    lb0 = Label(filewin, text='Momento de Reflexão',bg='Black',fg='white')
    lb01 = Label(filewin, text='',bg='Black')
    lb02 = Label(filewin, text='',bg='Black')
    lb03 = Label(filewin, text='',bg='Black')

    lb0.pack(side=TOP, fill=X)
    lb01.pack(side=LEFT, fill=Y)
    lb02.pack(side=RIGHT, fill=Y)
    lb03.pack(side=BOTTOM, fill=X)
    
    T=Text(filewin, height=20, width=50)
    T.pack()
    T.insert(END, "Assim como o Bom Pastor encontra Sua ovelha perdida, se você simplesmente elevar seu coração ao Salvador do mundo, Ele vai encontrá-lo.")
    T.insert(END,'Com frequência, o sofrimento deles decorria de algo que lhes parecia ser um ponto final. Alguns se veem diante do fim de um terno relacionamento, como a morte de um ente querido ou a alienação de um membro da família. Outros sentem que chegaram ao fim da esperança — a esperança de casar-se, de ter filhos ou de vencer uma doença. Outros podem estar encarando o fim de sua fé, quando vozes conflitantes e desorientadoras do mundo os tentam a questionar, ou até a abandonar o que antes sabiam ser verdade.')


# ==============================================================
# Menu Arquivo
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Arquivo", menu=filemenu)

# Submenu de Arquivo
filemenu.add_command(label="Palavras de Sabedoria", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Momentos de Reflexões", command=exemplo1)

# ==============================================================


janela.mainloop()
		
		
