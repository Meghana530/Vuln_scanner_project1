# scanner.py
import requests
from bs4 import BeautifulSoup
import re

# XSS & SQLi test payloads
xss_payloads = ["<script>alert(1)</script>", "\"'><script>alert(1)</script>"]
sqli_payloads = ["' OR '1'='1", "'; DROP TABLE users; --"]

def find_forms(url):
    try:
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"[!] Failed to fetch forms: {e}")
        return []

def submit_form(form, url, payload):
    action = form.get("action") or ""
    method = form.get("method", "get").lower()
    inputs = form.find_all("input")
    data = {}

    for input_tag in inputs:
        name = input_tag.get("name")
        if name:
            data[name] = payload

    target_url = url + action
    if method == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def scan_xss(url):
    print(f"[+] Scanning {url} for XSS")
    forms = find_forms(url)
    for form in forms:
        for payload in xss_payloads:
            response = submit_form(form, url, payload)
            if payload in response.text:
                print(f"[!!] XSS Detected on {url}")
                log_vulnerability("XSS", url, payload, "High")

                return True
    return False

def scan_sqli(url):
    print(f"[+] Scanning {url} for SQL Injection")
    for payload in sqli_payloads:
        response = requests.get(url + "?" + "q=" + payload)
        if "sql" in response.text.lower() or "error" in response.text.lower():
            print(f"[!!] SQL Injection vulnerability detected!")
            return True
    return False
def log_vulnerability(vuln_type, url, payload, severity):
    with open("scan_log.txt", "a") as log:
        log.write(f"{vuln_type} | {url} | Payload: {payload} | Severity: {severity}\n")
