from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
import re
from IPython.display import clear_output

def Menu():
    """Funcion que Muestra el Menu"""
    print ("""
        ********************************
        Seleccione un tipo de búsqueda
        ********************************
        OPCIONES
            1) IDs de los edificios de un barrio
            2) IDs de los edificios de un distrito
            3) Los 10 edificios que más consumen 
            4) Consumo total de un barrio/distrito
            5) Todos los edificios y calles de un barrio
            6) Salir
    """)

def myFunc(e):
    return e[0]


def Seleccionados_Barrio_Distrito():
    print("""
    ******************************
    Seleccione un tipo de búsqueda
    ******************************
    OPCIONES
        1) Barrios
        2) Distritos
        """)

lista_barrios = """        
        ******************************
        Seleccione el barrio
        ******************************
        
        OPCIONES
            1) SAN_ISIDRO
            2) ALUCHE
            3) JERONIMOS
            4) CASCO_HISTORICO_DE_VALLECAS
            5) ROSAS
            6) VENTAS
            7) VALDEFUENTES
            8) JUSTICIA 
            9) MEDIA_LEGUA
            10) PUEBLO_NUEVO
            11) ACACIAS
            12) UNIVERSIDAD
            13) EL_PILAR
            14) VALDEBERNARDO
            15) CORRALEJOS
            16) PALOS_DE_MOGUER
            17) AGUILAS
            18) PALOMERAS_BAJAS
            19) ALAMEDA_DE_OSUNA
            20) SANTA_EUGENIA
            21) CONCEPCION
            22) CASCO_HISTORICO_DE_VICALVARO
            23) CARMENES
            24) APOSTOL_SANTIAGO
            25) MIRASIERRA
            26) CANILLAS
            27) ZOFIO
            28) VILLAVERDE_ALTO
            29) BERRUGUETE
            30) IMPERIAL
            31) HELLIN
            32) SAN_JUAN_BAUTISTA
            33) LA_PAZ
            34) ENTREVIAS
            35) LUCERO
            36) VALLEHERMOSO
            37) COMILLAS
            38) PUERTA_BONITA
            39) NUMANCIA
            40) PALACIO
            41) ALMENDRALES
            42) ORCASITAS
            43) ESTRELLA
            44) ORCASUR
            45) BELLAS_VISTAS
            46) GUINDALERA
            47) LOS_ANGELES
            48) ALMENARA
            49) BUTARQUE
            50) LOS_ROSALES
            51) NINIO_JESUS
            52) ARAPILES
            53) ADELFAS
            54) CASCO_HISTORICO_DE_BARAJAS
            55) CHOPERA
            56) MOSCARDO
            57) PRADOLONGO
            58) LEGAZPI
            59) CASTILLA
            60) CASA_DE_CAMPO
            61) VINATEROS
            62) IBIZA
            63) FUENTE_DEL_BERRO
            64) CAMPAMENTO
            65) ARAVACA
            66) PACIFICO
            67) VALDEZARZA
            68) VISTA_ALEGRE
            69) SAN_CRISTOBAL
            70) EL_VISO
            71) TRAFALGAR
            72) ARCOS
            73) EL_GOLOSO
            74) ALMAGRO
            75) BUENAVISTA
    """

lista_distritos = """
            ******************************
            Seleccione el distrito
            ******************************
            OPCIONES
            1) CARABANCHEL
            2) LATINA
            3) RETIRO
            4) VILLA_DE_VALLECAS
            5) SAN_BLAS-CANILLEJAS
            6) CIUDAD_LINEAL
            7) HORTALEZA
            8) CENTRO 
            9) MORATALAZ
            10) ARGANZUELA
            11) FUENCARRAL-EL_PARDO
            12) VICALVARO
            13) BARAJAS
            14) PUENTE_DE_VALLECAS
            15) USERA
            16) VILLAVERDE
            17) TETUAN
            18) CHAMBERI
            19) SALAMANCA
            20) CHAMARTIN
            21) MONCLOA-ARAVACA
            
            """

