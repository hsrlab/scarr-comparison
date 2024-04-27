import subprocess
import time

def evict_file(filename):
    try:
        subprocess.run(["vmtouch", "-e", filename, " > /dev/null"],
        stdout = subprocess.DEVNULL,
        stderr = subprocess.DEVNULL,
        check=True)
        time.sleep(60)
        # print(f"{filename} evicted from cache successfully.")
    except subprocess.CalledProcessError:
        print(f"Error evicting {filename} from cache.")
