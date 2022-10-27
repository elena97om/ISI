import urllib.request
from bs4 import BeautifulSoup

# Paso 1: Importar la biblioteca de Python
url='https://www.farmaciaonlineblesa.es/'
ourUrl=urllib.request.urlopen(url)

# Paso 2: Extraer el HTML de la página web
soup = BeautifulSoup(ourUrl,'html.parser')

# Paso 3: Obtener las urls de los productos en html
productos = soup.find_all('a', class_='product-name')

urls = []

# Paso 4: Obtener la url de cada producto y la añadir a una lista
for prod in productos:
    url = prod.get('href')
    urls.append(url)

# (OPCIONAL) Paso 5: Exportar la lista de urls a un txt
f = open('urls_productos.txt', 'w')
f.write(str(urls))
f.close()

# Paso 6: Guardar las urls de dos productos (los dos primeros)
prod1 = urls[0]
prod2 = urls[1]

url1=urllib.request.urlopen(prod1)
url2=urllib.request.urlopen(prod2)

# Paso 7: Extraer el HTML de los dos productos
html1 = BeautifulSoup(url1,'html.parser')
html2 = BeautifulSoup(url2,'html.parser')

# (OPCIONAL) Paso 8: Exportar los htmls de los dos productos a txt distintos 
f = open('prod1.txt', 'w')
f.write(str(html1))
f.close()
f = open('prod2.txt', 'w')
f.write(str(html2))
f.close()

# Atributos a buscar:
# nombre_prod, nombre_lab, descripción, precio, ean, campo, resumen

# Paso 9: Obtener los principales datos del primer producto
# Gema Herrerias Kiré Emulsión Limpiadora Japonesa 100ml, nombre_lab, Descripción corta, 
# 35,90 €, ean, HIDRATACIÓN Y LIMPIADORES, Más, 
# https://www.farmaciaonlineblesa.es/hidratacion-limpiadores/60979-gema-herrerias-kire-emulsion-limpiadora-japonesa-100ml.html
nombre_prod1 = html1.title.get_text()
descripcion1 = html1.find('div', id = "short_description_content").get_text()
precio1 = html1.find('span', id = "our_price_display").get_text()
campo1 = html1.find('div', id = "tsp_titlepage").get_text()
resumen1 = html1.find('section', id = "tsp_tab_info").get_text()

print("Nombre del producto: " + nombre_prod1)
print("Descripción del producto: " + descripcion1)
print("Precio del producto: " + precio1)
print("Campo del producto: " + campo1)
print("Resumen del producto: " + resumen1)


# Paso 10: Obtener los principales datos del segundo producto
# Gema Herrerias Función Barrera Cremagel 50ml, nombre_lab, Descripción corta,
# 39,90 €, ean, ANTI-IMPERFECCIONES, Más,
# https://www.farmaciaonlineblesa.es/anti-imperfecciones/61321-gema-herrerias-funcion-barrera-cremagel-50ml.html
nombre_prod2 = html2.title.get_text()
descripcion2 = html2.find('div', id = "short_description_content").get_text()
precio2 = html2.find('span', id = "our_price_display").get_text()
campo2 = html2.find('div', id = "tsp_titlepage").get_text()
resumen2 = html2.find('section', id = "tsp_tab_info").get_text()

print("Nombre del producto: " + nombre_prod2)
print("Descripción del producto: " + descripcion2)
print("Precio del producto: " + precio2)
print("Campo del producto: " + campo2)
print("Resumen del producto: " + resumen2)

"""# Paso 11: Exportar la salida del programa a un txt
f = open('salida.txt', 'w')
f.write("PRIMER PRODUCTO: \n")
f.write("Nombre: " + str(nombre_prod1)"\n")
f.write("Descripción: " + str(descripcion1)"\n")
f.write("Precio: " + str(precio1)"\n")
f.write("Campo: " + str(campo1)"\n")
f.write("Resumen: " + str(resumen1)"\n")
f.close()"""