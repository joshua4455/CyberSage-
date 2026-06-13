# 🛡 CyberSage — Personalized Threat Intelligence Training

> **GitHub Copilot Creative Apps Challenge — Battle #1**

CyberSage is an AI-powered cybersecurity awareness training game that uses **Microsoft Work IQ** (via Microsoft Graph API) to pull your real organizational context and generate hyper-personalized social engineering simulations — phishing emails that reference your actual projects, colleagues, and managers.

## 🎯 What Makes It Unique

Most phishing training tools use generic templates. CyberSage is different:

- **Personalized to you** — Uses your real name, manager, company, and current project
- **Work IQ powered** — Pulls real M365 organizational context via Microsoft Graph
- **AI-generated scenarios** — Claude generates fresh, realistic attacks every session
- **Adaptive difficulty** — Easy, Medium, Hard modes for different experience levels
- **Confidence scoring** — Rewards accurate threat detection AND calibrated confidence

## 🏗 Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   CyberSage UI  │───▶│  FastMCP Server  │───▶│ Microsoft Graph │
│   (index.html)  │    │   (app.py)       │    │   Work IQ API   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                      │
         ▼                      ▼
┌─────────────────┐    ┌──────────────────┐
│  Claude API     │    │  Anthropic API   │
│  Scenario Gen   │    │  Threat Analysis │
└─────────────────┘    └──────────────────┘
```

## 🔗 Microsoft IQ Integration — Work IQ

CyberSage integrates the **Work IQ** intelligence layer through Microsoft Graph API:

| Graph Endpoint | Purpose |
|---|---|
| `/v1.0/users` | Pull org members for realistic colleague impersonation |
| `/v1.0/domains` | Get real company domains for spoofing scenarios |
| `/v1.0/me/messages` | Sample email patterns for realistic phishing |
| `/v1.0/me/calendar/events` | Reference real meetings in pretexting attacks |

When Graph credentials are provided, real organizational data enriches the AI-generated scenarios. When not available, the system generates realistic synthetic Work IQ context.

## 🤖 GitHub Copilot Usage

This project was built with extensive GitHub Copilot assistance:

- **Scenario generation prompts** — Copilot helped craft the Claude API prompts for realistic threat scenarios
- **Microsoft Graph API calls** — Copilot autocompleted authentication flows and endpoint queries
- **FastMCP server structure** — Copilot suggested tool definitions and async patterns
- **UI game logic** — Copilot accelerated the scoring system and state management code
- **Red flag detection** — Copilot helped build the `analyze_threat_indicators` heuristic engine

## 🚀 Quick Start

### Web App (No setup needed)
Open `index.html` in any browser. Use "Demo Profile" to start immediately.

### With Work IQ / Microsoft Graph
1. Register an app at `portal.azure.com`
2. Add `User.Read.All` and `Mail.Read` API permissions
3. Create a client secret
4. Enter credentials in the Setup tab

### MCP Server
```bash
pip install -r requirements.txt
python app.py
```

Add to GitHub Copilot / VS Code MCP config:
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

## 🎮 How It Works

1. **Setup** — Enter your name, role, company, manager, and current project
2. **Work IQ Pull** — CyberSage queries Microsoft Graph for real org context
3. **AI Generation** — Claude generates N personalized attack scenarios
4. **Training** — Analyze each scenario, set your confidence level, make your verdict
5. **Debrief** — Get detailed explanations of red flags and attacker techniques
6. **Score** — Points based on accuracy AND calibrated confidence

## 🏆 Scenario Types

| Type | Description | Example |
|---|---|---|
| 📧 Phishing | Fake emails using real context | "Your manager Sarah needs this file urgently" |
| 💬 Social Engineering | IM/chat impersonation | IT helpdesk asking for MFA code |
| 📞 Vishing | Voice/call pretexting | Vendor calling about your project |
| 🎭 Pretexting | Fabricated scenarios | Fake HR survey with credential harvesting |

## 🔒 Security Note

CyberSage never stores credentials. Microsoft Graph tokens are used only for the current session and never persisted. All API keys should be stored in `.env` files (see `.gitignore`).

## 👨‍💻 Built By

Joshua Appiah — Cybersecurity Researcher & SOC Analyst  
[linkedin.com/in/joshua-appiah-cyber](https://linkedin.com/in/joshua-appiah-cyber)

---
*Built with GitHub Copilot · Powered by Claude API · Work IQ via Microsoft Graph*