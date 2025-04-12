import pygame
import time

class MediaPlayer:
    def __init__(self, media_file):
        self.media_file = media_file
        pygame.mixer.init()
        pygame.mixer.music.load(self.media_file)

    def play(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

# Create an instance and control the media
player = MediaPlayer("D:\\SEM - 6\\Vista Engg Hackathon\\gesture_media_player\\WaveTune\\song.mp3")
player.play()
time.sleep(10)
player.stop()
