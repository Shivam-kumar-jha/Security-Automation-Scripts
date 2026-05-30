import json

with open("sample_logs.json") as f:
    logs = json.load(f)

failed_logons = 0
privileged_logons = 0
kerberos_requests = 0

for event in logs:

    if event["EventID"] == 4625:
        failed_logons += 1

    elif event["EventID"] == 4672:
        privileged_logons += 1

    elif event["EventID"] == 4769:
        kerberos_requests += 1

with open("sample_alerts.txt", "w") as out:

    out.write("=== Security Alerts ===\n")

    if failed_logons >= 3:
        out.write("[ALERT] Possible brute-force activity detected\n")

    if privileged_logons:
        out.write("[ALERT] Privileged account logon observed\n")

    if kerberos_requests:
        out.write("[ALERT] Kerberos service ticket activity observed\n")

print("[+] Analysis complete")
print("[+] Alerts written to sample_alerts.txt")
