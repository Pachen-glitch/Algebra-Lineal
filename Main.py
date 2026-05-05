#=================================================
#       UNIVERSIDAD DEL VALLE DE GUATEMALA
#=================================================
#   Curso: Algebra Lineal 1
#   Catedrático: Rodrigo Leonardo
#   Integrantes: Daniel Leal    - 25682
#                Jorge Martínez - 25556
#                Matías Zamora  - 25760
#
#   Descripción: Programa que implementa el 
#       algoritmo de reducción de matrices
#       Gauss-Jordan.
#=================================================

import GaussJordan as gg
from tkinter import Tk, Label, Entry, Button,Frame,messagebox, Text

subs = "₀₁₂₃₄₅₆₇₈₉"

def subindice(num):
    return ''.join(subs[int(d)] for d in str(num))

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gauss-Jordan")
        self.geometry("870x600")
        
        info = Button(self, bitmap="info", font=("Times", 12,"bold"),fg="white",bg="blue",width=24, height=24, command=self.mostrar_info)
        info.place(x=10, y=10)
        
        titulo = Label(self, text="Gauss-Jordan")
        titulo.config(font=("Times", 24),)
        titulo.pack(pady=10)
        
        
        frame1 = Frame(self)
        frame1.pack(pady=0)
        
        label = Label(frame1, text="Cantidad de ecuaciones: ")
        label.config(font=("Times", 12))
        label.grid(column=0,row=0, padx=5, pady=5)
        
        self.c_ecuaciones = Entry(frame1, width=10,justify='center',font=("Times", 12))
        self.c_ecuaciones.grid(column=1,row=0, padx=5, pady=5)
        
        label = Label(frame1, text="Cantidad de variables: ")
        label.config(font=("Times", 12))
        label.grid(column=0,row=1, padx=5, pady=5)
        
        self.c_variables = Entry(frame1, width=10,justify='center',font=("Times", 12))
        self.c_variables.grid(column=1,row=1, padx=5, pady=5)
        
        self.button = Button(frame1, text="Ingresar",font=("Times", 12,"bold"),bg="red", command=self.ingresar)
        self.button.grid(column=2,row=0,rowspan=2, padx=15, pady=5)
        
        self.frame = Frame(self)
        self.frame.pack(pady=10)
        
        self.result_label = Label(self, text="", font=("Times", 12))
        self.result_label.pack(pady=10)
        
        self.text_resultado = Text(self, height=10, width=30, font=("Times", 14))
        self.text_resultado.config(state="disabled")
        
    def ingresar(self):
        # limpiar frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        try:
            m = int(self.c_ecuaciones.get())
            n = int(self.c_variables.get())
            
            if(m <= 0 or n <= 0):
                messagebox.showerror("Error", "La cantidad de ecuaciones y variables debe ser mayor a cero.")
                return
            if(m>10 or n>10):
                messagebox.showerror("Error", "La cantidad de ecuaciones o variables no puede ser mayor a 10.")
                return
        except:
            messagebox.showerror("Error", "Entrada inválida.")
            return
        
        self.entrys = []
        
        for i in range(m):
            fila = []
            col = 0
            
            for j in range(n):
                # Entry coeficiente
                e = Entry(self.frame, width=5,justify='center')
                e.grid(row=i, column=col, padx=2, pady=5)
                fila.append(e)
                col += 1
                
                # Varieble 
                label = Label(self.frame, text=f"x{subindice(j+1)}")
                label.config(font=("Arial", 15))
                label.grid(row=i, column=col)
                col += 1
                
                if j < n-1:
                    plus = Label(self.frame, text="+")
                    plus.config(font=("Arial", 15))
                    plus.grid(row=i, column=col)
                    col += 1
            
            # Signo =
            igual = Label(self.frame, text="=")
            igual.config(font=("Arial", 15))
            igual.grid(row=i, column=col, padx=5)
            col += 1
            
            # Entry termino independiente
            e = Entry(self.frame, width=5,justify='center')
            e.grid(row=i, column=col, padx=2)
            fila.append(e)
            
            self.entrys.append(fila)
        
        # BOTON CALCULAR Y TEXTBOX DE RESULTADO
        boton2 = Button(self, text="Calcular" ,font=("Times", 15,"bold"),bg="red", command=self.calcular)
        boton2.pack(pady=10)
        self.text_resultado.pack(pady=10)
        
    
    def calcular(self):
        try:
            m = []
            for fila in self.entrys:
                fila_valores = [float(e.get()) for e in fila]
                m.append(fila_valores)
            
            gauss = gg.GaussJordan()
            gauss.nuevo(m)
            result_code = gauss.resolver()
            
            if result_code == 1:
                resultado = gauss.x[:, -1]
                respuesta = "Solución:\n" + "\n".join(
                    f"x{subindice(i+1)} = {round(resultado[i], 4)}"
                    for i in range(len(resultado))
                )
            elif result_code == 2:
                respuesta = "Infinitas soluciones"
            else:
                respuesta = "No hay solución"
        
        except Exception as e:
            respuesta = f"Error: {str(e)}"
        
        self.mostrar_resultado(respuesta)
            
    def mostrar_resultado(self, texto):
        self.text_resultado.config(state="normal")
        self.text_resultado.delete("1.0", "end")
        self.text_resultado.insert("end", texto)
        self.text_resultado.config(state="disabled")
            
    def mostrar_info(self):
        info_text = "Primero debes ingresar la cantidad de ecuaciones y variables del sistema. Luego, ingresa los coeficientes de cada variable y el término independiente para cada ecuación. Finalmente, haz clic en el boton \"Calcular\" para obtener la solución del sistema."
        messagebox.showinfo("INFO", info_text)

App().mainloop()