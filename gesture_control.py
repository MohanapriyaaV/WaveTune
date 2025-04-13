# Dummy gesture control function
def gesture_to_action(gesture, player):
    print("Gesture Detected:", gesture)

    if gesture == "play":
        player.play()
    elif gesture == "pause":
        player.pause()
    elif gesture == "unpause":
        player.unpause()
    elif gesture == "stop":
        player.stop()
