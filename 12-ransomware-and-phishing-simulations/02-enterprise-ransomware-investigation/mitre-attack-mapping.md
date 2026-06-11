# MITRE ATT&CK Mapping

| Phase | Technique | ATT&CK ID |
|---------|---------|---------|
| Initial Access | Spearphishing Attachment | T1566.001 |
| Execution | PowerShell | T1059.001 |
| Persistence | Scheduled Task | T1053.005 |
| Discovery | User Discovery | T1033 |
| Discovery | System Information Discovery | T1082 |
| Discovery | Network Configuration Discovery | T1016 |
| Discovery | Account Discovery | T1087 |
| Impact | Data Encrypted for Impact | T1486 |

## Attack Chain

### Initial Access
- T1566.001 – Spearphishing Attachment
- Malicious attachment: Invoice_2026.pdf.ps1

### Execution
- T1059.001 – PowerShell
- Payload execution via PowerShell

### Persistence
- T1053.005 – Scheduled Task
- UpdateTask created using schtasks.exe

### Discovery
- T1033 – System Owner/User Discovery
- T1082 – System Information Discovery
- T1016 – System Network Configuration Discovery
- T1087 – Account Discovery

Commands observed:

- whoami
- hostname
- ipconfig
- net user

### Impact
- T1486 – Data Encrypted for Impact

Evidence:

- budget.xlsx renamed to budget.locked
- README_RESTORE_FILES.txt created
