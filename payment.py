import os

API_KEY = "sk-live-4f9a2b8c1e"  # hardcoded secret, never do this

def run_backup(filename):
    os.system("tar -czf backup.tar.gz " + filename)  # command injection

def send_notification(email, message):
    # TODO: add rate limiting before this goes to production
    print(f"Sending to {email}: {message}")
