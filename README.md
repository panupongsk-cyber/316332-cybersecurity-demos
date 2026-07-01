# 316332 Cybersecurity — Live Classroom Demos

Runnable, browser-based demonstrations of real security and privacy design flaws, built for the university course **316332 Cybersecurity** (identity, privacy, risk, and governance — not penetration testing). Every demo uses a small fictional case (the "Campus Club Membership and Event Check-in Service") and **synthetic data only**. Each shows a **design flaw**, not an attack technique: there is no exploitation, no real system, and no real personal data anywhere in this repository.

**Live site:** https://panupongsk-cyber.github.io/316332-cybersecurity-demos/

## Demos

| Folder | Concept | What it shows |
|---|---|---|
| [`data-minimisation/`](data-minimisation/) | Data minimisation & confidentiality | A UI that only displays a name can still leak a full raw record (student ID, email, medical/accessibility notes) over the network — found using the browser's Developer Tools, Network tab. |
| [`broken-access-control/`](broken-access-control/) | Authentication vs. authorisation | A server with no authorisation check lets a Member read an Officer's record just by editing a URL — a missing function-level access-control check, not a login bypass. |

## Running locally (optional)

Each demo can also be run with a tiny local Python server instead of the hosted site:

```bash
cd data-minimisation        # or broken-access-control
python3 run_demo.py
```

This opens the same page at `http://localhost:8080` (or `8081`), using nothing but Python's built-in `http.server`.

## Why this is safe to run and safe to publish

- All data is invented (fictional names, fictional student IDs, fictional emails) — nothing here is a real person's information.
- Nothing here connects to a real server or a real institutional system.
- Each demo is a static site: HTML + JSON files only, no backend logic, no database, no accounts.
- The "vulnerability" in each demo is intentionally built into the sample data so it can be observed safely — it is not an exploit against any live target.

## Attribution

Built as teaching material for course 316332 Cybersecurity. Free to use, adapt, or reuse for educational purposes.
