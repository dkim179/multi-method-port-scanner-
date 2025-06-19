# port-scanner.py
import socket
import threading
from queue import Queue
from datetime import datetime
from colorama import init, Fore

init()

target = input("Target IP or domain: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))
output_file = "scan_results.txt"

print(f"\nStarting scan on {target} ({start_port} ~ {end_port})\n")

# Queue to manage ports
port_queue = Queue()

# Create or clear output file
with open(output_file, "w") as f:
    f.write(f"Port scan result for {target} ({datetime.now()}):\n\n")

def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            line = f"[OPEN] Port {port} → {service}"
            print(Fore.GREEN + line)
            with open(output_file, "a") as f:
                f.write(line + "\n")
        sock.close()
    except:
        pass

def worker():
    while not port_queue.empty():
        port = port_queue.get()
        scan(port)
        port_queue.task_done()

# Fill queue
for port in range(start_port, end_port + 1):
    port_queue.put(port)

# Launch threads
thread_count = 100
threads = []

for _ in range(thread_count):
    thread = threading.Thread(target=worker)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(Fore.CYAN + f"\nScan complete. Results saved in {output_file}")