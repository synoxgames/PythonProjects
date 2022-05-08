import random
import os
import time
import sys
from math import ceil as r

# Colours
colour = {
    'red' : '\033[31m',
    'green' : '\033[32m',
    'yellow' : '\033[33m',
    'blue' : '\033[34m',
    'reset' : '\033[m'
}

# This is the Pokemon Class. It holds the information about the base Pokemon.
class Pokemon():
    def __init__(self, name, health, weakness, _type):
        self.name = name
        self.health = health
        self.weakness = weakness
        self.pType = _type
        self.currentState = 1
        self.deffectTimer = 0

        self.state = {
            1 : 'Normal',
            2 : 'Stunned',
            3 : 'Poisioned'}
            

# This class will turn lists into printable lists.
class PrintDict():
    def Names(self, pokemon):
        pL = len(pokemon)
        charSelect = ""
        
        for i in range(pL):
            currentIndex = (i + 1)
            stringToAdd = str(currentIndex)+". "+pokemon[i].name+"\n"
            charSelect += stringToAdd

        print(charSelect)

    def Attacks(self, attackList):
        aL = len(attackList)
        attackStr = ""

        for i in range(aL):
            attack = attackList[i]
            strIndex = i + 1

            string = (str(strIndex)+". "+attack['name']+"\n")
            attackStr += string

        print(attackStr)

class Text():
    def Type(self, inputString, delay):
        for char in inputString:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)


# This will be the base for attacks.
class AttackBase():
    def GetAttack(self, attackName, attackDamage, hitChance, hitType):
        self.name = attackName
        self.damage = attackDamage
        self.chance = hitChance
        self.type = hitType
        attack = { 'name' : self.name,
                   'damage' : self.damage,
                   'chance' : self.chance,
                   'type' : self.type}
        return attack

# Add Different Attack Types Here!
class Attacks():
    def AttackReturn(self, _type):
        # This is the Type's and Attack Types { 'TYPE' : TypeFuntion() }
        returnTypes = {
            'electric' : Attacks().Thunder(),
            'fire' : Attacks().Fire(),
            'water' : Attacks().Water(),
            'plant' : Attacks().Plant(),
            'spirit' : Attacks().Spirit(),
            'rogue' : Attacks().Rogue()}

        attacks = returnTypes[_type.lower()]
        return attacks

    # This is where you will add Thunder attacks [AttackBase().GetAttack(NAME, DAMAGE, CHANCE, TYPE)"]
    def Thunder(self):
        tAttacks = [AttackBase().GetAttack("Tail Whip", 15, 83, 1),
                    AttackBase().GetAttack("Lightning Shock", 20, 68, 1),
                    AttackBase().GetAttack("Growl", 10, 95, 2),
                    AttackBase().GetAttack("Thunder Clap", 17, 72, 1),
                    AttackBase().GetAttack("Static Charge", 10, 92, 3),
                    AttackBase().GetAttack("Thunder Strike - Ultimate", 95, 10, 1)]
        return tAttacks

    def Fire(self):
        fAttacks = [AttackBase().GetAttack("Air Slash", 10, 95, 1),
                    AttackBase().GetAttack("Dragon Claw", 20, 60, 1),
                    AttackBase().GetAttack("Ember", 15, 75, 1),
                    AttackBase().GetAttack("Heat Wave", 17, 70, 2),
                    AttackBase().GetAttack("Fire Breath", 10, 92, 3),
                    AttackBase().GetAttack("Magma Breath - Ultimate", 90, 12, 1)]
        return fAttacks

    def Water(self):
        wAttacks = [AttackBase().GetAttack("Wave Splash", 10, 90, 1),
                    AttackBase().GetAttack("Tidal Slap", 20, 65, 2),
                    AttackBase().GetAttack("Rain Down", 15, 80, 3),
                    AttackBase().GetAttack("Water Flood", 25, 70, 1),
                    AttackBase().GetAttack("Tsunami Slamdown - Ultimate", 92, 11, 1)]
        return wAttacks

    def Plant(self):
        pAttacks = [AttackBase().GetAttack("Thorn Slash", 15, 85, 1),
                    AttackBase().GetAttack("Vine Whip", 20, 68, 1),
                    AttackBase().GetAttack("Pine Sweep", 10, 90, 2),
                    AttackBase().GetAttack("Leaf Slap", 22, 65, 1),
                    AttackBase().GetAttack("Thorn Prick", 12, 92, 3),
                    AttackBase().GetAttack("Forest Slam - Ultimate", 85, 15, 1)]
        return pAttacks

    def Spirit(self):
        sAttacks = [AttackBase().GetAttack("Phantom Whip", 15, 90, 1),
                    AttackBase().GetAttack("Possession", 10, 80, 3),
                    AttackBase().GetAttack("Hellfire", 20, 70, 1),
                    AttackBase().GetAttack("Ghost Eyes", 10, 90, 2),
                    AttackBase().GetAttack("Spirit Chill", 20, 70, 1),
                    AttackBase().GetAttack("Heart Attack - Ultimate", 200, 8, 1)]
        return sAttacks

    def Rogue(self):
        rAttacks = [AttackBase().GetAttack("Sucker Punch", 20, 70, 2),
                    AttackBase().GetAttack("Blade Swing", 15, 90, 1),
                    AttackBase().GetAttack("Infected Arrow", 30, 70, 3),
                    AttackBase().GetAttack("Dick Slap", 40, 60, 2),
                    AttackBase().GetAttack("Thunder Kick", 10, 95, 1),
                    AttackBase().GetAttack("Decaptation - Ultimate", 200, 5, 1)]

        return rAttacks
        

