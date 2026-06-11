# Enterprise Ransomware Investigation

## Overview

This project demonstrates a simulated enterprise ransomware investigation performed within a home SOC, Threat Hunting, and Incident Response lab.

The investigation follows the complete ransomware lifecycle from initial access through containment using endpoint telemetry, security monitoring, and threat intelligence concepts.

The objective was to identify attacker activity, reconstruct the attack timeline, document indicators of compromise, assess impact, and demonstrate incident response procedures.

---

## Lab Environment

Kali Linux

↓

Windows 7 Victim

↓

Sysmon

↓

Splunk

↓

TheHive

↓

MISP

---

## Investigation Objectives

* Identify attacker activity
* Reconstruct the attack timeline
* Identify indicators of compromise
* Map activity to MITRE ATT&CK
* Assess business impact
* Document containment actions
* Produce incident response findings

---

## Investigation Lifecycle

### Phase 1 – Initial Access

A phishing attachment was hosted on a Kali Linux system and delivered to the victim endpoint.

Evidence:

* Invoice_2026.pdf.ps1
* Kali HTTP server logs

MITRE ATT&CK:

* T1566.001 – Spearphishing Attachment

---

### Phase 2 – Execution

The phishing attachment launched a secondary PowerShell payload.

Evidence:

* PowerShell execution
* Sysmon Event ID 1

MITRE ATT&CK:

* T1059.001 – PowerShell

---

### Phase 3 – Persistence

A scheduled task named UpdateTask was created to maintain persistence.

Evidence:

* schtasks.exe execution
* Sysmon Event ID 1

MITRE ATT&CK:

* T1053.005 – Scheduled Task

---

### Phase 4 – Discovery

The payload executed discovery commands:

* whoami
* hostname
* ipconfig
* net user

MITRE ATT&CK:

* T1033 – System Owner/User Discovery
* T1082 – System Information Discovery
* T1016 – System Network Configuration Discovery
* T1087 – Account Discovery

---

### Phase 5 – Impact

The ransomware payload simulated encryption activity.

Evidence:

* budget.xlsx renamed to budget.locked
* README_RESTORE_FILES.txt created

MITRE ATT&CK:

* T1486 – Data Encrypted for Impact

---

### Phase 6 – Containment

Incident response actions included:

* Scheduled task removal
* Payload removal
* IOC documentation
* Investigation closure

---

### Phase 7 – Lessons Learned

Detection opportunities and preventive controls were identified to improve future ransomware detection and response capabilities.

---

## Investigation Deliverables

* Investigation Timeline
* Indicators of Compromise (IOCs)
* MITRE ATT&CK Mapping
* Incident Findings
* Containment Actions
* Lessons Learned

---

## Screenshots

* 01-sysmon-events-ingested.png
* 02-kali-hosting-payload.png
* 03-initial-access-and-execution-evidence.png
* 04-persistence-scheduled-task-created.png
* 05-discovery-reconnaissance-activity.png
* 06-ransomware-impact.png
* 07-containment-persistence-removal.png

---

## Skills Demonstrated

* Incident Response
* Threat Hunting
* Detection Engineering
* Threat Intelligence
* Sysmon Analysis
* Splunk Analysis
* MITRE ATT&CK Mapping
* IOC Analysis
* Security Operations
* Ransomware Investigation

---

## Key Lesson

Effective ransomware investigations require the correlation of endpoint telemetry, attacker behavior, threat intelligence, and analyst decision-making to accurately understand, contain, and document malicious activity.

