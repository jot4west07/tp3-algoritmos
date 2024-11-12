from lista import search, by_name, by_house, remove, show_list, show_list_list

entrenadores = [
{
"nombre": "Ash Ketchum",
"torneos_ganados": 7,
"batallas_perdidas": 50,
"batallas_ganadas": 120
},
{
"nombre": "Goh",
"torneos_ganados": 2,
"batallas_perdidas": 10,
"batallas_ganadas": 40
},
{
"nombre": "Leon",
"torneos_ganados": 10,
"batallas_perdidas": 5,
"batallas_ganadas": 100
},
{
"nombre": "Chloe",
"torneos_ganados": 1,
"batallas_perdidas": 8,
"batallas_ganadas": 30
},
{
"nombre": "Raihan",
"torneos_ganados": 4,
"batallas_perdidas": 15,
"batallas_ganadas": 60
}
]

pokemones = [
{
    "nombre": "Pikachu",
    "nivel": 36,
    "tipo": "Eléctrico",
    "subtipo": None
},
{
    "nombre": "Mewtwo",
    "nivel": 46,
    "tipo": None,
    "subtipo": "Psíquico"
},
{
    "nombre": "Mew",
    "nivel": 46,
    "tipo": None,
    "subtipo": "Psíquico"
},
{
    "nombre": "Alakazam",
    "nivel": 35,
    "tipo": None,
    "subtipo": "Psíquico"
},
{
    "nombre": "Jolteon",
    "nivel": 35,
    "tipo": "Eléctrico",
    "subtipo": None
},
{
    "nombre": "Pidgeot",
    "nivel": 35,
    "tipo": "Normal",
    "subtipo": "Volador"
},
{
    "nombre": "Arcanine",
    "nivel": 36,
    "tipo": "Fuego",
    "subtipo": None
},
{
    "nombre": "Victreebel",
    "nivel": 34,
    "tipo": "Planta",
    "subtipo": "Veneno"
},
{
    "nombre": "Tyrantrum",
    "nivel": 41,
    "tipo": "Roca",
    "subtipo": "Dragon"
},
{
    "nombre": "Terrakion",
    "nivel": 41,
    "tipo": "Roca",
    "subtipo": "Lucha"
},
{
    "nombre": "Wingull",
    "nivel": 27,
    "tipo": "Agua",
    "subtipo": "Volador"
},
{
    "nombre": "Charizard",
    "nivel": 40,
    "tipo": "Fuego",
    "subtipo": "Volador"
},
{
    "nombre": "Bulbasaur",
    "nivel": 30,
    "tipo": "Planta",
    "subtipo": "Veneno"
},
{
    "nombre": "Starmie",
    "nivel": 30,
    "tipo": "Agua",
    "subtipo": "Psíquico"
},
{
    "nombre": "Psyduck",
    "nivel": 25,
    "tipo": "Agua",
    "subtipo": None
},
{
    "nombre": "Gyarados",
    "nivel": 35,
    "tipo": "Agua",
    "subtipo": "Volador"
},
{
    "nombre": "Onix",
    "nivel": 38,
    "tipo": "Roca",
    "subtipo": "Tierra"
},
{
    "nombre": "Geodude",
    "nivel": 28,
    "tipo": "Roca",
    "subtipo": "Tierra"
},
{
    "nombre": "Vulpix",
    "nivel": 20,
    "tipo": "Fuego",
    "subtipo": None
},
{
    "nombre": "Blastoise",
    "nivel": 50,
    "tipo": "Agua",
    "subtipo": None
},
{
    "nombre": "Umbreon",
    "nivel": 45,
    "tipo": "Siniestro",
    "subtipo": None
},
{
    "nombre": "Nidoking",
    "nivel": 40,
    "tipo": "Veneno",
    "subtipo": "Tierra"
}]

lista_entrenadores = []
for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador) # a lista_entrenadores que es una lista [] le agrega los entrenadores

