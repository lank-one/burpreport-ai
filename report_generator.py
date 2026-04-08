from datetime import datetime

def generate_report(results: list[dict], output_file: str = None) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    hosts = list({r['host'] for r in results})

    lines = []
    lines.append(f"# Security Report")
    lines.append(f"\n**Date:** {now}  ")
    lines.append(f"**Targets:** {', '.join(hosts)}  ")
    lines.append(f"**Total requests analyzed:** {len(results)}\n")
    lines.append("---\n")

    for i, r in enumerate(results, 1):
        lines.append(f"## Finding {i} — {r['method']} {r['path']}")
        lines.append(f"\n**URL:** `{r['url']}`  ")
        lines.append(f"**Status:** `{r['status']}`  ")
        lines.append(f"**Time:** {r['time']}\n")
        lines.append("### Request")
        lines.append(f"```http\n{r['request'][:1000]}\n```\n")
        lines.append("### Analysis")
        lines.append(f"{r['analysis']}\n")
        lines.append("---\n")

    report = "\n".join(lines)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(report)
        print(f"[+] Reporte guardado en: {output_file}")

    return report
