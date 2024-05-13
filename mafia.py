import random 
import time 
 
class Sheriff: 
    def __init__(self, name): 
        self.name = name 
 
    def inspect(self, players): 
        print("Список гравців:") 
        for index, player in enumerate(players, 1): 
            print(f"{index}. {player}") 
         
        suspect_index = int(input("Оберіть номер гравця для перевірки: ")) - 1 
         
        return players[suspect_index] if 0 <= suspect_index < len(players) else None 
 
class Mafia: 
    def __init__(self, name): 
        self.name = name 
 
    def choose_target(self, players): 
        print("Список гравців:") 
        for index, player in enumerate(players, 1): 
            print(f"{index}. {player}") 
         
        target_index = int(input("Оберіть номер гравця, якого хочете вбити: ")) - 1 
         
        return players[target_index] if 0 <= target_index < len(players) else None 
 
class Villager: 
    def __init__(self, name): 
        self.name = name 
 
    def protect(self, players): 
        print("Список гравців:") 
        for index, player in enumerate(players, 1): 
            print(f"{index}. {player}") 
         
        protect_index = int(input("Оберіть номер гравця для захисту: ")) - 1 
         
        return players[protect_index] if 0 <= protect_index < len(players) else None 
 
def main(): 
    players = ["Петро", "Іван", "Катерина", "Андрій", "Марія"] 
    sheriff = Sheriff("Sheriff") 
    mafia = Mafia("Mafia") 
    villager = Villager("Мирний житель") 
 
    print("Гра почалася!") 
 
    while len(players) > 2: 
        print("\nНіч:") 
        time.sleep(1) 
        if isinstance(mafia, Mafia): 
            target = mafia.choose_target(players) 
            if target: 
                print(f"{mafia.name} вбиває {target}.") 
                if isinstance(target, Sheriff): 
                    print(f"{sheriff.name} був убитий мафією!") 
                    players.remove(sheriff) 
                    break
 
                else: 
                    players.remove(target) 
 
        time.sleep(1) 
        if isinstance(villager, Villager): 
            protector = villager.protect(players) 
            if protector: 
                print(f"{villager.name} захищає {protector}.") 
         
        print("\nДень:") 
        time.sleep(1) 
        suspect = sheriff.inspect(players) 
        print(f"{sheriff.name} перевіряє {suspect}.") 
        print(f"{suspect} - {mafia.name}" if suspect == players[-1] else f"{suspect} - звичайний гравець.") 
 
    if len(players) > 2: 
        print("Місто виграло!") 
 
if __name__ == "__main__": 
    main()
