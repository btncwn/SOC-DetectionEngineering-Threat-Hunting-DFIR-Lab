# Containment Actions

## Host Isolation

The affected Windows 7 endpoint was isolated from the network during the investigation.

## Persistence Removal

Scheduled task removed:

UpdateTask

Command executed:

schtasks /delete /tn UpdateTask /f

## Payload Removal

Removed files:

- Invoice_2026.pdf.ps1
- fake_ransomware.ps1

Location:

C:\Users\Public\Downloads

## IOC Management

Indicators identified during the investigation were documented and prepared for sharing with threat intelligence platforms.

## Outcome

- Persistence mechanism removed
- Further execution prevented
- Investigation completed
