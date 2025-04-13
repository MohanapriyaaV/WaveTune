import pygame

class MediaPlayer:
    def __init__(self, media_file):
        self.media_file = media_file
        pygame.mixer.init()
        pygame.mixer.music.load(self.media_file)

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
