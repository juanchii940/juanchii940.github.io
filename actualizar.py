from funciones import *
from bs4 import BeautifulSoup

archivo_productos_precios = open("productos_precios.csv", 'r', encoding="utf-8")
archivo_productos = open("productos.csv", 'w', encoding="utf-8")
archivo_salida = open('datos.csv', 'w', newline='', encoding='utf-8')
archivo_html = open("pagina.html" , "r" ,encoding= "utf-8" )


lista_productos = obtener_lista_productos(archivo_html)
crear_csv_productos(lista_productos,archivo_productos)
archivo_productos.close()
archivo_html.close()
archivo_productos = open("productos.csv" ,"r",encoding = "utf-8")
comparar_archivos(archivo_productos_precios,archivo_productos,archivo_salida)
archivo_salida.close()
archivo_productos.close()
archivo_productos_precios.close()


archivo_html = open("pagina.html" , "r" ,encoding= "utf-8" )
archivo_datos = open("datos.csv","r" , encoding= "utf-8")
diccionario_datos = procesar_csv(archivo_datos)
html_actualizado = reemplazar_contenido_html(archivo_html,diccionario_datos)
archivo_datos.close()
archivo_html.close()

archivo_html = open("pagina.html","w", encoding="utf-8")
escribir_html(archivo_html,html_actualizado)