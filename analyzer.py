import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are an expert web application security analyst.
You will analyze HTTP requests and responses from Burp Suite exports.
For each item, identify:
1. Potential vulnerabilities (SQLi, XSS, SSRF, IDOR, Auth issues, etc.)
2. Interesting parameters or headers
3. Anomalous status codes or responses
4. Security misconfigurations

Be concise, technical and precise. If no vulnerability is found, say so clearly.
Always respond in the same language the user writes to you."""


def analyze_item(item: dict) -> str:
    request_preview  = item['request'][:2000]
    response_preview = item['response'][:2000]

    user_message = f"""Analyze this HTTP exchange:

## Request
{request_preview}

## Response (first 2000 chars)
{response_preview}

## Metadata
- URL: {item['url']}
- Method: {item['method']}
- Status: {item['status']}
- Host: {item['host']}

Provide a security analysis of this HTTP exchange."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_message}
        ],
        temperature=0.2,
        max_tokens=1000,
    )

    return response.choices[0].message.content


def analyze_all(items: list[dict]) -> list[dict]:
    results = []
    for i, item in enumerate(items, 1):
        print(f"[*] Analizando item {i}/{len(items)}: {item['method']} {item['url']}")
        analysis = analyze_item(item)
        results.append({**item, 'analysis': analysis})
    return results
