#coding=utf8

from tkinter import Tk,Label,Frame,Menu,Button,StringVar,SUNKEN,BOTTOM,X,W,DISABLED 
from tkinter import filedialog as fd
from cryptography.fernet import Fernet
from tkinter import  messagebox as MessageBox
import webbrowser as wb
from os.path import os, sys


clave = """x-jQUTe4-RKwe5jegma93Nyxqg9GQjYEo0EN9AI2xCc=stupid
tY90uS7WC8dHmdq7DYf390iwW3IF1Z4jZqCtYGYuwTvrnseZz2YzgdbgKmKwZ
-2FfjRrLn
2bi3l9RyEwVEKhCpx
-2FN6F1Itrm5
2KBzRo71LCVhtoClXaWim9QA7pk6oUxvzm6
-2F7J
7
DtPBbdAj4ENRr
-2gCKhSzUsEIi1AY
-2FkrKTc8HDNQudojhQjmlzxVXH70SrVicTCd7sZ
-2BJjqXSvXlyv
-2FY6G
-2Fmwj7dlnV0DxymKB3b
2qzvtk
-2FM7FDu8c5fj56by6s6pBiVl8
atxW
2S4
8fFd3bwVc
2tVcUoORHpfk7NE
2oyIlfV4eh6F4
295KOYq
2PQ
-2FADvUaQpH8gtgDII1lRonh7susYeU3
-2By96DVKiDm14xuKQ7kKlhvQw0p1YSxAiJMwOE172ng1yOht8
-2Fv
GNjRj4s
GMJdR0w6r2wDbO42sEjKcSJHrHYnO1Fo
-2FYf7RISkYh9CM5uFJev5OEr
-2BtoLFVnhbJ5LC4LYtZUIwlKTfKMT3ANeDQZ8WwCI2gk51Iks7yEkY_PscS7KKuBKSMkC58Kn
-2FpHB
qLVFNf9iB2JE
5hWp9fuHQF6VY8nO8iBu3rJDrOKqDdJwI6SLP3oWEnSTgug
-2BNeIPgyyT2mYUXMF9O9IkvnReBKFUVvvCiABwFrV7p6FGU2eb7h270sZbv
-2Fd4z8ZSwlN2zgDzC
-2Fsbzq
Kjfdn3mNgC8k
lwdnamz1SaDkwFgIzIACW2yUU
-2B3qR
-2BE
-2FhwwB4TJy9k
-2F6bSMk2oeQWyKpuCXVA8WLn7iYDA8FyVs5mgjrxYo
PsjrEhEREi8Smx4pLl0FIN21y0sKm4OGMP4tP
URyxac7DnVffFS
-2FbV3
-2FEO9V402cm"""

direccion_archivo=""

################################################################
def generar_llave():
    try:
        direccion_archivo=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("Key files","*.key"),("Imagen JPG","*.jpg"),("Video Mp4","*.mp4"),("Winrar","*.rar"),("Documento Microsoft Word","*.docx"),("Documento Microsoft Excel","*.xlxs"),("Todos los archivos","*.*")),defaultextension=".key")
        claveFernet = Fernet.generate_key()
        with open(direccion_archivo,"wb") as nueva_clave:
            nueva_clave.write(claveFernet)
            nueva_clave.close()
    except:
        pass

def leer_llave():
    direccion_clave=fd.askopenfilename(initialdir = "/",title = "Seleccione Llave",filetypes = (("Key files","*.key"),("Imagen JPG","*.jpg"),("Video Mp4","*.mp4"),("Winrar","*.rar"),("Documento Microsoft Word","*.docx"),("Documento Microsoft Excel","*.xlxs"),("Todos los archivos","*.*")))
    if direccion_clave:
        global clave
        clave=open(direccion_clave,"rb").read()
        nombre_clave=direccion_clave.split("/")
        nombre_clave=nombre_clave.pop()
        largo_nombre=len(nombre_clave)
        global texto1
        if largo_nombre>0 and largo_nombre<20:        
            texto1.set(f"Llave actual: {nombre_clave}")
        else:
            nombre_clave = nombre_clave[(largo_nombre-20):]
            texto1.set(f"Llave actual:...{nombre_clave}")
    __check()

def seleccionar_archivo():
    global direccion_archivo
    direccion_archivo=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo")
    nombre_archivo=direccion_archivo.split("/")
    nombre_archivo=nombre_archivo.pop()
    largo_nombre=len(nombre_archivo)
    global texto2
    if largo_nombre>0 and largo_nombre<20:        
        texto2.set(f"Archivo actual: {nombre_archivo}")
    elif largo_nombre>20:
        nombre_archivo = nombre_archivo[(largo_nombre-20):]
        texto2.set(f"Archivo actual:...{nombre_archivo}")
    else:
        texto2.set("No has seleccionado ningun archivo")
    __check()
    
