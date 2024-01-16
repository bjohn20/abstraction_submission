

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self):
        super().__init__()

    def humanAge (self,age):
         print("You are {} in human years".format(age))

    @abstractmethod
    def age(self):
        pass


class hamsterYears(Person):
    def age(self,age):
        result = age / 2
        print("You would be {} in hamster years".format(result))







if __name__ == "__main__":
    Brandon = hamsterYears()
    Brandon.humanAge(33)
    Brandon.age(33)
