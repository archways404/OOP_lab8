# advertiser.py

import typing
from observer import Observer
from user import User
from event import Event
from user_event import UserEvent
from message import Message  # Import the Message class

class Advertiser(Observer):
    '''
    Den här klassen representerar en annonsör, som lyssnar på diverse
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
        if isinstance(event, UserEvent):
            self.__handle_user_event(event)
        elif isinstance(event, Message):  # Check if it's a Message event
          self.__handle_message_event(event)


    def __handle_user_event(self, event: UserEvent) -> None:
        '''
        Den här metoden hanterar alla användarhändelser och skickar dem
        vidare till rätt analysmetod.
        '''
        if event.get_event_type() == UserEvent.STATUS_UPDATED:
            self.__analyze_latest_post(event.get_subject())

    def __handle_message_event(self, event: Message) -> None:
        '''
        This method handles Message events.
        '''
        print("MESSAGE: " + event.get_message())


    def __analyze_latest_post(self, user: User) -> None:
        print("🪧 " + self.__name + ": " +
            user.get_name() + ' just posted "' +
            user.get_latest_status() + '" to their ' +
            str(len(user.list_friends())) + " friends.")
