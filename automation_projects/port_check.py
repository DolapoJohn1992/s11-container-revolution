import socket

targets = ["127.0.0.1", "8.8.8.8", "1.1.1.1", "10.0.0.1"]

for ip in targets:
    print(f"--- Checking Server: {ip} ---")
    
    # Setup the connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    # The Knock (Port 22)
    result = s.connect_ex((ip, 22))
    
    # The Decision Gate
    if result == 0:
        print(f"SUCCESS: Port 22 is OPEN on {ip}")
    else:
        print(f"FAILED: Port 22 is CLOSED on {ip}")
        
    s.close()