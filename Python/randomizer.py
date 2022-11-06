import random
from datetime import datetime

enemyList = ["Pyro Slime", "Cryo Slime", "Hydro Slime", "Electro Slime", "Geo Slime", "Dendro Slime", "Anemo Slime", "Eye of the Storm", 
        "Weaponless Hilichurl", "Club Weilding Hilichurl", "Shield Hilichurl Guard", "Hilichurl Shooter", "Elemental Hilichurl Shooter",
        "Shieldwall Mitachurl", "Blazing Axe Mitachurl", "Elemental Lawachurl (Cheiftan)", "Samachurl (Shaman)", "Pyro Abyss Mage", "Hydro Abyss Mage",
        "Cryo Abyss Mage", "Electro Abyss Mage",
        "Fatui Skirmisher - Pyroslinger", "Fatui Skirmisher - Hydrogunner", "Fatui Skirmisher - Anemoboxer", "Fatui Skirmisher - Electrohammer",
        "Fatui Skirmisher - Cryogunner", "Fatui Skirmisher - Geochanter", "Fatui Pyro Agent", "Fatui Electro Cicin Mage", "Fatui Cryo Cicin Mage", "Mirror Maiden",
        "Ruin Guard", "Ruin Hunter", "Ruin Grader", "Ruin Army(Cruiser, Destroyer, Scout, Defender)",
        "Treasure Hoarders", "Pyro Whopperflower", "Cryo Whopperflower", "Electro Whopperflower",
       "Geovishap Hatchling", "Mature Geovishap", "Primodial Bathysmal Vishap",
        "Hydro Specter", "Cyro Specter", "Pyro Specter","Geo Specter", "Electro Specter",
        "Nobushi(Samurai)", "Elemental Kairagi", "Rifthound Whelp", "Rifthound",
        "Maguu Kenki", "Golden Wolflord", "Hydro Hypostasis", "Pyro Hypostasis", "Electro Hypostasis", "Cryo Hypostasis", "Geo Hypostasis", "Anemo Hypostasis", "Oceanid", "Thunder Manifestation", "Perpetual Mechanical Array", "Primo Geovishap", "Cryo Regisvine", "Pyro Regisvine"]

itemList = ["Iron Chunk", "White Iron Chunk", "Crystal Chunk", "Magical Crystal Chunk", "Starsilver", "Apple", "Sunsettia", "Mushroom", "Sweet Flower",
            "Carrot", "Radish", "Snapdragon", "Mint", "Pinecone", "Berry", "Matsutake", "Bird Egg", "Wolfhook", "Valberry", "Cecilia", "Windwheel Aster",
            "Philanemo Mushroom", "Small Lamp Grass", "Calla Lily", "Lotus Head", "Horsetail", "Starconch", "Violetgrass", "Bamboo Shoot", "Mist Flower Corolla",
            "Flaming Flower Stamen", "Electro Crystal", "Cor Lapis", "Dandelion Seed", "Jueyun Chili", "Noctilucous Jade", "Silk Flower", "Glaze Lily",
            "Qingxin", "Crystal Core", "Crab", "Sea Ganoderma", "Sango Pearl", "Amakumo Fruit", "Fluorescent Fungus", "Sakura Bloom", "Naku Weed"]
            
flowerList = ["Pyro", "Cryo"]

# Intro area, can cut out list ptinting
print("Welcome to the GONER Randomize Speed Run Game Set-up uwu!")
print(" ")
print(" ")
#print("Here are the total lists of Items and Enemies that you will be pulling from!: ")
#print("Enemy List: ", enemyList)
#print(" ")
#print("Item List: ", itemList)
#print(" ")

# Section for coin toss of who picks flower first
Hval = "Heads"
Tval = "Tails"
trueVal = "Heads"
playerInput = input("We will now pick our flowers! Any player, enter 'Heads' or 'Tails':  ")
while (playerInput != Hval and playerInput != Tval):
    print("Please enter Heads or Tails (case sensitive)")
    playerInput = input("We will now pick our flowers! Any player, enter 'Heads' or 'Tails':  ")
    
