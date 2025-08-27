'''
Detect URLs Within a String
'''
import re

def extract_urls(text):
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)

input_text = "Check this link: https://openai.com and http://github.com"
urls = extract_urls(input_text)
print("URLs found:", urls)