import typing
from event import Event

class UserEvent(Event):
	'''
	Den här klassen representerar en händelse som påverkar en användare.
	
	Det finns fem händelsetyper kopplat till den här händelsen (se nedan),
	och dessa nås genom att ange exempel UserEvent.AGE_UPDATED.
	'''

	NAME_UPDATED = 0
	AGE_UPDATED = 1
	STATUS_UPDATED = 2
	FRIEND_ADDED = 3
	FRIEND_REMOVED = 4

	def __init__(self, subject: object, event_type: int):
		'''
		UserEvent instansieras genom att objektet som skapar ett
		UserEvent-objekt skickar med en referens till sig själva, samt
		en händelsetyp.
		'''
		super().__init__(subject)
		self.__event_type: int = event_type
	
	def get_event_type(self) -> int:
		'''
		Den här metoden returnerar händelsetypen. Använd sedan klassens
		fördefinierade händelsetyper för att jämföra med objektets
		händelsetyp, se exempelvis Advertiser eller SecretService.
		'''
		return self.__event_type
