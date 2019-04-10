from tkinter import*
import re
def validarexp(Expresion):
	global mensaje
	patron = re.compile(r'[0-9]{4}') 
	if patron.search(Expresion):
	    mensaje.config(text=" es valida")
	    print("Entrooooo en el if")
	   
	else:
		mensaje.config(text="No es valida")
		print("no entro en el if")

Ventana=Tk()
Ventana.geometry("300x300+100+100")
Ventana.title("Expresiones Regulares")

lblExpresion=Label(text="   Ingrese la expresión a validar:",fg="red", font=("Agency FB", 14))
lblExpresion.grid(row=0, column=1,sticky=W)
Expresion=StringVar()
txtExpresion=Entry(Ventana, text="Expresion",width=30)
txtExpresion.grid(row=1, column=1)
btnEnviar=Button(Ventana, text="Enviar",font=("Agency FB", 14),command=lambda:validarexp(Expresion.get()))
btnEnviar.grid(row=2, column=1)


mensaje = Label(Ventana, text="             ")
mensaje.grid(row=4,column=1)


Ventana.mainloop()

	
#correo	patron = re.compile(r"w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}")    
#fecha fecha = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$')
#Url url = re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")