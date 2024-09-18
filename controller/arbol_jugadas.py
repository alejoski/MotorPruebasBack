'''
 █████╗ ██████╗ ██████╗  ██████╗ ██╗                      
██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██║                      
███████║██████╔╝██████╔╝██║   ██║██║                      
██╔══██║██╔══██╗██╔══██╗██║   ██║██║                      
██║  ██║██║  ██║██████╔╝╚██████╔╝███████╗                 
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝                 
                                                          
     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  █████╗ ███████╗
     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔════╝
     ██║██║   ██║██║  ███╗███████║██║  ██║███████║███████╗
██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██╔══██║╚════██║
╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝██║  ██║███████║
 ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝
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
        selecciona aleatoreamente una
    """
    def seleccion_aleatorea_posibilidad(self, posibildades, nombre_equipo) -> str:
        maxProbabilidad = 0
        minProbabilidad = 1

        if (nombre_equipo ==  self.equipo_a.nombre):
            equipo = self.equipo_a
        elif (nombre_equipo ==  self.equipo_b.nombre):
            equipo = self.equipo_b
            

        # Arma la nueva lista de posibilidades, de esto:
        # [['pase_corto_adelante', 45], ['pase_corto_atras', 50], ['tiro_arco', 5]]
        # a esto:
        # [['pase_corto_adelante', 1, 45], ['pase_corto_atras', 46, 95], ['tiro_arco', 96, 100]]
        for posibilidad in posibildades:

            #Validacion del incremento por caracteristicas que aumentan la probabilidad
            nombre_jugada = posibilidad[0]
            print("......................................JUGADA BUSCADA >",nombre_jugada)
            jugada_json = self.jugada_json_by_key(nombre_jugada)
            potenciadores = jugada_json['caracteristicas_potencian']

            #Se suma el valor del potenciador 
            valor_potenciado = 0
            for potenciador in potenciadores:

                if potenciador == 'habilidad_portero':
                    valor_potenciado += equipo.habilidad_portero
                elif potenciador == 'fortaleza_defensa':
                    valor_potenciado += equipo.fortaleza_defensa
                elif potenciador == 'seguridad_pases':
                    valor_potenciado += equipo.seguridad_pases
                elif potenciador == 'penales':
                    valor_potenciado += equipo.penales
                elif potenciador == 'tiros_libres':
                    valor_potenciado += equipo.tiros_libres
                elif potenciador == 'agresividad':
                    valor_potenciado += equipo.agresividad
                elif potenciador == 'ofensividad':
                    valor_potenciado += equipo.ofensividad
                elif potenciador == 'defensividad':
                    valor_potenciado += equipo.defensividad

                print("...................POTENCIA>",potenciador, "Valor (",valor_potenciado,") equipo (",equipo.nombre,")"  )
                
               

            maxProbabilidad += posibilidad[1] + valor_potenciado
            posibilidad[1] = minProbabilidad
            posibilidad.append(maxProbabilidad)
            minProbabilidad = posibilidad[2] + 1

        num_alatoreo = randint(1, maxProbabilidad)
        print(posibildades)
        print("num_alatoreo", num_alatoreo)

        # Recorre la lista de posibilidades para validar cual fue la seleccionada leatoreamente
        for posibilidad in posibildades:
            if num_alatoreo >= posibilidad[1] and num_alatoreo <= posibilidad[2]:
                return posibilidad[0]