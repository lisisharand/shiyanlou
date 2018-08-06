#!/usr/bin/env python3
class Animal(object):
	def __init__(self,name):
		self.name = name
	def get_name(self):
		return self.name
	def set_name(self,value):
		self.name = value
	def make_sound(self):
		pass
class Dog(Animal):
	def make_sound(self):

		print(self.get_name() +'is making sound wangwangwang')
class Cat(Animal):
	def make_sound(self):
		print(self.get_name() + "is making miumiu miu")

dog = Dog("wangcai")
cat = Cat("kitty")
dog.make_sound()
cat.make_sound()
