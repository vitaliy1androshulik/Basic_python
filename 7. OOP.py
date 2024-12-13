class Person:
    def __init__(self, name, age):
        #print("Створено об'єкт класу")
        self.__name = name # __ це приватні змінні
        self.__age = age

    def display(self):
        print(self.__name, self.__age)

    def setName(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name=name


    def __del__(self):
        print("Даний об'єкт покинув корабель")

    #def __init__(self):
    #    print("Створено об'єкт класу")

ivan = Person("Ivan", 123)
#ilona = Person()
ivan.setName("Оксана")
ivan.display()
print(ivan.name)
ivan.name = "Віталій"
print(ivan.name)
