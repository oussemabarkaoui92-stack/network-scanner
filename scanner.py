import subprocess

# User enters the network
network = input("Enter network (example 192.168.1): ")

active_hosts = 0

print("\nScanning network...\n")

for i in range(1, 21):

    ip = f"{network}.{i}"

    result = subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{ip} --> ACTIVE")
        active_hosts += 1
    else:
        print(f"{ip} --> OFFLINE")

print("\n======================")
print(f"Total active devices: {active_hosts}")
print("======================")