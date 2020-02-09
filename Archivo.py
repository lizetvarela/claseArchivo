import shutil, os
class Archivo:
    def __init__(self, nombre):
        try:
            self.f = open(nombre, 'r')
            self.nombre = nombre
        except:
            print("No se puede abrir el archivo", nombre)
            exit()
        
    def muestra(self):
        i=1
        for linea in self.f:
            print(  "{:3}{}".format(i,linea), end="")
            i+=1
        self.f.seek(0)
        
        
    def cuentaVocales(self):
        def vocales(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set("AÁáaEÉéeIÍíiOÓóoUÚúu"):
                    contador +=1
            return contador

        contador = 0
        for linea in self.f:
            contador +=vocales(linea)
        self.f.seek(0)
        return contador
    
    def cuentaConsonantes(self):
        def consonantes(s):
            contador = 0
            for i in range(len(s)):
                if s[i].lower() in set("bcdfghjklmnpqrstvwxyz"):
                    contador += 1
            return contador
        
        contador = 0
        for linea in self.f:
            contador +=consonantes(linea)
        self.f.seek(0)
        return contador
    
    def cuentaSignos(self):
        def signos(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set(",;:!¡?¿''.-_"):
                    contador += 1
            return contador
        
        contador = 0
        for linea in self.f:
            contador +=signos(linea)
        self.f.seek(0)
        return contador
    
    def cuentaEspacios(self):
        def espacio(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set(" "):
                    contador += 1
            return contador
        
        contador = 0
        for linea in self.f:
            contador +=espacio(linea)
        self.f.seek(0)
        return contador
    
    def cuentaPalabras(self):
        def palabra(s):
            contador = 0
            for i in range(len(s)):  
                if s[i] in set(" \n"):
                    contador += 1
            return contador
        
        contador = 0
        for linea in self.f:
            contador +=palabra(linea)
        self.f.seek(0)
        return contador + 1

    
    def cuentaLinea(self):
        def lineas(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set("\n"):
                    contador += 1
            return contador
        
        contador = 1
        for linea in self.f:
            contador +=lineas(linea)
        self.f.seek(0)
        return contador 
    
    def cuentaMayusculas(self):
        def mayusculas(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set("AÁBCDEÉFGHIÍJKLMNOÓPQRSTUÚVWXYZ"):
                    contador += 1
            return contador

        contador = 0
        for linea in self.f:
            contador +=mayusculas(linea)
        self.f.seek(0)
        return contador
    
    def cuentaMinusculas(self):
        def minusculas(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set("aeiouáéíóúbcdfghjklmnpqrstvwxyz"):
                    contador += 1
            return contador

        contador = 0
        for linea in self.f:
            contador +=minusculas(linea)
        self.f.seek(0)
        return contador
    
    def copiaArchivo(self, archivocopiado):
        shutil.copy(self.f.name, archivocopiado)
        print("\n9._ Archivo copiado con el nombre de: Archivo copiado")
    
    
    
    def convierteMayusculas(self):
        contador = ""
        for linea in self.f:
            contador +=linea.upper()
        self.f.seek(0)
        return contador
    
    def convierteMinusculas(self):
        contador = ""
        for linea in self.f:
            contador += linea.lower()
        self.f.seek(0)
        return contador
    
    def convierteHexadecimal(self):
        conv = []
        def hexa(s):
            for i in range(len(s)):
                conv.append(hex(ord(s[i])))

        for linea in self.f:
            hexa(linea)
        print(conv)
        self.f.seek(0)

#main 
nomb = input('Nombre del archivo:')
archivo = Archivo(nomb)
archivo.muestra()
print("\n1-. El número de vocales es: ", archivo.cuentaVocales())
print("\n2-. El número de consonantes es: ", archivo.cuentaConsonantes())
print("\n3-. El número de signos de puntuación es: ", archivo.cuentaSignos())
print("\n4-. El número de espacios es: ", archivo.cuentaEspacios())
print("\n5-. El número de palabras es: ", archivo.cuentaPalabras())
print("\n6-. El número de líneas es: ", archivo.cuentaLinea())
print("\n7-. El número de mayúsculas es: ", archivo.cuentaMayusculas())
print("\n8-. El número de minúsculas es: ", archivo.cuentaMinusculas())
archivo.copiaArchivo("Archivo copiado.txt")
print("\n10-. El texto en mayúsculas es : ", archivo.convierteMayusculas())
print("\n11-. El texto en minusculas es: ", archivo.convierteMinusculas())
print("\n12-. El texto en hexadecimal es : ")
archivo.convierteHexadecimal()
