class MP4:
    def play(self):
        print("Playing MP4 Video")
class AVI:
    def play(self):
        print("Playing AVI Video")
class MKV:
    def play(self):
        print("Playing MKV Video")
videos = [MP4(), AVI(), MKV()]
for video in videos:
    video.play()