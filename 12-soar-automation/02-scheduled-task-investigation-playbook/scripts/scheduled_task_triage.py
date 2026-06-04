import re

event = {
    "parent_image": r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
    "image": r"C:\Windows\System32\schtasks.exe",
    "command_line": r'schtasks.exe /Create /F /RU system /SC DAILY /ST 18:45 /TN Updater /TR "powershell.exe -NonI -W hidden IEX(New-Object Net.WebClient).DownloadString(...)"',
    "user": r"AzureAD\FyodorMalteskesko"
}

score = 0
findings = []

cmd = event["command_line"].lower()
parent = event["parent_image"].lower()
image = event["image"].lower()

checks = {
    "Scheduled task creation": "schtasks.exe" in image and "/create" in cmd,
    "PowerShell parent process": "powershell.exe" in parent,
    "Runs as SYSTEM": "/ru system" in cmd,
    "Hidden PowerShell": "-w hidden" in cmd or "-windowstyle hidden" in cmd,
    "Non-interactive PowerShell": "-noni" in cmd or "-noninteractive" in cmd,
    "Invoke-Expression usage": "iex" in cmd,
    "Download cradle": "downloadstring" in cmd or "webclient" in cmd,
}

weights = {
    "Scheduled task creation": 20,
    "PowerShell parent process": 20,
    "Runs as SYSTEM": 20,
    "Hidden PowerShell": 15,
    "Non-interactive PowerShell": 10,
    "Invoke-Expression usage": 20,
    "Download cradle": 20,
}

for check, matched in checks.items():
    if matched:
        score += weights[check]
        findings.append(check)

if score >= 80:
    risk = "Critical"
    decision = "Escalate immediately"
elif score >= 60:
    risk = "High"
    decision = "Escalate for incident investigation"
elif score >= 30:
    risk = "Medium"
    decision = "Continue investigation"
else:
    risk = "Low"
    decision = "Close or monitor"

print("=" * 60)
print("SCHEDULED TASK TRIAGE REPORT")
print("=" * 60)
print(f"User: {event['user']}")
print(f"Parent Process: {event['parent_image']}")
print(f"Child Process: {event['image']}")
print(f"Command Line: {event['command_line']}")
print("-" * 60)
print("Findings:")
for finding in findings:
    print(f"[+] {finding}")
print("-" * 60)
print(f"Risk Score: {score}")
print(f"Risk Level: {risk}")
print(f"Analyst Decision: {decision}")
print("=" * 60)
