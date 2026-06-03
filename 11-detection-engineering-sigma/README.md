# Detection Engineering with Sigma

## Overview

This section focuses on developing, validating, and tuning detections using Sigma rules and Splunk Enterprise.

The objective is to transform threat hunting findings into reusable detections that can be translated across multiple SIEM platforms while maintaining visibility into attacker techniques and behaviors.

Throughout these projects, detections were developed from real BOTSv3 telemetry, converted into Splunk SPL using PySigma, and validated against actual endpoint events.

---

# Objectives

* Develop Sigma detection rules
* Map detections to MITRE ATT&CK
* Convert Sigma detections into Splunk SPL using PySigma
* Validate detections against BOTSv3 telemetry
* Tune detections for real-world data sources
* Improve detection engineering skills
* Support SOC monitoring and threat hunting operations

---

# Detection Engineering Workflow

Each project follows a structured detection engineering methodology:

```text
Threat Hunting
      ↓
Telemetry Analysis
      ↓
Detection Development
      ↓
Sigma Rule Creation
      ↓
PySigma Conversion
      ↓
Splunk Validation
      ↓
Detection Tuning
      ↓
Final Detection
```

This mirrors the workflow commonly used by Detection Engineers, Threat Hunters, and SOC Analysts when transforming investigative findings into production-ready detections.

---

# Projects

## 01 – PowerShell Encoded Command Detection

Detection of suspicious PowerShell execution involving encoded commands.

### Skills Demonstrated

* PowerShell Analysis
* Sigma Rule Development
* Splunk Detection Validation
* ATT&CK Mapping

### ATT&CK Mapping

* T1059.001 – PowerShell
* T1027 – Obfuscated Files or Information

---

## 02 – Suspicious Parent-Child Process Detection

Detection of unusual process relationships involving:

```text
fodhelper.exe
      ↓
powershell.exe
```

The project demonstrates how parent-child process analysis can be used to identify suspicious execution chains associated with privilege escalation and defense evasion activity.

### Skills Demonstrated

* Process Analysis
* Parent-Child Relationship Investigation
* Detection Engineering
* Sigma Development

### ATT&CK Mapping

* T1059.001 – PowerShell
* T1548 – Abuse Elevation Control Mechanism
* T1548.002 – Bypass User Account Control

---

## 03 – Network Discovery Detection

Detection of network and service enumeration activity using tools such as:

```text
netstat
findstr
```

The project demonstrates how discovery activity can be identified through process creation telemetry and converted into reusable Sigma detections.

### Skills Demonstrated

* Discovery Detection
* Command-Line Analysis
* Sigma Development
* Splunk Validation

### ATT&CK Mapping

* T1046 – Network Service Discovery

---

## 04 – Scheduled Task Persistence Detection

Detection of suspicious scheduled task creation initiated through PowerShell.

The project originated from threat hunting activities within the BOTSv3 dataset and evolved into a complete detection engineering case study.

The detection identifies:

```text
PowerShell
      ↓
schtasks.exe
      ↓
Scheduled Task Creation
```

The Sigma rule was converted into Splunk SPL using PySigma and validated against real Sysmon telemetry.

Validation confirmed a high-confidence event involving:

```text
PowerShell
      ↓
schtasks.exe /Create
      ↓
SYSTEM Execution
      ↓
Hidden PowerShell Activity
```

### Skills Demonstrated

* Threat Hunting
* Detection Engineering
* Sigma Rule Development
* PySigma Conversion
* Splunk Validation
* Detection Tuning
* Process Analysis
* ATT&CK Mapping

### ATT&CK Mapping

* T1053.005 – Scheduled Task
* T1059.001 – PowerShell
* T1027 – Obfuscated Files or Information

---

# Key Learning Outcomes

Through these projects, the following detection engineering concepts were demonstrated:

* Threat Hunting Driven Detection Development
* Sigma Rule Authoring
* Cross-Platform Detection Portability
* PySigma Query Translation
* Splunk SPL Development
* Detection Validation
* Detection Tuning
* MITRE ATT&CK Mapping
* Process Creation Analysis
* Adversary Behavior Identification

---

# Conclusion

This section demonstrates the complete lifecycle of modern detection engineering, from threat hunting and telemetry analysis through Sigma development, PySigma conversion, Splunk integration, validation, and ATT&CK mapping.

Rather than relying solely on predefined signatures, detections were developed from real telemetry and validated through investigative analysis, closely reflecting the workflows used by SOC Analysts, Threat Hunters, and Detection Engineers in operational environments.

