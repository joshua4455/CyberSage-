# 🛡 CyberSage — Personalized Threat Intelligence Training

> **GitHub Copilot Creative Apps Challenge — Battle #1**  
> *Train like the attack is real.*

CyberSage is an AI-powered cybersecurity awareness training game that uses **Microsoft Work IQ** (via Microsoft Graph API) to pull real organizational context and generate hyper-personalized social engineering simulations.

Unlike generic phishing simulators that use cookie-cutter templates, CyberSage generates attacks that reference your **real name, manager, company, and current project** — making every training session frighteningly realistic and uniquely personal to each individual.

---

## 🎯 What Makes It Unique

Every employee gets a **completely different training session** because scenarios are generated using:

- Their **real name** — the attacker addresses them personally
- Their **job role & department** — a SOC Analyst gets different attacks than a Finance Manager
- Their **company name** — emails look like they came from inside the organization
- Their **manager's name** — "Sarah asked me to follow up with you about this..."
- Their **current project** — "regarding the Q3 Security Audit findings..."
- A **random session seed** — even same-role employees never see the same scenario order

**Example:**
- 👨‍💻 *Joshua (SOC Analyst)* → fake IT security alert about compromised credentials on the Q3 audit system
- 💰 *Emma (Finance Manager)* → fake CFO wire transfer request referencing her current budget project  
- 🧑‍💼 *David (HR Director)* → fake employee data request from a spoofed legal department email

---

## 🔐 Security Design

CyberSage is built with a **two-tier access model**:

| User | What They See |
|------|--------------|
| **Employee** | Name, role, department, company, manager, project — simple and clean |
| **IT Admin** | Hidden admin panel to configure Work IQ / Microsoft Graph credentials once |

Microsoft Graph credentials are **never hardcoded**, **never visible to employees**, and **stored only in the browser's localStorage** — they can never be accidentally exposed or committed to source control.

---

## 🧠 Cybersecurity Threats Covered

CyberSage trains employees against **25+ real-world attack scenarios** across every major threat category:

### 📧 Phishing
- Fake corporate portal login links
- CEO fraud / Business Email Compromise (BEC)
- Fake invoice or payment requests
- Malicious calendar invites
- Fake HR policy updates requiring personal information
- Fake vendor emails requesting bank detail changes
- Password reset emails
- Watering hole attacks via industry newsletters
- Fake software update or security alert notifications
- Supply chain emails from compromised vendors

### 💬 Social Engineering
- IT helpdesk impersonation requesting credentials
- Colleague impersonation asking for file access
- Fake security team asking to disable MFA
- Insider threat — colleague requesting unauthorized system access
- Social media impersonation of real colleagues

### 📞 Vishing & Smishing
- Phone call pretending to be bank fraud team
- SMS phishing with urgent account alerts
- Caller impersonating external auditor

### 🎭 Pretexting
- Fake contractor requesting building or system access
- Caller pretending to be compliance auditor

### 🔌 Physical Attacks
- USB drop attack (found USB in car park)
- QR code attack on office notice board
- Tailgating attempt at secure door

### 🦠 Malware & Credential Attacks
- Ransomware via malicious attachment disguised as project document
- Fake MFA verification request from IT security

---

## 🏗 Architecture

```
┌─────────────────────┐    ┌──────────────────────┐    ┌──────────────────┐
│   CyberSage UI      │───▶│   FastMCP Server     │───▶│ Microsoft Graph  │
│   (index.html)      │    │   (app.py)           │    │   Work IQ API    │
└─────────────────────┘    └──────────────────────┘    └──────────────────┘
         │                           │
         ▼                           ▼
┌─────────────────────┐    ┌──────────────────────┐
│   AI Scenario Gen   │    │   Threat Analyzer    │
│   (OpenRouter API)  │    │   (FastMCP Tools)    │
└─────────────────────┘    └──────────────────────┘
```

---

## 🔗 Microsoft IQ Integration — Work IQ

CyberSage integrates the **Work IQ** intelligence layer through Microsoft Graph API to enrich AI-generated scenarios with real organizational context:

