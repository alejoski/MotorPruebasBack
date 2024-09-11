import json

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

print(inicio.print_posibildiades())



#     ██╗███████╗ ██████╗ ███╗   ██╗
#     ██║██╔════╝██╔═══██╗████╗  ██║
#     ██║███████╗██║   ██║██╔██╗ ██║
#██   ██║╚════██║██║   ██║██║╚██╗██║
#╚█████╔╝███████║╚██████╔╝██║ ╚████
# ╚════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝

jugada = "Pase"

json_Jugadas = {
    "inicio":{
        "id":1,
        "descripcion":"Inicia el partido",
        "posibilidades": [["pase",50]]
    },

    jugada:{
        "id":1,
        "descripcion":"Inicia el partido",
        "posibilidades": [["pase",50]]
    },

}

json_ob = json.dumps(json_Jugadas)

print(json_Jugadas)
print(json_ob)








