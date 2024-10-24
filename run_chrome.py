import subprocess

# Sử dụng subprocess để thực thi câu lệnh
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
result = subprocess.Popen([chrome_path, "--remote-debugging-port=9222", "--user-data-dir=C:/selenium/AutomationProfile"])