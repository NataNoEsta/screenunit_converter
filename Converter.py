from cgitb import text
import tkinter as tk
from tkinter.messagebox import showerror

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Conversor de temperaturas')
        self.geometry("300x120")
        self.resizable(0,0)
        

class TempConverter:
    @staticmethod
    def farenheit_to_celcius(f, format=True):
        result = (f - 32) * 5/9
        if format:
            return f'{f} Farenheit = {result:.2f} Celcius'
        return result
    @staticmethod
    def celcius_to_farenheit(c, format=True):
        result = c * 9/5 + 32
        if format:
            return f'{c} Celcius = {result:.2f} Farenheit'
        return result
    
class ConverterFrame(tk.Frame):
    def __init__(self, container, unit_from, converter):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter

        #opciones para grid
        options = {'padx': 5, 'pady':5}

        #label
        self.temp_label = tk.Label(self, text=self.unit_from)
        self.temp_label.grid(column=0, row=0, sticky="w", **options)

        #entry
        self.temp_value = tk.StringVar()
        self.temperature = tk.Entry(self, textvariable=self.temp_value)
        self.temperature.grid(column=1, row=0, sticky="w", **options)
        self.temperature.focus()

        #button
        self.btn_convert = tk.Button(self, text="Convert")
        self.btn_convert.grid(column=2, row=0, sticky="w", **options)
        self.btn_convert.configure(command=self.convertir)

        #result_label
        self.result_label = tk.Label(self)
        self.result_label.grid(row=1, columnspan=3, **options)
        
        # = frame.grid
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nswe")

    def convertir(self, event=None):
        try:
            input_value = float(self.temp_value.get())
            result = self.converter(input_value)
            self.result_label.confiure(text=result)
        except ValueError as error:
            showerror(title="Error", message=error)



if __name__== "__main__":
    app = App()
    app.mainloop()