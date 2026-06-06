# SOC Investigations

## Overview

This section contains end-to-end Security Operations Center (SOC) investigations performed using telemetry collected throughout the lab environment.

Investigations combine data from Splunk Enterprise, Sysmon, Windows Event Logs, Threat Intelligence, MITRE ATT&CK, and Detection Engineering activities to identify, investigate, and document suspicious behaviour.

The objective is to simulate the workflow of a SOC Analyst by validating alerts, collecting evidence, correlating multiple data sources, and producing investigation findings.

---

## Objectives

* Perform end-to-end SOC investigations
* Analyze attacker behaviour
* Validate security alerts
* Correlate telemetry across multiple data sources
* Reconstruct attack timelines
* Develop investigative methodologies
* Improve detection coverage
* Produce analyst findings and recommendations

---

## Investigation Workflow

```text
Alert Generated
        ↓
Initial Triage
        ↓
Evidence Collection
        ↓
Threat Hunting
        ↓
Threat Intelligence Correlation
        ↓
MITRE ATT&CK Mapping
        ↓
Investigation Findings
        ↓
Detection Improvement
```

---

## Investigation Areas

### Endpoint Investigations

Projects focus on suspicious process execution, PowerShell activity, persistence mechanisms, and attacker behaviour observed through Sysmon and Windows Event Logs.

Examples include:

* Process Creation Analysis
* Parent-Child Process Investigation
* PowerShell Activity Investigation
* Persistence Validation
* Endpoint Behaviour Analysis

---

### Network Investigations

Projects focus on network activity, communications analysis, and attacker infrastructure identification.

Examples include:

* DNS Analysis
* HTTP Traffic Investigation
* UDP Communication Analysis
* Command and Control Detection
* Data Exfiltration Investigation

---

### Threat Intelligence Investigations

Projects focus on IOC enrichment, adversary infrastructure analysis, and threat intelligence correlation.

Examples include:

* Malicious Domain Investigation
* Malicious IP Investigation
* Malware Hash Investigation
* MISP Intelligence Enrichment
* IOC Correlation

---

### Detection Validation

Projects focus on validating detections generated through Splunk searches, Sigma rules, and threat hunting activities.

Examples include:

* Alert Validation
* Detection Engineering
* Sigma Rule Testing
* Splunk Detection Analysis
* Detection Coverage Assessment

---

## Technologies Used

* Splunk Enterprise
* Sysmon
* Windows Event Logs
* Windows 7
* Kali Linux
* MISP
* MITRE ATT&CK
* Sigma
* PySigma
* PowerShell
* Python
* Wireshark
* BOTSv3 Dataset

---

## Skills Demonstrated

* SOC Analysis
* Security Monitoring
* Alert Triage
* Threat Hunting
* Threat Intelligence Analysis
* Incident Response
* Detection Engineering
* Log Analysis
* Network Traffic Analysis
* IOC Investigation
* MITRE ATT&CK Mapping
* Investigation Reporting

---

## Key Lesson

> Effective SOC investigations require correlating endpoint telemetry, network activity, threat intelligence, and detection data to develop a complete understanding of attacker behaviour.

The ability to collect evidence, validate findings, and improve future detections is a core skill for security operations professionals.