# Add New Enemy Pokemon Here! [Pokemon(NAME, HEALTH, WEAK, TYPE)]
class GetRandomPokemon():
    def Find(self):
        pokemon = [Pokemon("Magikarp", 100, "Electric", "Water"),
                   Pokemon("Bulbasaur", 100, "Fire", "Plant"),
                   Pokemon("Charmander", 100, "Water", "Fire"),
                   Pokemon("Raichu", 100, "Plant", "Electric"),
                   Pokemon("Giggler", 100, "Electric", "Spirit"),
                   Pokemon("The Evil Trainer - Boss", 200, "Spirit", "Rogue"),
                   Pokemon("The Devil - Boss", 200, "Electric", "Spirit"),
                   Pokemon("Joker - Boss", 300, "Fire", "Rogue")]

        pokemonGot = pokemon[random.randint(0, len(pokemon)-1)]
        return pokemonGot

# This is where the beginning stages take place.
class StartGame():
    def Begin(self):
        global colour
        title =("""
              _                              
  _ __   ___ | | _____ _ __ ___   ___  _ __  
 | '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ 
 | |_) | (_) |   <  __/ | | | | | (_) | | | |
 | .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|
 |_|                                         
 |_|

                Synox Games
____________________________________________________________
\n""")
        Text().Type(title, 0)
        print("Welcome to our very first battle of the day!"\
              +"\nOur first contestants are rearing to go"\
              +" so lets let them battle!")
        input("\nPlease Press Enter...")

        StartGame().PickGame()


    def PickGame(self):
        os.system('cls')
        print("Pick a Game Mode!\n\n1. Single Player!\n2. Multiplayer")

        while True:
            choice = input("\nI choose: ")
            try:
                choice = int(choice)
                if (choice < 0):
                    print("That's not an option!")
                elif (choice > 2):
                    print("That's not an option!")

                if (choice == 1):
                    StartGame().SelectCharacter(False)
                elif (choice == 2):
                    playerOne = StartGame().SelectCharacter(True)
                    playerTwo = StartGame().SelectCharacter(True)
                    os.system('cls')
                    print("Player One: {}\nPlayer Two: {}\n\nAre you ready?".format(playerOne.name, playerTwo.name))
                    input("\nPlease Press Enter...")
                    break
            except ValueError:
                print("That's not even a number!")

        
        MainGame(playerOne, playerTwo).Multiplayer()

    # Add New Pokemon Here [Pokemon(NAME, HEALTH, WEAK, TYPE)]
    def SelectCharacter(self, isMultiplayer):
        os.system('cls')

        print("""
 _____  _                               _              
/  __ \| |                             | |             
| /  \/| |__    __ _  _ __  __ _   ___ | |_  ___  _ __ 
| |    | '_ \  / _` || '__|/ _` | / __|| __|/ _ \| '__|
| \__/\| | | || (_| || |  | (_| || (__ | |_|  __/| |   
 \____/|_| |_| \__,_||_|   \__,_| \___| \__|\___||_|   
            _____        _              _              
           /  ___|      | |            | |             
           \ `--.   ___ | |  ___   ___ | |_            
            `--. \ / _ \| | / _ \ / __|| __|           
           /\__/ /|  __/| ||  __/| (__ | |_            
           \____/  \___||_| \___| \___| \__|
____________________________________________________________________
\n""")
        
        pokemon = [Pokemon("Pikachu", 100, "Plant", "Electric"),
                   Pokemon("Charizard", 100, "Water", "Fire"),
                   Pokemon("Gyarados", 100, "Electric", "Water"),
                   Pokemon("Squirtle", 100, "Electric", "Water"),
                   Pokemon("Emboar", 100, "Water", "Fire"),
                   Pokemon("Haunted", 100, "Electric", "Spirit"),
                   Pokemon("Swordsman Steve", 100, "Spirit", "Rogue")]

        PrintDict().Names(pokemon)

        pL = len(pokemon)

        while True:
            choice = input("Choose Your Pokemon!: ")
            chosen = []

            try:
                choice = int(choice)

                if (choice > pL):
                    print("\n")
                elif (choice <= 0):
                    print("\n")
                elif (choice > 0 and choice <= pL):
                    chosen = pokemon[choice - 1]
                    break
                
            except ValueError:
                print("\n")

        os.system('cls')
        print("You chose "+chosen.name)
        input("\nPlease Press Enter...")

        if (isMultiplayer == False):
            eP = GetRandomPokemon().Find()

            os.system('cls')
            print("Your Oppenent has summoned {}!\n".format(eP.name))
            input("Please Press Enter...")

            MainGame(chosen, eP).Game()
        elif (isMultiplayer == True):
            return chosen

