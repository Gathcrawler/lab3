from client import Client
from client_friends import ClientFriends

input_id = input('Enter id:')
user = Client(input_id)
user_friends = ClientFriends(user.execute())
user_friends.print_friends()