# BurpReport AI 🔍

AI-powered security report generator from Burp Suite exports.

Analyze HTTP requests automatically and generate professional 
pentest reports in Markdown using Groq AI (free tier).

## Demo

```bash
python3 burpreport.py export.xml -o report.md
```
BurpReport AI
[] Parsing: export.xml
[+] 3 requests found
[] Analyzing item 1/3: POST /login
[] Analyzing item 2/3: GET /admin
[] Analyzing item 3/3: GET /api/users
[+] Report saved: report.md
## Features

- Parses Burp Suite XML exports automatically
- Detects SQLi, XSS, SSRF, IDOR, auth issues and more
- Generates structured Markdown reports
- Uses Groq API (free, no credit card required)
- Works on Kali Linux and any Python 3.10+ environment

## Installation

```bash
git clone https://github.com/lank-one/burpreport-ai
cd burpreport-ai
pip install -r requirements.txt
```

Get a free API key at [console.groq.com](https://console.groq.com)

```bash
cp .env.example .env
# Add your GROQ_API_KEY to .env
```

## Usage

```bash
# Basic usage
python3 burpreport.py export.xml

# Custom output file
python3 burpreport.py export.xml -o my_report.md
```

Export your Burp Suite requests:
`Proxy → HTTP History → Select items → Right click → Save items`

## Requirements

- Python 3.10+
- Groq API key (free tier)
- Burp Suite (Community Edition works)

## Roadmap

- [ ] HTML report output
- [ ] Severity scoring per finding
- [ ] Multi-file batch analysis
- [ ] BSCP assistant mode (rapid attack surface mapping)

## Author

[@lank-one](https://github.com/lank-one) — 
[LinkedIn](https://linkedin.com/in/alanmartinalonso) — 
[GitBook](https://l4nk0n3.gitbook.io)