class AttackEnemy():
    global colour
    def DealDamage(self, attackerPokemon, attack, pokemonAttacked):
        damToDeal = attack['damage']
        aType = attack['type']
        typeBonus = False
        missed = False
        appliedEffect = False

        i = random.randint(0,100)
        z = random.randint(0,4)
        missed = (i > attack['chance'])
        
        if (missed == False):
            damageMod = random.randint(int(attack['damage'] / 2), attack['damage'])
            damageMod = damageMod / attack['damage']

            damToDeal = damToDeal * damageMod
            damToDeal = int(damToDeal)

            if (attackerPokemon.pType == pokemonAttacked.weakness):
                damToDeal *= 1.25
                damToDeal = int(damToDeal)
                typeBonus = True

            if (z <= 1 and aType != 1):
                if (pokemonAttacked.currentState == 1):
                    appliedEffect = True
                    pokemonAttacked.currentState = aType
                    pokemonAttacked.deffectTimer = 3

            pokemonAttacked.health -= damToDeal
            dam = colour['red']+str(damToDeal)+colour['reset']
            print(attackerPokemon.name,"Used",attack['name'],"On "\
                  +pokemonAttacked.name,"Dealing",dam,"damage!\n")

            if (typeBonus == True):
                print("It was super effective!\n")
            if (appliedEffect == True):
                print("{} has been {}!\n".format(pokemonAttacked.name, pokemonAttacked.state[aType]))

        else:
            print("{} Tried to Use {} on {} but Missed!\n".format(attackerPokemon.name,attack['name'],pokemonAttacked.name))

        input("Press Enter to Continue...")
        os.system('cls')

    def Effect(self, pokemon, turn):
        if (pokemon.deffectTimer < 1):
            print("{} has come to their senses and is no longer {}!".format(pokemon.name, pokemon.state[pokemon.currentState]))
            pokemon.currentState = 1
            input("\nPlease Press Enter...")
            os.system('cls')

        pokemon.deffectTimer -= 1

        if (pokemon.currentState == 2):
            failChance = random.randint(0,4)
            if (failChance <= 1):
                print("{} is too {}Stunned{} to attack!".format(pokemon.name, colour['yellow'], colour['reset']))
                input("Please Press Enter...")
                os.system('cls')

                return True
            
        if (pokemon.currentState == 3):
            print("{} has been {}poisioned!{} They took 5 damage!\n".format(pokemon.name, colour['green'], colour['reset']))
            pokemon.health -= 5
            input("Please Press Enter...")
            os.system('cls')


        return False

