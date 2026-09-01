# 316332 Cybersecurity — Live Classroom Demos

Runnable, browser-based demonstrations of real security and privacy design flaws, built for the university course **316332 Cybersecurity** (identity, privacy, risk, and governance — not penetration testing). Every demo uses a small fictional case (the "Campus Club Membership and Event Check-in Service") and **synthetic data only**. Each shows a **design flaw**, not an attack technique: there is no exploitation, no real system, and no real personal data anywhere in this repository.

**Live site:** https://panupongsk-cyber.github.io/316332-cybersecurity-demos/

## Demos

| Folder | Concept | What it shows |
|---|---|---|
| [`data-minimisation/`](data-minimisation/) | Data minimisation & confidentiality | A UI that only displays a name can still leak a full raw record (student ID, email, medical/accessibility notes) over the network — found using the browser's Developer Tools, Network tab. |
| [`broken-access-control/`](broken-access-control/) | Authentication vs. authorisation | A server with no authorisation check lets a Member read an Officer's record just by editing a URL — a missing function-level access-control check, not a login bypass. |
| [`security-usability-tradeoff/`](security-usability-tradeoff/) | Policy & Usability Trade-offs | An interactive simulator exploring how high-friction security policies trigger volunteer bypass behaviors, reducing actual effective security. |
| [`privilege-creep-audit/`](privilege-creep-audit/) | Identity Lifecycle & Least Privilege | An interactive dashboard tracing Bob's roles through the Identity Lifecycle, demonstrating privilege creep and periodic access reviews. |
| [`aaa-logging-inspector/`](aaa-logging-inspector/) | Audit Logs & Accountability | Analyze audit log details under shared account vs. RBAC config to investigate a data leak, demonstrating identity accountability. |

## Imported activities: NU MOOC 084 — Cybersecurity Awareness

These five are self-contained interactive scenarios built for a separate cybersecurity-awareness
MOOC, reused here as supplementary material. They use a different fictional company ("Sommuti Co.,
Ltd.") than the Campus Club case used by the demos above.

| Folder | Concept | What it shows |
|---|---|---|
| [`data-classification/`](data-classification/) | Data classification | Sort ten realistic company documents into Public, Internal, Confidential, or Restricted, with feedback on why each is correct. |
| [`threat-spotter/`](threat-spotter/) | Threat recognition | Judge ten items across an inbox, a desk, and a building entrance as a real threat or a false alarm — six genuine threats, four deliberate decoys. |
| [`policy-audit/`](policy-audit/) | Policy & compliance | Play an IT compliance auditor scanning five workplace checkpoints for password policy, MFA, BYOD, desk security, and patch management. |
| [`safe-prompting/`](safe-prompting/) | AI safety & data handling | Redact confidential company data and personal information from three draft prompts before sending them to an external AI chatbot. |
| [`incident-response/`](incident-response/) | Incident response | Walk three employees through a 3-step incident-response playbook each — a lost device, a ransomware infection, and an MFA-fatigue attack. |

## Running locally (optional)

Each demo can also be run with a tiny local Python server instead of the hosted site:

```bash
cd data-minimisation        # or any other demo/activity directory
python3 run_demo.py
```

This opens the same page at its own local port (see each folder's `run_demo.py`), using nothing
but Python's built-in `http.server`.

## Why this is safe to run and safe to publish

- All data is invented (fictional names, fictional student IDs, fictional emails) — nothing here is a real person's information.
- Nothing here connects to a real server or a real institutional system.
- Each demo is a static site: HTML + JSON files only, no backend logic, no database, no accounts.
- The "vulnerability" in each demo is intentionally built into the sample data so it can be observed safely — it is not an exploit against any live target.

## Attribution

Built as teaching material for course 316332 Cybersecurity. Free to use, adapt, or reuse for educational purposes.
