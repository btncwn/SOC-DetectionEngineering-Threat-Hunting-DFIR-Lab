# Lessons Learned

## Overview

This project began as a traditional threat intelligence exercise focused on identifying indicators of compromise associated with the Space Pirates threat actor.

Initially, the objective was to create detections based on indicators such as file hashes, domains, and IP addresses.

During the investigation, a more important detection engineering lesson emerged.

---

# Key Lesson

> Hashes change. IPs change. Domains change. Behaviors persist.

Threat actors frequently modify infrastructure and malware samples in order to evade detection.

Examples include:

* Registering new domains
* Rotating IP addresses
* Recompiling malware
* Changing hashes
* Repackaging payloads

As a result, detections based solely on indicators often have a limited operational lifespan.

Behavioral detections remain effective because they focus on attacker actions rather than attacker infrastructure.

---

# Intelligence vs Detection

A major lesson learned during this project was the difference between intelligence collection and detection engineering.

Traditional IOC-based thinking:

```text
Threat Report
        ↓
Hash
        ↓
Detection
```

Detection Engineering thinking:

```text
Threat Report
        ↓
Behavior
        ↓
Detection
```

The second approach provides significantly greater resilience against attacker changes.

---

# Threat Intelligence Operationalization

The Space Pirates intelligence report was used to identify behaviors associated with PlugX RAT.

Rather than creating a detection for a single indicator, the intelligence was translated into multiple behavioral detections including:

* PowerShell execution
* Scheduled task creation
* Service manipulation
* Network discovery activity

This demonstrates how threat intelligence can be operationalized into practical monitoring content.

---

# Sigma Rule Development

The project reinforced the value of Sigma as a platform-independent detection language.

Benefits observed:

* Vendor-neutral detection format
* Reusable detection logic
* Simplified ATT&CK mapping
* Easy conversion into SIEM-specific queries

---

# PySigma Conversion

PySigma successfully translated behavioral detections into Splunk SPL.

This demonstrated how detection content can be maintained in a common format while supporting multiple SIEM platforms.

The conversion process also highlighted the importance of validating generated queries against real telemetry.

---

# Detection Validation

A key finding was that successful Sigma conversion does not automatically guarantee successful SIEM detection.

Validation is required to confirm:

* Field availability
* Data quality
* Telemetry coverage
* Parsing accuracy
* Search performance

This mirrors real-world detection engineering workflows.

---

# ATT&CK-Based Detection Engineering

MITRE ATT&CK provided a useful framework for organizing detections around adversary behaviors.

Mapping detections to ATT&CK techniques improved:

* Detection coverage visibility
* Threat hunting alignment
* Adversary emulation planning
* Reporting consistency

---

# Professional Takeaway

This project demonstrates the transition from:

```text
IOC Consumer
```

to:

```text
Detection Engineer
```

Rather than asking:

```text
What is the bad hash?
```

the better question becomes:

```text
What behavior does the attacker need to perform?
```

That mindset creates detections that remain valuable long after individual indicators become obsolete.

---

# Final Reflection

Threat intelligence becomes most valuable when it drives detection development.

The combination of:

```text
Threat Intelligence
        ↓
ATT&CK Mapping
        ↓
Behavior Analysis
        ↓
Sigma Rule Development
        ↓
PySigma Conversion
        ↓
Splunk Validation
```

provides a repeatable methodology for transforming intelligence into actionable security monitoring content.
