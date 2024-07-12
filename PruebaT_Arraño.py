import os
import csv
import random
import math
opcion = " "

#asignacion de trabajadores
trabajadores = [
            'Juan Pérez',
            'María García',
            'Carlos López',
            'Ana Martínez',
            'Pedro Rodríguez',
            'Laura Hernández',
            'Miguel Sánchez',
            'Isabel Gómez',
            'Francisco Díaz',
            'Elena Fernández'
    ]

#designar sueldos
sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
def Crear_Archivo():
    with open('ReporteSueldoPrueba.csv', 'w', newline='') as doc:
        writer = csv.writer(doc)
        writer.writerow(['trabajador', 'sueldo', 'Estadisticas'])
        print('')
        print("===> Archivo de reporte creado")
        print('')
    
#asisgnar sueldos entre 300.000 y 2.500.000
def Asignar_Sueldos():
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print('')
    print("Sueldos asignadas:", sueldos)
    print('')
    
#asignar clasificacion de sueldos
def Clasificar_Sueldos():
    print('------  CLASIFICACION DE SUELDOS  ------')
    print('')
    clasificacion_sueldos = {
        'menores a $800.000': [],
        'entre $800.000 a $2.500.000': [],
        'mayor a 2.500.000': [],
    }
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            clasificacion = "Inferior a $800.000"
        elif sueldo >= 800000 and sueldo < 2500000:
            clasificacion = "Entre $800.000 y $2.500.000"
        else:
            clasificacion = "Superior a $2.500.000"
        clasificacion_sueldos [trabajador] = (clasificacion)
        print(f'trabajador:, {trabajador}\t sueldo:, {sueldo}\t Clasificacion:, {clasificacion}')

# mostrar sueldos por categoria
def Ver_Estadisticas():
    print('----- Estadisticas -----')
    print('')
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajo = min(sueldos)
    promedio_sueldo = sum(sueldos) /len(sueldos)
    media_geometrica = math.exp(sum(math.log(s) for s in sueldos) /len(sueldos))

    print(f"Sueldo más alto: ${sueldo_mas_alto}")
    print('')
    print(f"Sueldo más bajo: ${sueldo_mas_bajo}")
    print('')
    print(f"Promedio de sueldos: ${promedio_sueldo:.2f}")
    print('')
    print(f"Media geométrica de sueldos: ${media_geometrica:.2f}")
    print('')

# descuento de salud, afp y sueldo liquido   
def Reporte_Sueldos():
    print('------  REPORTE DE SUELDOS  ------')
    with open('ReporteSueldoPrueba.csv', 'w', newline='') as doc:
            writer = csv.writer(doc)
            writer.writerows(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento afp', 'Sueldo liquido'])
            
            for i in range(len(trabajadores)):
                descuento_salud = sueldos[i] * 0.07
                descuento_afp = sueldos[i] * 0.12
                SueldoLiquido = sueldos[i] - descuento_salud - descuento_afp
       
                print(f'{trabajadores[i]}: Sueldo base ${sueldos[i]}\t Descuento de salud ${descuento_salud:.2f}\t Descuento de Afp ${descuento_afp:.2f}\t SueldoLiquido ${SueldoLiquido:.2f}')
                writer.writerows(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento afp', 'Sueldo liquido'])
            print('')
            print('Reporte de sueldos generado en "ReporteSueldoPrueba.csv"')
            print('')
        
while opcion !=5:
    os.system("cls")
    print('------------------------------------')
    print('----------- GRUPO ARRAÑO -----------')
    print('-------- REPORTE DE SUELDOS --------')
    print('------------------------------------')
    print('')
    print('---------- MENÚ OPCIONES -----------')
    print('1.- Crear archivo')
    print('2.- Asignar sueldos')
    print('3.- Clasificar sueldos')
    print('4.- Ver estadisticas')
    print('5.- Reporte de sueldos')
    print('6.- Salir del prorgama')
    print('------------------------------------')
    print('')
    opcion = input("Ingrese opción: ")

    if opcion not in ['1','2','3','4','5','6']:
            print("Opción no válida")
            
    if opcion == "6":
        print('------------------------------------')
        print('Finalizando programa... Desarrollado por Fernanda Arraño 16.577.046-3')
        print('------------------------------------')
        print('')
        break 
    
    elif opcion == '1':
        Crear_Archivo()
        
    elif opcion == '2':
        Asignar_Sueldos()
        
    elif opcion == '3':
        Clasificar_Sueldos()
           
    elif opcion == '4':
        Ver_Estadisticas()
    
    elif opcion == '5':
        Reporte_Sueldos()
        
    input('Presione enter para continuar...')