# portscanner

Quick and color coded Python3 port scanner. Requires sudo/sudo-like permissions to run properly. After program execution, it will wait for input before closing. 


usage: python3 portscanner.py {IP} {q or f}

q: ports 1-1024 (well-known ports)
f: ports 1-65535 (all ports)


Weaknesses:

**requires sudo, does not return filtered ports**

Useful for CTFs as I have used it personally, as it is faster than nmap when the above conditions are not issues.