class HealthUI():
    def __init__(self, pokeOne, pokeTwo):
        self.p1 = pokeOne
        self.p2 = pokeTwo
        self.p1State = pokeOne.state[pokeOne.currentState]
        self.p2State = pokeTwo.state[pokeTwo.currentState]

    def Display(self):
        healthBar = "_"
        baseGapX = 8
        baseGapY = 20 + baseGapX
        finalDistance = baseGapY - r(self.p1.health / 5)
        gap = " " * r(finalDistance)
        global colour
        string0 = ("{}{}|{}{}".format(self.p1.name,(" ")*10 ,(" ") * 10, self.p2.name))
        string2 = ("_" *len(string0))
        string3 = ("{}HP: {}{}HP: {}{}".format(colour['red'],self.p1.health,(" ")*21,self.p2.health,colour['reset']))
        healthLines = colour['green']+healthBar * r((self.p1.health / 5)) + gap + healthBar * int((self.p2.health / 5))+colour['reset']
        string4 = ("Status: {}{}Status: {}\n".format(self.p1State,(" ")*(8+len(self.p1State)),self.p2State))

        print(string0)
        print(string2)
        print(string3)
        print(healthLines)
        print(string4)

#This is where the main game takes place.
class MainGame():
    def __init__(self, playerPokemon, enemyPokemon):
        self.playerP = playerPokemon
        self.pAttacks = Attacks().AttackReturn(playerPokemon.pType)
        self.enemyP = enemyPokemon
        self.enemyAttack = Attacks().AttackReturn(enemyPokemon.pType)


    def Multiplayer(self):
        os.system('cls')
        gameFinished = False
        currentTurn = 1
        attackL = len(self.pAttacks)
        eAttackL = len(self.enemyAttack)
        winner = None
        loser = None
        winP = 0

        while gameFinished == False:
            End().CheckGameOver(self.playerP, self.enemyP)
            if (currentTurn == 1):

                if (self.playerP.currentState > 1):
                    skip = AttackEnemy().Effect(self.playerP, currentTurn)

                    if (skip == True):
                        currentTurn = 2

                if (currentTurn == 1):
                    End().CheckGameOver(self.playerP, self.enemyP)
                    print("Player One! You're Up!\n")
                    HealthUI(self.playerP, self.enemyP).Display()
                    PrintDict().Attacks(self.pAttacks)
                    attack = input("> ")

                    try:
                        attack = int(attack)

                        if (attack > attackL or attack <= 0):
                            os.system('cls')
                            print("That's not an attack!\n")
                        else:
                            attackChose = self.pAttacks[attack - 1]
                            os.system('cls')
                            AttackEnemy().DealDamage(self.playerP, attackChose, self.enemyP)
                            currentTurn = 2
                    except ValueError:
                        os.system('cls')
                        print("That's not an attack!\n")

            if (currentTurn == 2):
                End().CheckGameOver(self.playerP, self.enemyP)
                if (self.enemyP.currentState > 1):
                    skip = AttackEnemy().Effect(self.enemyP, currentTurn)

                    if (skip == True):
                        currentTurn = 1

                if (currentTurn == 2):

                    print("Player Two! You're Up!\n")
                    HealthUI(self.playerP, self.enemyP).Display()
                    PrintDict().Attacks(self.enemyAttack)
                    attack = input("> ")

                    try:
                        attack = int(attack)

                        if (attack > eAttackL or attack <= 0):
                            os.system('cls')
                            print("That's not an attack!\n")
                        elif (attack < eAttackL + 1 and attack > 0):
                            attackChose = self.enemyAttack[attack - 1]
                            os.system('cls')
                            AttackEnemy().DealDamage(self.enemyP, attackChose, self.playerP)
                            currentTurn = 1
                    except ValueError:
                        os.system('cls')
                        print("That's not an attack!\n")

        End().GameOver(winner, loser, winP)
                    
    
    def Game(self):
        os.system('cls')
        gameFinished = False
        currentTurn = 1
        attackL = len(self.pAttacks)
        winner = None
        loser = None
        winP = 0

        while gameFinished == False:
            End().CheckGameOver(self.playerP, self.enemyP)
            if (currentTurn == 1):
                if (self.playerP.currentState > 1):
                    skip = AttackEnemy().Effect(self.playerP, currentTurn)

                    if (skip == True):
                        currentTurn = 2

                if (currentTurn == 1):
                    End().CheckGameOver(self.playerP, self.enemyP)
                    HealthUI(self.playerP, self.enemyP).Display()
                
                    PrintDict().Attacks(self.pAttacks)
                    attack = input("> ")

                    try:
                        attack = int(attack)

                        if (attack > attackL or attack <= 0):
                            os.system('cls')
                            print("That's not an attack!\n")
                        else:
                            attackChose = self.pAttacks[attack - 1]
                            os.system('cls')
                            AttackEnemy().DealDamage(self.playerP, attackChose, self.enemyP)
                            currentTurn = 2
                    except ValueError:
                        os.system('cls')
                        print("That's not an attack!\n")

            if (currentTurn == 2):
                if (self.enemyP.currentState > 1):
                    skip = AttackEnemy().Effect(self.enemyP, currentTurn)
                    if (skip == True):
                        currentTurn = 1
                if (currentTurn == 2):
                    chosenAttack = self.enemyAttack[random.randint(0,(len(self.enemyAttack) - 1))]
                    AttackEnemy().DealDamage(self.enemyP, chosenAttack, self.playerP)
                    currentTurn = 1

        End().GameOver(winner,loser, winP)


