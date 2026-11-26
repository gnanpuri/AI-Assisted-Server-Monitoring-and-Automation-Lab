import csv
import json
import os
import sys

from groq import Groq

MODEL = "openai/gpt-oss-20b"
SEVERITIES = {"INFO", "LOW", "MEDIUM", "HIGH", "CRITICAL"}
PROMPT = (
    "You are a sysadmin assistant. Read the log snippet and reply with ONLY JSON: "
    '{"summary": "max 2 sentences", "severity": "INFO|LOW|MEDIUM|HIGH|CRITICAL", '
    '"suggested_check": "one command or step"}. Use only facts in the logs.'
)

client = Groq(api_key=os.environ["GROQ_API_KEY"])


def triage(snippet):
    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": snippet},
        ],
    )
    text = resp.choices[0].message.content.strip()
    try:
        out = json.loads(text[text.index("{"): text.rindex("}") + 1])
    except ValueError:
        return {"summary": "Could not parse output", "severity": "MEDIUM", "suggested_check": "Review manually"}
    if out.get("severity") not in SEVERITIES:
        out["severity"] = "MEDIUM"
    return out


logfile = sys.argv[1]
with open(logfile, errors="replace") as f:
    lines = f.readlines()

chunks = ["".join(lines[i:i + 20]) for i in range(0, len(lines), 20)]

with open("triage_report.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["chunk", "severity", "summary", "suggested_check", "reviewed_by_human"])
    for n, c in enumerate(chunks, 1):
        r = triage(c)
        w.writerow([n, r["severity"], r.get("summary", ""), r.get("suggested_check", ""), "NO"])
        print(f"[{r['severity']}] chunk {n}: {r.get('summary', '')}")
