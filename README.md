
---

### 2. Wi-Fi Password Grabber

```markdown
# 📶 Wi-Fi Password Grabber (Educational)

> Demonstrates how to retrieve stored Wi-Fi passwords on Windows using Python.

## Description

Enumerates Wi-Fi profiles saved on the Windows machine and attempts to extract their stored passwords. Designed solely for educational purposes to raise awareness of local credential risks.

## Features

- Lists all stored Wi-Fi profiles  
- Retrieves clear-text Wi-Fi passwords (requires admin)  
- Windows-only due to netsh commands

## Requirements

Run Python as Administrator on Windows.

## Usage

Run from an Administrator command prompt:

```bash
python wifi_password_grabber.py
