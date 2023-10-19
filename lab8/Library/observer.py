import typing
from abc import ABC, abstractmethod
from event import Event

class Observer(ABC):
	'''
	Observer är basklass för alla klasser som ska kunna övervaka andra
	klasser. Den här klassen är en abstrakt klass, som inte kan
	instansieras direkt, utan måste implementeras som en subklass.
	'''

	@abstractmethod
	def update(self, event: Event) -> None:
		print(f"Received event: {event.data}")
