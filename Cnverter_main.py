import tkinter as tk
from tkinter import IntVar, messagebox as msg

class FrameSwitcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Frame switcher")
        self.geometry("300x220")
        self.config(padx=10, pady=20)

        #crear dos frmaes
        self.frame_uno = FrameUno(self)
        self.frame_dos = FrameDos(self)

        btn_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        btn_cerrar.pack(side="bottom", pady=10)

        #menu
        menu = tk.Menu(self, name="main")
        self.config(menu=menu)
        filemenu = tk.Menu(menu, tearoff=0)
        helpmenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Archivo", menu=filemenu)
        menu.add_cascade(label="Ayuda", menu=helpmenu)

        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.destroy)

        helpmenu.add_command(label="Acerca de...", command=self.show_message)
        self.radioVal = IntVar()
        radio_input_rp = tk.Radiobutton(self, text="Pixels a rem", value=0, variable=self.radioVal, command=self.pick_frmae)
        radio_input_rp.pack()
        radio_input_pr = tk.Radiobutton(self, text="Rem a pixels", value=1, variable=self.radioVal, command=self.pick_frmae)
        radio_input_pr.pack()
        #mostrar uno primero
        self.show_frame_uno()

    def pick_frmae(self):
        print(self.radioVal.get())
        if self.radioVal.get() == 0:
            self.show_frame_uno()
        elif self.radioVal.get() == 1:
            self.show_frame_dos()

    def show_frame_uno(self):
        self.frame_dos.pack_forget() 
        self.frame_uno.pack()   

    def show_frame_dos(self):
        self.frame_uno.pack_forget()
        self.frame_dos.pack()

    @staticmethod
    def show_message():
        msg.showinfo("Información", "Este es un mensage de prueba")

class Actualizar_label:
    def __init__(self):
        pass
    def convertir(self,unit, val):
        try:
            if unit == 'px'.lower():
                result = val * 0.063
                return result , 'rem'
            elif unit == 'rem'.lower():
                result = val * 16
                return int(result)
            else:
                msg.showerror('Error', "Escriba como se debe malditazea")
        except ValueError:
            msg.showerror("Error", ValueError)


    def pixel_rem(self,label,value):
        label.configure(text=self.convertir("px",value))

    def rem_pixel(self,label,value):  
        label.configure(text=self.convertir("rem",value))
    

class FrameUno(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        entry_value = IntVar()
        input_value = tk.Entry(self, textvariable=entry_value)
        input_value.pack(pady=5, side="left")  
        label_result = tk.Label(self)
        act = Actualizar_label()
        convertButton = tk.Button(self,text="Convertir", command=lambda: act.pixel_rem(label_result, entry_value.get()))
        convertButton.pack(pady=5)
        #resultado
        label_result.pack()
        

class FrameDos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        entry_value = IntVar()
        input_value = tk.Entry(self, textvariable=entry_value)
        input_value.pack(pady=5, side="left")  
        act = Actualizar_label()
        convertButton = tk.Button(self,text="Convertir", command=lambda: act.rem_pixel(label_result, entry_value.get()))
        convertButton.pack(pady=5)
        #resultado
        label_result = tk.Label(self)
        label_result.pack()

if __name__ == '__main__':
    app = FrameSwitcher()
    app.mainloop()