| Graph Endpoint | Purpose |
|---|---|
| `/v1.0/users` | Pull org members for realistic colleague impersonation |
| `/v1.0/domains` | Get real company domains for domain spoofing scenarios |
| `/v1.0/me/messages` | Sample email patterns for realistic phishing |
| `/v1.0/me/calendar/events` | Reference real meetings in pretexting attacks |

**Admin Setup (IT Only):**
1. Register app in Azure AD at `portal.azure.com`
2. Add permissions: `User.Read.All`, `Directory.Read.All`, `Mail.Read`
3. Grant admin consent
4. Enter credentials via the hidden ⚙ Admin panel in CyberSage

**Employee Experience:** Just fill in name, role, company — no credentials needed.

---

## 🤖 GitHub Copilot Usage

This project was built with extensive GitHub Copilot assistance throughout:

- **Microsoft Graph API** — Copilot autocompleted OAuth2 token flows and Graph endpoint queries
- **FastMCP server** — Copilot suggested tool definitions, async patterns, and MCP decorators
- **Scenario generation prompts** — Copilot helped craft and iterate the Claude API prompts for realistic threat scenarios
- **Attack library** — Copilot helped expand the 25+ scenario category system with realistic attack themes
- **UI game logic** — Copilot accelerated the scoring system, confidence mechanics, and state management
- **Threat indicator system** — Copilot helped build the animated clue card system
- **Admin/employee separation** — Copilot suggested the localStorage pattern for secure credential storage

---

## 🎮 How to Play

1. **Open** `index.html` in any modern browser
2. **Fill in** your name, job title, department, company, manager, and current project
3. **Choose** difficulty (Easy / Medium / Hard) and number of scenarios
4. **Click** "Start Training Session" — AI generates your personalized scenarios
5. **Analyze** each email or chat message carefully
6. **Set** your confidence level (0–100%)
7. **Verdict** — Is this a THREAT or LEGITIMATE?
8. **Learn** — Get detailed debrief with red flags explained
9. **Score** — Points based on accuracy AND calibrated confidence

---

## 🚀 Quick Start

### Web App (No setup needed)
```bash
# Just open in browser
open index.html
```

### With Work IQ / Microsoft Graph (IT Admin)
1. Register app at `portal.azure.com` → App registrations → New registration
2. Add API permissions: `User.Read.All`, `Directory.Read.All`, `Mail.Read` (Application permissions)
3. Grant admin consent
4. In CyberSage → click **⚙ Admin** button → enter Client ID, Client Secret, Tenant ID
5. Credentials saved locally — employees never see them

### MCP Server
```bash
pip install -r requirements.txt
python app.py
```

**Add to GitHub Copilot / VS Code MCP config:**
```json
{
  "mcpServers": {
    "cybersage": {
      "command": "python",
      "args": ["app.py"]
    }
  }
}
```

---

## 📁 Project Structure

```
CyberSage/
├── index.html          # Main app — full training game UI
├── app.py              # FastMCP server with Work IQ tools
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Keeps secrets out of git
└── README.md           # This file
```

---

## 🏆 Scoring System

| Action | Points |
|--------|--------|
| Correct verdict (100% confidence) | +100 |
| Correct verdict (50% confidence) | +75 |
| Wrong verdict | -25 |
| Session bonus (perfect score) | +50 |

Higher confidence + correct answer = more points. Overconfident wrong answers cost more — teaching calibrated judgment, not just binary detection.

---

## 🔒 Security & Privacy

- ✅ No credentials ever hardcoded in source code
- ✅ Microsoft Graph credentials stored in browser localStorage only
- ✅ Employee profiles never leave the browser
- ✅ No backend server required for core functionality
- ✅ `.env` excluded from git via `.gitignore`
- ✅ No real user data used in scenarios — all AI-generated

---

## 👨‍💻 Built By

**Joshua Appiah** — Cybersecurity Researcher & SOC Analyst  
🔗 [linkedin.com/in/joshua-appiah-cyber](https://linkedin.com/in/joshua-appiah-cyber)  
🐙 [github.com/joshua4455](https://github.com/joshua4455)

---

*Built with GitHub Copilot · Powered by Claude AI via OpenRouter · Work IQ via Microsoft Graph*