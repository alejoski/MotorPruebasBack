import json
import copy

from random import randint


# ██████╗██╗      █████╗ ███████╗███████╗███████╗
#██╔════╝██║     ██╔══██╗██╔════╝██╔════╝██╔════╝
#██║     ██║     ███████║███████╗█████╗  ███████╗
#██║     ██║     ██╔══██║╚════██║██╔══╝  ╚════██║
#╚██████╗███████╗██║  ██║███████║███████╗███████║
# ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝


class Jugada():


    def __init__(self, id = int , descripcion = str, posibilidades = []) -> None:
        self.id = id
        self.descripcion = descripcion #Esta descripcion debe tener varias opciones
        self.posibilidades = posibilidades

    def add_posibilidad(self, posibilidad):
        self.posibilidades.append(posibilidad)

    def print_posibildiades(self):
        for posibilidad in self.posibilidades:
            print(posibilidad)

    def __str__(self):
        return f"Desc => {self.descripcion}"

inicio = Jugada()
pase_corto = Jugada()


pase_corto = Jugada(2, "realiza pase corto",[])
inicio = Jugada(1, "Inicia el partido", [pase_corto])

# inicio.print_posibildiades()



#     ██╗███████╗ ██████╗ ███╗   ██╗
#     ██║██╔════╝██╔═══██╗████╗  ██║
#     ██║███████╗██║   ██║██╔██╗ ██║
#██   ██║╚════██║██║   ██║██║╚██╗██║
#╚█████╔╝███████║╚██████╔╝██║ ╚████
# ╚════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝

jugada = "Pase"


#Tiempo por jugada
#Factores que aumentan (potencian) la probabilidad de que se de una jugada
#determnar quien esta jugando

#Considerar que en un solo JSON pueden venir diferentes datos (Tablas)
#{
#  "Jugadas":[
#        {
#
#        },
#    ],
# "otro":[
#        {
#
#        }
#    ]
#}

json_Jugadas = '''{
    "inicio":{
        "id":1,
        "descripcion":"Inicia el partido",
        "posibilidades": [["pase_corto_adelante",45],["pase_corto_atras", 50], ["tiro_arco",5]]
    },

    "portero_despeja_corto":{
        "id":2,
        "descripcion":"Portero despeja corto",
        "posibilidades": [["pase_corto_adelante",35],["pase_corto_atras",35], ["tiro_arco",30]]
    },

    "portero_despeja_lago":{
        "id":3,
        "descripcion":"Portero despeja largo",
        "posibilidades": [["pase_corto_adelante",35],["pase_corto_atras",35], ["tiro_arco",30]]
    },

    "pase_corto_atras":{
        "id":4,
        "descripcion":"Pase corto atras",
        "posibilidades": [["pase_corto_adelante",35], ["pase_corto_atras",35], ["tiro_arco",70]]
    },

    "pase_corto_adelante":{
        "id":4,
        "descripcion":"Pase corto adelante",
        "posibilidades": [["pase_corto_adelante",35], ["pase_corto_atras",35], ["tiro_arco",70]]
    },

    "tiro_arco":{
        "id":5,
        "descripcion":"Lanza tiro al arco",
        "posibilidades": [["arquero_tapa",70], ["tiro_desviado",20], ["gol",10]]
    },

    "arquero_tapa":{
        "id":6,
        "descripcion":"El arquero tapa el tiro",
        "posibilidades": [["portero_despeja_corto",40], ["portero_despeja_lago",60]]
    },

    "tiro_desviado":{
        "id":7,
        "descripcion":"el tiro sale desviado",
        "posibilidades": [["portero_despeja_corto",40], ["portero_despeja_lago",60]]
    },

    "gol":{
        "id":8,
        "descripcion":"Anota Gol!!",
        "posibilidades": [["saque_mitad_cancha",100]]
    },

    "saque_mitad_cancha":{
        "id":9,
        "descripcion":"Se reanuda el partido a mitad de cancha",
        "posibilidades": [["pase_corto_adelante",45],["pase_corto_atras", 50], ["tiro_arco",5]]
    }
}'''


json_ob2 = json.loads(json_Jugadas)
#print(type(json_ob2))
#print(json_ob2)


'''
print(type(json_Jugadas))
print(json_Jugadas)

#dumps() conviert el JSON a String
#indent, sort_keys
json_ob = json.dumps(json_Jugadas, indent=2)
print(type(json_ob))
print(json_ob)

print(type(json_ob2['gol']))
print(json_ob2['gol'])

print(type(json_ob2['gol']['id']))
print(json_ob2['gol']['id'])

print("cantidad de regsitros ",len(json_ob2))
'''

#1) Lanzar jugada inicial
#2) Determinar las posibilidades despues de esa jugada
#3) Validar q potencializadores afectan las probabilidades
#4) Seleccionar aleatoriamente una de esas posibilidades


'''
    Seleciona la siguiente jugadaa partir de una jugada inicial
'''
def siguiente_jugada(jugada):

    #Realiza copia profunda de la lista de posibilidades para que no se pase por referencia
    posi = jugada_json(jugada)['posibilidades']
    jugada_seleccionada = seleccion_aleatorea_posibilidad(posi)
    return jugada_seleccionada

'''
    Retorna el JSON especifico de una jugada
'''
def jugada_json(jugada):
    j_json = copy.deepcopy(json_ob2[jugada])
    return j_json

'''
    Entre las posibilidades de una Jugada inicial
    selecciona aleatoreamente una
'''
def seleccion_aleatorea_posibilidad(posibildades):

    maxProbabilidad = 0
    minProbabilidad = 1

    # Arma la nueva lista de posibilidades, de esto:
    # [['pase_corto_adelante', 45], ['pase_corto_atras', 50], ['tiro_arco', 5]]
    # a esto:
    # [['pase_corto_adelante', 1, 45], ['pase_corto_atras', 46, 95], ['tiro_arco', 96, 100]]
    for posibilidad in posibildades:
        maxProbabilidad += posibilidad[1]
        posibilidad[1] = minProbabilidad
        posibilidad.append(maxProbabilidad)
        minProbabilidad = posibilidad[2]+1

    num_alatoreo = randint(1,maxProbabilidad)

    print(posibildades)
    print("num_alatoreo",num_alatoreo)

    #Recorre la lista de posibilidades para validar cual fue la seleccionada leatoreamente
    for posibilidad in posibildades:
        if (num_alatoreo >= posibilidad[1] and  num_alatoreo <=  posibilidad[2]):
            return posibilidad[0]





'''
    Inicia el proceso
'''
def inicio():

    sig_jugada = "inicio"

    print("#############")
    print(sig_jugada)
    print("#############")

    contador = 0
    while True:
        print(">>>>>>>> ",sig_jugada)
        sig_jugada = siguiente_jugada(sig_jugada)
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
# 1) Cambio de equipo 
# 2) afectacion probabilidades
# 3) Sacar el JSON aparte
#