pos_pikachu = search(pokemones,'nombre','Pikachu')
pos_jolteon = search(pokemones,'nombre','Jolteon')
pos_mewtwo = search(pokemones,'nombre','Mewtwo')
pos_mew = search(pokemones,'nombre','Mew')
pos_pidgeot = search(pokemones,'nombre','Pidgeot')
pos_alakazam = search(pokemones,'nombre','Alakazam')
pos_arcanine = search(pokemones,'nombre','Arcanine')
pos_victreebel = search(pokemones,'nombre','Victreebel')
pos_tyrantrum = search(pokemones,'nombre','Tyrantrum')
pos_terrakion = search(pokemones,'nombre','Terrakion')
pos_wingull = search(pokemones,'nombre','Wingull')
pos_charizard = search(pokemones,'nombre','Charizard')
pos_bulbasaur = search(pokemones,'nombre','Bulbasaur')
pos_starmie = search(pokemones,'nombre','Starmie')
pos_psyduck = search(pokemones,'nombre','Psyduck')
pos_gyarados = search(pokemones,'nombre','Gyarados')
pos_onix = search(pokemones,'nombre','Onix')
pos_geodude = search(pokemones,'nombre','Geodude')
pos_vulpix = search(pokemones,'nombre','Vulpix')
pos_blastoise = search(pokemones,'nombre','Blastoise')
pos_umbreon = search(pokemones,'nombre','Umbreon')
pos_nidoking = search(pokemones,'nombre','Nidoking')


pos_ash = search(lista_entrenadores, 'nombre', 'Ash Ketchum')
if pos_ash is not None:
    # agrega a ash su pokemon pikachu 
    lista_entrenadores[pos_ash]['sublist'].append(pokemones[pos_pikachu])
    lista_entrenadores[pos_ash]['sublist'].append(pokemones[pos_charizard])
    lista_entrenadores[pos_ash]['sublist'].append(pokemones[pos_bulbasaur])
    lista_entrenadores[pos_ash]['sublist'].append(pokemones[pos_bulbasaur])
    lista_entrenadores[pos_ash]['sublist'].append(pokemones[pos_pidgeot])
    lista_entrenadores[pos_ash]['sublist'].append(pokemones[pos_tyrantrum])
    lista_entrenadores[pos_ash]['sublist'].append(pokemones[pos_mew])
    lista_entrenadores[pos_ash]['sublist'].append(pokemones[pos_jolteon])


pos_goh = search(lista_entrenadores, 'nombre', 'Goh')
if pos_goh is not None:
    lista_entrenadores[pos_goh]['sublist'].append(pokemones[pos_starmie])
    lista_entrenadores[pos_goh]['sublist'].append(pokemones[pos_starmie])
    lista_entrenadores[pos_goh]['sublist'].append(pokemones[pos_psyduck])
    lista_entrenadores[pos_goh]['sublist'].append(pokemones[pos_victreebel])
    lista_entrenadores[pos_goh]['sublist'].append(pokemones[pos_victreebel])

pos_chloe = search(lista_entrenadores, 'nombre', 'Chloe')
if pos_chloe is not None:
    lista_entrenadores[pos_chloe]['sublist'].append(pokemones[pos_gyarados])
    lista_entrenadores[pos_chloe]['sublist'].append(pokemones[pos_onix])
    lista_entrenadores[pos_chloe]['sublist'].append(pokemones[pos_arcanine])
    lista_entrenadores[pos_chloe]['sublist'].append(pokemones[pos_arcanine])
    lista_entrenadores[pos_chloe]['sublist'].append(pokemones[pos_alakazam])
    lista_entrenadores[pos_chloe]['sublist'].append(pokemones[pos_psyduck])
    lista_entrenadores[pos_chloe]['sublist'].append(pokemones[pos_psyduck])       

pos_raihan = search(lista_entrenadores, 'nombre', 'Raihan')
if pos_raihan is not None:
    lista_entrenadores[pos_raihan]['sublist'].append(pokemones[pos_geodude])
    lista_entrenadores[pos_raihan]['sublist'].append(pokemones[pos_geodude])
    lista_entrenadores[pos_raihan]['sublist'].append(pokemones[pos_vulpix])
    lista_entrenadores[pos_raihan]['sublist'].append(pokemones[pos_wingull])   

pos_leon = search(lista_entrenadores, 'nombre', 'Leon')
if pos_leon is not None:
    lista_entrenadores[pos_leon]['sublist'].append(pokemones[pos_nidoking])
    lista_entrenadores[pos_leon]['sublist'].append(pokemones[pos_umbreon])
    lista_entrenadores[pos_leon]['sublist'].append(pokemones[pos_blastoise])
    lista_entrenadores[pos_leon]['sublist'].append(pokemones[pos_blastoise])
    lista_entrenadores[pos_leon]['sublist'].append(pokemones[pos_terrakion])
    lista_entrenadores[pos_leon]['sublist'].append(pokemones[pos_mewtwo])

