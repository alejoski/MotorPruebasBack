from controller.arbol_jugadas import Arbol_jugadas
from modelo.equipo import Equipo
import random


equipo_a = Equipo("")

equipo_b = Equipo("")


def sorteo_inicio_partido(equipo_a, equipo_b)-> Equipo:

    return random.choice([equipo_a, equipo_b])


'''
    Inicia el proceso
'''
def inicio():



    #Inicializa equipos
    global equipo_a
    global equipo_b
    

    equipo_a.nombre = "Millonarios"
    equipo_a.goles = 0
    equipo_a.habilidad_portero = 10
    equipo_a.fortaleza_defensa = 10
    equipo_a.seguridad_pases = 10
    equipo_a.penales = 10
    equipo_a.tiros_libres = 10
    equipo_a.agresividad = 10
    equipo_a.ofensividad = 10
    equipo_a.defensividad = 10
    #equipo.Al anotar gol subir el animo (confianza)

    equipo_b.nombre = "SantaFe"
    equipo_b.goles = 0
    equipo_b.habilidad_portero = 5
    equipo_b.fortaleza_defensa = 5
    equipo_b.seguridad_pases = 5
    equipo_b.penales = 5
    equipo_b.tiros_libres = 5
    equipo_b.agresividad = 5
    equipo_b.ofensividad = 5
    equipo_b.defensividad = 5


    equipo_juega = sorteo_inicio_partido(equipo_a,equipo_b)

    print(equipo_juega.nombre)

        #Inicializa el arbol de jugadas
    arbol_jugadas = Arbol_jugadas('jugadas.json', equipo_juega)



    sig_jugada = "inicio"
    sig_jugada_list =[]

    print("#############")
    print(sig_jugada)
    print("#############")

    #print(arbol_jugadas.jugada_json_by_id(1))
    #print(arbol_jugadas.jugada_json_by_id(2))
    #print(arbol_jugadas.jugada_json_by_id(3))

    contador = 0
    while True:
        
        
        #sig_jugada_str = sig_jugada_list['descripcion'].replace("XYZ","")

        sig_jugada_list = arbol_jugadas.siguiente_jugada(sig_jugada)

        narracion = sig_jugada_list['descripcion'].replace("XYZ",equipo_juega.nombre)
        sig_jugada = sig_jugada_list['key']

        print(f"*[{equipo_juega.nombre}]  {narracion}")

        

        contador+=1
        # if sig_jugada == 'gol':
        #     equipo_juega = cambio_equipo_juega_x_gol(equipo_juega)
        print(sig_jugada_list['cambio_equipo'])
        

        if sig_jugada_list['cambio_equipo']:
            equipo_juega = cambio_equipo_juega_x_gol(equipo_juega, sig_jugada)
            
        
        if contador == 100:
            break

    print(f'{equipo_a.nombre} ({equipo_a.goles}) - {equipo_b.nombre} ({equipo_b.goles})')
    

def cambio_equipo_juega_x_gol(equipo_juega, jugada):
    if jugada == 'gol':
        equipo_juega.goles =  equipo_juega.goles + 1

    if equipo_juega.nombre == equipo_a.nombre:
        return equipo_b
    else:
        return equipo_a

    


inicio()




# ████████╗ ██████╗ ██████╗  ██████╗ 
# ╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗
#    ██║   ██║   ██║██║  ██║██║   ██║
#    ██║   ██║   ██║██║  ██║██║   ██║
#    ██║   ╚██████╔╝██████╔╝╚██████╔╝
#    ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ 
#
# [x] Seleccionar aleatoriamente una de esas posibilidades
# [x] Determinar las posibilidades despues de esa jugada
# [x] Crear clase arbol 
# [x] Crear clase Equipo
# [x] Cambio de equipo 
# [x] Sacar el JSON aparte 
# [ ] Identificar  si el equipo que juega es quien hace la jugada o no (XYZ)(Arquero)
# [ ] Lanzar jugada inicial
# [ ] afectacion probabilidades
# [ ] Validar q potencializadores afectan las probabilidades



