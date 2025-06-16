# 🔐 Web Application Vulnerability Scanner

A lightweight Python-based scanner that detects common web application vulnerabilities like **XSS (Cross-Site Scripting)** and **SQL Injection** using simple payload injection and response analysis.

## 🚀 Features

- Detects:
  - ✅ XSS
  - ✅ SQL Injection
- Flask-based web interface
- Logs scan results to `scan_log.txt`
- Clean UI for URL input and result viewing

## 🛠️ Tools Used

- Python 3
- Flask
- Requests
- BeautifulSoup4
- Regex
- HTML/CSS (for front-end)

## 📂 Project Structure

```
vuln_scanner/
├── app.py               # Flask web app
├── scanner.py           # Vulnerability scanning logic
├── templates/
│   └── index.html       # Web UI
├── scan_log.txt         # Scan results
└── README.md            # Project description
```

## 📸 Screenshot

![Screenshot](screenshot.png) <!-- You can rename your UI screenshot to screenshot.png -->

## 📄 Report

Project Report available: `Web_Vulnerability_Scanner_Report.pdf`

## ✅ How to Run

```bash
pip install flask requests beautifulsoup4
python app.py
```

Then open your browser to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🙋‍♀️ Author

**Meghana** — Cybersecurity Intern Project (June 2025)
