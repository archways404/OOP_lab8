from __future__ import annotations
import typing
from observable import Observable
from event import Event  # Import the Event class
from user import User

user_pairs = {}

class Message(Observable):
  '''
  Den här klassen representerar ett meddelande mellan två användare. Det
  använder sig av metodlänkning (se https://en.wikipedia.org/wiki/Method_chaining)
  för att skapa objekten. Bekanta dig gärna med hur detta fungerar.
  '''

  def __init__(self):
    super().__init__()
    self.__message: str = ""
    self.__sender: User = None
    self.__receiver: User = None
  
  def message(self, message: str) -> Message:
    if len(message) > 0:
      self.__message = message
    return self
  
  def sender(self, sender: User) -> Message:
    self.__sender = sender
    return self
  
  def receiver(self, receiver: User) -> Message:
    self.__receiver = receiver
    return self
  
  def get_message(self) -> str:
    return self.__message
  
  def get_sender(self) -> User:
    return self.__sender
  
  def get_receiver(self) -> User:
    return self.__receiver
  
  def build(self) -> Message:
    if "mössor" in self.__message:
      print("Message contains 'mössor'")
      if self.__sender is not None:  # Check if sender is set
        self.add_observer(self)
        message_event = Event("MESSAGE", self)
        self.notify_observers(message_event)
        display_user_pairs(user_pairs, self.__message)
    return self
  
  def notify_observers(self, event: Event) -> None:
    for observer in self.__observers:
        observer.update(event)
        if isinstance(observer, MessageObserver):
            sender = event.get_subject().get_sender().get_name()
            receiver = event.get_subject().get_receiver().get_name()

            # Create a tuple representing the user pair
            user_pair = (sender, receiver)
            # Check if this user pair already exists in the dictionary
            if user_pair in user_pairs:
                user_pairs[user_pair] += 1
            else:
                user_pairs[user_pair] = 1


def display_user_pairs(user_pairs, message: Message):
  for pair, count in user_pairs.items():
    sender, receiver = pair
    print(f"{sender} <-> {receiver}: {count} messages from '{message.get_message()}'")




