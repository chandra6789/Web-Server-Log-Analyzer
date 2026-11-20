
import re
from collections import Counter

def analyze_logs(content):

    records = []

    pattern = r'^(\S+) \S+ \S+ \[.*?\] "(.*?)" (\d{3}) (\S+)'

    for line in content.splitlines():

        match = re.search(pattern, line)

        if match:
            ip, request, status, size = match.groups()

            records.append({
                "ip": ip,
                "request": request,
                "status": int(status)
            })

    ips = Counter(r["ip"] for r in records)
    statuses = Counter(r["status"] for r in records)

    pages = Counter(
        r["request"].split()[1]
        for r in records
        if len(r["request"].split()) > 1
    )

    return {
        "total": len(records),
        "success": sum(200 <= r["status"] < 300 for r in records),
        "errors": sum(r["status"] >= 400 for r in records),
        "ips": ips,
        "statuses": statuses,
        "pages": pages
    }
