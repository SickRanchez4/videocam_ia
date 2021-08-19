import os
import tkinter
from tkinter.messagebox import*
import imutils
import cv2
from utils.db_Firestore import fb_post

def regNew(ci, name, bday, treev):
	personName = name
	crear=0
	if not os.path.exists(crear):
		crear = os.makedirs('datos')
	dataPath = os.path.join(os.getcwd(),'datos') 		#Cambia a la ruta donde hayas almacenado Data (para procesar videos)
	personPath = dataPath + '/' + personName
	if not os.path.exists(personPath):
		print('Carpeta creada: ',personPath)
		treev.insert(index='end', parent='', text='Nueva carpeta personal creada')
		os.makedirs(personPath)
	cap = cv2.VideoCapture(0)
	faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
	count = 0
	treev.insert(index='end', parent='', text='Escaneando...')
	while True:
		ret, frame = cap.read()
		if ret == False: break
		frame =  cv2.resize(frame,(400,400),interpolation= cv2.INTER_CUBIC)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		auxFrame = frame.copy()
		faces = faceClassif.detectMultiScale(gray,1.3,5)
		cv2.putText(frame,'Escanenado...-',(10,20), 2, 0.7,(128,0,255),1,cv2.LINE_AA)
		for (x,y,w,h) in faces:
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			rostro = auxFrame[y:y+h,x:x+w]
			rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
			cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count),rostro)
		count = count + 1
		cv2.imshow('Escaneando',frame)
		k =  cv2.waitKey(1)
		if k == (27) or count >= 300:
			if count == 300:
				tkinter.messagebox.showinfo('PROVIDENCIA','Registro Finalizado con exito')
				treev.insert(index='end', parent='', text='Registro Finalizado con éxito')
			break

	datos = {
		'ci':ci,
		'name':name,
		'bday':bday
	}
	fb_post(datos)

	cap.release()
	cv2.destroyAllWindows()

	