from lista import search, by_name, by_house, remove

super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hank Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos. Usa un traje que lo hace pequeño."
  }
]


super_heroes.sort(key=by_house)


# a. eliminar el nodo que contiene la información de Linterna Verde

remove(super_heroes, 'nombre', 'Linterna Verde')
eliminado = search(super_heroes,'nombre','Linterna Verde') # search devuelve None si
# el personaje no esta en la lista
if eliminado == None: # Si eliminado == None significa que no esta en la lista
    print("Linterna verde fue eliminado de la lista")
else:
    print("Linterna verde no fue eliminado de la lista")
  
# b. mostrar el año de aparición de Wolverine

pos_wolverine = search(super_heroes,'nombre','Wolverine')
# super_heroes[pos_wolverine] accede a la posicion donde esta wolverine y ['año_aparicion'] es la clave del año de aparicion 
print("Año de aparicion de Wolverine:",super_heroes[pos_wolverine]['año_aparicion'])

# c. cambiar la casa de Dr. Strange a Marvel

pos_dr_strange = search(super_heroes,'nombre','Doctor Strange')
print("Casa comic original de Dr. Strange:",super_heroes[pos_dr_strange]['casa_comic'])
super_heroes[pos_dr_strange]['casa_comic'] = 'Marvel' # un solo = y no dos
print("Casa comic modificada de Dr. Strange:",super_heroes[pos_dr_strange]['casa_comic'])

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”

for i in range(len(super_heroes)):
  if 'traje' in super_heroes[i]['biografia'] or 'armadura' in super_heroes[i]['biografia']:
    print(i, super_heroes[i]['nombre']+":", super_heroes[i]['biografia'])
print("")
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;

print("Nombre y casa de los superhéroes cuya fecha de aparición sea anterior a 1963:")
for i in range(len(super_heroes)):
  if super_heroes[i]['año_aparicion'] < 1963:
    print(super_heroes[i]['nombre']+", "+super_heroes[i]['casa_comic'])
print("")
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
pos_capitana = search(super_heroes,'nombre','Capitana Marvel')
post_wonder_wm = search(super_heroes,'nombre','Mujer Maravilla')

print("Casa comic de Capitana Marvel:",super_heroes[pos_capitana]['casa_comic'])
print("Casa comic de Mujer Maravilla :",super_heroes[post_wonder_wm]['casa_comic'])
print("")

# g. mostrar toda la información de Flash y Star-Lord
pos_flash = search(super_heroes,'nombre','Flash')
pos_star_lord = search(super_heroes,'nombre','Star-Lord')
print("Informacion de Flash:")
print(super_heroes[pos_flash]) # Printea todo en la posicion donde esta flash 
print("Informacion de Star-Lord:")
print(super_heroes[pos_star_lord]) # # Printea todo en la posicion donde esta star_lord 
print("")

# h. listar los superhéroes que comienzan con la letra B, M y S
for index, heroe in enumerate(super_heroes):
  if heroe['nombre'].startswith(('B', 'S', 'M')):
    print(index, heroe['nombre'])
print("")

# i. determinar cuántos superhéroes hay de cada casa de comic.

contador_marvel = 0
contador_dc = 0
# Se vuelve a cambiar la casa comic de Dr. Strange a "Marvel Comics" para sumarla al contador
super_heroes[pos_dr_strange]['casa_comic'] = 'Marvel Comics'
for i in range(len(super_heroes)):
  if super_heroes[i]['casa_comic'] == 'DC Comics':
    contador_dc += 1
for i in range(len(super_heroes)):
  if super_heroes[i]['casa_comic'] == 'Marvel Comics':
    contador_marvel += 1
print("Cantidad de super-heroes de Marvel:",contador_marvel)
print("Cantidad de super-heroes de DC:",contador_dc)


