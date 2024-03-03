import subprocess
from pynput.keyboard import Key, Listener
import threading
import time

# This variable is used to control the loop execution
loop_running = True

def on_press(key):
    global loop_running
    # Check if the pressed key is 'q'
    if key.char == 'q':
        loop_running = False
        return False  # Returning False stops the listener

def listen_for_exit_key():
    # Start listening for keypress
    with Listener(on_press=on_press) as listener:
        listener.join()

# Start the key listener in a separate thread
listener_thread = threading.Thread(target=listen_for_exit_key)
listener_thread.start()

print("Press 'q' to exit the loop.")

def main():
    while loop_running:
        subprocess.run(["python", "livestream.py"])
        print('livestream exited!')
        time.sleep(1)
        subprocess.run(["python", "ads.py"])
        print('ads exited!')
        time.sleep(1)

    listener_thread.join()  # Wait for the listener thread to finish
    print("You pressed 'q'. Exiting loop...")
        

main()
