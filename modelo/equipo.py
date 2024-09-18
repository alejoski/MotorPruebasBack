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
        self._habilidad_portero = None
        self._fortaleza_defensa = None
        self._seguridad_pases = None
        self._penales = None
        self._tiros_libres = None
        self._agresividad = None
        self._ofensividad = None
        self._defensividad = None
        self._delantera = None


        self._goles= None

    

    
