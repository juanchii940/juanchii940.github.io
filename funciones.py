from bs4 import BeautifulSoup

PRODUCTO = 0
PRECIO = 2

def leer_linea(archivo):
    linea = archivo.readline()
    if linea:
        linea = linea.strip()
    else:
        linea = ""
    return linea


def comparar_archivos(archivo_productos_precios, archivo_productos, salida):
    producto_actual = leer_linea(archivo_productos)
    while producto_actual:
        producto_actual = producto_actual.upper()
        linea_producto_precios = leer_linea(archivo_productos_precios)
        encontrado = False
        archivo_productos_precios.seek(0)
        while linea_producto_precios and not encontrado:
            producto = linea_producto_precios.rstrip().split(",")[PRODUCTO]
            if producto_actual.strip() == producto.strip():
                salida.write(linea_producto_precios + '\n')
                encontrado = True
            linea_producto_precios = leer_linea(archivo_productos_precios)
        if not encontrado:
            salida.write(f"{producto_actual},no hay dato,0\n")
        producto_actual = leer_linea(archivo_productos)


def obtener_lista_productos(archivo_html):
    nombres_productos = []
    linea_archivo_html = archivo_html.readline()
    while linea_archivo_html:
        soup = BeautifulSoup(linea_archivo_html, 'html.parser')
        imagenes = soup.find_all('img')
        for img in imagenes:
            nombre_producto = img['alt']
            nombres_productos.append(nombre_producto)
        linea_archivo_html = archivo_html.readline()
    return nombres_productos

def crear_csv_productos(lista,salida):
    for producto in lista:
        salida.write(producto + "\n")


def procesar_csv(archivo):
    productos_precios_dicc = {}
    linea_datos = leer_linea(archivo)
    while(linea_datos):
        lista_datos = linea_datos.split(',')
        productos_precios_dicc[lista_datos[PRODUCTO]] = lista_datos[PRECIO]
        linea_datos = leer_linea(archivo)
    return productos_precios_dicc

def reemplazar_contenido_html(html, diccionario_precios):
    #crear objeto 
    soup = BeautifulSoup(html, 'html.parser')
    #iterar sobre los div de la clase producto
    for producto_div in soup.find_all('div', class_='producto'):
        #defino la variable (alt) De la etiqueta img y que toma  el atributo alt
        alt = producto_div.find('img')['alt']
        if alt in diccionario_precios:
            precio = diccionario_precios[alt]
            #itero sobre todas las etiquetas p, y dentro de la misma busco la palabra precio para reeemplazar.
            for p_tag in producto_div.find_all('p'):
                if 'Precio' in p_tag.text:
                    p_tag.string = f'Precio: ${precio}'
    return str(soup)

def escribir_html(archivo,contenido):
    archivo.write(contenido)