def App():
    """Funcion Para Calcular Operaciones Aritmeticas"""

    Menu()

    opc1 = int(input("Opción seleccionada: \n"))
    clear_output()
    
    DISTRITOS = ['CARABANCHEL', 'LATINA', 'RETIRO', 'VILLA_DE_VALLECAS', 'SAN_BLAS-CANILLEJAS', 'CIUDAD_LINEAL', 'HORTALEZA', 'CENTRO', 'MORATALAZ', 'ARGANZUELA', 'FUENCARRAL-EL_PARDO', 'VICALVARO', 'BARAJAS', 'PUENTE_DE_VALLECAS', 'USERA', 'VILLAVERDE', 'TETUAN', 'CHAMBERI', 'SALAMANCA', 'CHAMARTIN', 'MONCLOA-ARAVACA']
    BARRIOS = ['SAN_ISIDRO','ALUCHE','JERONIMOS','CASCO_HISTORICO_DE_VALLECAS','ROSAS','VENTAS','VALDEFUENTES','JUSTICIA','MEDIA_LEGUA','PUEBLO_NUEVO','ACACIAS','UNIVERSIDAD','EL_PILAR','VALDEBERNARDO','CORRALEJOS','PALOS_DE_MOGUER','AGUILAS','PALOMERAS_BAJAS','ALAMEDA_DE_OSUNA','SANTA_EUGENIA','CONCEPCION','CASCO_HISTORICO_DE_VICALVARO','CARMENES','APOSTOL_SANTIAGO','MIRASIERRA','CANILLAS','ZOFIO','VILLAVERDE_ALTO','BERRUGUETE','IMPERIAL','HELLIN','SAN_JUAN_BAUTISTA','LA_PAZ','ENTREVIAS','LUCERO','VALLEHERMOSO','COMILLAS','PUERTA_BONITA','NUMANCIA','PALACIO','ALMENDRALES','ESTRELLA','ORCASUR','BELLAS_VISTAS','GUINDALERA','LOS_ANGELES','ALMENARA','BUTARQUE','LOS_ROSALES','NINIO_JESUS','ARAPILES','ADELFAS','CASCO_HISTORICO_DE_BARAJAS','CHOPERA','MOSCARDO','PRADOLONGO','CIUDAD_JARDIN','LEGAZPI','CASTILLA','CASA_DE_CAMPO','VINATEROS','IBIZA','FUENTE_DEL_BERRO','CAMPAMENTO','ARAVACA','PACIFICO','VALDEZARZA','VISTA_ALEGRE','SAN_CRISTOBAL','EL_VISO','TRAFALGAR','ARCOS','EL_GOLOSO','ALMAGRO','BUENAVISTA']
    
    g = Graph()
    g.namespace_manager.bind('our', Namespace("http://www.consumo_madrid.com/ontology#"), override=False)
    g.namespace_manager.bind('rr', Namespace("http://www.w3.org/ns/r2rml#"), override=False)
    g.namespace_manager.bind('rdf', Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), override=False)
    g.namespace_manager.bind('owl', Namespace("http://www.w3.org/2002/07/owl#"), override=False)
    g.namespace_manager.bind('rdfs', Namespace("http://www.w3.org/2000/01/rdf-schema#"), override=False)
    g.namespace_manager.bind('district', Namespace("http://www.consumo_madrid.com/ontology/District/"), override=False)
    g.namespace_manager.bind('neighborhood', Namespace("http://www.consumo_madrid.com/ontology/Neighborhood/"), override=False)
    g.parse("output-with-links.ttl", format="ttl")
    our = Namespace("http://www.consumo_madrid.com/ontology#")
    rr = Namespace ("http://www.w3.org/ns/r2rml#")
    rdf = Namespace ("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
    owl = Namespace ("http://www.w3.org/2002/07/owl#")
    rdfs = Namespace ("http://www.w3.org/2000/01/rdf-schema#")
    district = Namespace("http://www.consumo_madrid.com/ontology/District/")
    neighborhood = Namespace("http://www.consumo_madrid.com/ontology/Neighborhood/")
    
    if (opc1==1):
        
        print ("1) IDs de los edificios de un barrio")
        print (lista_barrios)
        opc2 = int(input("Barrio seleccionado:\n"))-1
        # clear_output(wait=False)

        query = 'SELECT DISTINCT ?Edificio WHERE {?Edificio a our:Building. ?Edificio our:isFromNeighborhood neighborhood:'+ str(BARRIOS[opc2])+'.}'
        q = prepareQuery(query, initNs = { "our": our, "rr": rr, "rdf":rdf, "owl":owl, "rdfs":rdfs, "district":district, "neighborhood":neighborhood})
        
        found = []
        for r in g.query(q):
            found.append(r)
            found = re.findall( r'\d+', str(found))
        print ('Los IDs de los edififcos que se encuentran en el barrio de {0} son: {1}'.format(BARRIOS[opc2], found))

    elif(opc1==2):

        print ("2) IDs de los edificios de un distrito")
        print (lista_distritos)
        opc2 = int(input("Opcion seleccionada:\n"))-1

        query = 'SELECT DISTINCT ?Edificio WHERE{?Edificio a our:Building. ?Edificio our:isFromDistrict district:'+ str(DISTRITOS[opc2])+'.}'
        q = prepareQuery(query , initNs = { "our": our, "rr": rr, "rdf":rdf, "owl":owl, "rdfs":rdfs, "district":district, "neighborhood":neighborhood})

        found = []
        for r in g.query(q):
            found.append(r)
            found = re.findall( r'\d+', str(found))
        
        print('Los IDs de los edififcos que se encuentran en el distrito de {0} son:\n{1}'.format(DISTRITOS[opc2], found))

    elif(opc1==3):
        print ("3) Los 10 edificios que más consumen ")
        query = '''SELECT DISTINCT ?C ?B ?M WHERE {?x a our:Energy_use. ?k a our:Building. ?k our:buildingName ?B. ?k our:hasEnergyUse ?x. 
                    ?x our:hasMagnitude ?M. ?x our:Amount ?C.}'''
        q = prepareQuery(query , initNs = { "our": our, "rr": rr, "rdf":rdf, "owl":owl, "rdfs":rdfs, "district":district, "neighborhood":neighborhood})
        
        found = []
        for r in g.query(q):
            found.append(r)

        m = []; w = []; v = []
        print(found[0][1].value)

        for pol in found:
            try:
                float(pol[0])
                if str(pol[2].value) == 'kWh':
                    w.append([pol[0].value,pol[1].value,pol[2].value])
                if str(pol[2].value) == 'kVAr':
                    v.append([pol[0].value,pol[1].value,pol[2].value])
                if str(pol[2].value) == 'm3/h':
                    m.append([pol[0].value,pol[1].value,pol[2].value])
            except:
                pass
            
        m.sort(key=myFunc, reverse=True)
        w.sort(key=myFunc, reverse=True)
        v.sort(key=myFunc, reverse=True)
        print("\nLos edificios que mas kWh consumen son: \n")
        for a in range(10):
            print("Top " + str(a+1) + ", " + str(w[a][1]) + " que consume " + str(w[a][0]) + " " + str(w[a][2]))
        print("\nLos edificios que mas kVAr consumen son: \n")
        for a in range(10):
            print("Top " + str(a+1) + ", " + str(v[a][1]) + " que consume " + str(v[a][0]) + " " + str(v[a][2]))
        print("\nLos edificios que mas m3/h consumen son: \n")
        for a in range(10):
            print("Top " + str(a+1) + ", " + str(m[a][1]) + " que consume " + str(m[a][0]) + " " + str(m[a][2]))
        
    elif(opc1==4):
        Seleccionados_Barrio_Distrito()
        opc2 = int(input("Opción seleccionada:\n"))


        # CONSUMO TOTAL DE UN BARRIO
        if (opc2==1):

            print ("Has elegido barrios.\n")
            print (lista_barrios)
            
            # Obtiene los tipos de energía
            opc3 = int(input("Opción seleccionada: \n")) - 1
            print ("Has elegido el barrio: ", BARRIOS[opc3])

            query4_1_1 = '''SELECT ?type WHERE { ?edificio a our:Building. ?edificio our:isFromNeighborhood neighborhood:''' +str(BARRIOS[opc3])+'''.
                            ?edificio our:hasEnergyUse ?hasEnergy.?hasEnergy our:hasMagnitude ?type} '''
            q4_1_1 = prepareQuery(query4_1_1, initNs = { "our": our, "rr": rr, "rdf":rdf, "owl":owl, "rdfs":rdfs, "district":district, "neighborhood":neighborhood})

            # Obtiene los valores de consumo
            query4_1_2 = '''SELECT ?magnitude WHERE { ?edificio a our:Building.?edificio our:isFromNeighborhood neighborhood:''' +str(BARRIOS[opc3])+ '''.
                            ?edificio our:hasEnergyUse ?hasEnergy. ?hasEnergy our:Amount ?magnitude} '''
            q4_1_2 = prepareQuery(query4_1_2, initNs = { "our": our, "rr": rr, "rdf":rdf, "owl":owl, "rdfs":rdfs, "district":district, "neighborhood":neighborhood})

            found = dict(); valores = list(); consumo = list()
            # Como en nuestro archivo ttl aprarecen de forma ordenada el tipo de energía y debajo el consumo, podemos obtenerlas por separado y ordenarlsa respecto sus índices
            # Guardamos en un diccionario los tipos de energía como claves y el consumo como sus claves

            for r in g.query(q4_1_1):
                valores.append(str(r[0]))

            for s in g.query(q4_1_2):
                valor = re.findall( r'\d+\.\d+', s[0])
                if len(valor)>0:
                    consumo.append(float(valor[-1]))

            for i, j in zip(valores, consumo):
                if i not in found:
                    found[i] = [j]
                else:
                    found[i].append(j)

            for i in found:
                print('El consumo total de {2} del barrio {0} es: {1} {2}'.format(BARRIOS[opc3], sum(found[i]), i))


        # CONSUMO TOTAL DE UN DISTRITO
        elif (opc2==2):

            print ("Has elegido distritos.\n")
            print (lista_distritos)

            # Obtiene los tipos de energía
            opc3 = int(input("Opción seleccionada: \n")) - 1
            print ("Has elegido el barrio: ", DISTRITOS[opc3])
 
            query4_1 = '''SELECT ?type WHERE { ?edificio a our:Building. ?edificio our:isFromDistrict district:''' +str(DISTRITOS[opc3])+'''.
                        ?edificio our:hasEnergyUse ?hasEnergy. ?hasEnergy our:hasMagnitude ?type}'''
            q4_1 = prepareQuery(query4_1, initNs = { "our": our, "rr": rr, "rdf":rdf, "owl":owl, "rdfs":rdfs, "district":district, "neighborhood":neighborhood})

            # Obtiene los valores de consumo
            query4_1_2 = '''SELECT ?magnitude WHERE { ?edificio a our:Building. ?edificio our:isFromDistrict district:''' +str(DISTRITOS[opc3])+ '''.
                            ?edificio our:hasEnergyUse ?hasEnergy. ?hasEnergy our:Amount ?magnitude} '''
            q4_1_2 = prepareQuery(query4_1_2, initNs = { "our": our, "rr": rr, "rdf":rdf, "owl":owl, "rdfs":rdfs, "district":district, "neighborhood":neighborhood})

            found = dict(); valores = list(); consumo = list()
            # Sigue la misma estructura al caso de Barrios de la opción 4

            for r in g.query(q4_1):
                valores.append(str(r[0]))

            for s in g.query(q4_1_2):
                valor = re.findall( r'\d+\.\d+', s[0])
                if len(valor) > 0:
                    consumo.append(float(valor[-1]))

            for i, j in zip(valores, consumo):
                if i not in found:
                    found[i] = [j]
                else:
                    found[i].append(j)

            for i in found:
                print('El consumo total de {2} del distrito {0} es: {1} {2}'.format(DISTRITOS[opc3], sum(found[i]), i))
    
    elif(opc1==5):
        
        print ("5) Todos los edificios y calles de un barrio")
        print (lista_barrios)
        opc2 = int(input("Barrio seleccionado:\n"))-1

        query = '''SELECT DISTINCT ?name ?street WHERE {?building our:isFromNeighborhood neighborhood:'''+ str(BARRIOS[opc2])+'''; 
                    our:isLocatedAt ?street; our:buildingName ?name.}'''
        q6 = prepareQuery(query , initNs = { "our": our, "rr": rr, "rdf":rdf, "owl":owl, "rdfs":rdfs, "district":district, "neighborhood":neighborhood})

        Building_names = []
        clear_output()
        print ('En el barrio de', BARRIOS[opc2], 'tenemos:')
        for r in g.query(q6):
            Name = re.findall(r"\w{5,}", str(r[0]))
            Street = re.findall(r"\w{10,}", str(r[1]))

            if Name[-1] not in Building_names:
                Building_names.append(Name[-1])
                print('   El edificio {0} se sitúa en {1}'.format(Name[-1], Street[-1]))
      
    elif(opc1==6):
        print ("Gracias por usar nuestros servicios. ¡Hasta pronto!")
    
    else:
        print ("El valor introducido es incorrecto, por favor, inténtelo de nuevo")
        opc1 = int(input("Selecione Opcion\n"))

if __name__ == "__main__":
    App()
