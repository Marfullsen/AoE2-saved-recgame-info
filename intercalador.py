#!/usr/bin/env python
#-*- coding: utf-8 -*-

from ageofempires_en import en
from ageofempires_es import es

en_es = dict()
for key, value in en.items():
	value = dict(zip(value.values(),es[key].values()))
	en_es[key] = value

# You should get the following dict from the above code, if uncommented, changes in imports must be taken into consideration.
# en_es = {'ages': {'Dark Age': 'Alta Edad Media', 'Feudal Age': 'Edad Feudal', 'Castle Age': 'Edad de los Castillos', 'Imperial Age': 'Edad Imperial', 'Post-Imperial Age': 'Edad Post-Imperial'}, 'game_types': {'Standard Game': 'Partida estándar', 'Regicide': 'Regicida', 'Death Match': 'Combate total', 'Custom Scenario': 'Escenario personalizado', 'Custom Campaign': 'Campaña personalizada', 'King of the Hill': 'Rey de la colina', 'Wonder Race': 'Carrera de las Maravillas', 'Defend the Wonder': 'Defender la Maravilla', 'Turbo Random Map': 'Mapa aleatorio turbo'}, 'map_styles': {'Standard': 'Estándar', 'Real World': 'Mundo real', 'Custom': 'Personalizado', 'Special Maps': 'Mapas especiales'}, 'map_names': {'Arabia': 'Arabia', 'Archipelago': 'Archipiélago', 'Baltic': 'Báltico', 'Black Forest': 'Selva negra', 'Coastal': 'Costa', 'Continental': 'Continental', 'Crater Lake': 'Lago de cráter', 'Fortress': 'Fortaleza', 'Gold Rush': 'Fiebre del oro', 'Highland': 'Montañas', 'Islands': 'Islas', 'Mediterranean': 'Mediterráneo', 'Migration': 'Migración', 'Rivers': 'Ríos', 'Team Islands': 'Islas de equipo', 'Full Random': 'Aleatorio total', 'Scandinavia': 'Escandinavia', 'Mongolia': 'Mongolia', 'Salt Marsh': 'Marisma', 'Yucatan': 'Yucatán', 'Arena': 'Arena', 'King of the Hill': 'Rey de la colina', 'Oasis': 'Oasis', 'Ghost Lake': 'Lago fantasma', 'Nomad': 'Nómada', 'Iberia': 'Iberia', 'Britain': 'Inglaterra', 'Mideast': 'Oriente Medio', 'Texas': 'Texas', 'Italy': 'Italia', 'Central America': 'América Central', 'France': 'Francia', 'Norse Lands': 'Tierras Nórdicas', 'Sea of Japan (East Sea}': 'Mar del Japón', 'Byzantium': 'Bizancio', 'Custom': 'Personalizado', 'Blind Random': 'Aleatorio a ciegas', 'Acropolis': 'Acrópolis', 'Budapest': 'Budapest', 'Cenotes': 'Cenotes', 'City of Lakes': 'La Ciudad de los Lagos', 'Golden Pit': 'Cuenca del oro', 'Hideout': 'Guaridas', 'Hill Fort': 'Castros', 'Lombardia': 'Lombardía', 'Steppe': 'Estepa', 'Valley': 'Valle', 'MegaRandom': 'Mega-Aleatorio', 'Hamburger': 'Hamburger', 'CtR Random': 'ClR Aleatorio', 'CtR Monsoon': 'ClR Región monzónica', 'CtR Pyramid Descent': 'ClR Pirámide abajo', 'CtR Spiral': 'ClR Espiral', 'Kilimanjaro': 'Kilimanjaro', 'Mountain Pass': 'Pasaje montañoso', 'Nile Delta': 'Delta del Nilo', 'Serengeti': 'Serengueti', 'Socotra': 'Socotra', 'Amazon': 'Amazonia', 'China': 'China', 'Horn of Africa': 'Cuerno de África', 'India': 'India', 'Madagascar': 'Madagascar', 'West Africa': 'África Occidental', 'Bohemia': 'Bohemia', 'Earth': 'La Tierra', 'Canyons': 'Cañones', 'Enemy Archipelago': 'Archirrivales de archipiélago', 'Enemy Islands': 'Rivales intraisleños', 'Far Out': 'Apartados', 'Front Line': 'Frente de batalla', 'Inner Circle': 'Círculo interno', 'Motherland': 'Cuna de la humanidad', 'Open Plains': 'Planicie', 'Ring of Water': 'Anillo de agua', 'Snakepit': 'Pozo de serpientes', 'The Eye': 'El ojo'}, 'resources': {'Food': 'Alimento', 'Wood': 'Madera', 'Stone': 'Piedra', 'Gold': 'Oro'}, 'game_speeds': {'Slow': 'Lenta', 'Normal': 'Normal', 'Fast': 'Rápida'}, 'reveal_map': {'Normal': 'Normal', 'Explored': 'Explorado', 'All Visible': 'Todo visible'}, 'civilizations': {'Random': 'Aleatoria', 'Britons': 'Ingleses', 'Franks': 'Francos', 'Goths': 'Godos', 'Teutons': 'Teutones', 'Japanese': 'Japoneses', 'Chinese': 'Chinos', 'Byzantines': 'Bizantinos', 'Persians': 'Persas', 'Saracens': 'Sarracenos', 'Turks': 'Turcos', 'Vikings': 'Vikingos', 'Mongols': 'Mongoles', 'Celts': 'Celtas', 'Spanish': 'Españoles', 'Aztecs': 'Aztecas', 'Mayans': 'Mayas', 'Huns': 'Hunos', 'Koreans': 'Coreanos', 'Italians': 'Italianos', 'Indians': 'Indios', 'Incas': 'Incas', 'Magyars': 'Magiares', 'Slavs': 'Eslavos', 'Portuguese': 'Portugueses', 'Ethiopians': 'Etíopes', 'Malians': 'Malíes', 'Berbers': 'Bereberes', 'Khmer': 'Jemeres', 'Malay': 'Malayos', 'Burmese': 'Birmanos', 'Vietnamese': 'Vietnamitas'}, 'map_sizes': {'Tiny (2 player}': 'Pequeñito (2 jug.)', 'Small (3 player}': 'Pequeño (3 jug.)', 'Medium (4 player}': 'Medio (4 jug.)', 'Normal (6 player}': 'Normal (6 jug.)', 'Large (8 player}': 'Grande (8 jug.)', 'Giant': 'Gigantesco', 'LudiKRIS': 'Descomunal'}, 'difficulties': {'Hardest': 'Máxima', 'Hard': 'Difícil', 'Moderate': 'Moderada', 'Standard': 'Estándar', 'Easiest': 'Muy fácil'}, 'units': {'Legionary': 'Legionario', 'Archer': 'Arquero', 'Hand Cannoneer': 'Artillero manual', 'Elite Skirmisher': 'Guerrillero de élite', 'Skirmisher': 'Guerrillero', 'Longbowman': 'Arquero de tiro largo', 'Arrow': 'Flecha', 'Archery Range': 'Galería tiro con arco', 'Mangudai': 'Mangudai', 'Barracks': 'Cuarteles', 'Fishing Ship': 'Pesquero', 'Junk': 'Junco', 'Trade Cog': 'Urca mercante', 'Blacksmith': 'Herrería', 'War Galley': 'Galera de guerra', 'Crossbowman': 'Ballestero', 'Teutonic Knight': 'Cab. Orden Teutónica', 'Dead crossbowman': 'Restos de ballestero', 'Monastery': 'Monasterio', 'Fortress': 'Fortaleza', 'Battering Ram': 'Ariete', 'Bombard Cannon': 'Cañón de asedio', 'Light Cavalry': 'Caballería ligera', 'Knight': 'Jinete', 'Cavalry Archer': 'Arquero a caballo', 'Cataphract': 'Catafracta', 'Huskarl': 'Huscarle', 'Trebuchet': 'Trebuchet', 'Dock': 'Muelle', 'Janissary': 'Jenízaro', 'Wild Boar': 'Jabalí', 'Siege Workshop': 'Taller maq. de asedio', 'Farm': 'Granja', 'Royal Janissary': 'Jenízaro de la guardia', 'Fish (Perch}': 'Pez (perca)', 'Fisherman': 'Pescador', 'Forage Bush': 'Arbusto de bayas', 'Dolphin': 'Delfín', 'Gate': 'Puerta', 'Deer': 'Ciervo', 'Gold Mine': 'Mina de oro', 'Mill': 'Molino', 'Shore Fish': 'Pez de costa', 'House': 'Casa', 'Town Center': 'Centro urbano', 'Palisade Wall': 'Empalizada', 'Chu Ko Nu': 'Chu ko nu', 'Militia': 'Milicia', 'Man-at-Arms': 'Hombre de armas', 'Heavy Swordsman': 'Espadachín pesado', 'Long Swordsman': 'Espad. espada larga', 'Watch Tower': 'Torre de guardia', 'Castle': 'Castillo', 'Villager': 'Aldeano', 'Market': 'Mercado', 'Stable': 'Establo', 'Dire Wolf': 'Lobo salvaje', 'Spearman': 'Lancero', 'Berserk': 'Berserker', 'Hawk': 'Halcón', 'Stone Mine': 'Cantera de piedra', 'Trade Workshop': 'Taller comercial', 'Dead knight': 'Restos de jinete', 'Flare': 'Bengala', 'Stone Wall': 'Muro de piedra', 'Builder': 'Constructor', 'Fortified Palisade Wall': 'Empalizada reforzada', 'Forager': 'Recolector', 'Hunter': 'Cazador', 'Lumberjack': 'Leñador', 'Stone Miner': 'Cantero', 'Monk': 'Monje', 'Wolf': 'Lobo', 'Trade Cart': 'Carreta mercancías', 'Rubble 1 x 1': 'Escombros 1 x 1', 'Rubble 2 x 2': 'Escombros 2 x 2', 'Rubble 3 x 3': 'Escombros 3 x 3', 'Rubble 4 x 4': 'Escombros 4 x 4', 'Rubble 6 x 6': 'Escombros 6 x 6', 'Rubble 8 x 8': 'Escombros 8 x 8', 'Fortified Wall': 'Muralla fortificada', 'Repairer': 'Reparador', 'Relic Cart': 'Carro de reliquias', 'Richard the Lionheart': 'Ricardo Corazón de León', 'The Black Prince': 'El Príncipe Negro', 'Stupa': 'Estupa', 'Friar Tuck': 'Fray Tuck', 'Sheriff of Nottingham': 'Sheriff de Nottingham', 'Charlemagne': 'Carlomagno', 'Roland': 'Roldán', 'Belisarius': 'Belisario', 'Theodoric the Goth': 'Teodorico el Godo', 'Aethelfirth': 'Etelfredo', 'Siegfried': 'Sigfrido', 'Erik the Red': 'Erik el Rojo', 'Tamerlane': 'Tamerlán', 'King Arthur': 'Rey Arturo', 'Lancelot': 'Sir Lanzarote', 'Gawain': 'Sir Gawain', 'Mordred': 'Mordred', 'Archbishop': 'Arzobispo', 'Dead long swordman': 'Restos esp. espada larga', 'Condottiero': 'Condotiero', 'Slinger': 'Hondero', 'Flamethrower': 'Lanzallamas', 'Fire Tower': 'Torre lanzallamas', 'Vlad Dracula': 'Vlad Drácula', 'Kitabatake': 'Kitabatake', 'Minamoto': 'Minamoto', 'Alexander Nevski': 'Alexander Nevski', 'El Cid': 'El Cid', 'Fish Trap': 'Trampa para peces', 'Robin Hood': 'Robin Hood', 'Rabid Wolf': 'Lobo rabioso', 'VMDL': 'VDML ', 'Imperial Camel': 'Camello imperial', 'Buddha Statue A': 'Estatua de Buda A', 'University': 'Universidad', 'Farmer': 'Agricultor', 'Falcon': 'Halcón', 'Aqueduct': 'Acueducto', 'Woad Raider': 'Woad raider', 'Guard Tower': 'Torre de vigilancia', 'Keep': 'Torre de homenaje', 'Bombard Tower': 'Torre bombardeo', 'War Elephant': 'Elefante de guerra', 'Cracks': 'Grietas', 'Osman': 'Osmán', 'Pile of Stone': 'Montón de piedra', 'Longboat': 'Barco dragón', 'Amphitheatre': 'Anfiteatro', 'Pile of Gold': 'Montón de oro', 'Pile of Wood': 'Montón de madera', 'Pile of Food': 'Montón de alimento', 'Colosseum': 'Coliseo', 'Harbor': 'Puerto', 'Centurion': 'Centurión', 'Wonder': 'Maravilla', 'Dead Fish Trap': 'Trampa para peces exhausta', 'Scorpion': 'Escorpión', 'Mangonel': 'Mangonel', 'Throwing Axeman': 'Lanzador de hachas', 'Mameluke': 'Mameluco', 'Cavalier': 'Caballero', 'Tree TD': 'Árbol TD', 'Relic': 'Reliquia', 'Monk with Relic': 'Monje con reliquia', 'British Relic': 'Reliquia inglesa', 'Byzantine Relic': 'Reliquia bizantina', 'Chinese Relic': 'Reliquia china', 'Frankish Relic': 'Reliquia franca', 'Samurai': 'Samurái', 'Gothic Relic': 'Reliquia goda', 'Japanese Relic': 'Reliquia japonesa', 'Persian Relic': 'Reliquia persa', 'Saracen Relic': 'Reliquia sarracena', 'Teutonic Relic': 'Reliquia teutona', 'Turkish Relic': 'Reliquia turca', 'Bandit': 'Bandolero', 'Grass Patch': 'Parcela de Césped', 'Bush': 'Matorral', 'Seagulls': 'Gaviotas', 'Bonfire': 'Hoguera', 'Llama': 'Llama', 'Black Tile': 'Parcela negra', 'Cuauhtemoc': 'Cuauhtémoc', 'Monk with Turkish Relic': 'Monje con reliquia turca', 'Mountain 1': 'Montaña 1', 'Mountain 2': 'Montaña 2', 'Camel': 'Camello', 'Heavy Camel': 'Camello con armad.', 'Trebuchet (Packed}': 'Trebuchet', 'Flowers 1': 'Flores 1', 'Flowers 2': 'Flores 2', 'Flowers 3': 'Flores 3', 'Flowers 4': 'Flores 4', 'Path 4': 'Camino 4', 'Path 1': 'Camino 1', 'Path 2': 'Camino 2', 'Path 3': 'Camino 3', 'Ruins': 'Ruinas', 'Bamboo Forest Tree': 'Bosque de bambúes', 'Oak Forest Tree': 'Bosque de robles', 'Pine Forest Tree': 'Bosque de pinos', 'Palm Forest Tree': 'Bosque de palmeras', 'Army Tent': 'Tienda de las tropas', 'Dead Farm': 'Granja muerta', 'Pikeman': 'Piquero', 'Halberdier': 'Alabardero', 'Nordic Swordsman': 'Espadachín nórdico', 'City Wall': 'Muralla urbana', 'Sea Rocks 1': 'Rocas de mar 1', 'Pagoda': 'Pagoda', 'Sea Rocks 2': 'Rocas de mar 2', 'Sanchi Stupa': 'Estupa de Sanchi', 'Gol Gumbaz': 'Gol Gumbaz', 'Tree A': 'Árbol A', 'Tree B': 'Árbol B', 'Tree C': 'Árbol C', 'Tree D': 'Árbol D', 'Tree E': 'Árbol E', 'Tree F': 'Árbol F', 'Tree G': 'Árbol G', 'Tree H': 'Árbol H', 'Tree I': 'Árbol I', 'Tree J': 'Árbol J', 'Tree K': 'Árbol K', 'Tree L': 'Árbol L', 'Forest Tree': 'Bosque de árboles', 'Snow Pine Tree': 'Pino nevado', 'Jungle Tree': 'Árbol de la selva', 'Stump': 'Tocón', 'Cannon Galleon': 'Galeón artillado', 'Capped Ram': 'Ariete cubierto', 'Charles Martel': 'Carlos Martel', 'Francisco de Orellana': 'Francisco de Orellana', 'Harald Hardraade': 'Harald Hardrade', 'Gonzalo Pizarro': 'Gonzalo Pizarro Alonso', 'Hrolf the Ganger': 'Hrolf el Capataz', 'Frederick Barbarossa': 'Federico Barbarroja', 'Joan the Maid': 'Juana la doncella', 'William Wallace': 'William Wallace', 'King': 'Rey', 'Prithviraj': 'Prithviraj Chauhan', 'Francesco Sforza': 'Francesco Sforza', 'Petard': 'Petardo', 'Hussar': 'Húsar', 'Galleon': 'Galeón', 'Poenari Castle': 'Castillo de Poenari', 'Port': 'Puerto', 'Scout Cavalry': 'Cab. de exploración', 'Great Fish (Marlin}': 'Pez grande (aguja)', 'Fish (Dorado}': 'Pez (dorada)', 'Fish (Salmon}': 'Pez (salmón)', 'Fish (Tuna}': 'Pez (atún)', 'Fish (Snapper}': 'Pez (pargo o huachinango)', 'Loot': 'Botín', 'Two-Handed Swordsman': 'Espad. de mandoble', 'Heavy Cavalry Archer': 'Cab. pesada de arq.', 'Bear': 'Oso', 'Arbalest': 'Arbalesta', 'Advanced Heavy Crossbowman': 'Ballestero pesado avanzado', 'Torch': 'Antorcha', 'Dead pikeman': 'Restos de piquero', 'Demolition Ship': 'Buque de demolición', 'Heavy Demolition Ship': 'Buque dem. pesado', 'Fire Ship': 'Brulote', 'Elite Longbowman': 'Arq. tiro largo élite', 'Elite Throwing Axeman': 'Lanzador hachas élite', 'Fast Fire Ship': 'Brulote rápido', 'Elite Longboat': 'Barco dragón de élite', 'Elite Woad Raider': 'Woad raider de élite', 'Galley': 'Galera', 'Heavy Scorpion': 'Escorpión pesado', 'Transport Ship': 'Barco transporte', 'Dead light cavalry': 'Restos caballería ligera', 'Siege Ram': 'Ariete de asedio', 'Onager': 'Onagro', 'Elite Cataphract': 'Catafracta de élite', 'Elite Teutonic Knight': 'Cab O. Teutónica élite', 'Elite Huskarl': 'Huscarle de élite', 'Elite Mameluke': 'Mameluco de élite', 'Elite Janissary': 'Jenízaro de élite', 'Elite War Elephant': 'Elefante guerra élite', 'Elite Chu Ko Nu': 'Chu ko nu de élite', 'Elite Samurai': 'Samurái de élite', 'Elite Mangudai': 'Mangudai de élite', 'Lumber Camp': 'Campam. maderero', 'Champion': 'Campeón', 'Paladin': 'Paladín', 'Gold Miner': 'Minero de oro', 'Genitour': 'Escaramuzador zenete', 'Mining Camp': 'Campamento minero', 'Siege Onager': 'Onagro de asedio', 'Shepherd': 'Pastor', 'Sheep': 'Oveja', 'Elite Genitour': 'Escaramuzador zenete de élite', 'Outpost': 'Puesto avanzado', 'Cathedral': 'Catedral', 'Flag A': 'Bandera A', 'Flag B': 'Bandera B', 'Flag C': 'Bandera C', 'Flag D': 'Bandera D', 'Flag E': 'Bandera C', 'Bridge A--Top': 'Puente tipo A (principio)', 'Bridge A--Middle': 'Puente tipo A (centro)', 'Bridge A--Bottom': 'Puente tipo A (final)', 'Bridge B--Top': 'Puente tipo B (principio)', 'Bridge B--Middle': 'Puente tipo B (centro)', 'Bridge B--Bottom': 'Puente tipo B (final)', 'Rock 1': 'Roca tipo 1', 'Pavilion': 'Pabellón', 'Joan of Arc': 'Juana de Arco', 'Frankish Paladin': 'Paladín franco', 'Sieur de Metz': 'Señor de Metz', 'Sieur Bertrand': 'Señor Bertrand', 'Temple of Heaven': 'Templo del Cielo', 'Duke DAlençon': 'Duque de Alençon', 'Penguin': 'Pingüino', 'La Hire': 'La Hire', 'Lord de Graville': 'Lord de Graville', 'Jean de Lorrain': 'Jean de Lorena', 'Constable Richemont': 'Condestable Richemont', 'Guy Josselyne': 'Guy Josselyne', 'Jean Bureau': 'Jean Bureau', 'Sir John Fastolf': 'Sir John Fastolf', 'Mosque': 'Mezquita', 'Reynald de Chatillon': 'Reinaldo de Chatillon', 'Master of the Templar': 'Maestre del Temple', 'Bad Neighbor': 'Mal vecino', "God's Own Sling": 'Honda de Dios', 'The Accursed Tower': 'La Torre maldita', 'The Tower of Flies': 'La Torre de las moscas', 'Archers of the Eyes': 'Arqueros de los ojos', 'Piece of the True Cross': 'Pedazo de la Vera Cruz', 'Pyramid': 'Pirámide', 'Dome of the Rock': 'Cúpula de la Roca', 'Elite Cannon Galleon': 'Galeón artillado élite', 'Elite Berserk': 'Berserker de élite', 'Great Pyramid': 'Gran pirámide', 'Subotai': 'Subotai', 'Hunting Wolf': 'Lobo de caza', 'Kushluk': 'Kushluk', 'Shah': 'Sha', 'Cow': 'Vaca', 'Saboteur': 'Saboteador', 'Ornlu the Wolf': 'Ornlu el Lobo', 'Cactus': 'Cactus', 'Skeleton': 'Esqueleto', 'Rugs': 'Alfombras', 'Yurt': 'Yurta', 'Nine Bands': 'Nueve bandas', 'Shipwreck': 'Naufragio', 'Crater': 'Cráter', 'Jaguar Warrior': 'Guerrero jaguar', 'Elite Jaguar Warrior': 'Guerrero jaguar de élite', 'Ice': 'Hielo', "God's Own Sling (Packed}": 'Honda de Dios (desarm.)', 'Bad Neighbor (Packed}': 'Mal vecino (desarmado)', 'Genghis Khan': 'Genghis Khan', 'Emperor in a Barrel': 'Emperador en un tonel', 'Bamboo Stump': 'Tocón de bambú', 'Bridge A--Cracked': 'Puente A--Roto', 'Bridge A--Broken Top': 'Puente A--Roto arriba', 'Bridge A--Broken Bottom': 'Puente A--Roto abajo', 'Bridge B--Cracked': 'Puente B--Roto', 'Bridge B--Broken Top': 'Puente B--Roto arriba', 'Bridge B--Broken Bottom': 'Puente B--Roto abajo', 'Mountain 3': 'Montaña 3', 'Mountain 4': 'Montaña 4', 'Cobra Car': 'Cobra Car', 'Eagle Scout': 'Explorador águila', 'Elite Eagle Warrior': 'Guerrero águila de élite', 'Eagle Warrior': 'Guerrero águila', 'Tarkan': 'Tarcano', 'Elite Tarkan': 'Tarcano de élite', 'Burned building': 'Edificación quemada', 'Plumed Archer': 'Arquero de plumas', 'Elite Plumed Archer': 'Arquero de plumas de élite', 'Conquistador': 'Conquistador', 'Elite Conquistador': 'Conquistador de élite', 'Missionary': 'Misionero', 'Attila the Hun': 'Atila el huno', 'Canoe': 'Piragua', 'Bleda the Hun': 'Bleda el huno', 'Pope Leo I': 'Papa León I', 'Scythian Wild Woman': 'Amazona escita', 'Sea Tower': 'Torre marítima', 'Sea Wall': 'Muralla marítima', 'Palisade Gate': 'Portón de madera', 'Iron Boar': 'Jabalí de hierro', 'Jaguar': 'Jaguar', 'Horse': 'Caballo', 'Macaw': 'Guacamayo', 'Statue': 'Estatua', 'Plant': 'Planta', 'Sign': 'Señal', 'Grave': 'Sepultura', 'Head': 'Cabeza', 'Javelina': 'Jabalina', 'El Cid Campeador': 'El Cid Campeador', 'Amazon Warrior': 'Guerrera amazona', 'Monument': 'Monumento', 'War Wagon': 'Carreta de guerra', 'Elite War Wagon': 'Carreta de guerra de élite', 'Turtle Ship': 'Barco tortuga', 'Elite Turtle Ship': 'Barco tortuga de élite', 'Turkey': 'Pavo', 'Wild Horse': 'Caballo salvaje', 'Map Revealer': 'Mostrador de mapa', 'King Sancho': 'Rey Sancho', 'Rock (Stone}': 'Filón (piedra)', 'King Alfonso': 'Rey Alfonso', 'Rock (Gold}': 'Filón (oro)', 'Imam': 'Imán', 'Admiral Yi Sun-shin': 'Almirante Yi Sun-shin', 'Nobunaga': 'Nobunaga', 'Donkey': 'Burro', 'Henry V': 'Enrique V', 'William the Conqueror': 'Guillermo Conquistador', 'Amazon Archer': 'Arquera amazona', 'ES Flag': 'Bandera ES', 'Scythian Scout': 'Explorador escita', 'Torch (Converting}': 'Antorcha (conversora)', 'Old Stone Head': 'Lápida antigua', 'Roman Ruins': 'Ruinas romanas', 'Hay Stack': 'Almiar', 'Broken Cart': 'Carreta destrozada', 'Flower Bed': 'Arriate', 'Furious the Monkey Boy': 'Hijo del mono feroz', 'Stormy Dog': 'Perro feroz', 'Genoese Crossbowman': 'Genovés ballestero', 'Elite Genoese Crossbowman': 'Genovés ballestero de elite', 'Magyar Huszar': 'Huszár magiar', 'Elite Magyar Huszar': 'Huszár magiar de elite', 'Quimper Cathedral': 'Catedral de Quimper', 'Elephant Archer': 'Elefante arquero', 'Elite Elephant Archer': 'Elefante arquero de elite', 'Boyar': 'Boyardo', 'Elite Boyar': 'Boyardo de elite', 'Kamayuk': 'Kamayuk', 'Elite Kamayuk': 'Kamayuk de elite', 'Wild Camel': 'Camello salvaje', 'Siege Tower': 'Torre de asedio', 'Heavy Pikeman': 'Piquero pesado', 'Eastern Swordsman': 'Espadachín oriental', 'Waterfall': 'Caída de agua', 'Camel (Gaia}': 'Camello (Gaia)', 'Arch of Constantine': 'Arco de Constantino', 'Rain': 'LLuvia', 'Flag F': 'Bandera F', 'Smoke': 'Humo', 'Wooden Bridge A--Top': 'Puente mad. A (Principio)', 'Wooden Bridge A--Middle': 'Puente madera A (Centro)', 'Wooden Bridge A--Bottom': 'Puente madera A (Final)', 'Wooden Bridge B--Top': 'Puente mad. B (Principio)', 'Wooden Bridge B--Middle': 'Puente madera B (Centro)', 'Wooden Bridge B--Bottom': 'Puente madera B (Final)', 'Impaled Corpse': 'Occiso empalado', 'Quarry': 'Yacimiento', 'Lumber': 'Leños', 'Goods': 'Mercancías', 'Vulture': 'Buitre', 'Rock 2': 'Roca tipo 2', 'Queen': 'Reina', 'Sanyogita': 'Sanyogita', 'Prithvi': 'Prithvi', 'Chand Bhai': 'Chand Bhai', 'Saladin': 'Saladino', 'Khosrau': 'Rey Cosroes I', 'Jarl': 'Jarl', 'Savaran': 'Savarano', 'Barrels': 'Barriles', 'Alfred the Alpaca': 'Alfred la alpaca', 'Elephant': 'Elefante salvaje', 'Dragon Ship': 'Bote dragón', 'Flame 1': 'Llama 1', 'Flame 2': 'Llama 2', 'Flame 3': 'Llama 3', 'Flame 4': 'Llama 4', 'Organ Gun': 'Cañón de salvas', 'Elite Organ Gun': 'Cañón de salvas de élite', 'Caravel': 'Carabela', 'Elite Caravel': 'Carabela de élite', 'Camel Archer': 'Camello arquero', 'Elite Camel Archer': 'Camello arquero de élite', 'Gbeto': 'Guardiana gbeto', 'Elite Gbeto': 'Guardiana gbeto de élite', 'Shotel Warrior': 'Shotelai', 'Elite Shotel Warrior': 'Shotelai de élite', 'Zebra': 'Cebra', 'Feitoria': 'Factoría', 'Priest': 'Sacerdote', 'Ostrich': 'Avestruz', 'Stork': 'Cigüeña', 'Lion': 'León', 'Crocodile': 'Cocodrilo', 'Savannah Grass Patch': 'Parc. césped de sabana', 'Musa ibn Nusayr': 'Musa Ibn Nusair', 'Sundjata': 'Sundiata', 'Tariq ibn Ziyad': 'Tariq Ibn Ziyad', 'Richard de Clare': 'Ricardo de Clare', 'Tristan': 'Tristán', 'Princess Yodit': 'Princesa Judith', 'Henry II': 'Enrique II Plantagenet', 'Mountain 5': 'Montaña 5', 'Mountain 6': 'Montaña 6', 'Mountain 7': 'Montaña 7', 'Mountain 8': 'Montaña 8', 'Snow Mountain 1': 'Montaña nevada 1', 'Snow Mountain 2': 'Montaña nevada 2', 'Snow Mountain 3': 'Montaña nevada 3', 'Rock Formation 1': 'Formación rocosa 1', 'Rock Formation 2': 'Formación rocosa 2', 'Rock Formation 3': 'Formación rocosa 3', 'Dragon Tree': 'Árbol dragón', 'Baobab Tree': 'Baobab', 'Bush 2': 'Arbusto 2', 'Bush 3': 'Arbusto 3', 'Fruit Bush': 'Arbusto de drupas', 'Goat': 'Cabra', 'Fence': 'Cerco', 'Acacia Tree': 'Acacia', 'Yekuno Amlak': 'Yekuno Amlak', 'Yodit': 'Judith', 'Itzcoatl': 'Itzcoátl', 'Mustafa Pasha': 'Mustafá Pasha', 'Pacal II': 'Pakal el Grande', 'Babur': 'Babur', 'Abraha Elephant': 'Elefante de Abraha', 'Guglielmo Embriaco': 'Guillermo Embriaco', 'Su Dingfang': 'Su Dingfang', 'Pachacuti': 'Pachacútec', 'Huayna Capac': 'Huayna Cápac', 'Miklos Toldi': 'Nicolás Toldi', 'Little John': 'Pequeño Juan', 'Zawisza the Black': 'Zawisza Czarny', 'Sumanguru': 'Sumanguru', 'Storage': 'Depósito', 'Hut': 'Cabaña" //   xx check in the Scenario Editor if this is the same building as [64038 "cabaña"] present in "key-value-strings-utf8.txt", and if not, use a different building name for string 522', 'Granary': 'Granero', 'Barricade': 'Barricada', 'Animal skeleton': 'Esqueleto animal', 'Stelae A': 'Estelas A', 'Stelae B': 'Estelas B', 'Stelae C': 'Estelas C', 'Gallow': 'Horca', 'Palace': 'Palacio', 'Tent': 'Tienda de camp.', 'Sea Fortification': 'Fortificación marítima', 'Fire Galley': 'Galeota incendiaria', 'Demolition Raft': 'Balsa de demolición', 'Dagnajan': 'Dagnaján', 'Gidajan': 'Gidaján', 'Ballista Elephant': 'Elefante con balista', 'Elite Ballista Elephant': 'Elefante con balista de élite', 'Karambit Warrior': 'Recluta con karambit', 'Elite Karambit Warrior': 'Recluta con karambit de élite', 'Arambai': 'Arambai', 'Elite Arambai': 'Arambai de élite', 'Rattan Archer': 'Arquero de ratán', 'Elite Rattan Archer': 'Arquero de ratán de élite', 'Battle Elephant': 'Elefante de combate', 'Elite Battle Elephant': 'Elefante de combate de élite', 'Komodo Dragon': 'Dragón de Komodo', 'Tiger': 'Tigre', 'Rhinoceros': 'Rinoceronte', 'Box Turtles': 'Tortugas de caja" //  xx tortuga de caja indochina o vietnamit', 'Water Buffalo': 'Búfalo de agua', 'Mangrove Tree': 'Árbol de manglar', 'Rainforest Tree': 'Árbol de la jungla', 'Rock (Beach}': 'Roca (playa)', 'Rock (Jungle}': 'Roca (selva)', 'Flag G': 'Bandera G', 'Flag H': 'Bandera H', 'Flag I': 'Bandera I', 'Flag J': 'Bandera J', 'Imperial Skirmisher': 'Guerrillero imperial', 'Gajah Mada': 'Gayamada', 'Jayanegara': 'Jayanegara', 'Raden Wijaya': 'Raden Wijaya', 'Sunda Royal Fighter': 'Combatiente real sondanés', 'Suryavarman I': 'Suryavarmán I', 'Udayadityavarman I': 'Udayadityavarmán I', 'Jayaviravarman': 'Jayaviravarmán', 'Bayinnaung': 'Bayinnaung', 'Tabinshwehti': 'Tabinshwehti', 'Buddha Statue B': 'Estatua de Buda B', 'Buddha Statue C': 'Estatua de Buda C', 'Buddha Statue D': 'Estatua de Buda D', 'Fern Patch': 'Parcela de helechos', 'Trowulan Gate': 'Puerta de Trowulan', 'Vases': 'Jarrones" //  xx check in-gam', 'Le Loi': 'Le Loi', 'Le Lai': 'Le Lai', 'Le Trien': 'Le Trien', 'Luu Nhan Chu': 'Luu Nhan Chu', 'Bui Bi': 'Bui Bi', 'Dinh Le': 'Dinh Le', 'Wang Tong': 'Wang Tong', 'Envoy': 'Emisario" //  xx chequear que no sea el \'enviado diplomático\' que visitó a Rajendra Chol', 'Rice Farm': 'Arrozal" //  xx aternatively: \'Granja de arroz', 'Dead Rice Farm': 'Arrozal muerto', 'Bridge C--Top': 'Puente tipo C (principio)', 'Bridge C--Middle': 'Puente tipo C (centro)', 'Bridge C--Bottom': 'Puente tipo C (final)', 'Bridge D--Top': 'Puente tipo D (principio)', 'Bridge D--Middle': 'Puente tipo D (centro)', 'Bridge D--Bottom': 'Puente tipo D (final)', 'Bridge C--Cracked': 'Puente C--Roto', 'Bridge C--Broken Top': 'Puente C--Roto arriba', 'Bridge C--Broken Bottom': 'Puente C--Roto abajo', 'Bridge D--Cracked': 'Puente D--Roto', 'Bridge D--Broken Top': 'Puente D--Roto arriba', 'Bridge D--Broken Bottom': 'Puente D--Roto abajo', 'Sharkatzor': 'Tiburogatito volador" //  xx Sharkatzor: \'gatiburón\', \'escualofelino\', \'tiburogatito volador\', \'tiburogatito demoledor\', \'tiburogatito voraz'}, 'researches': {'Elite Tarkan': 'Tarcano de élite', 'Yeomen': 'Voluntarios de caballería', 'El Dorado': 'El Dorado', 'Furor Celtica': 'Furor celta', 'Drill': 'Instrucción militar', 'Mahouts': 'Cornacas', 'Town Watch': 'Guardia urbana', 'Zealotry': 'Fanatismo', 'Artillery': 'Artillería', 'Crenellations': 'Almenas', 'Crop Rotation': 'Rotación de cultivos', 'Heavy Plow': 'Arado pesado', 'Horse Collar': 'Collera', 'Guilds': 'Gremios', 'Anarchy': 'Anarquía', 'Banking': 'Banca', 'Cartography': 'Cartografía', 'Atheism': 'Ateísmo', 'Loom': 'Telar', 'Coinage': 'Acuñación', 'Garland Wars': 'Guerras florales', 'Elite Plumed Archer': 'Arquero de plumas de élite', 'War Galley': 'Galera de guerra', 'Galleon': 'Galeón', 'Cannon Galleon': 'Galeón artillado', 'Husbandry': 'Ganadería', 'Faith': 'Fe', 'Chemistry': 'Química', 'Caravan': 'Caravana', 'Berserkergang': 'Trance frenético', 'Masonry': 'Albañilería', 'Architecture': 'Arquitectura', 'Rocketry': 'Cohetería', 'Treadmill Crane': 'Grúa', 'Gold Mining': 'Minería aurífera', 'Kataparuto': 'Kataparuto', 'Elite Conquistador': 'Conquistador de élite', 'Logistica': 'Logística', 'Keep': 'Torre del homenaje', 'Bombard Tower': 'Torre de bombardeo', 'Gillnets': 'Red agallera', 'Forging': 'Forja', 'Iron Casting': 'Fundición de hierro', 'Scale Mail Armor': 'Armadura de láminas', 'Blast Furnace': 'Alto horno', 'Chain Mail Armor': 'Arm. cota de malla', 'Plate Mail Armor': 'Arm. placas malla', 'Plate Barding Armor': 'Arm. placas caball.', 'Scale Barding Armor': 'Arm. láminas caball.', 'Chain Barding Armor': 'Cota malla caball.', 'Bearded Axe': 'Hacha de arista', 'Hand Cannon': 'Cañón manual', 'Tracking': 'Rastreo', 'Ballistics': 'Balística', 'Scorpion': 'Escorpión', 'Capped Ram': 'Ariete cubierto', 'Elite Skirmisher': 'Guerrillero de élite', 'Crossbowman': 'Ballestero', 'Feudal Age': 'Edad Feudal', 'Castle Age': 'Edad de los Castillos', 'Imperial Age': 'Edad Imperial', 'Dark Age': 'Alta Edad Media', 'Guard Tower': 'Torre de vigilancia', 'Gold Shaft Mining': 'Pozo minero aurífero', 'Bombard Cannon': 'Cañón de asedio', 'Fortified Wall': 'Muralla fortificada', 'Pikeman': 'Piquero', 'Fletching': 'Emplumado de flechas', 'Bodkin Arrow': 'Flecha de punzón', 'Bracer': 'Brazalete de cuero', 'Double-Bit Axe': 'Hacha de doble filo', 'Bow Saw': 'Sierra de arco', 'Long Swordsman': 'Espad. espada larga', 'Cavalier': 'Caballero', 'Padded Archer Armor': 'Arm. acolchada arq.', 'Leather Archer Armor': 'Arm. cuero arqueros', 'Wheelbarrow': 'Carretilla', 'Squires': 'Escuderos', 'Two-Handed Swordsman': 'Espad. de mandoble', 'Heavy Cav Archer': 'Cab. pesada de arq.', 'Ring Archer Armor': 'Arm. anillos arqueros', 'Two-Man Saw': 'Sierra a dos', 'Man-at-Arms': 'Hombre de armas', 'Block Printing': 'Letras de imprenta', 'Sanctity': 'Santidad', 'Illumination': 'Iluminación', 'Heavy Camel': 'Camello con armad.', 'Arbalest': 'Arbalesta', 'Heavy Scorpion': 'Escorpión pesado', 'Heavy Demolition Ship': 'Buque de dem. pesado', 'Fast Fire Ship': 'Brulote rápido', 'Hand Cart': 'Carro de mano', 'Fervor': 'Fervor', 'Light Cavalry': 'Caballería ligera', 'Siege Ram': 'Ariete de asedio', 'Onager': 'Onagro', 'Maghrabi Camels': 'Dromedarios magrebíes', 'Farimba': 'Farimba', 'Champion': 'Campeón', 'Paladin': 'Paladín', 'Stone Mining': 'Explotac. de canteras', 'Stone Shaft Mining': 'Pozo de cantera', 'Town Patrol': 'Patrulla urbana', 'Tusk Swords': 'Colmillos de acero', 'Double Crossbow': 'Ballesta doble', 'Forced Levy': 'Leva en masa', 'Paper Money': 'Papel moneda', 'Elite Rattan Archer': 'Arquero de ratán de élite', 'Conscription': 'Leva', 'Redemption': 'Redención', 'Atonement': 'Expiación', 'Siege Onager': 'Onagro de asedio', 'Sappers': 'Zapadores', 'Murder Holes': 'Matacanes', 'Elite Longbowman': 'Arq. tiro largo élite', 'Elite Cataphract': 'Catafracta de élite', 'Elite Chu Ko Nu': 'Chu ko nu de élite', 'Elite Throwing Axeman': 'Lanzador hachas élite', 'Elite Teutonic Knight': 'Cab O. Teutónica élite', 'Elite Huskarl': 'Huscarle de élite', 'Elite Samurai': 'Samurái de élite', 'Elite War Elephant': 'Elefante guerra élite', 'Elite Mameluke': 'Mameluco de élite', 'Elite Janissary': 'Jenízaro de élite', 'Elite Woad Raider': 'Woad raider de élite', 'Elite Mangudai': 'Mangudai de élite', 'Elite Longboat': 'Barco dragón de élite', 'Shipwright': 'Carpintero naval', 'Careening': 'Carenado', 'Dry Dock': 'Dique seco', 'Elite Cannon Galleon': 'Galeón artillado élite', 'Siege Engineers': 'Ingenieros de asedio', 'Hoardings': 'Ladronera', 'Heated Shot': 'Bala roja', 'Eagle Warrior': 'Guerrero águila', 'Elite Berserk': 'Berserker de élite', 'Spies/Treason': 'Espionaje y traición', 'Hussar': 'Húsar', 'Halberdier': 'Alabardero', 'Elite Jaguar Warrior': 'Guerrero jaguar de élite', 'Elite Eagle Warrior': 'Guerrero águila de élite', 'Bloodlines': 'Pureza de sangre', 'Parthian Tactics': 'Tácticas de los partos', 'Thumb Ring': 'Dactilera', 'Theocracy': 'Teocracia', 'Heresy': 'Herejía', 'Supremacy': 'Supremacía', 'Herbal Medicine': 'Hierbas medicinales', 'Shinkichon': 'Shinkichon', 'Elite Turtle Ship': 'Barco tortuga de élite', 'Elite War Wagon': 'Carreta de guerra de élite', 'Perfusion': 'Movilización', 'Atlatl': 'Átlatl', 'Warwolf': 'Warwolf', 'Great Wall': 'Gran Muralla', 'Chieftains': 'Hérsires', 'Greek Fire': 'Fuego griego', 'Elite Genoese Crossbowman': 'Genovés ballestero de elite', 'Elite Magyar Huszar': 'Huszár magiar de elite', 'Elite Elephant Archer': 'Elefante arquero de elite', 'Stronghold': 'Bastión', 'Marauders': 'Razias', 'Yasama': 'Yasama', 'Obsidian Arrows': 'Saeta de obsidiana', 'Panokseon': 'Panokseon', 'Nomads': 'Nómades', 'Boiling Oil': 'Barbacana', 'Ironclad': 'Blindaje', 'Madrasah': 'Madraza', 'Sipahi': 'Sipahi', 'Inquisition': 'Inquisición', 'Chivalry': 'Código caballeresco', 'Pavise': 'Escudo pavés', 'Silk Road': 'Ruta de la Seda', 'Elite Boyar': 'Boyardo de elite', 'Sultans': 'Sultanato', 'Shatagni': 'Shatagni', 'Elite Kamayuk': 'Kamayuk de elite', 'Orthodoxy': 'Ortodoxia', 'Druzhina': 'Druzhina', 'Mercenaries': 'Mercenarios', 'Recurve Bow': 'Arco recurvo', 'Andean Sling': 'Huaracas', 'Couriers': 'Postas', 'Imperial Camel': 'Camello imperial', 'Revetments': 'Revestimiento', 'Hunting Dogs': 'Perros de caza', 'Fire Tower': 'Torre lanzallamas', 'Britons': 'Ingleses', 'Franks': 'Francos', 'Goths': 'Godos', 'Teutons': 'Teutones', 'Japanese': 'Japoneses', 'Chinese': 'Chinos', 'Byzantines': 'Bizantinos', 'Persians': 'Persas', 'Saracens': 'Sarracenos', 'Turks': 'Turcos', 'Vikings': 'Vikingos', 'Mongols': 'Mongoles', 'Celts': 'Celtas', 'Spanish': 'Españoles', 'Aztecs': 'Aztecas', 'Mayans': 'Mayas', 'Huns': 'Hunos', 'Koreans': 'Coreanos', 'Italians': 'Italianos', 'Indians': 'Indios', 'Incas': 'Incas', 'Magyars': 'Magiares', 'Slavs': 'Eslavos', 'Enable Sheep': 'Desbloquear ovejas', 'Enable Llamas': 'Desbloquear llamas', 'Enable Cows': 'Desbloquear vacas', 'Enable Turkeys': 'Desbloquear pavos', 'Elite Organ Gun': 'Cañón de salvas de élite', 'Elite Camel Archer': 'Camello arquero de élite', 'Elite Gbeto': 'Guardiana gbeto de élite', 'Elite Shotel Warrior': 'Shotelai de élite', 'Carrack': 'Carracas', 'Arquebus': 'Arcabuz', 'Royal Heirs': 'Centralización', 'Torsion Engines': 'Mecanismos de torsión', 'Tigui': 'Gran asamblea', 'Kasbah': 'Alcazabas', 'Portuguese': 'Portugueses', 'Ethiopians': 'Etíopes', 'Malians': 'Malíes', 'Berbers': 'Bereberes', 'Elite Caravel': 'Carabela de élite', 'Elite Genitour': 'Escaram. zenete de élite', 'Free Cartography': 'Cartografía gratis', 'Arson': 'Incendiarismo', 'Arrowslits': 'Aspillera en cruz', 'Elite Ballista Elephant': 'Elefante con balista de élite', 'Elite Karambit Warrior': 'Recluta con karambit de élite', 'Elite Arambai': 'Arambai de élite', 'Thalassocracy': 'Talasocracia', 'Howdah': 'Howdah', 'Manipur Cavalry': 'Caballería manipur', 'Chatras': 'Chatras" //  xx check late', 'Elite Battle Elephant': 'Elefante de combate de élite', 'Khmer': 'Jemeres', 'Malay': 'Malayos', 'Burmese': 'Birmanos', 'Vietnamese': 'Vietnamitas', 'Imperial Skirmisher': 'Guerrillero imperial', 'Set maximum population (no Houses}': 'Elegir población máxima (sin casas)', 'Disable Vietnamese Vision': 'Deshab. visión vietnamita del enemigo'}}