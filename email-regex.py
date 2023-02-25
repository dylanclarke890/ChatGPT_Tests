import re

text = "Please contact us at support@example.com for more information. Also try dylan@gmail.co.uk"

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
matches = re.findall(pattern, text)

print(matches)  # Output: ['support@example.com']