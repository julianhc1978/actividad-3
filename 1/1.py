import math

calificaciones = []

print("ingrese 5 calificaciones en un rango de 1 a 10")

for i in range(5):
    while len(calificaciones) < 5:
        try:
            nota = float(input("ingrese la nota: "))
            if 1<= nota <=10:
                 calificaciones.append(nota)
            else:
                 print("nota erronea. debe estar en el rango correspondiente")
        except ValueError:
            print("ERROR. ingrese el valor de nuevo")

promedio = (sum(calificaciones))/5

#calcular la media
calificaciones.sort()
suma = sum(calificaciones)
cantidad = len(calificaciones)
media = suma / cantidad

#calcular la desviacion estandar
suma_cuadrados = sum((x - media) ** 2 for x in calificaciones)
varianza = suma_cuadrados / len(calificaciones)
desviacion_estandar = math.sqrt(varianza)
desviacion_estandar = round(desviacion_estandar, 2)

nota_minima = min(calificaciones)
nota_maxima = max(calificaciones)
print(f"tus notas son: {calificaciones}")
if promedio >= 9:
    print(f"El desempeño fue excelente. tu promedio es {promedio}")
    print(f"tu nota minima es {nota_minima} y la nota maxima es {nota_maxima}")
    print(f"la media de las notas es {media} y la desviaciones estandar es {desviacion_estandar}")
elif promedio >= 7:
    print(f"El desempeño es bueno. tu promedio es {promedio}")
    print(f"tu nota minima es {nota_minima} y la nota maxima es {nota_maxima}")
    print(f"la media de las notas es {media} y la desviaciones estandar es {desviacion_estandar}")
elif promedio >= 5:
    print(f"El desempeño fue aprobado. tu promedio es {promedio}")
    print(f"tu nota minima es {nota_minima} y la nota maxima es {nota_maxima}")
    print(f"la media de las notas es {media} y la desviaciones estandar es {desviacion_estandar}")
else:
    print(f"El desempeño fue reprobado. tu promedio es {promedio}")
    print(f"tu nota minima es {nota_minima} y la nota maxima es {nota_maxima}")
    print(f"la media de las notas es {media} y la desviaciones estandar es {desviacion_estandar}")

if desviacion_estandar < 1:
    print("Las calificaciones son consistentes. Se recomienda continuar con el metodo actual en la enseñanza.")
elif 1 <= desviacion_estandar < 2:
    print("Las calificaciones muestran cierta variabilidad. Se recomienda revisar el método de enseñanza para identificar áreas de mejora.")
else:
    print("Las calificaciones son muy variables. Se sugiere implementar nuevas estrategias de enseñanza o proporcionar más apoyo al estudiante.")