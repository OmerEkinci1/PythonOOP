from os import system
from random import randint

class Weapon:
    def __init__(self , name:str , damage:int):
        self.__name = name
        self.__damage = damage

    def hit(self, rival):
        rival.setHp(rival.getHp() - self.__damage)
        self.__damage -= 1

    def getName(self):
        return self.__name

    def getDamage(self):
        return self.__damage

class Character:
    def __init__(self , hp:int , weapon:Weapon):
        self.__weapon = weapon
        self.__hp = hp

    def hit(self,rival):
        self.__weapon.hit(rival)

    def getHp(self):
        return self.__hp

    def setHp(self , newHp:int):
        self.__hp = newHp

    def getWeaponName(self):
        return self.__weapon.getName()

    def getDamage(self):
        return self.__weapon.getDamage()

class Enemy(Character):
    pass

class Player(Character):
    def __init__(self, name:str , hp:int , weapon:Weapon):
        Character.__init__(self,hp,weapon)
        self.__name = name

    def getName(self):
        return self.__name

def Main():
    enemies = []
    for i in range(10):
        enemy = Enemy(randint(30,50),Weapon("Knife",randint(10,50)))
        enemies.append(enemy)

    player = Player("Omer", 100 , Weapon("Sword" , 50))

    while True:
        system("cls")
        print("Player: {}  ----------  Hp: {}   -------------  Weapon: {}  ---- Damage: {}".format(player.getName(),player.getHp(),player.getWeaponName(),player.getDamage()))
        print("---------------------------------------")
        for sayi,i in enumerate(enemies):
            print("No:{} Enemy Hp:{} ------ Enemy Damage:{} ------ Enemy Weapon:{}".format(sayi,enemy.getHp(),enemy.getDamage(),enemy.getWeaponName()))

        print("---------------------")
        choice = input("Enemy who will attack: ")
        dusman = enemy[int(choice)]
        player.hit(dusman)
        if  dusman.getCan() <=0:
            enemy.remove(item)
            if not enemy:
                print("Congratilouns!!!")
        if enemy:
            enemy[randint(0,len(enemy) - 1).hit(player)]
            if player.getHp() <=0:
                print("Game Over")
                quit()

if __name__ == "__main__":
    Main()