# a. obtener la cantidad de Pokémons de un determinado entrenador: Ash
posicion_ash = search(entrenadores,'nombre','Ash Ketchum')
# la longitud de la sublist del entrenador es la cantidad de sus pokemones 
cant_pokes_ash = len(lista_entrenadores[posicion_ash]['sublist'])
print("La cantidad de pokemons de Ash es:", cant_pokes_ash)
print("")

# b. listar los entrenadores que hayan ganado más de tres torneos
print("Entrenadores con mas de 3 torneos ganados:")
for entrenador in entrenadores:
    if entrenador["torneos_ganados"] > 3:
        print(entrenador["nombre"]+" | ", end='') # end='' no deja un salto de linea
print("")
print("")

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
mas_torneos = 0

for entrenador in entrenadores:
    torneos_entrenador = entrenador["torneos_ganados"] # torneos_entrenador asume la cantidad de torneos ganados
    if torneos_entrenador > mas_torneos: # Si el entrenador actual tiene mas torneos ganados, mas_torneos asume esa cantidad de torneos ganados de ese entrenador
        mas_torneos = torneos_entrenador
# entrenador1 es el entrenador con mas torneos ganados    
entrenador1 = search(lista_entrenadores,'torneos_ganados',mas_torneos)
nivel_mayor = 0
# for que recorre la lista de pokemones del entrenador con mas torneos ganados
for pokemons in lista_entrenadores[entrenador1]['sublist']:
    nivel_actual = pokemons['nivel']
    if nivel_actual > nivel_mayor:
        nivel_mayor = nivel_actual
index_poke_mas_nivel = search(lista_entrenadores[entrenador1]['sublist'],'nivel',nivel_mayor)
poke_mas_nivel = lista_entrenadores[entrenador1]['sublist'][index_poke_mas_nivel]['nombre']

print("El entrenador con mas torneos ganados es:", lista_entrenadores[entrenador1]['nombre'])
print("El pokemon de mayor nivel del entrenador con mas torneos ganados es:",poke_mas_nivel)
print("")

# d. mostrar todos los datos de un entrenador y sus Pokémons
show_list_list('Lista de entrenadores','Lista de pokemons',lista_entrenadores)
print("")

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %
print("Entrenadores con batallas ganadas > 79%:")
for entrenador in lista_entrenadores:
    batallas_totales = entrenador['batallas_perdidas']+entrenador['batallas_ganadas']
    ganadas_porcentaje = entrenador['batallas_ganadas']*100/batallas_totales
    if ganadas_porcentaje > 79:
        print(entrenador['nombre']+" | ", end="")
print("")
print("")

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo agua y subtipo volador)
print("Entrenadores con Pokémons de tipo fuego:")
for entrenador in lista_entrenadores:
    for pokemons in entrenador['sublist']:
        if pokemons["tipo"] == "Fuego":
            print(entrenador['nombre']+" | ",end=(""))
print("")
print("Entrenadores con Pokémons de tipo planta:")
for entrenador in lista_entrenadores:
    for pokemons in entrenador['sublist']:
        if pokemons["tipo"] == "Planta":
            print(entrenador['nombre']+" | ",end=(""))
print("")
print("Entrenadores con Pokémons de tipo agua y subtipo volador:")
for entrenador in lista_entrenadores:
    for pokemons in entrenador['sublist']:
        if pokemons["tipo"] == "Agua" and pokemons['subtipo'] == "Volador":
            print(entrenador['nombre']+" | ",end=(""))
print("")
print("")

# g. el promedio de nivel de los Pokémons de un determinado entrenador: Ash y Leon
pos_ash = search(lista_entrenadores, 'nombre', 'Ash Ketchum')
pos_leon = search(lista_entrenadores, 'nombre', 'Leon')
suma_nivel = 0
suma_nivel1 = 0
for pokemons in lista_entrenadores[pos_ash]['sublist']:
    nivel = pokemons['nivel']
    suma_nivel = suma_nivel+nivel
