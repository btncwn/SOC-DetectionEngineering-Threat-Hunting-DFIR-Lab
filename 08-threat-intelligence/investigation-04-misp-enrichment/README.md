# Investigation 04 – MISP Threat Intelligence Enrichment

## Overview

This investigation extends the findings from Investigation 03 by enriching a suspicious SHA256 hash using MISP.

During Investigation 03, the executable:

```text
C:\Windows\Temp\hdoor.exe
```

was identified executing from a temporary directory and performing internal network enumeration.

The investigation extracted the following SHA256 hash:

```text
99925199059EE049F7AEDA8904C2F5BDFBA86671FD7A5989BD60B72F26EF737C
```

The objective of this investigation is to determine whether the hash is known to threat intelligence sources, assess its reputation, and demonstrate how MISP can support SOC investigations through indicator enrichment and intelligence-driven analysis.

---

## Investigation Hypothesis

A suspicious executable identified during threat hunting may correspond to a known malicious indicator.

Threat intelligence enrichment may provide:

* Additional context
* Threat attribution
* Related indicators
* Detection opportunities
* Investigation leads
