import pygame
import time

# Initialize pygame mixer for media control
pygame.mixer.init()

# Load a media file (adjust path to your media)
pygame.mixer.music.load("D:\\SEM - 6\\Vista Engg Hackathon\\gesture_media_player\\WaveTune\\song.mp3")  # Replace with your media file path

# Start playing the media
pygame.mixer.music.play()

# Wait for some time before stopping
time.sleep(10)
pygame.mixer.music.stop()  # Stop media after 10 seconds
