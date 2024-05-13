import random
import time
import tkinter as tk
from tkinter import messagebox

class Sheriff:
    def __init__(self, name):
        self.name = name

    def inspect(self, players, root):
        self.selected_player = None

        def select_player():
            nonlocal self
            selected_index = listbox.curselection()
            if selected_index:
                self.selected_player = players[selected_index[0]]
                root.destroy() 
                root.quit()     

        root.title("Шериф вибирає гравця")
        label = tk.Label(root, text="Виберіть гравця для перевірки:")
        label.pack()

        listbox = tk.Listbox(root)
        for player in players:
            listbox.insert(tk.END, player)
        listbox.pack()

        button = tk.Button(root, text="Перевірка", command=select_player)
        button.pack()

        root.mainloop()

        return self.selected_player

class Mafia:
    def __init__(self, name):
        self.name = name

    def choose_target(self, players, root):
        self.selected_target = None

        def select_target():
            nonlocal self
            selected_index = listbox.curselection()
            if selected_index:
                self.selected_target = players[selected_index[0]]
                root.destroy()  
                root.quit()     

        root.title("Мафія вибирає ціль")
        label = tk.Label(root, text="Виберіть гравця для убивства:")
        label.pack()

        listbox = tk.Listbox(root)
        for player in players:
            listbox.insert(tk.END, player)
        listbox.pack()

        button = tk.Button(root, text="Виберіть ціль", command=select_target)
        button.pack()

        root.mainloop()

        return self.selected_target

class Villager:
    def __init__(self, name):
        self.name = name

    def protect(self, players, root):
        self.selected_protector = None

        def select_protector():
            nonlocal self
            selected_index = listbox.curselection()
            if selected_index:
                self.selected_protector = players[selected_index[0]]
                root.destroy()  
                root.quit()     

        root.title("Житель вибирає захисника")
        label = tk.Label(root, text="Виберіть гравця для захисту:")
        label.pack()

        listbox = tk.Listbox(root)
        for player in players:
            listbox.insert(tk.END, player)
        listbox.pack()

        button = tk.Button(root, text="Виберіть захиснека", command=select_protector)
        button.pack()

        root.mainloop()

        return self.selected_protector

def main():
    players = ["Петро", "Іван", "Катерина", "Андрій", "Марія"]
    sheriff = Sheriff("Sheriff")
    mafia = Mafia("Mafia")
    villager = Villager("Мирний житель")

    root = tk.Tk()
    root.withdraw()  

    messagebox.showinfo("Гра почалася!", "Гра почалася!")

    while len(players) > 2:
        time.sleep(1)
        messagebox.showinfo("Ніч:", "Наступила ніч!")
        if isinstance(mafia, Mafia):
            target_window = tk.Toplevel()
            target = mafia.choose_target(players, target_window)
            target_window.destroy() 
            if target:
                messagebox.showinfo("Ніч:", f"{mafia.name} вбиває {target}.")
                if isinstance(target, Sheriff):
                    messagebox.showinfo("Результат:", f"{sheriff.name} був убитий мафією!")
                    players.remove(sheriff)
                    break
                else:
                    players.remove(target)

        time.sleep(1)
        if isinstance(villager, Villager):
            protector_window = tk.Toplevel()
            protector = villager.protect(players, protector_window)
            protector_window.destroy()
            if protector:
                messagebox.showinfo("День:", f"{villager.name} захищає {protector}.")

        time.sleep(1)
        messagebox.showinfo("День:", "Наступив день!")
        suspect_window = tk.Toplevel()
        suspect = sheriff.inspect(players, suspect_window)
        suspect_window.destroy() 
        messagebox.showinfo("Перевірка:", f"{sheriff.name} перевіряє {suspect}.")
        messagebox.showinfo("Результат:", f"{suspect} - {mafia.name}" if suspect == players[-1] else f"{suspect} - звичайний гравець.")

    if len(players) > 2:
        messagebox.showinfo("Кінець гри:", "Місто виграло!")

if __name__ == "__main__":
    main()