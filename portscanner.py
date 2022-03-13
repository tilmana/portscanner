import socket
import sys
import threading
import concurrent.futures
import colorama
from colorama import Fore
from pythonping import ping

colorama.init()
print_lock = threading.Lock()

try:
    ip = sys.argv[1]
    type = sys.argv[2]
    if type not in ["q", "f"]:
        print("===================================================\n"
              "                    scanner.py                     \n"
              "  q PORTS 1-1000                   f PORTS 1-65535 \n"
              "===================================================\n")
        sys.exit()
except Exception:
    ip = input("Enter the IP to scan: ")
    type = input("'q' for quick scan, 'f' for full scan: ")

try:
    ms = ping(ip, count=1)
    print(Fore.BLUE + f"Valid IP: {ip}! Proceeding...")
    response = str(ms.rtt_avg_ms)
    if ms.rtt_avg_ms < 50:
        print(Fore.WHITE + "Ping is: " + Fore.LIGHTGREEN_EX + response)
    elif ms.rtt_avg_ms < 200:
        print(Fore.WHITE + "Ping is: " + Fore.YELLOW + response)
    else:
        print(Fore.WHITE + "Ping is: " + Fore.RED + response)

except Exception:
    print(Fore.RED + f"Unable to resolve: {ip}")
    sys.exit()


def scan(ipaddr, ipport):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ipaddr, ipport))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{ipport}]" + Fore.GREEN + " Opened")
    except:
        pass


try:
    if type == "q":
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(1, 1001):
                executor.submit(scan, ip, port)
        input("Waiting to exit...")
    elif type == "f":
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(1, 65536):
                print("Currently scanning port: " + str(port))
                executor.submit(scan, ip, port)
        input("Waiting to exit...")
except Exception:
    print("Closing...")
