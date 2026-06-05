# Incident Response Investigation 02 – Windows Persistence Investigation

## Overview

This investigation documents the identification and validation of Windows persistence mechanisms using Atomic Red Team simulation and a custom persistence hunting tool.

The objective was to determine whether persistence artifacts could be established on the endpoint and successfully detected through manual investigation and automated analysis.

---

## Investigation Workflow

```text
Persistence Simulation Executed
        ↓
Registry Run Key Created
        ↓
Manual Validation Performed
        ↓
Persistence Hunting Tool Executed
        ↓
Suspicious Entry Identified
        ↓
Evidence Collected
        ↓
Incident Response Assessment
```

---

## Evidence Collected

### Registry Persistence Detection

![Registry Persistence Detection](screenshots/01-registry-persistence-detection.png)

The Registry Run Key investigation identified a suspicious persistence entry associated with Atomic Red Team testing.

---

### Persistence Hunting Results

![Persistence Hunting Results](screenshots/02-persistence-hunting-results.png)

A custom persistence hunting tool successfully identified and flagged the persistence mechanism as suspicious.

---

## Key Findings

### Registry Run Key Persistence

A persistence mechanism was identified within:

```text
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

The entry was configured to launch automatically during user logon.

### Automated Detection

The custom hunting tool successfully detected the persistence artifact and generated evidence suitable for incident response investigations.

### Validation

Manual review confirmed the registry modification and validated the automated detection results.

---

## MITRE ATT&CK Mapping

| Technique                         | ID        | Description                           |
| --------------------------------- | --------- | ------------------------------------- |
| Boot or Logon Autostart Execution | T1547.001 | Registry Run Keys and Startup Folder  |
| Modify Registry                   | T1112     | Registry modification for persistence |

---

## Incident Response Assessment

The investigation confirmed successful creation of a Registry Run Key persistence mechanism.

The persistence artifact was identified through both manual validation and automated analysis.

No additional persistence mechanisms were identified during this investigation.

---

## Skills Demonstrated

* Incident Response
* Windows Registry Analysis
* Persistence Investigation
* MITRE ATT&CK Mapping
* Atomic Red Team
* Python Security Automation
* Evidence Collection
* Security Monitoring

---

## Key Lesson

> Registry Run Keys remain one of the most common persistence mechanisms used by attackers and should be routinely reviewed during incident response investigations.

This investigation demonstrated how persistence techniques can be identified through registry analysis, automated hunting, and evidence validation.

