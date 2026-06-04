# Scheduled Task Investigation Playbook

## Overview

This project demonstrates a SOAR-inspired investigation workflow for suspicious scheduled task creation activity.

The workflow automates the initial triage process by evaluating command-line indicators commonly associated with persistence and malicious PowerShell execution.

The objective is to reduce analyst investigation time and provide a repeatable process for assessing scheduled task alerts.

---

## Scenario

A detection identifies the creation of a scheduled task involving:

```text
PowerShell
      ↓
schtasks.exe
      ↓
/Create
      ↓
SYSTEM
      ↓
Hidden PowerShell
```

The analyst must determine whether the activity represents legitimate administration or malicious persistence.

---

## Automated Workflow

```text
Alert Triggered
      ↓
Extract Command Line
      ↓
Check Parent Process
      ↓
Check SYSTEM Context
      ↓
Check Hidden Execution
      ↓
Check PowerShell Usage
      ↓
Assign Risk Score
      ↓
Generate Analyst Decision
```

---

## Python Automation

The Python script automatically evaluates suspicious characteristics including:

* Scheduled Task Creation
* PowerShell Parent Process
* SYSTEM Execution Context
* Hidden PowerShell
* Invoke-Expression (IEX)
* Download Cradles
* Non-Interactive Execution

The script generates a risk score and analyst recommendation.

---

## Risk Scoring Logic

| Indicator               | Score |
| ----------------------- | ----- |
| Scheduled Task Creation | 20    |
| PowerShell Parent       | 20    |
| SYSTEM Context          | 20    |
| Hidden Execution        | 15    |
| IEX Usage               | 20    |
| DownloadString Usage    | 20    |

---

## MITRE ATT&CK Mapping

### T1053.005 – Scheduled Task

Adversaries may create scheduled tasks to execute malware or maintain persistence.

### T1059.001 – PowerShell

PowerShell may be used to execute malicious payloads.

### T1027 – Obfuscated Files or Information

Hidden or obfuscated execution may indicate defense evasion.

---

## Skills Demonstrated

* SOAR Concepts
* Incident Response
* Python Automation
* PowerShell Investigation
* Persistence Analysis
* Detection Triage
* MITRE ATT&CK Mapping
* SOC Operations

---

## Key Learning Outcome

> Automation should reduce analyst workload while preserving investigation quality.