class End():
    def CheckGameOver(self, playerP, enemyP):
        winner = None
        loser = None
        winP = 0
        if (playerP.health <= 0 or enemyP.health <= 0):
            if (enemyP.health > 0):
                winner = enemyP
                loser = playerP
                winP = 2
            else:
                winner = playerP
                loser = enemyP
                winP = 1

            End().GameOver(winner, loser, winP)
                
    def GameOver(self, winner, loser, winP):
        os.system('cls')
        print("After rounds of intense battles, {} came out victorious against {}!\n".format(winner.name, loser.name))

        if (winP == 1):
            print("Player One Wins!")
        elif(winP == 2):
            print("Player Two Wins!")
        
        input("\nPlease Press Enter...")

        os.system('cls')
        print("1. Play Again\n2. Quit\n")

        while True:
            choice = input("I choose: ")

            try:
                choice = int(choice)
                if (choice < 1):
                    print("That's not an option!")
                elif(choice > 2):
                    print("That's not an option!")

                if (choice == 1):
                    os.system('cls')
                    StartGame().Begin()
                elif (choice == 2):
                    os.system('cls')
                    print("Thanks for playing! :)")
                    time.sleep(2.5)
                    sys.exit()
            except ValueError:
                print("That's not even a number")


StartGame().Begin()
