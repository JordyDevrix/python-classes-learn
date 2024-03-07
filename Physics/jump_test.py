from pynput import keyboard
starting_pos = 4.0

def math_function():

    return


def on_key_release(key):
    if key == key.space:
        print(key)


with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
