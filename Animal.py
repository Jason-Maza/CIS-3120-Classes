class Animal:
    def __init__(self, name, food, sleep, drink, hunt):  
        self.__name = name
        self.__food = food
        self.__sleep = sleep
        self.__drink = drink
        self.__hunt = hunt
        print("hello, I am", self.__name)
        
    def food(self):
        print("Crunch", self.__food)
    
    def sleep(self):
       print("zzz", self.__sleep)

    def drink(self):
       print("slurp", self.__drink)
    
    def hunt(self):
       print("I Hunt", self.__hunt)




        

