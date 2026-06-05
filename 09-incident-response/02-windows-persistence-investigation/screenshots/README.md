# Incident Response Investigation 02 – Windows Registry Persistence Detection

## Overview

This investigation documents the identification and validation of a Windows Registry Run Key persistence mechanism using Atomic Red Team simulation and a custom Python-based persistence hunting tool.

The objective was to determine whether persistence artifacts could be established on a Windows endpoint and successfully detected through manual investigation and automated analysis.

---

## Scenario

A registry-based persistence technique was simulated using Atomic Red Team (MITRE ATT&CK T1547.001).

The simulation created a Registry Run Key configured to execute automatically during user logon.

An incident response investigation was then conducted to identify the persistence mechanism, validate the registry modification, and assess the effectiveness of the detection process.

---

## Investigation Workflow

```text
Persistence Simulation Executed
          ↓
Registry Run Key Created
          ↓
Manual Registry Validation
          ↓
Automated Persistence Hunting
          ↓
Suspicious Entry Identified
          ↓
Evidence Exported
          ↓
Incident Response Assessment
```

---

## Environment

| Component        | Specification                                |
| ---------------- | -------------------------------------------- |
| Operating System | Windows 11 ARM64 (UTM on macOS)              |
| User Privileges  | Non-Administrator (UAC Enabled)              |
| Network          | Isolated Lab Environment                     |
| Tools            | Atomic Red Team, Python 3.14, PowerShell 5.1 |

---

## Attack Simulation

The Atomic Red Team simulation executed MITRE ATT&CK technique:

```text
T1547.001
Boot or Logon Autostart Execution
Registry Run Keys / Startup Folder
```

PowerShell execution:

```powershell
Import-Module "C:\AtomicRedTeam\invoke-atomicredteam\Invoke-AtomicRedTeam.psd1" -Force
Invoke-AtomicTest T1547.001 -TestNumbers 1
```

The simulation created a Registry Run Key under:

```text
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

which executed automatically when the user logged on.

---

## Detection Methodology

### Manual Registry Validation

The Registry Run Key was manually reviewed using:

```powershell
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

The investigation confirmed the presence of the Atomic Red Team persistence entry.

### Automated Persistence Hunting

A custom Python persistence scanner was developed to examine:

* Registry Run Keys
* Registry RunOnce Keys
* Startup Folders
* Scheduled Tasks
* Windows Services
* WMI Subscriptions

The scanner successfully identified the persistence artifact and marked it as suspicious.

---

## Evidence

### Registry Persistence Detection

![Registry Persistence Detection](screenshots/01-registry-persistence-detection.png)

The Registry Run Key investigation identified a persistence entry associated with the Atomic Red Team simulation.

---

### Persistence Hunting Results

![Persistence Hunting Results](screenshots/02-persistence-hunting-results.png)

The custom Python scanner successfully detected the persistence mechanism and exported the results to a CSV report.

---

## Windows Event Log Analysis

PowerShell ScriptBlock Logging (Event ID 4104) captured the execution of the Atomic Red Team persistence activity.

Relevant event sources included:

| Event ID | Log Source             | Investigation Value         |
| -------- | ---------------------- | --------------------------- |
| 4104     | PowerShell Operational | Full Script Block Logging   |
| 4657     | Security               | Registry Value Modification |
| 4688     | Security               | Process Creation            |

The captured artifacts provided additional validation of the persistence activity.

---

## Key Findings

### Registry-Based Persistence

A Registry Run Key persistence mechanism was successfully created and validated.

![Persistence Hunting Results](screenshots/02-persistence-hunting-results.png)

### Automated Detection

The Python hunting tool identified the persistence artifact and generated evidence suitable for investigation and reporting.

### Investigation Validation

Manual registry inspection confirmed the persistence mechanism and validated the automated hunting results.

---

## MITRE ATT&CK Mapping

| Tactic          | Technique                         | ID        |
| --------------- | --------------------------------- | --------- |
| Persistence     | Boot or Logon Autostart Execution | T1547.001 |
| Defense Evasion | Modify Registry                   | T1112     |

---

## Incident Response Assessment

The investigation confirmed successful creation of a Registry Run Key persistence mechanism.

The persistence artifact was identified through both manual validation and automated analysis.

The combination of registry inspection, PowerShell logging, and custom hunting automation provided multiple sources of evidence supporting the investigation findings.

No additional persistence mechanisms were identified during this investigation.

---

## Skills Demonstrated

* Incident Response
* Persistence Investigation
* Windows Registry Analysis
* MITRE ATT&CK Mapping
* Atomic Red Team Validation
* Python Security Automation
* Evidence Collection
* Windows Event Log Analysis

---

## Key Lesson

> Registry Run Keys remain one of the most common persistence mechanisms used by attackers and should be routinely reviewed during incident response investigations.

This investigation demonstrated how persistence techniques can be identified through registry analysis, PowerShell logging, automated hunting, and evidence validation.








## Evidence

### Registry Persistence Detection



The Registry Run Key investigation identified a persistence entry associated with the Atomic Red Team simulation.

---

### Persistence Hunting Results



The custom Python scanner successfully detected the persistence mechanism and exported the results to a CSV report.
