

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

##Almacena JSON en String
#json_Jugadas = ''''''

#Convierte String en JSON
#json_ob2 = json.loads(json_Jugadas)

#Carga archivo jugadas.json 

###with open('jugadas.json') as f:
###    json_ob2 = json.load(f)


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




'''
    Seleciona la siguiente jugadaa partir de una jugada inicial
'''

