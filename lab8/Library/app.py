from user import User
from message import Message
from advertiser import Advertiser
from secret_service import SecretService
from social_network import SocialNetwork

friend_face: SocialNetwork = SocialNetwork("FriendFace")

shady_ad_company: Advertiser = Advertiser("ShadyAds")
fra: SecretService = SecretService("FRA")

friend_face.add_affiliate(shady_ad_company)
friend_face.add_affiliate(fra)

johan: User = User("Johan", 40)
anton: User = User("Anton", 32)
dipak: User = User("Dipak", 39)

friend_face.register_user(johan)
friend_face.register_user(anton)
friend_face.register_user(dipak)

# Johan och Anton blir vänner
print("> Johan och Anton blir vänner")
johan.add_friend(anton)
anton.add_friend(johan)

# Johan och Dipak blir vänner
print("> Johan och Dipak blir vänner")
johan.add_friend(dipak)
dipak.add_friend(johan)

# Johan gör bort sig, Anton blir sur
print("> Johan gör bort sig, Anton blir sur")
johan.post_status("Star Wars är som Star Trek, fast för kretiner")
anton.unfriend(johan)

# Johan skickar ett meddelande till Dipak
print("> Johan skickar ett meddelande till Dipak")
friend_face.send_message(friend_face.new_message()
	.sender(johan)
	.receiver(dipak)
	.message("Hallå Dipak! Jag har köpt en ny mössa!")
	.build())

# Dipak svarar Johan
print("> Dipak svarar Johan")
friend_face.send_message(friend_face.new_message()
	.sender(dipak)
	.receiver(johan)
	.message("Vad kul! Är det en pälsmössa?")
	.build())

# Johan svarar Dipak
print("> Johan svarar Dipak")
friend_face.send_message(friend_face.new_message()
	.sender(johan)
	.receiver(dipak)
	.message("Japp, det är isbjörn.")
	.build())

# Dipak och Anton blir vänner
print("> Dipak och Anton blir vänner")
dipak.add_friend(anton)
anton.add_friend(dipak)

# Dipak skickar ett meddelande till Anton
print("> Dipak skickar ett meddelande till Anton")
friend_face.send_message(friend_face.new_message()
	.sender(dipak)
	.receiver(anton)
	.message("Hej Anton! Har du en mössa som jag kan få låna?")
	.build())

# Nu loggar någon in och tittar på alla meddelanden
message: Message = friend_face.get_next_message()
while message is not None:
	print("🗨️ " + message.get_sender().get_name() + " till " +
		message.get_receiver().get_name() + ": " + 
		message.get_message())
	message = friend_face.get_next_message()
