from __future__ import annotations
import typing
from observable import Observable
from user import User

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
    # Check if "mössor" exists in the message
    if "mössor" in self.__message:
        print("Message contains 'mössor'")
        self.notify_observers(self)
    return self

message = Message()
message.message("mössor")
message.build()  # This will check for "mössor" in the message
