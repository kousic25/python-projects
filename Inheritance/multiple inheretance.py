class Camera:
    def take_photo(self):
        print("Photo Captured")
class MusicPlayer:
    def play_music(self):
        print("Playing Music")
class Smartphone(Camera, MusicPlayer):
    def call(self):
        print("Calling...")
phone = Smartphone()
phone.take_photo()
phone.play_music()
phone.call()