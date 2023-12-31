from __future__ import annotations
import typing
from observable import Observable
from event import Event  # Import the Event class
from user import User

user_pairs = []


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
    print("Message built")
    if "mössor" in self.__message:
      print("Message contains 'mössor'")
      if self.__sender is not None:  # Check if sender is set
        self.notify_observers(self)
    sender = self.__sender.get_name()
    receiver = self.__receiver.get_name()
    user_pair = (sender, receiver)
    user_pair_reverse = (receiver, sender)
    if user_pair_reverse in user_pairs:
      user_pairs.append(user_pair_reverse)
    else:
      user_pairs.append(user_pair)
    count = 0
    for user_pairs in user_pairs:
      print(user_pairs)
      count += 1
    print(count)
    #  user_pairs.append[user_pair] += 1
    #else:
    #  user_pairs[user_pair] = 1
    #  for pair, count in user_pairs.items():
    #    sender, receiver = pair
    #    print(f"{pair} <-> : {count}")
    return self






