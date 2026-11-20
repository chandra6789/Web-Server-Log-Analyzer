
# Web Server Log Analyzer

## Project Description
Web Server Log Analyzer is a Python-based web application used to analyze web server log files. It helps users understand website activity by displaying total requests, successful requests, error requests, IP addresses, HTTP status codes, and requested pages.

## Features
- Upload web server log files.
- Count total requests.
- Identify successful requests.
- Detect error requests.
- Track IP addresses.
- Analyze HTTP status codes.
- Display frequently requested pages.
- Show analysis results through a web interface.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- Regular Expressions

## Project Structure

Web-Server-Log-Analyzer/
- analyzer.py
- app.py
- requirements.txt
- sample.log
- README.md
- .gitignore
- templates/
  - index.html
- static/
  - style.css

## Installation

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open Project Folder

```bash
cd Web-Server-Log-Analyzer
```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

http://127.0.0.1:5000

## How to Use
1. Open the Web Server Log Analyzer website.
2. Select a server log file.
3. Click the Analyze Logs button.
4. View the analysis results.
5. Check IP addresses, status codes, and requested pages.

## Sample Input
The project includes a sample.log file for testing.

## Output
The application displays:
- Total Requests
- Successful Requests
- Error Requests
- IP Address Details
- HTTP Status Codes
- Requested Pages

## Conclusion
The Web Server Log Analyzer helps analyze server log files easily and provides useful information about website traffic and server errors.

## Author
Manogna
