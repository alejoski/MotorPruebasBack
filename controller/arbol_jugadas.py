#     ██╗███████╗ ██████╗ ███╗   ██╗
#     ██║██╔════╝██╔═══██╗████╗  ██║
#     ██║███████╗██║   ██║██╔██╗ ██║
#██   ██║╚════██║██║   ██║██║╚██╗██║
#╚█████╔╝███████║╚██████╔╝██║ ╚████
# ╚════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝

import json
import copy
from random import randint



class Arbol_jugadas:
    def __init__(self, json, equipo) -> None:
        self.json = json
        self._json_ob2 = ""
        self.equipo = equipo
        self.cargar_josn()

    """
        Carga archivo jugadas.json 
    """

    def cargar_josn(self):
        with open(self.json) as f:
            self._json_ob2 = json.load(f)

    """
        Seleciona la siguiente jugada partir de una jugada inicial
    """

    def siguiente_jugada(self, jugada)-> list:
        # Realiza copia profunda de la lista de posibilidades para que no se pase por referencia
        posi = self.jugada_json_by_key(jugada)["posibilidades"]
        #Seleciona aleatoreamente la jugada
        jugada_seleccionada = self.seleccion_aleatorea_posibilidad(posi)        
        return self.jugada_json_by_key(jugada_seleccionada)

    """
        Retorna el JSON especifico de una jugada
    """
    def jugada_json_by_key(self, jugada)->list:
        j_json = copy.deepcopy(self._json_ob2[jugada])
        return j_json
    
    """
        Retorna el JSON especifico de una jugada
    """
    def jugada_json_by_id(self, id)->list:
        for jugada in self._json_ob2:
            if id == self._json_ob2[jugada]['id']:                
                return copy.deepcopy(self._json_ob2[jugada])
        


    """
        Entre las posibilidades de una Jugada inicial
        selecciona aleatoreamente una
    """

    def seleccion_aleatorea_posibilidad(self, posibildades)->str:
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
            minProbabilidad = posibilidad[2] + 1

        num_alatoreo = randint(1, maxProbabilidad)
        #print(posibildades)
        #print("num_alatoreo", num_alatoreo)

        # Recorre la lista de posibilidades para validar cual fue la seleccionada leatoreamente
        for posibilidad in posibildades:
            if num_alatoreo >= posibilidad[1] and num_alatoreo <= posibilidad[2]:
                return posibilidad[0]
            