def encriptar():
    try:
        confirmacion = MessageBox.askokcancel("Confirmar encriptación","¿Desea encriptar el archivo seleccionado?")
        if confirmacion:  
            f=Fernet(clave) 
            with open(direccion_archivo,"rb") as file:
                archivo_info = file.read()
                file.close()
            informacion_encriptada = f.encrypt(archivo_info)
            with open(direccion_archivo,"wb") as file:
                file.write(informacion_encriptada)
                file.close()
            MessageBox.showinfo("Exito", "Se ha encriptado correctamente el archivo")
    except:
        MessageBox.showerror("Error", "Llave no valida, seleccione una llave correcta")

def desencriptar():
    try:
        confirmacion = MessageBox.askokcancel("Confirmar desencriptación","¿Desea desencriptar el archivo seleccionado?")
        if confirmacion:
            f=Fernet(clave)
            with open(direccion_archivo,"rb") as file:
                informacion_encriptada=file.read()
                file.close()
            decrypted_data=f.decrypt(informacion_encriptada)
            with open(direccion_archivo,"wb") as file:
                file.write(decrypted_data)
                file.close()
            MessageBox.showinfo("Exito", "Se ha desencriptado correctamente el archivo")
    except:
        MessageBox.showerror("Error", "La llave no es la correcta o el archivo ya se encuentra desencriptado")

#Habilita y desabilita botones de encriptar/desencriptar
def __check():
    if clave and direccion_archivo:
        btnEncrypt.config(state="normal")
        btnDesencript.config(state="normal")
    else:
        btnEncrypt.config(state="disabled")     
        btnDesencript.config(state="disabled")

def colabo():
    return wb.open("http://paypal.me/facuquero")
def menAyuda():
    return wb.open("https://drive.google.com/file/d/1GtYqZjGK8PttReI5lVnmU2kkWRNpZfMU/view?usp=sharing")
def menAcerca():
    MessageBox.showinfo("Acerca de...", "Ponele llave v2.0 \nHecho con mucho amor por Facundo Quero \n Contacto:facuquero@gmail.com")
    

#Esta función es para que, al compilar todo con pyinstaller, el icono se adjunte dentro del .exe
def resource_path(relative_path): 
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

icono_path=resource_path("icono.ico")
#---------------------------------Main---------------------------------#
raiz=Tk()
raiz.title("Ponele llave")
raiz.resizable(False, False)
raiz.geometry("380x200")
raiz.config(bg="black")
raiz.iconbitmap(icono_path)
Label(raiz, text="Encriptador de archivos", width=20,bg="black",fg="green").pack(anchor="center")
miFrame=Frame(raiz)
miFrame.config(bd=1, relief="groove",padx=10,bg="black")
miFrame.pack(fill="x")

#---------------------------Menu---------------------#
menubar = Menu(raiz)
raiz.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)
colaborar = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
menubar.add_cascade(label="Colaborar",menu=colaborar)
colaborar.add_command(label="Colaborar con el desarrollador",command=colabo)

filemenu.add_command(label="Salir",command=raiz.quit)

helpmenu.add_command(label="Ayuda",command=menAyuda)
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...",command=menAcerca)

statusbar=Label(raiz,text="Desarrollado por Facundo Quero",bd=1,relief=SUNKEN,anchor=W,bg="black",fg="green")
statusbar.pack(side=BOTTOM,fill=X)



#---------------------------------Columna 0, botones---------------------------------#
btnGenerarClave=Button(miFrame,text="Generar llave",width=20,command=generar_llave,bg="black",fg="green",activebackground="green",activeforeground="black")
btnGenerarClave.grid(row=1,column=0)

btnSelect=Button(miFrame,text="Seleccionar llave",width=20, command=leer_llave,bg="black",fg="green",activebackground="green",activeforeground="black")
btnSelect.grid(row=2,column=0,pady=1)

btnSelectA=Button(miFrame,text="Seleccionar archivo",width=20,command=seleccionar_archivo,bg="black",fg="green",activebackground="green",activeforeground="black")
btnSelectA.grid(row=3,column=0,pady=1)

btnEncrypt=Button(miFrame,text="Encriptar archivo",width=20,command=encriptar,state=DISABLED,bg="black",fg="green",activebackground="green",activeforeground="black")
btnEncrypt.grid(row=4,column=0,pady=1)

btnDesencript=Button(miFrame,text="Desencriptar archivo",width=20,command=desencriptar,state=DISABLED,bg="black",fg="green",activebackground="green",activeforeground="black")
btnDesencript.grid(row=5,column=0,pady=1)

#---------------------------------Columna 2, textos dinamicos---------------------------------#
texto1=StringVar()
texto1.set("No has seleccionado ninguna llave")
t1=Label(miFrame,textvariable=texto1,bg="black",fg="green").grid(row=2,column=1,sticky=W)

texto2=StringVar()
texto2.set("No has seleccionado ningun archivo")
t2=Label(miFrame,textvariable=texto2,bg="black",fg="green").grid(row=3,column=1,sticky=W)


raiz.mainloop()