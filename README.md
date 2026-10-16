```text 
                           _           ___   ___  
                            (_)       / _ \ / _ \    not©         not©         not©         not©         not©         not©         not©         not©         not©
   __ _ __ _ __ _ __ ___ _ __ _ _  __| (_) | (_) |        not©         not©         not©         not©         not©         not©         not©         not©         not©    
  / _` |/ _` |/ _` | '__/ __| |/ _` |   > _ < > _ <             not©         not©         not©         not©         not©         not©         not©         not©         not©     
 | (_| | (_| | (_| | |  (__| | (_| | || (_) | (_) |
  \__, |\__, |\__,_|_|\_ ___|_|\__,_|_| \___/ \___/                  
   __/ | __/ |                                       
  |___/ |___/


@ggarciar88  // Cyber-Threat-Log-Analyzer

Cyber Threat Log Analyzer
A Python-based security log analysis tool designed to parse system and network event logs, apply heuristic detection rules for threat anomalies, and generate structured analytical security alerts.

Features
Parsing engine for standard system event logs (Syslog / text format)

Heuristic anomaly detection rules (e.g., brute-force threshold monitoring)

Structured JSON-formatted security alert export

Lightweight, scriptable architecture for security operations workflows

File Structure
log_analyzer.py: Core log parsing and heuristic detection script

sample_logs.log: Sample dataset for testing detection logic

How It Works
Ingests text log files line by line.

Applies threshold-based regular expressions to flag suspicious activities (such as repeated failed authentication attempts).

Outputs a comprehensive analytical report.

How to Run
Ensure Python 3 is installed.

Execute the analyzer script:
python3 log_analyzer.py

License
