svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect x="12" y="40" width="40" height="10" rx="3" fill="#f0a03c"/>
  <rect x="12" y="34" width="40" height="8" rx="2" fill="#64321e"/>
  <rect x="12" y="30" width="40" height="4" fill="#ffdc00"/>
  <ellipse cx="20" cy="30" rx="7" ry="3" fill="#ff5050"/>
  <ellipse cx="34" cy="32" rx="7" ry="3" fill="#ff5050"/>
  <ellipse cx="45" cy="30" rx="6" ry="3" fill="#ff5050"/>
  <path d="M 12 30 Q 12 14 32 14 Q 52 14 52 30 Z" fill="#f0a03c"/>
</svg>'''

with open('favicon.svg', 'w') as f:
    f.write(svg_content)

print("favicon.svg generated successfully in the current working directory!")