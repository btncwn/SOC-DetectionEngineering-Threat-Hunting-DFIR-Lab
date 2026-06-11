# Investigation Timeline

## Overview

This timeline reconstructs the attack sequence observed during the ransomware investigation.

The objective is to understand attacker actions, identify key events, and support incident response activities.

# Investigation Timeline

| Phase | Activity | Evidence |
|---------|---------|---------|
| Initial Access | Invoice_2026.pdf.ps1 downloaded from Kali web server | Kali HTTP logs |
| Execution | PowerShell payload executed | Sysmon Event ID 1 |
| Persistence | UpdateTask scheduled task created | schtasks.exe |
| Discovery | whoami, hostname, ipconfig, net user | Sysmon telemetry |
| Impact | budget.xlsx renamed to budget.locked | File system evidence |
| Impact | README_RESTORE_FILES.txt created | Ransom note |
| Containment | UpdateTask removed | schtasks /delete |
| Closure | Investigation completed | Findings |
## Attack Progression

Initial Access
↓
Execution
↓
Persistence
↓
Discovery
↓
Impact
↓
Detection
↓
Containment

---

## Analyst Notes

The timeline will be updated as additional evidence is collected during the investigation.

Correlating events across Sysmon, Splunk, TheHive, and MISP improves analyst visibility and supports accurate incident reconstruction.

