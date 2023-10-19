from __future__ import annotations
import typing
from observable import Observable
from user_event import UserEvent

class User(Observable):
	'''
	Den här klassen representerar en användare. Den har ett namn och en
	ålder, och kan kopplas till andra användare genom att läggas i vän-
	listan. Dessutom kan användaren posta statusar.
	
	Eftersom våra annonsörer och andra är väldigt nyfikna på vad användarna
	gör, måste vi notifiera dem så fort något i användar-objektet ändras.
	'''

	def __init__(self, name: str, age: int):
		super().__init__()
		self.__name: str = name
		self.__age: int = 0
		# Listan över användarens vänner
		self.__friends: list[User] = []
		# Listan över användarens alla statusar
		self.__statuses: list[str] = []
	
	def get_name(self) -> str:
		return self.__name
	
	def set_name(self, name: str) -> None:
		if len(name) > 1:
			self.__name = name
			self.notify_observers(UserEvent(self, UserEvent.NAME_UPDATED))
	
	def get_age(self) -> int:
		return self.__year
	
	def set_age(self, age: int) -> None:
		if age > 0:
			self.__age = age
			self.notify_observers(UserEvent(self, UserEvent.AGE_UPDATED))
	
	def add_friend(self, friend: User) -> None:
		'''
		Lägger till en användare i vänlistan om den inte redan finns.
		'''
		if isinstance(friend, User) and friend not in self.__friends:
			self.__friends.append(friend)
			self.notify_observers(UserEvent(self, UserEvent.FRIEND_ADDED))
	
	def unfriend(self, friend: User) -> None:
		'''
		Tar bort en användare ur vänlistan förutsatt att den finns där.
		'''
		if isinstance(friend, User) and friend in self.__friends:
			self.__friends.remove(friend)
			self.notify_observers(UserEvent(self, UserEvent.FRIEND_REMOVED))
	
	def list_friends(self) -> list[User]:
		'''
		Skickar tillbaka en kopia av användarens vän-lista. Vi skapar
		en kopia för att ingen ska kunna komma och ändra direkt i
		listan. Hade vi bara skickat tillbaka listan, hade vi fått en
		referens till den, och då kan ven som helst ändra i den.
		'''
		return self.__friends.copy()
	
	def post_status(self, status: str) -> None:
		'''
		Postar en status genom att lägga till den i sin statuslista.
		Det här är förstås egentligen fruktansvärt fult byggt, men det
		duger gott för våra behov.
		'''
		if len(status) > 0:
			self.__statuses.append(status)
			self.notify_observers(UserEvent(self, UserEvent.STATUS_UPDATED))
	
	def get_latest_status(self) -> str:
		'''
		Hämtar den användarens senaste statusmeddelande.
		'''
		if len(self.__statuses) > 0:
			return self.__statuses[-1]
		else:
			return ""
	
	def get_status(self, index: int) -> str:
		'''
		Hämtar en status i listan på platsen index.
		'''
		if index > -1 and len(self.__statuses) <= index + 1:
			return self.__statuses[index]
		else:
			return ""

