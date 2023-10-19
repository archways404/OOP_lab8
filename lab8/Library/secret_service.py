import typing
from observer import Observer
from event import Event
from user_event import UserEvent
from user import User

class SecretService(Observer):
	'''
	Den här klassen representerar en säkerhetstjänst, som övervakar diverse
	händelser i vårt sociala nätverk. Varje annonsör har ett namn, men i
	övrigt gör de inte så mycket mer än att analysera händelser.
	'''

	def __init__(self, name: str):
		self.__name: str = name
	
	def update(self, event: Event) -> None:
		'''
		Den här metoden lyssnar på uppdateringar om olika objekt och
		skickar händelserna till rätt händelsehanterare.
		'''
		if (isinstance(event, UserEvent)):
			self.__handle_user_event(event)
	
	def __handle_user_event(self, event: UserEvent) -> None:
		'''
		Den här metoden hanterar alla användarhändelser och skickar dem
		vidare till rätt analysmetod.
		'''
		if event.get_event_type() == UserEvent.FRIEND_ADDED:
			self.__analyze_new_friend(event.get_subject())
		elif event.get_event_type() == UserEvent.FRIEND_REMOVED:
			self.__analyze_unfriend(event.get_subject())
		elif event.get_event_type() == UserEvent.MESSAGE:
			self.__analyze_message(event.get_subject())


	def __analyze_new_friend(self, user: User) -> None:
		print("🕵️ " + self.__name + ": " +
			"Noting that " + user.get_name() +
			" is now friends with " +
			user.list_friends()[-1].get_name())
	
	def __analyze_unfriend(self, user: User) -> None:
		print("🕵️ " + self.__name + ": " +
			"Noting that " + user.get_name() + " has one less friend")
		
	def __analyze_message(self, user: User) -> None:
	  print("🕵️ " + self.__name + ": " +	"ERROR")
