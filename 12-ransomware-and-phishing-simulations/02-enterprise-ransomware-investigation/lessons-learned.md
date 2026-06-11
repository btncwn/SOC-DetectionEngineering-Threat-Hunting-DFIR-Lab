# Lessons Learned

## Executive Summary

A simulated ransomware intrusion was successfully investigated from initial access through containment using endpoint telemetry, threat intelligence concepts, and incident response procedures.

The investigation demonstrated how attacker activity can be reconstructed using Sysmon telemetry and Splunk analysis.

---

## Root Cause

The attack originated from the execution of a malicious phishing attachment:

Invoice_2026.pdf.ps1

The attachment launched a secondary PowerShell payload which established persistence, performed discovery activity, and simulated ransomware impact.

---

## Detection Opportunities

### Initial Access

Improve detection of:

- Suspicious PowerShell downloads
- Phishing attachments
- External file retrieval

### Execution

Monitor:

- PowerShell execution
- ExecutionPolicy Bypass usage
- Script execution from user directories

### Persistence

Monitor:

- schtasks.exe execution
- Scheduled task creation
- Registry persistence mechanisms

### Discovery

Monitor:

- whoami
- hostname
- ipconfig
- net user

### Impact

Monitor:

- File renaming activity
- Ransom note creation
- Mass file modification events

---

## Response Improvements

- Faster phishing identification
- Automated IOC enrichment
- Automated threat intelligence correlation
- Improved endpoint visibility

---

## Preventive Controls

- User awareness training
- PowerShell logging
- Application control
- Endpoint detection and response
- Network segmentation
- Email filtering

---

## Skills Demonstrated

- Incident Response
- Threat Hunting
- Detection Engineering
- Sysmon Analysis
- Splunk Analysis
- MITRE ATT&CK Mapping
- Threat Intelligence
- Security Operations

---

## Key Lesson

Effective ransomware investigations require the correlation of endpoint telemetry, attacker behavior, threat intelligence, and analyst decision-making to accurately understand and contain malicious activity.
