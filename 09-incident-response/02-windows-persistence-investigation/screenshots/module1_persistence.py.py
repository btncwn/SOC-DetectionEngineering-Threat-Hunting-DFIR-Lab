
import os
import winreg
import csv
import subprocess
from datetime import datetime

# ============================================
# 1. REGISTRY PERSISTENCE TARAMASI
# ============================================
def check_registry_persistence():
    """Registry Run, RunOnce, RunServices anahtarlarını tarar"""
    registry_paths = [
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"),
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx"),
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunServices"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices"),
    ]
    
    findings = []
    print("\n[1] REGISTRY PERSISTENCE TARANIYOR...\n" + "="*60)
    
    for hkey, subkey in registry_paths:
        try:
            key = winreg.OpenKey(hkey, subkey, 0, winreg.KEY_READ)
            i = 0
            while True:
                try:
                    name, value, _ = winreg.EnumValue(key, i)
                    suspicious = check_suspicious(value)
                    findings.append({
                        'type': 'Registry',
                        'location': f"{'HKCU' if hkey==winreg.HKEY_CURRENT_USER else 'HKLM'}\\{subkey}",
                        'name': name,
                        'value': value,
                        'suspicious': suspicious
                    })
                    print(f"[{'⚠️' if suspicious else '✓'}] {name} = {value[:70]}")
                    i += 1
                except OSError:
                    break
            winreg.CloseKey(key)
        except FileNotFoundError:
            continue
        except Exception as e:
            print(f"Hata: {subkey} okunamadı - {e}")
    
    return findings

# ============================================
# 2. STARTUP KLASÖRLERİ TARAMASI
# ============================================
def check_startup_folders():
    """Startup klasörlerindeki dosyaları tarar"""
    startup_paths = [
        os.path.expandvars(r"%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"),
        os.path.expandvars(r"%ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Startup"),
        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup",
    ]
    
    findings = []
    print("\n[2] STARTUP KLASÖRLERİ TARANIYOR...\n" + "="*60)
    
    for path in startup_paths:
        if os.path.exists(path):
            print(f"\n📁 {path}")
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isfile(full_path):
                    suspicious = check_suspicious(full_path)
                    findings.append({
                        'type': 'Startup Folder',
                        'location': path,
                        'name': item,
                        'value': full_path,
                        'suspicious': suspicious
                    })
                    print(f"  [{'⚠️' if suspicious else '📄'}] {item}")
    
    return findings

# ============================================
# 3. SCHEDULED TASKS TARAMASI
# ============================================
def check_scheduled_tasks():
    """Şüpheli zamanlanmış görevleri tarar"""
    findings = []
    print("\n[3] SCHEDULED TASKS TARANIYOR...\n" + "="*60)
    
    try:
        result = subprocess.run(
            ["schtasks", "/query", "/fo", "csv", "/v"],
            capture_output=True,
            text=True,
            timeout=30
        )
        lines = result.stdout.splitlines()
        suspicious_keywords = ['powershell', 'cmd', 'temp', 'wscript', 'cscript', 'mshta', 'download']
        
        for line in lines[1:]:
            lower_line = line.lower()
            if any(keyword in lower_line for keyword in suspicious_keywords):
                findings.append({
                    'type': 'Scheduled Task',
                    'location': 'Task Scheduler',
                    'name': line[:80],
                    'value': line,
                    'suspicious': True
                })
                print(f"[⚠️] Şüpheli görev: {line[:80]}")
    except Exception as e:
        print(f"[-] Scheduled tasks hatası: {e}")
    
    return findings

# ============================================
# 4. WINDOWS SERVICES TARAMASI
# ============================================
def check_services():
    """Şüpheli servisleri tarar"""
    findings = []
    print("\n[4] SUSPICIOUS SERVICES TARANIYOR...\n" + "="*60)
    
    try:
        result = subprocess.run(
            ["powershell", "-Command", "Get-Service | Select Name, DisplayName, Status, StartType | ConvertTo-Csv -NoTypeInformation"],
            capture_output=True,
            text=True,
            timeout=30
        )
        lines = result.stdout.splitlines()
        suspicious_keywords = ['temp', 'fake', 'mal', 'update', 'remote', 'agent', 'crypt']
        
        for line in lines[1:]:
            lower_line = line.lower()
            if any(keyword in lower_line for keyword in suspicious_keywords):
                findings.append({
                    'type': 'Service',
                    'location': 'Services.msc',
                    'name': line[:80],
                    'value': line,
                    'suspicious': True
                })
                print(f"[⚠️] Şüpheli servis: {line[:80]}")
    except Exception as e:
        print(f"[-] Services hatası: {e}")
    
    return findings

