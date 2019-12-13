import os
import zipfile
import getpass

def tamaño():
	tamaño=int(input("Escribe el numero de bytes para el tamaño especificado: "))
	return tamaño
def direccionRegistro():
	direccion=input("Escribe la ruta donde desea crear el registro: ")
	return direccion
try:
	opcion=1

    #Presentamos al usuario las distintas opciones que ofrece el optimizador
	while (opcion>=1 and opcion<=5):
		print("Elija el proceso que desea realizar")
		print("1. Mostrar archivos superiores en tamaño a uno especificado")
		print("2. Borrar archivos superiores en tamaño a uno especificado")
		print("3. Comprimir un fichero o carpeta especificada")
		print("4. Borrar los archivos temporales del navegador")
		print("5. Cerrar el programa")
		opcion = int(input("Selecciona una opción (1-5): "))
        
    #PROCESO1
		if (opcion==1):
			direccion=input("Escribe la ruta donde deseas analizar los archivos: ")
			os.chdir(direccion)
			tamañoInicial=tamaño()
			listaArchivos=os.listdir(".")
			direccion2=direccionRegistro()
			os.chdir(direccion2)
			f = open("registro.log", "a")
			f.write("\n")
			contador=0
			for archivo in listaArchivos:
				tamaño=os.stat(archivo).st_size
				if (tamaño)>=(tamañoInicial):
					contador+=1
					print(archivo)
					f.write(archivo + "\n")
			print("Se han encontrado %i archivos de tamaño superior a %i Bytes en el directorio " %(contador,tamañoInicial))
			f.write("Se han encontrado %i archivos de tamaño superior a %i Bytes en el directorio " %(contador,tamañoInicial))
			f.close()
            
            
        #PROCESO2       
		if (opcion==2):
			direccion2=direccionRegistro()
			os.chdir(direccion2)
			f=open("registro.log", "a")
			f.write("\n")
			direccion=input("Escribe la ruta donde deseas analizar los archivos")
			os.chdir(direccion)
			tamañoInicial=tamaño()
			listaArchivos=os.listdir(".")
			contador=0
			f.close()
			
			for archivo in listaArchivos:
				tamaño=os.stat(archivo).st_size
				if (tamaño)>=(tamañoInicial):
					contador=contador+1
					print(archivo)
					
					f.write(archivo + "\n")
					os.remove(archivo)
			
			print("Se han encontrado %i archivos de tamaño superior a %i Bytes en la carpeta actual, los cuales se han borrado" %(contador,tamañoInicial))
			f.write("Se han encontrado %i archivos de tamaño superior a %i Bytes en la carpeta actual, los cuales se han borrado" %(contador,tamañoInicial))
			f.close()
        #PROCESO3
		if (opcion==3):
			direccion2=direccionRegistro()
			direccion=input("Dame una ruta donde se encuentra el archivo (no incluyas al archivo en dicha ruta): ")
			archivo=input("Dame el nombre del archivo: ")
			direccionNueva=input("Escribe la nueva ruta donde deseas ubicar el archivo comprimido: ")
			rutaArchivoComprimido=direccionNueva+"\archivoComprimido.zip"
			archivoComprimido=zipfile.ZipFile(rutaArchivoComprimido,"w")
			archivoComprimido.write(archivo,compress_type=zipfile.ZIP_DEFLATED)
			archivoComprimido.close()
			os.chdir(direccion2)
			f=open("registro.log","a")
			f.write("\n")
			f.write("Se ha comprimido %s, y su nueva ubicación es %s" %(archivo,direccionNueva))
			f.close()
		
        #PROCESO4
		if (opcion==4):
			direccion2=direccionRegistro()
			os.chdir(direccion2)
			f=open("registro.log","a")
			print("Por favor cierre Google Chrome antes de realizar esta tarea")
			usuario = getpass.getuser()
			os.chdir("C:\\Users\\" + usuario + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache")
			archivos = os.listdir()
			borrar = input("¿Está seguro de que quiere borrar la caché(SI/NO): ")
			contador=0
			
			if (borrar=="SI"):
				for elemento in archivos:
					os.remove(elemento)
					f.write(elemento)
					contador+=1
			f.write("Se han eliminado %i archivos temporales" %contador)
			f.close()
        #PROCESO5
		if (opcion==5):
			print("\n")
			print("SE CERRARÁ EL PROGRAMA")
			exit()
		if (opcion>5):
			print("\n")
			print("ERROR-->SELECCIONA DEL 1 AL 5")
			opcion=1
except:
	if (opcion!=5):
		print("\n")
		print("Algo ha fallado, vuelve a intentarlo y revisa bien los datos")
