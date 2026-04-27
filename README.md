# S20: Mapping the Shadows — Network Enumeration

## 🎯 Mission
This project involved mapping a discovered internal subnet (**172.99.0.0/24**) to locate active hosts, identify open ports, and determine running service versions for security documentation.

## ⚙️ Methodology
* **Host Discovery:** Performed a Ping Sweep (`nmap -sn`) to identify live targets.
* **Port Enumeration:** Conducted version scans (`-sV`) and full-range scans (`-p-`) on active hosts.
* **Service Interrogation:** Documented specific software versions for Apache and Redis services.

## 🛠 Tools Used
* **Nmap:** Primary network scanning tool.
* **Ubuntu VM:** Environment for execution.
* **Docker:** Used to host the isolated target network.

## ✅ Results
All three hosts (.5, .6, and .7) were successfully identified and scanned, with results documented in `nmap_scan_results.txt`.

2. Save and Exit (FAST)# S20: Mapping the Shadows - Network Enumeration
This project demonstrates active scanning and network mapping using Nmap within a Dockerized sandbox environment.
