import random

def roll_dice():
    
    cube = random.randint(1, 6)
    print(f"Выпало значение кубика: {cube}")

    if cube in (5, 6):
        print("Вы победили!")
    elif cube in (3, 4):
        print("Пробуем ещё раз...")
        roll_dice() 
    else:
        print("Вы проиграли!")

if __name__ == "__main__":
    roll_dice()
