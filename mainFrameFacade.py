from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar, DateEntry
from faceRegister import regNew
from registry import getRegistro
from scanAround import providencia

class Product:

	def __init__(self, window):
		self.wind = window
		self.wind.title('Videocam Security')
		self.wind.geometry('550x350')
		#self.wind.configure(background='steel blue1')

		#Report container
		sb = Scrollbar(window, orient=VERTICAL)
		sb.grid(row=0, column=6, sticky=NS, pady=(40,0))

		self.tree = ttk.Treeview(window, height=6, yscrollcommand=sb.set, selectmode="extended")
		self.tree.heading("#0", text="Info")
		self.tree.grid(row=0, column=5, pady=(40,0))
		self.tree.config(yscrollcommand=sb.set)
		
		sb.config(command=self.tree.yview)

		#Register container
		frameNew = LabelFrame(self.wind, text='Registre nuevo personal')
		frameNew.grid(row=0, column=0, columnspan=4, pady=20, padx=20)

		Label(frameNew, text='CI:').grid(row=1, column=0)
		self.ci = Entry(frameNew)
		self.ci.grid(row=1, column=1, pady=10, padx=10)

		Label(frameNew, text='Nombre Completo:').grid(row=2, column=0)
		self.name = Entry(frameNew)
		self.name.grid(row=2, column=1, pady=10, padx=10)

		Label(frameNew, text='Fecha de Nacimiento:').grid(row=3, column=0)
		self.bday = DateEntry(frameNew)
		self.bday.grid(row=3, column=1, pady=10, padx=10)
			# button register
		def triggerNew():
			if len(self.name.get()) == 0 or self.ci.get() == 0:
				self.tree.insert(index='end', parent='', text='Debes rellenar todos los datos')
			else:
				regNew(self.ci.get(), self.name.get(), self.bday.get(), self.tree)
		
		ttk.Button(frameNew, text='Registro Facial', command=triggerNew ).grid(row=4, column=0, columnspan=2, pady=5)
	
		#Work container
		frameWork = LabelFrame(self.wind, text='Empiece a trabajar')
		frameWork.grid(row=5, column=0, columnspan=4)
			# buttons work
		def triggerTraino():
			getRegistro(self.tree)

		ttk.Button(frameWork, text='Procesar registro', command=triggerTraino ).grid(row=3, column=0, columnspan=2, padx=80, pady=10)

		def triggerWork():
			self.tree.insert(index='end', parent='', text='VIGILANDO...')
			providencia()

		ttk.Button(frameWork, text='Trabajar!', command=triggerWork ).grid(row=4, column=0, columnspan=2, pady=(0,10))


if __name__ == '__main__':
	window = Tk()
	application = Product(window)
	window.mainloop()