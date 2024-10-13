"""
La instruccion para este ejercicio es:

* Crear un programa/juego que elija una palabra secreta.
* Muestra en pantalla una serie de guiones en lugar de letras.
* El jugador elige una letra.
    - Si la letra esta en la palabra, pone en cada lugar correcto.
    - Si no esta en la palabra, pierde una vida.
* El jugador inicia con 6 vidas.
* Si se agotan las vidas y no adivina la palabra, el jugador pierde.
* Pero si adivina la palabra completa antes, entonces gana.
"""
from random import choice


# ELEGIR PALABRA
palabras_adivinar = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard',
                     'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree',
                     'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata',
                     'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Seel', 'Dewgong',
                     'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix',
                     'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute',
                     'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung',
                     'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan',
                     'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'MrMime', 'Scyther',
                     'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados',
                     'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte',
                     'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos',
                     'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew']


# MAPEO EN BLANCO
vidas = 6
ganador = False

pkmn_adivinar = choice(palabras_adivinar).upper()
adivinando = list('_' * len(pkmn_adivinar))
x_adivinar = list(pkmn_adivinar)
usadas = set()

print(f'Hoy toca adivinar un Pokémon de {len(x_adivinar)} letras \n')
print(adivinando)


# REVISION
def revision():
    global vidas, ganador
    letra = input('\nElige una letra o adivina el Pokémon:  ').upper()
    if list(letra) == x_adivinar:
        ganador = True

    else:
        contador = 0
        error = True
        while contador != len(x_adivinar):
            for x in x_adivinar:
                if x == letra:
                    adivinando[contador] = letra
                    contador += 1
                    error = False
                else:
                    usadas.add(letra)
                    contador += 1
            if error:
                vidas -= 1
        return adivinando


# CHEQUEOS
while vidas > 0 and not ganador:
    revision()
    print(adivinando)
    print(f'\nHas usado: {usadas} y te quedan {vidas} intentos.')

    if adivinando == x_adivinar:
        ganador = True
        print(f'Has acertado, el Pokémon secreto era {pkmn_adivinar}')
