from guizero import App, PushButton, Text
import random
# Key - value == item - chance
loot_pool = {
    "Common":50,
    "Uncommon":25,
    "Rare": 15, 
    "Epic": 10,
    "Mythic": 5,
    "Godly": 4,
    "Secret": 1
}

def gacha_ing():
    global result
    cummulative = 0
    roll = random.randint(1, 100)
    for item, chance in loot_pool.items():
        cummulative += chance # Adding up the chance, creating a range for every rarity
        if roll <= cummulative: # Checking if its in range
            result.value = f"You got: {item}"
            break # Stop once getting an item to prevent override data
        
window = App(title = "gacha is my life")

result = Text(window, text = "You got:")

gacha = PushButton(window, command = gacha_ing, text = "jst go ahead you gambler")

window.display()