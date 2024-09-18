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

    

    
