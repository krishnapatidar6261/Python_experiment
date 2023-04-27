from abc import ABC,abstractmethod

class shape(ABC):

    def __init__(self,name):
        self.name=name


    @abstractmethod
    def draw(self):
        pass

class tringle(shape):

    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print("Drawing Tringle")


t1=tringle("circle")
t1.draw()