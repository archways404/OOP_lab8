import typing
from observer import Observer
from event import Event

class Observable:
	'''
	Den här klassen är superklass till alla klasser som kan övervakas.
	'''
	
	def __init__(self):
		# Det här är listan över samtliga objekt som bevakar det
		# aktuella objektet
		self.__observers: list[Observer] = []
	
	def add_observer(self, observer: Observer) -> None:
		self.__observers.append(observer)
	
	def remove_observer(self, observer: Observer) -> None:
		self.__observers.remove(observer)
	
	def notify_observers(self, event: Event) -> None:
		for observer in self.__observers:
			observer.update(event)