coin = random.randint(1, 2)
if (coin == 1):
    trueVal = Hval
    if (trueVal == playerInput):
        print("It was Heads! You won the coin toss and get to pick your flower first!!")
    else:
        print("It was Heads! You lost the coin toss and the other player gets to pick the flower first!!")
elif (coin == 2):
    trueVal = Tval
    if (trueVal == playerInput):
        print("It was Tails! You won the coin toss and get to pick your flower first!!")
    else:
        print("It was Tails! You lost the coin toss and the other player gets to pick the flower first!!")

# Player pick and flower choice
print(" ")
flowerChoice = input("Winning Player 1, please choose either 'Pyro' or 'Cryo' Flower!: ")
while (flowerChoice not in flowerList):
    print("Please enter Pyro or Cryo (case sensitive)")
    flowerChoice = input("Winning Player 1, please choose either 'Pyro' or 'Cryo' Flower!:  ")
player1List = []
player2List = [] 

if (flowerChoice == "Pyro"):
    player1List.append("Pyro")  
    player2List.append("Cryo")
else:
    player1List.append("Cryo")
    player2List.append("Pyro")

print("Now randomizing lists for each player! uwu")
print(" ")
print(" ")

randSeed = random.seed(datetime.now())

# does the randomizing
for i in range(7):
    #enemy choice
    choice1 = random.choice(enemyList)
    if (choice1 not in player1List and choice1 not in player2List):
        player1List.append(choice1)
    else:
        while (choice1 in player1List or choice1 in player2List):
            choice1 = random.choice(enemyList)
        player1List.append(choice1)
    
    choice2 = random.choice(enemyList)
    if (choice2 not in player1List and choice2 not in player2List):
        player2List.append(choice2)
    else:
        while (choice2 in player1List or choice2 in player2List):
            choice2 = random.choice(enemyList)
        player2List.append(choice2)

    #item choice
    choice3 = random.choice(itemList)
    if (choice3 not in player1List and choice3 not in player2List):
        player1List.append(choice3)
    else:
        while (choice3 in player1List or choice3 in player2List):
            choice3 = random.choice(itemList)
        player1List.append(choice3)
    
    choice4 = random.choice(itemList)
    if (choice4 not in player1List and choice4 not in player2List):
        player2List.append(choice4)
    else:
        while (choice4 in player1List or choice4 in player2List):
            choice4 = random.choice(itemList)
        player2List.append(choice4)

    choice5 = random.choice(itemList)
    if (choice5 not in player1List and choice5 not in player2List):
        player1List.append(choice5)
    else:
        while (choice5 in player1List or choice5 in player2List):
            choice5 = random.choice(itemList)
        player1List.append(choice5)

    choice6 = random.choice(itemList)
    if (choice6 not in player1List and choice6 not in player2List):
        player1List.append(choice6)
    else:
        while (choice6 in player1List or choice6 in player2List):
            choice6 = random.choice(itemList)
        player1List.append(choice6)

    choice7 = random.choice(itemList)
    if (choice7 not in player1List and choice7 not in player2List):
        player1List.append(choice7)
    else:
        while (choice7 in player1List or choice7 in player2List):
            choice7 = random.choice(itemList)
        player1List.append(choice7)

#print stuff out!!
print("Player 1 Set! :  ")
print("Player 1 Flower = ", player1List[0])
print("Player 1 Enemies = ", player1List[1], ", ", player1List[3], ", ", player1List[5], ", ",player1List[7], ", ",player1List[9], player1List[11], ", ")
print("Player 1 Items = ", player1List[2], ", ",player1List[4], ", ",player1List[6], ", ",player1List[8], ", ",player1List[10], player1List[12], ", ")
print(" ")
print("Player 2 Set! :  ")
print("Player 2 Flower = ", player2List[0])
print("Player 2 Enemies = ", player2List[1], ", ", player2List[3], ", ", player2List[5], ", ",player2List[7], ", ", player2List[9], player1List[11], ", ")
print("Player 2 Items = ", player2List[2],  ", ",player2List[4], ", ", player2List[6], ", ",player2List[8],  ", ",player2List[10], player1List[12], ", ")