# 🚀 Automated SOC Threat Detection System

## 📌 Overview
This **Python-based threat detection system** continuously monitors system logs to identify and respond to potential security threats in real-time.

### 🔥 Features:
✅ **Detects Brute Force Attacks, Privilege Escalations, and Suspicious Activity**  
✅ **Real-time log monitoring & alerting**  
✅ **Sends Email Alerts** when threats are detected  
✅ **Regex-based pattern matching for log analysis**  
✅ **Easily customizable for different logs (Linux, Windows, Firewalls, etc.)**  

---

## 📂 Project Structure
```
SOC-Threat-Detection/
│-- threat_detection.py   # Main script
│-- README.md             # Documentation
```

---

## ⚙️ How It Works
1️⃣ The script continuously monitors **Linux auth logs** (`/var/log/auth.log`).  
2️⃣ Uses **regex patterns** to detect threats such as:  
   - **Brute Force Attacks** (Failed SSH login attempts)  
   - **Privilege Escalation** (Unauthorized sudo activity)  
   - **Suspicious Activity** (Failed authentication attempts)  
3️⃣ **Triggers an email alert** when a threat is detected.  

---

## 🚀 Running the Project

### 1️⃣ Install Dependencies
```bash
pip install smtplib
```

### 2️⃣ Configure Email Alerts
Edit the script with your email credentials:
```python
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"
RECIPIENT_EMAIL = "security-team@example.com"
```

### 3️⃣ Start Monitoring Logs
```bash
python3 threat_detection.py
```

🔍 **Now it will monitor logs and alert you on detected threats!**

---

## 🛡️ Security & Legal Notice
⚠ **Use this tool only in authorized environments. Unauthorized use of log monitoring tools may violate company policies or legal regulations.**  

---