promedio_ash = suma_nivel/len(lista_entrenadores[pos_ash]['sublist'])
promedio_ash_round = round(promedio_ash,2) # round(algo,2) el 2 indica cuantos nros despues de la coma
print("El promedio de nivel de los pokemons de Ash es:", promedio_ash_round)

for pokemons in lista_entrenadores[pos_leon]['sublist']:
    nivel1 = pokemons['nivel']
    suma_nivel1 = suma_nivel1+nivel1
promedio_leon = suma_nivel1/len(lista_entrenadores[pos_leon]['sublist'])
promedio_leon_round = round(promedio_leon,2)
print("El promedio de nivel de los pokemons de Leon es:", promedio_leon_round)
print("")

# h. determinar cuántos entrenadores tienen a un determinado Pokémon
lista_h = []
for entrenador in lista_entrenadores:
    for pokemons in entrenador['sublist']:
        if pokemons['nombre'] == "Psyduck":
            lista_h.append(entrenador['nombre']) # guarda en lista_h el nombre de los entrenadores
print("Entrenadores que tienen a Psyduck:")
for entrenador in lista_h:
    print(entrenador+" | ", end="")
print("")
print("")

# i. mostrar los entrenadores que tienen Pokemones repetidos
print("Entrenadores que tienen pokemons repetidos:")
lista_pokemons = []
lista_a_quitar = []

for entrenador in lista_entrenadores:
    for pokemons in entrenador['sublist']:
        lista_pokemons.append(pokemons['nombre']) # guarda en lista_pokemons todos los pokemones de todos los entrenadores
    # set no repite los elementos en una lista, por eso si las longitudes son distintas significa
    # que hay pokemones repetidos 
    if len(lista_pokemons) != len(set(lista_pokemons)): # significa que hay pokemons que se repiten
        lista_a_quitar = set(lista_pokemons) # set () devuelve una lista set: {x,y,z}
        quit_list = list(lista_a_quitar) # list() transforma el set a lista para usar indices []
        print(entrenador['nombre']+": ", end="")
        for i in range (len(quit_list)):
            lista_pokemons.remove(quit_list[i]) # a la lista_pokemons le deja solo los repetidos
        for pokemones in lista_pokemons:
            print(pokemones+" | ",end="")
        print("")
    lista_pokemons.clear() # Se vacia la lista para que en cada vuelta empiece sin nada
    lista_a_quitar.clear() # Se vacia la lista para que en cada vuelta empiece sin nada
print("")

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum,
# Terrakion o Wingull

for entrenador in lista_entrenadores:
    for pokemon in entrenador['sublist']:
        if pokemon['nombre'] == "Tyrantrum":
            print("Entrenador que tiene a Tyrantrum:", entrenador['nombre'])
        elif pokemon['nombre'] == "Terrakion":
            print("Entrenador que tiene a Terrakion:", entrenador['nombre'])
        elif pokemon['nombre'] == "Wingull":
            print("Entrenador que tiene a Wingull:", entrenador['nombre'])
print("")

""" k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos """ 
trainers = ["Ash Ketchum", "Goh", "Leon", "Chloe", "Raihan"]
print("Los entrenadores son: Ash Ketchum, Goh, Leon, Chloe, Raihan")
print("Ingrese el nombre de un entrenador respetando mayusculas y minusculas")
name_entrenador = input()
if name_entrenador not in trainers:
    print("El nombre ingresado no es valido")
print("Ingrese el nombre de un pokemon con su primer letra en mayusculas")
name_pokemon = input()
lista_pokes = []
list_pokes = []
for entrenador in lista_entrenadores:
    if name_entrenador == entrenador['nombre']:
        for pokemones in entrenador['sublist']:
            lista_pokes.append(pokemones['nombre'])
        list_pokes = list(lista_pokes)
        if name_pokemon in list_pokes: # si el nombre del pokemon esta en list_pokes
            index_trainer = search(lista_entrenadores,'nombre',name_entrenador) # indice del entrenador
            index_poke = search(entrenador['sublist'],'nombre',name_pokemon) # indice del pokemon
            print("El entrenador",name_entrenador,"tiene al pokemon",name_pokemon)
            print(lista_entrenadores[index_trainer])
            print("")
            print(entrenador['sublist'][index_poke])
        else:
            print("El entrenador no tiene ese pokemon o el dato ingresado no es valido")
print("")           
