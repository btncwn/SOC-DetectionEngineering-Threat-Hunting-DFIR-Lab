# Findings

## Phase 3 – Persistence

Persistence was established through a scheduled task named UpdateTask.

Sysmon Event ID 1 recorded the execution of schtasks.exe with the following command:

schtasks.exe /Create /TN UpdateTask /SC ONLOGON /TR "powershell.exe -ExecutionPolicy Bypass -File C:\Users\Public\Downloads\fake_ransomware.ps1" /F

The parent process was PowerShell, indicating the persistence mechanism was deployed by the ransomware payload.

### MITRE ATT&CK

T1053.005 – Scheduled Task/Job: Scheduled Task

### Evidence

- Sysmon Event ID 1
- schtasks.exe execution
- UpdateTask persistence mechanism
- Parent process: powershell.exe
- PowerShell executed from fake_ransomware.ps1

### Assessment

The attacker established persistence by creating a scheduled task configured to execute at user logon. This technique enables the ransomware payload to regain execution following system reboots or user logins and is commonly observed in ransomware intrusions.

## Phase 4 – Discovery

Following execution and persistence establishment, the ransomware payload performed system reconnaissance.

Observed commands:

- whoami
- hostname
- ipconfig
- net user

These commands were used to identify the current user context, host information, network configuration, and local user accounts.

### MITRE ATT&CK

T1033 – System Owner/User Discovery

T1082 – System Information Discovery

T1016 – System Network Configuration Discovery

T1087 – Account Discovery

### Evidence

- whoami.exe execution observed
- hostname.exe execution observed
- ipconfig.exe execution observed
- net.exe execution observed
- Discovery output written to:
  - C:\Finance\whoami.txt
  - C:\Finance\hostname.txt
  - C:\Finance\ipconfig.txt
  - C:\Finance\netuser.txt

### Assessment

The attacker performed host reconnaissance to gather information about the compromised system, user accounts, and network configuration. This information could be used to support lateral movement, privilege escalation, or further ransomware deployment activities.

## Phase 5 – Impact

The ransomware payload simulated file encryption activity by renaming a business document.

Observed activity:

- budget.xlsx renamed to budget.locked
- Ransom note created as README_RESTORE_FILES.txt

### MITRE ATT&CK

T1486 – Data Encrypted for Impact

### Evidence

- budget.locked
- README_RESTORE_FILES.txt

### Assessment

The attacker successfully executed the impact phase of the ransomware attack. Business data was rendered inaccessible through simulated encryption activity and a ransom note was deployed to the victim system.

## Phase 4 – Discovery

Following execution and persistence establishment, the ransomware payload performed system reconnaissance.

Observed commands:

- whoami
- hostname
- ipconfig
- net user

These commands were used to identify the current user context, host information, network configuration, and local user accounts.

### MITRE ATT&CK

T1033 – System Owner/User Discovery

T1082 – System Information Discovery

T1016 – System Network Configuration Discovery

T1087 – Account Discovery

### Evidence

- whoami.exe execution observed
- hostname.exe execution observed
- ipconfig.exe execution observed
- net.exe execution observed
- Discovery output written to:
  - C:\Finance\whoami.txt
  - C:\Finance\hostname.txt
  - C:\Finance\ipconfig.txt
  - C:\Finance\netuser.txt

### Assessment

The attacker performed host reconnaissance to gather information about the compromised system, user accounts, and network configuration. This information could be used to support lateral movement, privilege escalation, or further ransomware deployment activities.

## Phase 5 – Impact

The ransomware payload simulated file encryption activity by renaming a business document.

Observed activity:

- budget.xlsx renamed to budget.locked
- Ransom note created as README_RESTORE_FILES.txt

### MITRE ATT&CK

T1486 – Data Encrypted for Impact

### Evidence

- budget.locked
- README_RESTORE_FILES.txt

### Assessment

The attacker successfully executed the impact phase of the ransomware attack. Business data was rendered inaccessible through simulated encryption activity and a ransom note was deployed to the victim system.
