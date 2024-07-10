import csv
import random

trabajadores = [
    {
        "Nombre": "Juan Perez",
        "Sueldo": 0,
        "Desct. Salud": 0,
        "Desct. AFP": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre": "Maria Garcia",
        "Sueldo": 0,
        "Desct. Salud": 0,
        "Desct. AFP": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre": "Carlos Lopez",
        "Sueldo": 0,
        "Desct. Salud": 0,
        "Desct. AFP": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre": "Ana Martinez",
        "Sueldo": 0,
        "Desct. Salud": 0,
        "Desct. AFP": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre": "Pedro Rodriguez",
        "Sueldo": 0,
        "Desct. Salud": 0,
        "Desct. AFP": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre": "Laura Hernandez",
        "Sueldo": 0,
        "Desct. Salud": 0,
        "Desct. AFP": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre": "Miguel Sanchez",
        "Sueldo": 0,
        "Desct. Salud": 0,
        "Desct. AFP": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre": "Isabel Gomez",
        "Sueldo": 0,
        "Desct. Salud": 0,
        "Desct. AFP": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre": "Francisco Diaz",
        "Sueldo": 0,
        "Desct. Salud": 0,
        "Desct. AFP": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre": "Elena Fernandez",
        "Sueldo": 0,
        "Desct. Salud": 0,
        "Desct. AFP": 0,
        "Sueldo liquido": 0,
    }
]

try:
    def asignar_sueldos():
        for trabajador in trabajadores:
            sueldo = random.randint(300000, 2500000)
            trabajador['Sueldo'] = sueldo
            print(f"Nombre: {trabajador['Nombre']}     Sueldo: ${trabajador['Sueldo']}")
            
        print("Se han asignado los sueldos aleatoriamente")
    
    def clasificar_sueldos():
        sueldos_bajos = []
        sueldos_medios = []
        sueldos_altos = []
        for trabajador in trabajadores:
            if trabajador['Sueldo'] < 800000:
                sueldos_bajos.append(trabajador)
            elif 800000 < trabajador['Sueldo'] and trabajador['Sueldo'] < 2000000:
                sueldos_medios.append(trabajador)
            elif trabajador['Sueldo'] > 2000000 :
                sueldos_altos.append(trabajador)
        
        print(f"""   Sueldos menores a $800.000      Total : {len(sueldos_bajos)}  
                     Nombre empleado                   Sueldo""")
        for trabajador in sueldos_bajos:
            print(f"""
                    {trabajador['Nombre']}            ${trabajador['Sueldo']}
                     """)     
        
        print(f"""   Sueldos entre $800.000 y $2.000.000    Total : {len(sueldos_medios)}  
                     Nombre empleado                   Sueldo""")
        for trabajador in sueldos_medios:
            print(f"""
                    {trabajador['Nombre']}            ${trabajador['Sueldo']}
                      """)   
        
        print(f"""   Sueldos superior a $2.000.000    Total : {len(sueldos_altos)}  
                     Nombre empleado                   Sueldo""")
        for trabajador in sueldos_altos:
            print(f"""
                    {trabajador['Nombre']}            ${trabajador['Sueldo']}
                       """)   
    
    def estadisticas():
        sueldo_minimo = 0
        sueldo_maximo = 0
        sumatoria = 0
        for trabajador in trabajadores:
            if sueldo_minimo == 0 or trabajador['Sueldo'] < sueldo_minimo:
                sueldo_minimo = trabajador['Sueldo']
                trabajador_minimo = trabajador
            
            if sueldo_maximo == 0 or trabajador['Sueldo'] > sueldo_maximo:
                sueldo_maximo = trabajador['Sueldo']
                trabajador_maximo = trabajador
                
                
            sumatoria += trabajador["Sueldo"]
            
        promedio = sumatoria/10
        print(f"El trabajador con el sueldo menor es {trabajador_minimo['Nombre']} y su sueldo es de {sueldo_minimo} ")
        print(f"El trabajador con el sueldo mayor es {trabajador_maximo['Nombre']} y su sueldo es de {sueldo_maximo} ")
        print(f"El promedio de los sueldos es de {promedio}")   
        
                
    def reporte_de_sueldos():
        print(f"""
                  Nombre empleado Sueldo Base Descuento Salud Descuento AFP Sueldo liquido
                  """)
        for trabajador in trabajadores:
            trabajador['Desc. salud'] = trabajador['Sueldo'] * 0.7
            trabajador['Desc. afp'] = trabajador['Sueldo'] * 0.12
            
            descTotales = trabajador['Desc. salud'] + trabajador['Desc. afp']
            
            trabajador['Sueldo liquido'] = trabajador['Sueldo'] - descTotales
            
            print(f"""
                  {trabajador['Nombre']}  {trabajador['Sueldo']} {trabajador['Desc. salud']} {trabajador['Desc. afp']} {trabajador['Sueldo liquido']}
                  """)
        
        with open("reporte_de_sueldos.csv", "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(['Nombre', 'Sueldo base', 'Desc. salud', 'Desc. afp', 'Sueldo liquido'])
                for i in trabajadores:
                    escritor.writerows(
                        [[i['Nombre'], i['Sueldo'], i['Desc. salud'], i['Desc. afp'], i['Sueldo liquido']]
                         ])   
        print("¡Descarga del archivo realizada con exito!")
            
            
    
    def menu():
        menu = int(input("""
                        ﹉﹉﹉﹉﹉﹉﹉୨♡୧﹉﹉﹉﹉﹉﹉﹉﹉
                                ୨୧ ꒰ Menú ꒱ ୨୧
                        1. Asignar sueldos aleatorios
                        2. Clasificar sueldos
                        3. Ver estadísticas
                        4. Reporte de sueldos
                        5. Salir del programa
                        
                        Ingrese una opción:
                        ﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍
                        """))
        return menu


    while True:
        op = menu()
        
        if op == 1:
            print("⊹ ࣪ ˖₊˚⊹⋆ Asignar sueldos aleatorios ⊹ ࣪ ˖₊˚⊹⋆")
            asignar_sueldos()
        elif op == 2:
            print("⊹ ࣪ ˖₊˚⊹⋆ Clasificar sueldos ⊹ ࣪ ˖₊˚⊹⋆")
            clasificar_sueldos()
        elif op == 3:
            print("⊹ ࣪ ˖₊˚⊹⋆ Estadísticas ⊹ ࣪ ˖₊˚⊹⋆")
            estadisticas()
        elif op == 4:
            print("⊹ ࣪ ˖₊˚⊹⋆ Reporte de sueldos ⊹ ࣪ ˖₊˚⊹⋆")
            reporte_de_sueldos()
        elif op == 5:
            print("Finalizando programa...")
            print("Desarrollado por Paula Frías Navarro")
            print("RUT 20.458.065-0")
            print(""" 
    ∧＿∧
　 (｡･ω･｡)つ━☆・*。
  ⊂/　 /　       ・゜
　しーＪ　　　     °。+ * 。　
　　　　　                  .・゜
　　　　　                     ｡ﾟﾟ･｡･ﾟﾟ。
　　　　                     　ﾟ。　  ｡ﾟ
                               　ﾟ･｡･ﾟ 
                  """)
            break
        else: print("Ingrese una opción válida del menú")

except Exception as e: print(f"Ingrese una opción válida segun lo solicitado {e}")