# ============================================
# 5. WMI PERSISTENCE TARAMASI
# ============================================
def check_wmi_persistence():
    """WMI event filter'larını tarar (Phantom Protocol tespiti)"""
    findings = []
    print("\n[5] WMI PERSISTENCE TARANIYOR...\n" + "="*60)
    
    try:
        result = subprocess.run(
            ["powershell", "-Command", "Get-WmiObject -Namespace root/subscription -Class __EventFilter | Select Name, Query, EventNameSpace | ConvertTo-Csv -NoTypeInformation"],
            capture_output=True,
            text=True,
            timeout=30
        )
        lines = result.stdout.splitlines()
        
        for line in lines[1:]:
            if any(keyword in line.lower() for keyword in ['powershell', 'cmd', 'temp', 'phantom']):
                findings.append({
                    'type': 'WMI Persistence',
                    'location': 'root/subscription',
                    'name': 'WMI EventFilter',
                    'value': line[:100],
                    'suspicious': True
                })
                print(f"[⚠️] Şüpheli WMI filtresi: {line[:80]}")
    except Exception as e:
        print(f"[-] WMI kontrolü yapılamadı (yönetici yetkisi gerekebilir): {e}")
    
    return findings

# ============================================
# 6. SUSPICIOUS INDICATORS (IOC)
# ============================================
def check_suspicious(file_or_path):
    """Dosya veya komut içinde şüpheli kalıpları ara"""
    suspicious_indicators = [
        'temp', 'tmp', 'download', 'powershell', 'cmd.exe /c',
        'wscript', 'cscript', 'mshta', 'rundll32', 'regsvr32',
        '.vbs', '.ps1', '.js', '.jse', '.hta', '.scr', '.jar',
        'base64', '-enc', '-decode', 'iex', 'invoke-expression',
        'atomicredteam'
    ]
    lower = file_or_path.lower()
    return any(ind in lower for ind in suspicious_indicators)

# ============================================
# 7. RAPOR OLUŞTURMA (CSV)
# ============================================
def generate_report(findings):
    """CSV raporu oluşturur ve özet gösterir"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"C:\\Omega\\persistence_hunt_{timestamp}.csv"
    
    os.makedirs("C:\\Omega", exist_ok=True)
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['type', 'location', 'name', 'value', 'suspicious'])
        writer.writeheader()
        writer.writerows(findings)
    
    suspicious_count = sum(1 for f in findings if f['suspicious'])
    
    print("\n" + "="*60)
    print("📊 RAPOR ÖZETİ")
    print("="*60)
    print(f"📁 Rapor kaydedildi: {filename}")
    print(f"📋 Toplam bulgu: {len(findings)}")
    print(f"⚠️  Şüpheli bulgu: {suspicious_count}")
    
    if suspicious_count > 0:
        print("\n🚨 TESPİT EDİLEN ŞÜPHELİ MADDELER:")
        for f in findings:
            if f['suspicious']:
                print(f"   - [{f['type']}] {f['name']} -> {f['value'][:60]}")

# ============================================
# 8. MAIN (ÇALIŞTIRMA)
# ============================================
if __name__ == "__main__":
    print("="*60)
    print("🔍 OMEGA PROTOCOL - PROJE 1: PERSISTENCE HUNTER")
    print("   Windows Registry, Startup, Tasks, Services, WMI")
    print("="*60)
    
    all_findings = []
    
    all_findings.extend(check_registry_persistence())
    all_findings.extend(check_startup_folders())
    all_findings.extend(check_scheduled_tasks())
    all_findings.extend(check_services())
    all_findings.extend(check_wmi_persistence())
    
    generate_report(all_findings)
    
    print("\n✅ Hunting tamamlandı!")