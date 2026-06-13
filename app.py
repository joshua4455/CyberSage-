from fastmcp import FastMCP
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("CyberSage-WorkIQ")

GRAPH_BASE = "https://graph.microsoft.com/v1.0"

async def get_graph_token(tenant_id: str, client_id: str, client_secret: str) -> str:
    """Get Microsoft Graph access token."""
    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "scope": "https://graph.microsoft.com/.default",
                "grant_type": "client_credentials"
            }
        )
        return res.json().get("access_token", "")

@mcp.tool()
async def get_work_iq_context(tenant_id: str, client_id: str, client_secret: str) -> dict:
    """
    Pulls Work IQ context from Microsoft Graph API.
    Returns organizational data to personalize threat scenarios.
    """
    token = await get_graph_token(tenant_id, client_id, client_secret)
    if not token:
        return {"error": "Authentication failed", "source": "none"}

    headers = {"Authorization": f"Bearer {token}"}
    context = {"source": "Microsoft Graph Work IQ"}

    async with httpx.AsyncClient() as client:
        # Pull users (org context)
        try:
            users_res = await client.get(f"{GRAPH_BASE}/users?$top=10", headers=headers)
            context["users"] = users_res.json().get("value", [])
        except:
            context["users"] = []

        # Pull domains (for spoofing scenarios)
        try:
            domains_res = await client.get(f"{GRAPH_BASE}/domains", headers=headers)
            context["domains"] = [d.get("id") for d in domains_res.json().get("value", [])]
        except:
            context["domains"] = []

    return context

@mcp.tool()
async def generate_threat_scenario(
    user_name: str,
    user_role: str,
    company: str,
    manager: str,
    project: str,
    difficulty: str,
    attack_type: str,
    work_iq_context: dict = None
) -> dict:
    """
    Generates a personalized social engineering scenario using Work IQ context.
    Uses real organizational data to create hyper-realistic attacks.
    """
    context_str = ""
    if work_iq_context and work_iq_context.get("users"):
        colleagues = [u.get("displayName", "") for u in work_iq_context["users"][:3]]
        context_str = f"Real colleagues from Work IQ: {', '.join(colleagues)}"

    async with httpx.AsyncClient(timeout=30) as client:
        res = await client.post(
            "https://api.anthropic.com/v1/messages",
            headers={"Content-Type": "application/json"},
            json={
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 1000,
                "system": "Generate cybersecurity training scenarios as JSON only.",
                "messages": [{
                    "role": "user",
                    "content": f"""Generate a {difficulty} {attack_type} scenario for:
Name: {user_name}, Role: {user_role}, Company: {company}
Manager: {manager}, Project: {project}
{context_str}

Return JSON with: type, title, isThreat, artifact(kind,from_name,from_email,to,subject,body,timestamp), clues[], redFlags[], explanation, scoreValue"""
                }]
            }
        )
        return res.json()

@mcp.tool()
async def analyze_threat_indicators(message_content: str) -> dict:
    """
    Analyzes a message for social engineering indicators.
    Returns risk score and specific red flags detected.
    """
    indicators = {
        "urgency": any(w in message_content.lower() for w in ["urgent", "immediate", "asap", "right now", "expires"]),
        "authority": any(w in message_content.lower() for w in ["ceo", "hr", "it department", "security team", "management"]),
        "credential_request": any(w in message_content.lower() for w in ["password", "login", "mfa", "verify", "authenticate"]),
        "suspicious_link": "http" in message_content.lower() or "click here" in message_content.lower(),
        "fear_tactics": any(w in message_content.lower() for w in ["suspended", "terminated", "locked", "breach", "compromised"]),
    }
    risk_score = sum(indicators.values()) * 20
    return {
        "risk_score": min(risk_score, 100),
        "indicators": indicators,
        "recommendation": "HIGH RISK - Do not act" if risk_score >= 60 else "MEDIUM - Verify before acting" if risk_score >= 40 else "LOW RISK"
    }

if __name__ == "__main__":
    mcp.run()