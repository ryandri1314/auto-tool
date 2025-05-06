# Voucher Checker Tool

A simple GUI tool built with **Tkinter** and **Selenium** to automate the process of checking discount vouchers on a website.

## 🔧 Features

- GUI built with Tkinter for ease of use.
- Automates browser control using Selenium with Chrome's remote debugging.
- Lets you paste a list of voucher codes to be checked automatically.
- Displays result status for each code (e.g., success, expired, or limit reached).
- Supports clipboard copy for individual voucher codes.
- Simple layout with responsive list and scroll.

## 🛠️ Requirements

- Python 3.x
- Google Chrome installed
- Required Python packages:
  ```bash
  pip install selenium
  ```
  
## 🧪 How it works

1. Run `run_chrome.py` to launch Chrome in debugging mode with a separate user profile.
  ```bash
  python run_chrome.py
  ```
2. Once Chrome opens, manually navigate to the target website containing the voucher input field. Make sure you're logged in if authentication is required.

3. Then, run `main.py` to launch the GUI application.
  ```bash
  python main.py
  ```
4. Paste your voucher codes into the input field and click the “Add” button to populate the list.

5. Click “CHECK VOUCHERS” to let the tool automatically enter each voucher into the website and retrieve the result (e.g., valid, expired, or usage limit reached).

6. You can copy individual vouchers using the “Copy” button next to each entry or refresh the interface to check again.

## 📁 File Structure

- `main.py`: Main application with GUI and Selenium logic.
- `run_chrome.py`: Launches Chrome with remote debugging enabled.
- `README.md`: Documentation file.

## 📌 Notes

- You need to manually open and prepare the target website before starting the check.
- Make sure the element selectors (e.g., IDs and class names) used in `main.py` match the current structure of the website. Update them if they change.

## 🧠 To Do

- Add export functionality for voucher results.
- Improve the voucher input parser for bulk formats.
- Enhance error handling and add user notifications.

  ----------
Created by [Uri]
