import os

assets_dir = r'C:\Users\NAVEEN\.gemini\antigravity\scratch\ece-portfolio\assets'
os.makedirs(assets_dir, exist_ok=True)

certs = [
    {
        'filename': 'cert_cadence_semicon.svg',
        'title': 'Semiconductor 101 v1.0',
        'issuer': 'Cadence Design Systems',
        'color': '#00f2fe',
        'code': 'CADENCE-SEM-101'
    },
    {
        'filename': 'cert_cadence_digital_ic.svg',
        'title': 'Digital IC Design Fundamentals v2.0',
        'issuer': 'Cadence Design Systems',
        'color': '#4facfe',
        'code': 'CADENCE-DIC-20'
    },
    {
        'filename': 'cert_cadence_verilog.svg',
        'title': 'Verilog Language & Application v28.0',
        'issuer': 'Cadence Design Systems',
        'color': '#7000ff',
        'code': 'CADENCE-VLOG-28'
    },
    {
        'filename': 'cert_cisco_c.svg',
        'title': 'C Essentials 1',
        'issuer': 'Cisco Networking Academy',
        'color': '#10b981',
        'code': 'CISCO-C-PROG-2026'
    },
    {
        'filename': 'cert_microsoft_powerbi.svg',
        'title': 'Power Platform Fundamentals',
        'issuer': 'Microsoft Certified',
        'color': '#f59e0b',
        'code': 'MS-PBI-CERT-8392'
    },
    {
        'filename': 'cert_eduexpose_iot.svg',
        'title': 'IoT & Embedded Systems Internship',
        'issuer': 'EduExpose',
        'color': '#ec4899',
        'code': 'EDU-IOT-2026'
    },
    {
        'filename': 'cert_hackerrank_problem_solving.svg',
        'title': 'Problem Solving (Basic)',
        'issuer': 'HackerRank Verified',
        'color': '#3b82f6',
        'code': 'HR-PS-BASIC-2026'
    }
]

for c in certs:
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500">
    <rect width="800" height="500" fill="#0b1329" rx="16"/>
    <rect x="20" y="20" width="760" height="460" rx="12" fill="none" stroke="{c['color']}" stroke-width="3" stroke-dasharray="10,5"/>
    <rect x="35" y="35" width="730" height="430" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
    <circle cx="400" cy="110" r="45" fill="{c['color']}" opacity="0.15"/>
    <circle cx="400" cy="110" r="35" fill="none" stroke="{c['color']}" stroke-width="2"/>
    <text x="400" y="116" fill="{c['color']}" font-family="Outfit, sans-serif" font-size="24" font-weight="bold" text-anchor="middle">★</text>
    <text x="400" y="190" fill="#94a3b8" font-family="Fira Code, monospace" font-size="14" letter-spacing="3" text-anchor="middle">VERIFIED CERTIFICATE OF ACHIEVEMENT</text>
    <text x="400" y="230" fill="#ffffff" font-family="Outfit, sans-serif" font-size="24" font-weight="bold" text-anchor="middle">{c['title']}</text>
    <text x="400" y="270" fill="{c['color']}" font-family="Inter, sans-serif" font-size="16" font-weight="600" text-anchor="middle">PROUDLY PRESENTED TO</text>
    <text x="400" y="315" fill="#ffffff" font-family="Outfit, sans-serif" font-size="28" font-weight="800" text-anchor="middle">Challa Naga Sai Lakshmi Naveen</text>
    <line x1="250" y1="335" x2="550" y2="335" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <text x="400" y="375" fill="#cbd5e1" font-family="Inter, sans-serif" font-size="15" text-anchor="middle">Issued by {c['issuer']}</text>
    <text x="400" y="435" fill="#64748b" font-family="Fira Code, monospace" font-size="12" text-anchor="middle">CREDENTIAL ID: {c['code']} | VERIFIED ACADEMIC RECORD</text>
</svg>'''
    filepath = os.path.join(assets_dir, c['filename'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated {c['filename']}")