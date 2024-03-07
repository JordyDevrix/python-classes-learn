from pynput import keyboard
starting_pos = 2.0


def math_function(x):
    y = x**2
    return y


def on_key_release(key):
    if key == key.space:
        print(math_function(starting_pos))
    elif key == 'q':
        exit(0)


def main():
    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()


if __name__ == '__main__':
    main()


