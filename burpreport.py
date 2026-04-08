import argparse
from parser import parse_burp_xml
from analyzer import analyze_all
from report_generator import generate_report
from rich.console import Console
from rich.progress import track

console = Console()

def main():
    parser = argparse.ArgumentParser(
        description="BurpReport AI - Análisis de exports de Burp Suite con IA"
    )
    parser.add_argument("input",  help="Archivo XML exportado desde Burp Suite")
    parser.add_argument("-o", "--output", default="report.md",
                        help="Archivo de salida (default: report.md)")
    args = parser.parse_args()

    console.print(f"\n[bold green]BurpReport AI[/bold green]")
    console.print(f"[*] Parseando: {args.input}")

    items = parse_burp_xml(args.input)
    console.print(f"[+] {len(items)} requests encontradas\n")

    results = analyze_all(items)
    generate_report(results, args.output)

    console.print(f"\n[bold green][+] Listo![/bold green] Reporte en: {args.output}")

if __name__ == "__main__":
    main()
