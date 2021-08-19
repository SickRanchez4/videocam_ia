import os
import cv2
import tkinter
from tkinter.messagebox import*
import imutils
import numpy as np

def getRegistro(treev):
	dataPath = os.path.join(os.getcwd(),'datos') #Cambia a la ruta donde hayas almacenado Data
	peopleList = os.listdir(dataPath)
	print('Lista de personas: ', peopleList)
	labels = []
	facesData = []
	label = 0
	for nameDir in peopleList:
		personPath = dataPath + '/' + nameDir
		print('Leyendo las imágenes')
		treev.insert(index='end', parent='', text='Leyendo las imágenes')
		for fileName in os.listdir(personPath):
			print('Rostros: ', nameDir + '/' + fileName)
			labels.append(label)
			facesData.append(cv2.imread(personPath+'/'+fileName,0))
			image = cv2.imread(personPath+'/'+fileName,0)
			cv2.imshow('image',image)
			#cv2.waitKey(10)
		label = label + 1
	#Métodos para entrenar el reconocedor
	#face_recognizer = cv2.face.EigenFaceRecognizer_create()
	#face_recognizer = cv2.face.FisherFaceRecognizer_create()
	face_recognizer = cv2.face.LBPHFaceRecognizer_create()

	# Entrenando el reconocedor de rostros
	print("Entrenando...")
	treev.insert(index='end', parent='', text='Entrenando...')
	face_recognizer.train(facesData, np.array(labels))

	# Almacenando el modelo obtenido
	#face_recognizer.write('modeloEigenFace.xml')
	#face_recognizer.write('modeloFisherFace.xml')
	face_recognizer.write('modeloLBPHFace.xml')
	print("Modelo almacenado...")
	treev.insert(index='end', parent='', text='Modelo almacenado con éxito')
	cv2.destroyAllWindows()
	tkinter.messagebox.showinfo('PROVIDENCIA','Registro Finalizado con exito')
