'''
 █████╗ ██████╗ ██████╗  ██████╗ ██╗              ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  █████╗ ███████╗
██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██║              ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔════╝
███████║██████╔╝██████╔╝██║   ██║██║              ██║██║   ██║██║  ███╗███████║██║  ██║███████║███████╗
██╔══██║██╔══██╗██╔══██╗██║   ██║██║         ██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██╔══██║╚════██║
██║  ██║██║  ██║██████╔╝╚██████╔╝███████╗    ╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝██║  ██║███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝     ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝

'''
import json
import copy
from random import randint



class Arbol_jugadas:
    def __init__(self, json, equipo_a, equipo_b) -> None:
        self.json = json
        self._json_ob2 = ""
        self.equipo_a = equipo_a
        self.equipo_b = equipo_b
        self.cargar_josn()

    """
        Carga archivo jugadas.json 
    """
    def cargar_josn(self):
        with open(self.json, encoding='utf-8') as f:
            self._json_ob2 = json.load(f)

    """
        Seleciona la siguiente jugada apartir de una jugada inicial
    """
    def siguiente_jugada(self, jugada, nombre_equipo)-> list:   
        posibilidades = self.jugada_json_by_key(jugada)["posibilidades"]
        #Seleciona aleatoreamente la jugada
        jugada_seleccionada = self.seleccion_aleatorea_posibilidad(posibilidades, nombre_equipo)        
        return self.jugada_json_by_key(jugada_seleccionada)

    """
        Retorna el JSON especifico de una jugada
    """
    def jugada_json_by_key(self, jugada)->list:
        # Realiza copia profunda de la lista de posibilidades para que no se pase por referencia
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
        selecciona aleatoreamente una teniendo en cuenta las 
        caracteristicas de cada equipo
    """
    def seleccion_aleatorea_posibilidad(self, posibildades, nombre_equipo) -> str:
        maxProbabilidad = 0
        minProbabilidad = 1

        #Identifica el equipo que esta jugando
        if (nombre_equipo ==  self.equipo_a.nombre):
            equipo_juega = self.equipo_a
            equipo_no_juega = self.equipo_b
        elif (nombre_equipo ==  self.equipo_b.nombre):
            equipo_juega = self.equipo_b
            equipo_no_juega = self.equipo_a
            

        # Arma la nueva lista de posibilidades, de esto:
        # [['pase_corto_adelante', 45], ['pase_corto_atras', 50], ['tiro_arco', 5]]
        # a esto:
        # [['pase_corto_adelante', 1, 45], ['pase_corto_atras', 46, 95], ['tiro_arco', 96, 100]]
        for posibilidad in posibildades:

            #Validacion del incremento o reduccion por caracteristicas que varian la probabilidad
            nombre_jugada = posibilidad[0]
            #print("......................................JUGADA BUSCADA >>>>>>>>>> ",nombre_jugada, "(",posibilidad[1],")")
            jugada_json = self.jugada_json_by_key(nombre_jugada)
            caracteristicas_potencian = jugada_json['caracteristicas_aumentan']
            caracteristicas_reducen = jugada_json['caracteristicas_disminuyen']
            caracteristicas_equipo_contrario_aumentan = jugada_json['caracteristicas_equipo_contrario_aumentan']
            caracteristicas_equipo_contrario_disminuye = jugada_json['caracteristica_equipo_contrario_disminuye']

            #########################################################
            # Se calcula el valor del POTENCIADOR del propio equipo # 
            #########################################################
            valor_potenciado = 0
            for caracteristica_potencia in caracteristicas_potencian:
                #Obtoene el valor de la caracteristica para el equipo especifico
                valor_potenciado += equipo_juega.retorna_valor_caracteristica(caracteristica_potencia)
                
                #print("...................POTENCIA>",caracteristica_potencia, "Valor (",valor_potenciado,") equipo (",equipo_juega.nombre,")"  )

            ######################################################
            # Se calcula el valor del REDUCTOR del propio equipo #
            ######################################################
            valor_reducido = 0
            for caracteristica_reduce in caracteristicas_reducen:
                #Obtoene el valor de la caracteristica para el equipo especifico
                valor_reducido += equipo_juega.retorna_valor_caracteristica(caracteristica_reduce)

            #####################################################################################
            # Calcula el valor de AUMENTO de posibiliadd por una habilidad del equipo contrario #
            #####################################################################################
            valor_aumenta_contrario =0
            for caracteristica_equipo_contrario_aumenta in caracteristicas_equipo_contrario_aumentan:
                valor_aumenta_contrario += equipo_no_juega.retorna_valor_caracteristica(caracteristica_equipo_contrario_aumenta)

                #print("...................REDUCE>",caracteristica_reduce, "Valor (",valor_reducido,") equipo (",equipo_juega.nombre,")"  )
           
           
            ########################################################################################
            # calcula el valor de REDUCCION de posibilidad dada una habilidad del equipo contrario #   
            ########################################################################################
            valor_reducido_contrario = 0
            for caracteristica_equipo_contrario_disminuye in caracteristicas_equipo_contrario_disminuye:
                valor_reducido_contrario += equipo_no_juega.retorna_valor_caracteristica(caracteristica_equipo_contrario_disminuye)

            #print(f"TOTAL -> Valor POTENCIADO  Aumenta<{valor_potenciado}> Disminuye  <{valor_reducido}>     CONTRARIO Aumenta -> <{valor_aumenta_contrario}> reduce <{valor_reducido_contrario}>")

            ########################################################################################
            # Sealiza los calculos (+,-) de las probabiidades dados los refuctores y potenciadores #
            ########################################################################################
            maxProbabilidad += posibilidad[1] + valor_potenciado + valor_aumenta_contrario
            maxProbabilidad += -(valor_reducido if valor_reducido < posibilidad[1] else (posibilidad[1]-5) )
            maxProbabilidad += -(valor_reducido_contrario if valor_reducido_contrario < (posibilidad[1] + valor_potenciado ) else ((posibilidad[1] + valor_potenciado )-3) )
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