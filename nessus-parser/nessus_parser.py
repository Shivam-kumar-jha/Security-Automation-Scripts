import xml.etree.ElementTree as ET
import csv

INPUT_FILE = "sample_report.nessus"
OUTPUT_FILE = "sample_output.csv"

tree = ET.parse(INPUT_FILE)
root = tree.getroot()

rows = []

for report_host in root.iter("ReportHost"):
    host = report_host.attrib.get("name", "Unknown")

    for item in report_host.iter("ReportItem"):
        severity = item.attrib.get("severity", "0")
        plugin_name = item.attrib.get("pluginName", "Unknown")

        rows.append([host, plugin_name, severity])

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "Host",
        "Plugin",
        "Severity"
    ])

    writer.writerows(rows)

print(f"[+] Parsed {len(rows)} findings")
print(f"[+] Output saved to {OUTPUT_FILE}")
