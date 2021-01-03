contador = 1
aprobados = 0
suspendidos = 0


numero_alumnos = int(input('cuando alumnos tienes?:'))

while contador <= numero_alumnos:

    nota = int(input(f'que nota quieres ponerle al \"alumno{contador}\" ?:')

    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1

    contador += 1

print(f'alumnos aprobados': {aprobados})
print(f'alumnos suspendidos': {suspendidos})
