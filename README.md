# AI-Assisted-Server-Monitoring-and-Automation-Lab
A small lab combining Linux/Windows administration, Zabbix monitoring, Ansible automation, and LLM-assisted log triage.

**Stack:** Ubuntu | Windows Server 2022 | Zabbix 8.0 | Ansible | Python | Groq

## What I built
- Two VirtualBox VMs: Ubuntu and Windows Server. Practiced user/permission management, services, cron jobs, and log checks.
- Zabbix monitoring CPU, memory, and disk on both VMs, with alerts for high usage and host downtime.
- Ansible playbook that applies updates and installs packages on the Linux VM.
- Python script that sends log snippets to the Groq LLM for a short summary and severity label. Results are checked manually before use.
- Troubleshooting guide of issues I hit and how I fixed them.

## Repo layout
- `ansible/` playbook and inventory
- `scripts/log_triage.py` LLM log triage
- `docs/` screenshots, sample report, troubleshooting guide

## Screenshots
![Zabbix hosts](docs/screenshots/zabbix-hosts-green.png)
![Ansible run](docs/screenshots/ansible-recap.png)
![Triage output](docs/screenshots/triage-output.png)

## Run the triage script
    pip install groq
    export GROQ_API_KEY=your_key
    python scripts/log_triage.py sample.log
Output goes to `triage_report.csv` with `reviewed_by_human=NO` on every row.

## Results
| Planted event | Expected | AI label |
|---|---|---|
| 4 failed SSH logins | HIGH | HIGH |
| MySQL OOM kill | HIGH | HIGH |
| Repeated AppArmor denials | LOW | MEDIUM |

## Limitations
The model can mislabel severity and sometimes returns unparseable output, so every result is reviewed by hand. Only small log chunks (20 lines) are sent.

## Troubleshooting
See [docs/troubleshooting.md](docs/troubleshooting.md).
