# Incident Response

## Overview

This section documents hands-on Incident Response investigations performed within the lab environment.

Projects focus on identifying malicious activity, collecting evidence, validating attacker behaviour, and mapping findings to the MITRE ATT&CK framework.

The investigations combine Windows Event Logs, PowerShell analysis, persistence detection, lateral movement validation, command and control activity, data exfiltration scenarios, and incident response methodologies.

---

## Incident Response Workflow

```text
Alert or Suspicious Activity
            ↓
Evidence Collection
            ↓
Log Analysis
            ↓
Threat Identification
            ↓
Investigation & Validation
            ↓
Containment Strategy
            ↓
Incident Response Assessment
```

---

## Projects

### 01 – Lateral Movement Investigation

Investigation of remote activity between Windows and Kali Linux systems.

Focus Areas:

* Windows Event ID 4688 Analysis
* WMI Remote Execution
* SSH Activity Validation
* Reverse Tunnel Investigation
* MITRE ATT&CK Mapping

Key Techniques:

* T1021 – Remote Services
* T1047 – Windows Management Instrumentation
* T1572 – Protocol Tunnelling

---

### 02 – Windows Persistence Investigation

Investigation of Registry Run Key persistence using Atomic Red Team and custom hunting automation.

Focus Areas:

* Registry Persistence Analysis
* Atomic Red Team Simulation
* PowerShell Event ID 4104 Analysis
* Python Persistence Hunting
* Registry Validation

Key Techniques:

* T1547.001 – Registry Run Keys / Startup Folder
* T1112 – Modify Registry

---

### 03 – Low and Slow UDP Exfiltration

Investigation of low-frequency UDP-based data exfiltration between Windows and Kali Linux systems.

Focus Areas:

* PowerShell Analysis
* UDP Communication Validation
* Packet Capture Analysis
* Wireshark Investigation
* Data Exfiltration Detection

Key Techniques:

* T1048 – Exfiltration Over Alternative Protocol
* T1071 – Application Layer Protocol

---

### 04 – Fileless PowerShell Beacon Investigation

Investigation of a fileless PowerShell beacon operating entirely in memory.

Focus Areas:

* Fileless Malware Analysis
* PowerShell ScriptBlock Logging
* Event ID 4104 Investigation
* Command and Control Activity
* Beacon Detection

Key Techniques:

* T1059.001 – PowerShell
* T1071.001 – Web Protocols
* T1027 – Obfuscated Files or Information

---

### 05 – Incident Response Playbook

Standardised incident response workflow used throughout the lab.

Focus Areas:

* Detection
* Investigation
* Evidence Collection
* Containment
* Eradication
* Recovery
* Lessons Learned

---

## Skills Demonstrated

* Incident Response
* Security Monitoring
* Windows Event Log Analysis
* PowerShell Analysis
* Persistence Detection
* Lateral Movement Investigation
* Command and Control Analysis
* Data Exfiltration Investigation
* Evidence Collection
* MITRE ATT&CK Mapping
* Threat Hunting
* Security Operations

---

## Technologies Used

* Splunk Enterprise
* Sysmon
* Windows 7
* Windows 11
* Kali Linux
* Atomic Red Team
* PowerShell
* Python
* Wireshark
* MITRE ATT&CK

---

## Key Lesson

> Effective incident response depends on accurate evidence collection, thorough investigation, and the ability to correlate activity across multiple data sources.

These projects demonstrate practical incident response workflows used to identify, investigate, and validate malicious activity within a controlled lab environment.

