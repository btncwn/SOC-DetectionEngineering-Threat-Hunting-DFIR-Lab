# Indicators of Compromise (IOCs)

## File Names

- Invoice_2026.pdf.ps1
- fake_ransomware.ps1
- README_RESTORE_FILES.txt
- budget.locked

## Scheduled Task

- UpdateTask

## Command Line Activity

powershell.exe -ExecutionPolicy Bypass -File C:\Users\Public\Downloads\Invoice_2026.pdf.ps1

powershell.exe -ExecutionPolicy Bypass -File C:\Users\Public\Downloads\fake_ransomware.ps1

schtasks.exe /Create /TN UpdateTask

## Discovery Commands

- whoami
- hostname
- ipconfig
- net user

## MITRE ATT&CK

T1566.001 – Spearphishing Attachment

T1059.001 – PowerShell

T1053.005 – Scheduled Task

T1033 – System Owner/User Discovery

T1082 – System Information Discovery

T1016 – System Network Configuration Discovery

T1087 – Account Discovery

T1486 – Data Encrypted for Impact
