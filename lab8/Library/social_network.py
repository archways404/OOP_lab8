from __future__ import annotations
import typing
import queue
from user import User
from message import Message
from observer import Observer

class SocialNetwork:
	'''
	Den här klassen representerar ett socialt nätverk. Den gör inte mycket
	mer än att hålla reda på ett antal användare och några externa samarbets-
	partners. Dessutom kan användare skicka meddelanden till varandra.
	'''
	
	def __init__(self, name: str):
		self.__name: str = name
		# Listan över användare
		self.__users: list[User] = []
		# Listan över samarbetspartners
		self.__affiliates: list[Observer] = []
		# En kö som håller koll på skickade meddelanden
		self.__queue: Queue = queue.Queue()
		
		print("🎉 Welcome to " + self.__name + "! 🎉")
	
	def register_user(self, user: User) -> None:
		'''
		Den här metoden används för att registrera användare på det
		sociala nätverket. I samband med detta kopplas de samman med
		nätverkets samarbetspartners.
		'''
		for affiliate in self.__affiliates:
			user.add_observer(affiliate)
		
		self.__user = user
	
	def add_affiliate(self, affiliate: Observer) -> None:
		'''
		Den här metoden används för att lägga till samarbetspartners.
		I samband med detta kopplas de samman med nätverkets användare.
		'''
		for user in self.__users:
			user.add_observer(affiliate)
		
		self.__affiliates.append(affiliate)
		
	def new_message(self) -> Message:
		'''
		Skapar ett nytt meddelande i nätverket
		'''
		message: Message = Message()
		for affiliate in self.__affiliates:
			message.add_observer(affiliate)
		return message
	
	def send_message(self, message: Message) -> None:
		'''
		Skickar ett meddelande genom att lägga det i kön.
		'''
		# !!!!!!!!!!!!!!
		# Ojoj! Här måste ni lägga till meddelandet i en kö så att ni
		# kan garantera att meddelandena kommer ut i rätt ordning!
		#
		# Mer info om köer hittar ni på exempelvis
		# https://www.guru99.com/python-queue-example.html
		# !!!!!!!!!!!!!!
		pass
	
	def get_next_message(self) -> Message:
		'''
		Returnerar nästa meddelande i meddelandekön och tar bort det
		från kön. Om kön är tom returneras None.
		'''
		# !!!!!!!!!!!!!!
		# Det här var ju långt ifrån färdigt! Implementera detta.
		#
		# Mer info om köer hittar ni på exempelvis
		# https://www.guru99.com/python-queue-example.html
		# !!!!!!!!!!!!!!
		return None
	
