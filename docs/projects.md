[Home](index.md) | [About](about.md) | [Certifications](certifications.md) | [Projects](projects.md) | [Contact](contact.md)



# SOC Project Portfolio

This portfolio documents the development of a complete SOC Detection Engineering, Threat Hunting, Incident Response, Threat Intelligence, and SOAR Automation lab environment.

# SOC Project Portfolio

This portfolio documents the development of a complete SOC Detection Engineering, Threat Hunting, Incident Response, Threat Intelligence, and SOAR Automation lab environment.

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

* [Malicious Domain Investigation](../08-threat-intelligence/investigation-01-malicious-domain/README.md)
* [Malicious IP Investigation](../08-threat-intelligence/investigation-02-malicious-ip/README.md)
* [Malware Hash Investigation](../08-threat-intelligence/investigation-03-malware-hash/README.md)
* [MISP Enrichment Investigation](../08-threat-intelligence/investigation-04-misp-enrichment/README.md)
* [Threat Intelligence Driven Hunting](../08-threat-intelligence/investigation-05-threat-intelligence-driven-hunting/README.md)

# 09 - Incident Response
Hands-on Incident Response investigations focused on attacker behaviour validation, evidence collection, log analysis, and MITRE ATT&CK mapping.

Projects include:

* [Lateral Movement Investigation](../09-incident-response/01-lateral-movement-investigation/README.md)
* [Windows Persistence Investigation](../09-incident-response/02-windows-persistence-investigation/README.md)
* [Low and Slow UDP Exfiltration](../09-incident-response/03-low-and-slow-udp-exfiltration/README.md)
* [Fileless PowerShell Beacon Investigation](../09-incident-response/04-fileless-powershell-beacon-investigation/README.md)
* [Incident Response Playbook](../09-incident-response/05-incident-response-playbook/README.md)

# 10 - SOC Investigations

End-to-end SOC investigations combining telemetry, threat intelligence, and analyst workflows.

# 11 - Detection Engineering with Sigma
Development, conversion, validation, and tuning of Sigma detection rules using real telemetry, threat hunting findings, and threat intelligence analysis.

Projects include:

* [PowerShell Encoded Command Detection](../11-detection-engineering-sigma/01-powershell-encoded-command/README.md)
* [Suspicious Parent-Child Detection](../11-detection-engineering-sigma/02-suspicious-parent-child/README.md)
* [Listening Port Discovery Detection](../11-detection-engineering-sigma/03-listening-port-discovery/README.md)
* [Scheduled Task Persistence Detection](../11-detection-engineering-sigma/04-scheduled-task-persistence/README.md)
* [Threat Intelligence Driven Detection](../11-detection-engineering-sigma/05-threat-intelligence-driven-detection/README.md)

# 12 - SOAR Automation


Security Orchestration, Automation, and Response workflows designed to automate investigation and enrichment activities.

# 12 - SOAR Automation

Projects include:

* [IOC Enrichment Playbook](../12-soar-automation/01-ioc-enrichment-playbook/README.md)
* [Scheduled Task Investigation Playbook](../12-soar-automation/03-scheduled-task-investigation-playbook/README.md)
* [Phishing Triage Workflow](../12-soar-automation/04-phishing-triage/README.md)
* [PowerShell Investigation Workflow](../12-soar-automation/05-powershell-investigation/README.md)
* [Threat Intelligence Workflow](../12-soar-automation/06-threat-intelligence-workflow/README.md)


