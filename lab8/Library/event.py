import typing
from abc import ABC

class Event(ABC):
	'''
	Klassen Event är basklass för alla händelser i systemet. Den är
	abstrakt och måste därför utökas av en annan klass för att kunna
	användas.
	
	Klassen håller koll på det objekt som övervakas, kallat subjektet.
	När Observer-objekten vill arbeta med det objekt som skapade händelsen,
	dvs subjektet, hämtas detta med hjälp av get_subject().
	'''

	def __init__(self, subject: object):
		self.__subject = subject
	
	def get_subject(self) -> object:
		return self.__subject
