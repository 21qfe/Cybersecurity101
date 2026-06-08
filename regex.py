with open("server_logs.txt", "w") as file:
    file.write("2026-06-08 21:14:02 Access denied for user root from 192.168.43.10 port 49152\n")
    file.write("2026-06-08 21:15:44 User Milind logged in successfully from 192.168.43.15\n")
    file.write("2026-06-08 21:18:20 Failed password for admin from 10.0.0.5 port 22\n")
import re
IP_pattern=r"([0-9]{1,3}\.){3}[0-9]{1,3}"
auth_failure=r"Failed password|Invalid user|Access denied"
flagged_incidents=[]
blocked_ips=set()
with open("server_logs.txt", "r") as f:
    logs=f.readlines()
    for log in logs:
        if re.search(auth_failure, log, re.IGNORECASE):
            if(re.search(IP_pattern, log)):
                ip=re.search(IP_pattern, log).group()
                flagged_incidents.append(f"{log.strip()}\n")
                blocked_ips.add(ip)
with open("threats_report.txt", "w") as report:
    report.write("THREAT DETECTION REPORT\n")
    report.write("=====================\n\n")
    report.write("Flagged Incidents:\n")
    report.writelines(flagged_incidents)
with open ("Firewall blocklist.txt", "w") as firewall:
    firewall.write("Blocked IP Addresses:\n")
    for ip in blocked_ips:
        firewall.write(f"{ip}\n")
print("Incident response routing complete. Check threat_report.txt and firewall_blocklist.conf")
