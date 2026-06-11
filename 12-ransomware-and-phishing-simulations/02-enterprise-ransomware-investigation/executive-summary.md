# Executive Summary

## Incident Overview

A simulated ransomware incident was investigated within a controlled SOC and Incident Response lab environment.

The attack originated from a phishing attachment delivered from an attacker-controlled Kali Linux system. Following execution, the payload established persistence, performed host discovery activities, and simulated ransomware impact by renaming files and creating a ransom note.

The investigation leveraged Sysmon endpoint telemetry and Splunk analysis to reconstruct attacker activity and document the full attack lifecycle.

## Key Findings

* Malicious PowerShell payload executed successfully.
* Persistence established through a scheduled task named UpdateTask.
* Discovery activity performed using:

  * whoami
  * hostname
  * ipconfig
  * net user
* Simulated encryption activity observed.
* Ransom note deployed.
* Persistence mechanism successfully removed during containment.

## Impact Assessment

The simulated attack demonstrated how ransomware operators can maintain access, collect host information, and disrupt business operations through file encryption activity.

## Response Actions

* Identified malicious payload execution.
* Documented indicators of compromise.
* Removed persistence mechanism.
* Contained simulated ransomware activity.
* Documented lessons learned and detection opportunities.

## Conclusion

The investigation successfully reconstructed the ransomware attack lifecycle from initial access through containment and demonstrated incident response, threat hunting, and detection engineering capabilities using enterprise security monitoring workflows.

