from controller.arbol_jugadas import Arbol_jugadas
from modelo.equipo import Equipo



'''
    Inicia el proceso
'''
def inicio():

    #Inicializa el arbol de jugadas
    arbol_jugadas = Arbol_jugadas('jugadas.json')

    #Inicializa equipos
    equipo_a = Equipo("Millonarios")

    equipo_a.habilidad_portero = 10
    equipo_a.fortaleza_defensa = 10
    equipo_a.seguridad_pases = 10
    equipo_a.penales = 10
    equipo_a.tiros_libres = 10
    equipo_a.agresividad = 10
    equipo_a.ofensividad = 10
    equipo_a.defensividad = 10

    equipo_b = Equipo("Santa Fe")
    equipo_b.habilidad_portero = 10
    equipo_b.fortaleza_defensa = 10
    equipo_b.seguridad_pases = 10
    equipo_b.penales = 10
    equipo_b.tiros_libres = 10
    equipo_b.agresividad = 10
    equipo_b.ofensividad = 10
    equipo_b.defensividad = 10



    sig_jugada = "inicio"

    print("#############")
    print(sig_jugada)
    print("#############")

    contador = 0
    while True:
        print(">>>>>>>> ",sig_jugada)
        sig_jugada = arbol_jugadas.siguiente_jugada(sig_jugada)
        contador+=1
        if sig_jugada == 'gol':
            break

    print("numero jugadas a gol", contador)
    #print(json.dumps(json_ob2,indent=2))

    # print(json_Jugadas)



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
# [ ] Cambio de equipo 
# [ ] Lanzar jugada inicial
# [ ] afectacion probabilidades
# [ ] Sacar el JSON aparte 
# [ ] Validar q potencializadores afectan las probabilidades



