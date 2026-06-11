# Enterprise Ransomware Investigation Workflow

## Environment

Kali Linux
↓
Windows 7
↓
Sysmon
↓
Splunk
↓
TheHive
↓
MISP

---

## Investigation Lifecycle

### Phase 1 – Initial Access

Identify how the attacker gained access to the system.

Evidence:

* Source IP
* User Account
* Initial Process
* Authentication Events

---

### Phase 2 – Execution

Identify malicious execution activity.

Evidence:

* Process Creation Events
* Command Line Activity
* PowerShell Activity
* Script Execution

---

### Phase 3 – Persistence

Determine whether persistence mechanisms were established.

Evidence:

* Scheduled Tasks
* Registry Run Keys
* Services
* Startup Items

---

### Phase 4 – Discovery

Identify reconnaissance activity.

Evidence:

* File Enumeration
* User Enumeration
* Network Discovery
* System Discovery

---

### Phase 5 – Impact

Identify ransomware execution and business impact.

Evidence:

* File Modifications
* Encryption Activity
* Ransom Notes
* Process Activity

---

### Phase 6 – Containment

Document response actions.

Examples:

* Host Isolation
* IOC Blocking
* User Disablement
* Malware Removal

---

### Phase 7 – Lessons Learned

Document:

* Root Cause
* Detection Opportunities
* Response Improvements
* Preventive Controls

---

## Investigation Outcome

Threat Intelligence
+
Telemetry
+
Incident Response
=
Ransomware Investigation

