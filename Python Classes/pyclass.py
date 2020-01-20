'''
class snake :
	name = "python"

print(snake.name)  # python
'''
#----------------------------------------

class snake:
	name_attribute = "python"

	def __init__(self,a):
		print("in intial function",a)

	def change_name_method(self,new_name):
		self.name_attribute = new_name


testInstance_01 = snake(1)
testInstance_02 = snake(2)
 
testInstance_01.change_name_method("Kasun")
print(testInstance_01.name_attribute)
#>>>
#in intial function 1
#in intial function 2
#Kasun

print(testInstance_02.name_attribute)
#>>
#in intial function 1
#in intial function 2
#python

#-----------------------------------------------
class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)


class MarsRover(Rocket): # inheriting from the base class
    def __init__(self, name, distance, maker):
        Rocket.__init__(self, name, distance)
        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s" % (self.name, self.maker)



x = Rocket("simple rocket", "till stratosphere")
y = MarsRover("mars_rover", "till Mars", "ISRO")
print(x.launch())
print(y.launch())
print(y.get_maker())

#---------------------------------------------
import numpy as np

class matrix1:
	List = [] 
	
	def __init__(self, Matrix):
		print(Matrix)
		self.List= List.append[Matrix]
	
a = 5
b = 3 
for i in range(1,4):
	instance_01 = matrix1(np.zeros((i+1,i+1))) 

print (List)