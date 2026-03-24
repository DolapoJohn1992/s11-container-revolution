# 🧭 Traveler’s Guide: Session 07 - The Automation Forge

## 🏫 Institutional Credit
**Fellowship:** The Knowledge House (TKH)
**Program:** Cybersecurity Fellowship 2026
**Track:** Network Security & Python Automation
**Reference:** Pillar 3, Session 07 | The Automation Forge  

---

## 🎯 Mission: Operation Port-Scan
**Objective:** Transition from a "passenger" to a "pilot" by building a Python tool to audit digital doors (Ports) across multiple server targets.

---

## 🛠️ Project Overview
This project is a Python-based network utility built to automate the "knocking" process on five different servers to identify active SSH services (Port 22). It replaces manual `ssh` attempts with programmatic logic.

### 🧪 Phase 1: The ID Checker (Logic Foundations)
- **Goal:** Understand how computers handle lists and decisions.
- **Outcome:** Built a logic gate using `if/else` to verify authorized users within the TKH lab environment.

### 🛡️ Phase 2: The Port-Scanner (Network Audit)
- **Goal:** Build a permanent script to audit network targets.
- **Reference File:** `~/lab_prep/target_intel.txt`
- **Core Technology:** Python `socket` library for TCP handshakes.

---

## 🚀 Technical Implementation
1. **Target List**: IPs are stored in a Python list for batch processing.
2. **The Loop**: A `for` loop iterates through each target to ensure efficiency.
3. **The Socket**:
   - `socket.AF_INET`: Specifies IPv4.
   - `socket.SOCK_STREAM`: Specifies TCP protocol.
   - `s.settimeout(1)`: Ensures the script doesn't hang on dead IPs.
4. **The "Knock"**: `s.connect_ex((ip, 22))` returns `0` if the door is open.

## 📈 Results & Artifacts
- **Verified Open Port:** `127.0.0.1` (SSH Port 22 - OPEN)
- **Submission Artifact:** `~/port_check.py`
- **Official Status:** MISSION COMPLETE (Logged at `~/SESSION_04_FINAL.txt`)

---

## 🧠 Skills Mastered
- **Automation**: Moving from manual commands to reusable scripts.
- **Repo Hygiene**: Organizing projects into dedicated directories (`~/Session_07_Forge`).
- **Network Reconnaissance**: Identifying surface area vulnerabilities (Port 22).

---
*Developed by DolapoJohn1992 | The Knowledge House Cybersecurity Portfolio*
