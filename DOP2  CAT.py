class Cat(object):
    """ Виртуальная кошка """
    total = 0
    @staticmethod
    def count():
        print("Всего кошек: ", Cat.total)
    
    def __init__(self):
        print("Родилась новая кошка!")
        self.name = input("Как мы её назовём? ")
        Cat.total += 1
        self.__w = 300
        self.hunger = 1
        
    def __str__(self):
        res = "Объект класса Cat\n name: " + self.name + "\nBec: " + str(self.__w)
        return res
        
    @property
    def weight(self):
        return self.__w
    
    def talk(self):
        print(self.name, ": Мяу")
    
    def eat(self):
        if self.hunger == 5:
            print("Кошка не голодная")
        else:
            self.hunger += 1
            self.__w += 30
            print("Мур!")

    def play(self):
        self.talk()
        self.__w -= 5
        if self.hunger > 0:
            self.hunger -= 1
        else:
            self.hunger = 1
    
def main():

    bagira = Cat()
    choice = None
    while choice != "0":
        print \
        ("""
        Что будем делать?
            
        0 - Выйти
        1 - Поговорить с кошкой
        2 - Покормить
        3 - Поиграть
        4 - Взвесить
        """)
            
        choice = input(">>: ")
        print()

        # exit
        if choice == "0":
            print("Пока.")
            
        # послушать
        elif choice == "1":
            bagira.talk()
                
        # покормить
        elif choice == "2":
            bagira.eat()
                
        # поиграть
        elif choice == "3":
            bagira.play()
        elif choice == "4":
            print("Вес: ", bagira.weight, " гр. ")
            
        # неправильный ввод
        else:
            print("\nНеправильный ввод!")  
main()            
input()