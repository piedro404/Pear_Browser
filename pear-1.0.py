#Imports || Biblioteca usada foi PyQt5 || cmd:(pip install PyQt5)
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolButton, QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QLine, QUrl, QSize, qInf
from PyQt5.QtGui import QIcon, QPixmap, qPixelFormatAlpha

#Urls
home_url = "https://www.google.com"
creator_url= "https://www.instagram.com/piedro_404/"
github_url = "https://github.com"
discord_url = "https://discord.com/app"
whatsapp_url = "https://whatsapp.com/app"
twitch_url = "https://www.twitch.tv"
youtube_url = "https://www.youtube.com"
twitter_url = "https://twitter.com/home"
inst_url = "https://www.instagram.com"


application = QApplication([])

#Redimencionando a Janela Princial
mainWindow = QMainWindow()
mainWindow.setGeometry(0, 0, 1600, 900)
mainWindow.setMinimumHeight(900)
mainWindow.setMaximumHeight(900)
mainWindow.setMinimumWidth(1600)
mainWindow.setMaximumWidth(1600)

#Custimização da Janela
mainWindow.setWindowTitle("Pear")
mainWindow.setStyleSheet("background-color: rgb(0,255,127);")
mainWindow_icon = QIcon()
mainWindow_icon.addPixmap(QPixmap("./Icones/pear.png"))
mainWindow.setWindowIcon(mainWindow_icon)

#Barra Superior
web = QWebEngineView(mainWindow)
web.setStyleSheet("background-color: rgb(255, 255, 255);")
web.setGeometry(0, 30, 1600, 1000)
web.load(QUrl(home_url))

#Botão de Home
home_button = QToolButton(mainWindow)
home_button.setGeometry(12, 5, 20, 20)
home_button_icon = QIcon()
home_button_icon.addPixmap(QPixmap("./Icones/home.png"))
home_button.setIcon(home_button_icon)
home_button.setStyleSheet("background-color: transparent;")

#Botão de Home
reload_button = QToolButton(mainWindow)
reload_button.setGeometry(145, 5, 20, 20)
reload_button_icon = QIcon()
reload_button_icon.addPixmap(QPixmap("./Icones/reload.png"))
reload_button.setIcon(reload_button_icon)
reload_button.setStyleSheet("background-color: transparent;")

#Botão de Voltar
back_button = QToolButton(mainWindow)
back_button.setGeometry(65, 5, 20, 20)
back_button_icon = QIcon()
back_button_icon.addPixmap(QPixmap("./Icones/back.png"))
back_button.setIcon(back_button_icon)
back_button.setStyleSheet("background-color: transparent;")

#Botão de Avançar
forward_button = QToolButton(mainWindow)
forward_button.setGeometry(100, 5, 20, 20)
forward_button_icon = QIcon()
forward_button_icon.addPixmap(QPixmap("./Icones/forward.png"))
forward_button.setIcon(forward_button_icon)
forward_button.setStyleSheet("background-color: transparent;")

#Botão de Barra de Pesquisa
go_line = QLineEdit(mainWindow)
go_line.setGeometry(180, 2, 950, 25)
go_line.setStyleSheet("background-color: rgb(255,255,255);")

#Botão de Pesquisa
go_button = QToolButton(mainWindow)
go_button.setGeometry(1140, 5, 20, 20)
go_button_icon = QIcon()
go_button_icon.addPixmap(QPixmap("./Icones/go.png"))
go_button.setIcon(go_button_icon)
go_button.setStyleSheet("background-color: transparent;")

#Botão Icon do Criador
creator_button = QToolButton(mainWindow)
creator_button.setGeometry(1235, 0, 30, 30)
creator_button_icon = QIcon()
creator_button_icon.addPixmap(QPixmap("./Icones/piedro.png"))
creator_button.setIcon(creator_button_icon)
creator_button.setStyleSheet("background-color: transparent;")
creator_button.setIconSize(QSize(25, 25))

#Botão Icon do Github
github_button = QToolButton(mainWindow)
github_button.setGeometry(1280, 0, 30, 30)
github_button_icon = QIcon()
github_button_icon.addPixmap(QPixmap("./Icones/github.png"))
github_button.setIcon(github_button_icon)
github_button.setStyleSheet("background-color: transparent;")
github_button.setIconSize(QSize(25, 25))

#Botão Icon do Discord
discord_button = QToolButton(mainWindow)
discord_button.setGeometry(1325, 0, 30, 30)
discord_button_icon = QIcon()
discord_button_icon.addPixmap(QPixmap("./Icones/discord.png"))
discord_button.setIcon(discord_button_icon)
discord_button.setStyleSheet("background-color: transparent;")
discord_button.setIconSize(QSize(25, 25))

#Botão Icon do Whatsapp
whatsapp_button = QToolButton(mainWindow)
whatsapp_button.setGeometry(1370, 0, 30, 30)
whatsapp_button_icon = QIcon()
whatsapp_button_icon.addPixmap(QPixmap("./Icones/whatsapp.png"))
whatsapp_button.setIcon(whatsapp_button_icon)
whatsapp_button.setStyleSheet("background-color: transparent;")
whatsapp_button.setIconSize(QSize(25, 25))

