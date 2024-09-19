'''
# ███████╗ ██████╗ ██╗   ██╗██╗██████╗  ██████╗ 
# ██╔════╝██╔═══██╗██║   ██║██║██╔══██╗██╔═══██╗
# █████╗  ██║   ██║██║   ██║██║██████╔╝██║   ██║
# ██╔══╝  ██║▄▄ ██║██║   ██║██║██╔═══╝ ██║   ██║
# ███████╗╚██████╔╝╚██████╔╝██║██║     ╚██████╔╝
# ╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝╚═╝      ╚═════╝ 
'''
class Equipo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

        #Caracteristicas
        self.habilidad_portero = None
        self.fortaleza_defensa = None
        self.seguridad_pases = None
        self.penales = None
        self.tiros_libres = None
        self.agresividad = None
        self.ofensividad = None
        self.defensividad = None
        self.precision_tiros = None

        #Datos del partido
        self.goles= None

    def retorna_valor_caracteristica(self,caracteristica)->int:
        if caracteristica == 'habilidad_portero':            
            return self.habilidad_portero
        elif caracteristica == 'fortaleza_defensa':
            return self.fortaleza_defensa
        elif caracteristica == 'seguridad_pases':
            return self.seguridad_pases
        elif caracteristica == 'penales':
            return self.penales
        elif caracteristica == 'tiros_libres':
            return self.tiros_libres
        elif caracteristica == 'agresividad':
            return self.agresividad
        elif caracteristica == 'ofensividad':
            return self.ofensividad
        elif caracteristica == 'defensividad':
            return self.defensividad
        elif caracteristica == 'precision_tiros':
            return self.precision_tiros
        return 0


    

    
