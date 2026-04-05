from file import File
from mine import Mine

player_data = File()
data = player_data.load()
player_mine = Mine(data)
