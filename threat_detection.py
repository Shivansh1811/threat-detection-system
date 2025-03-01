import re
import os
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Define log file path
LOG_FILE = "/var/log/auth.log"  # Change this for different log sources

# Define threat detection patterns (regex-based)
THREAT_PATTERNS = {
    "Brute Force Attack": r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)",
    "Privilege Escalation": r"sudo: session opened for user root",
    "Suspicious Activity": r"pam_unix.*authentication failure"
}

# Email Alert Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"
RECIPIENT_EMAIL = "security-team@example.com"

def send_alert(threat_type, log_entry):
    """Send email alerts for detected threats"""
    msg = MIMEText(f"Threat Detected: {threat_type}\n\nLog Entry:\n{log_entry}")
    msg['Subject'] = f"[ALERT] {threat_type} Detected!"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        server.quit()
        print(f"Alert Sent: {threat_type}")
    except Exception as e:
        print(f"Error Sending Alert: {e}")

def monitor_logs():
    """Monitor log file for security events"""
    with open(LOG_FILE, 'r') as file:
        file.seek(0, os.SEEK_END)  # Move to end of file
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  # Wait for new log entries
                continue
            
            for threat, pattern in THREAT_PATTERNS.items():
                if re.search(pattern, line):
                    print(f"[!] {threat} detected! Sending alert...")
                    send_alert(threat, line)

if __name__ == "__main__":
    print("[🔍] Monitoring logs for security threats...")
    monitor_logs()
