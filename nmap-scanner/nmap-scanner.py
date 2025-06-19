# nmap-scanner.py
import subprocess
import os

target = input("Enter target IP or domain: ")
ports = input("Enter port range (e.g., 1-1000 or leave blank for default): ") or "1-1024"

output_file = f"nmap_scan_{target}.txt"
command = ["nmap", "-p", ports, "-sV", target]

print(f"Running Nmap scan on {target} ports {ports}...\n")

try:
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print(result.stdout)

    with open(output_file, "w") as f:
        f.write(result.stdout)
    
    print(f"\nScan complete. Results saved to {output_file}")

except subprocess.CalledProcessError as e:
    print("Error running Nmap:", e)

except FileNotFoundError:
    print("Nmap is not installed or not in PATH.")