# PDF Title Changer
Simple app that allows users to drag and drop pdfs and change its metadata title.

- Drag and drop functionality
- Updated file created in the same directory as the dropped file.

## Disclaimer
The application *may be flagged as malicious* by certain security vendors and antivirus programs (8/71 on VirusTotal).

This is a false positive likely due to:
- The executable being unsigned
- Application's file-writing capabilities
- PyInstaller packaging everything in to one executable

**The application does not transmit any data. You are encouraged to inspect the code and build it yourself. Steps below.**

---
### Download the executable:
- You can download the precompiled executable directly (Windows):
[Download](https://github.com/wooyeoup-rho/icon-converter/releases/download/v1.0/pdf-title-changer.exe)

- Or check out the releases page:
[PDF Title Changer releases](https://github.com/wooyeoup-rho/pdf-title-changer/releases/tag/v1.0)

---
### Requirements
1. Python
2. PyInstaller (For creating the executable)

### Installation
Clone the repository:

```commandline
git clone https://github.com/wooyeoup-rho/pdf-title-changer.git
```

### Running the application:
```commandline
cd pdf-title-changer
python main.py
```

### Creating an executable
1. Install PyInstaller
```commandline
pip install pyinstaller
```
2. Create the executable:
```commandline
pyinstaller --onefile --add-data "assets;assets" --name pdf-title-changer --windowed --icon=assets/images/pdf.ico main.py --additional-hooks-dir=. --hidden-import=PyPDF2
```
- `--onefile` bundles everything into a single executable.
- `--add-data "assets;assets"` includes everything in the `assets` file into the executable.
- `--name pdf-title-changer` names the executable file.
- `--windowed` prevents a command-line window from appearing.
- `--icon=assets/images/pdf.ico` specifies the application icon.
- `main.py` specifies the Python script to bundle.
- `--additional-hooks-dir=.` specifies hook file for tkinterdnd2
- `--hidden-import=PyPDF2` explicitly tells pyinstaller to include the module "PyPDF2"

3. Locate and run the executable:

The executable will be located in the `dist` folder. You can now open the `pdf-title-changer.exe` inside to open the application.
