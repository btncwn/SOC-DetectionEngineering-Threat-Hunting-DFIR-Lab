[Home](index.md) | [About](about.md) | [Certifications](certifications.md) | [Projects](projects.md) | [Contact](contact.md)



# SOC Project Portfolio

This portfolio documents the development of a complete SOC Detection Engineering, Threat Hunting, Incident Response, Threat Intelligence, and Ransomware Investigations & Phishing Analysis.


## Repository Structure

[![Tree diagram](./assets/tree.png)](./assets/tree.png)

# Core Technologies

* Splunk Enterprise
* Sysmon
* Windows 7
* Windows 11
* Kali Linux
* Nessus
* Docker
* Docker Compose
* MISP
* Sigma
* PySigma
* PowerShell
* Python
* Wireshark
* MITRE ATT&CK
* BOTSv3 Dataset
* Threat Intelligence Analysis
* Detection Engineering
* Incident Response
* SOAR Automation


# 01 - Lab Architecture

Design and implementation of the lab environment including Splunk, Windows, Kali Linux, and supporting security tools.


# 02 - Vulnerability Assessment

Vulnerability assessment activities using Nessus.

Projects include:

* Vulnerability discovery
* Risk analysis
* Remediation recommendations
* Security assessment reporting


# 03 - Attack Simulation

Controlled attack simulations used to generate telemetry and investigative artifacts.

Projects include:

* SMB Enumeration
* Network Reconnaissance
* PowerShell Execution
* Remote Execution Simulation


# 04 - Endpoint Telemetry

Endpoint visibility using Sysmon.

Projects include:

* Sysmon deployment
* Sysmon configuration
* Event analysis
* Process monitoring


# 05 - Splunk Ingestion

Data onboarding and log management using Splunk Enterprise.

Projects include:

* Universal Forwarder deployment
* Index configuration
* Data validation
* Search optimization


# 06 - Threat Hunting

Threat hunting investigations using BOTSv3 and Sysmon telemetry.

Projects include:

* Process analysis
* Parent-child investigation
* PowerShell hunting
* Network activity analysis
* Attack timeline reconstruction


# 07 - MITRE ATT&CK Mapping

Mapping observed attacker behaviors to MITRE ATT&CK techniques and tactics.

Projects include:

* ATT&CK mapping
* Detection coverage analysis
* Technique documentation

  # 08 - Threat Intelligence


Projects include:

* [Malicious Domain Investigation](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/08-threat-intelligence/investigation-01-malicious-domain)
* [Malicious IP Investigation](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/08-threat-intelligence/investigation-02-malicious-ip)
* [Malware Hash Investigation](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/08-threat-intelligence/investigation-03-malware-hash)
* [MISP Enrichment Investigation](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/08-threat-intelligence/investigation-04-misp-enrichment)
* [Threat Intelligence Driven Hunting](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/08-threat-intelligence/investigation-05-threat-intelligence-driven-hunting)


# 09 - Incident Response
Hands-on Incident Response investigations focused on attacker behaviour validation, evidence collection, log analysis, and MITRE ATT&CK mapping.
Projects include:

* [Lateral Movement Investigation](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/09-incident-response/01-lateral-movement-investigation)
* [Windows Persistence Investigation](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/09-incident-response/02-windows-persistence-investigation)
* [Low and Slow UDP Exfiltration](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/09-incident-response/03-low-and-slow-udp-exfiltration)
* [Fileless PowerShell Beacon Investigation](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/09-incident-response/04-fileless-powershell-beacon-investigation)
* [Incident Response Playbook](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/09-incident-response/05-incident-response-playbook)




# 10 - SOC Investigations

End-to-end SOC investigations combining telemetry, threat intelligence, and analyst workflows.

# 11 - Detection Engineering with Sigma
Development, conversion, validation, and tuning of Sigma detection rules using real telemetry, threat hunting findings, and threat intelligence analysis.

Projects include:

* [PowerShell Encoded Command Detection](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/11-detection-engineering-sigma/01-powershell-encoded-command)
* [Suspicious Parent-Child Detection](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/11-detection-engineering-sigma/02-suspicious-parent-child)
* [Listening Port Discovery Detection](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/11-detection-engineering-sigma/03-listening-port-discovery)
* [Scheduled Task Persistence Detection](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/11-detection-engineering-sigma/04-scheduled-task-persistence)
* [Threat Intelligence Driven Detection](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/11-detection-engineering-sigma/05-threat-intelligence-driven-detection)


# 12 - Ransomware & Phishing Simulations

Hands-on ransomware investigations, phishing analysis, IOC enrichment, and investigation workflows designed to simulate real-world Security Operations Center (SOC) and Incident Response activities.

Projects include:

* [IOC Enrichment Playbook](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/12-ransomware-and-phishing-simulations/01-ioc-enrichment-playbook)

* [Enterprise Ransomware Investigation](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/12-ransomware-and-phishing-simulations/02-enterprise-ransomware-investigation)

* [Scheduled Task Investigation Playbook](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/12-ransomware-and-phishing-simulations/03-scheduled-task-investigation-playbook)

* [Phishing Triage Workflow](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/12-ransomware-and-phishing-simulations/04-phishing-triage)

* [PowerShell Investigation Workflow](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/12-ransomware-and-phishing-simulations/05-powershell-investigation)

* [Threat Intelligence Workflow](https://github.com/btncwn/SOC-IR-Threat-Hunting-Detection-Engineering-SOAR-Lab/tree/main/12-ransomware-and-phishing-simulations/06-threat-intelligence-workflow)


