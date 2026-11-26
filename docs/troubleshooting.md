# Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| Zabbix shows Windows host red: "[104] Connection reset by peer" | Agent `Server=` didn't include the Zabbix server IP | Set `Server=` and `ServerActive=` to the server IP in `zabbix_agent2.conf`, then `Restart-Service "Zabbix Agent 2"` |
| Zabbix URL shows the nginx default page | Default nginx site takes port 80 | Remove `/etc/nginx/sites-enabled/default`, restart nginx |
| Windows VM browser can't download | IE Enhanced Security blocks sites | Turn it off in Server Manager > Local Server |
| `python3 -m venv` fails on Ubuntu | `python3-venv` not installed | `sudo apt install python3-venv` |
| Groq 404 `model_not_found` | Model was retired | List models with the API and pick a current one |
| VM install: `VERR_DISK_FULL` | Host drive full | Free space, resume or recreate the VM |
| Ubuntu console won't paste | No clipboard without Guest Additions | Connect over SSH instead |

