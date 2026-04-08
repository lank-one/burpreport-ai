import xml.etree.ElementTree as ET
import base64

def parse_burp_xml(filepath: str) -> list[dict]:
    tree = ET.parse(filepath)
    root = tree.getroot()
    items = []

    for item in root.findall('item'):
        request_b64  = item.findtext('request', default='')
        response_b64 = item.findtext('response', default='')

        try:
            request_decoded  = base64.b64decode(request_b64).decode('utf-8', errors='replace')
        except Exception:
            request_decoded = ''

        try:
            response_decoded = base64.b64decode(response_b64).decode('utf-8', errors='replace')
        except Exception:
            response_decoded = ''

        items.append({
            'time':     item.findtext('time', default=''),
            'url':      item.findtext('url', default=''),
            'host':     item.findtext('host', default=''),
            'port':     item.findtext('port', default=''),
            'protocol': item.findtext('protocol', default=''),
            'method':   item.findtext('method', default=''),
            'path':     item.findtext('path', default=''),
            'status':   item.findtext('status', default=''),
            'request':  request_decoded,
            'response': response_decoded,
        })

    return items


if __name__ == '__main__':
    items = parse_burp_xml('test_export.xml')
    print(f"[+] {len(items)} items parseados")
    for i, item in enumerate(items, 1):
        print(f"\n--- Item {i} ---")
        print(f"  URL:    {item['url']}")
        print(f"  Method: {item['method']}")
        print(f"  Status: {item['status']}")
        print(f"  Request preview:\n{item['request'][:200]}")