#Botão Icon do Twitch
twitch_button = QToolButton(mainWindow)
twitch_button.setGeometry(1415, 0, 30, 30)
twitch_button_icon = QIcon()
twitch_button_icon.addPixmap(QPixmap("./Icones/twitch.png"))
twitch_button.setIcon(twitch_button_icon)
twitch_button.setStyleSheet("background-color: transparent;")
twitch_button.setIconSize(QSize(25, 25))

#Botão Icon do Youtube
youtube_button = QToolButton(mainWindow)
youtube_button.setGeometry(1460, 0, 30, 30)
youtube_button_icon = QIcon()
youtube_button_icon.addPixmap(QPixmap("./Icones/youtube.png"))
youtube_button.setIcon(youtube_button_icon)
youtube_button.setStyleSheet("background-color: transparent;")
youtube_button.setIconSize(QSize(25, 25))

#Botão Icon do Twitter
twitter_button = QToolButton(mainWindow)
twitter_button.setGeometry(1505, 0, 30, 30)
twitter_button_icon = QIcon()
twitter_button_icon.addPixmap(QPixmap("./Icones/twitter.png"))
twitter_button.setIcon(twitter_button_icon)
twitter_button.setStyleSheet("background-color: transparent;")
twitter_button.setIconSize(QSize(25, 25))

#Botão Icon do Instagram
inst_button = QToolButton(mainWindow)
inst_button.setGeometry(1550, 0, 30, 30)
inst_button_icon = QIcon()
inst_button_icon.addPixmap(QPixmap("./Icones/instagram.png"))
inst_button.setIcon(inst_button_icon)
inst_button.setStyleSheet("background-color: transparent;")
inst_button.setIconSize(QSize(25, 25))

#Funções
def home(mainWindow):
    web.load(QUrl(home_url))

def reload(mainWindow):
    web.reload()

def back(mainWindow):
    web.back()

def forward(mainWindow):
    web.forward()

def go(mainWindow):
    go_url = go_line.text()
    request1 = "https://"
    request2 = "www."
    request3 = ".com"
    request4 = "https://.com"
    request5 = "php"
    request6 = "https://php.com"
    go_len = len(go_url)

    if(request1 in go_url and go_url[0:8] == request1 and request2 in go_url and request3 in go_url):
        web.load(QUrl(go_url))
        #print(request1 in go_url and go_url[0:8] == request1 and request2 in go_url and request3 in go_url)

    elif(request2 in go_url and go_url[0:4] == request2 and request3 in go_url):
        go_url = request1+go_url
        web.load(QUrl(go_url))
        #print(request2 in go_url and go_url[0:4] == request2 and request3 in go_url)
    
    elif(request1 in go_url and go_url[go_len-4:go_len] == request3 and go_url[0:8] == request1 and go_url is not request4):
        web.load(QUrl(go_url))
        #print(request1 in go_url and go_url[go_len-4:go_len] == request3 and go_url[0:8] == request1 and request4 is not go_url)

    elif(request1 in go_url and go_url[0:8] == request1 and request5 in go_url and request3 in go_url and go_url != request6):
        web.load(QUrl(go_url))
        #print(request1 in go_url and go_url[0:8] == request1 and request5 in go_url and request3 in go_url and go_url != request6)

    else:
        #https://www.google.com/search?client=pear-gx&q=oi+,+tudo+bem+?&sourceid=pear&ie=UTF-8&oe=UTF-8
        len_go = len(go_url)
        #print(go_url)
        go_url = go_url.replace(" ", "+")
        #print(go_url)
        go_google_url= f"https://www.google.com/search?client=opera-gx&q={go_url}&sourceid=opera&ie=UTF-8&oe=UTF-8"
        #print(go_google_url)
        web.load(QUrl(go_google_url))

def creator(mainWindow):
    web.load(QUrl(creator_url))

def github(mainWindow):
    web.load(QUrl(github_url))

def discord(mainWindow):
    web.load(QUrl(discord_url))

def whatsapp(mainWindow):
    web.load(QUrl(whatsapp_url))

def twitch(mainWindow):
    web.load(QUrl(twitch_url))

def youtube(mainWindow):
    web.load(QUrl(youtube_url))

def twitter(mainWindow):
    web.load(QUrl(twitter_url))

def instagram(mainWindow):
    web.load(QUrl(inst_url))

def download(item):
    item.accept()
    msg = QMessageBox()
    msg.setWindowTitle("Download")
    msg.setText("Download Iniciado")
    msg_icon = QIcon()
    msg_icon.addPixmap(QPixmap("./Icones/download.png"))
    msg.setWindowIcon(msg_icon)
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()

#Conectado as Funções aos Botãos  
home_button.clicked.connect(home)
reload_button.clicked.connect(reload)
back_button.clicked.connect(back)
forward_button.clicked.connect(forward)
go_button.clicked.connect(go)
creator_button.clicked.connect(creator)
github_button.clicked.connect(github)
discord_button.clicked.connect(discord)
whatsapp_button.clicked.connect(whatsapp)
twitch_button.clicked.connect(twitch)
youtube_button.clicked.connect(youtube)
twitter_button.clicked.connect(twitter)
inst_button.clicked.connect(instagram)
web.page().profile().downloadRequested.connect(download)


#Exibir
mainWindow.show()
application.exec_()

