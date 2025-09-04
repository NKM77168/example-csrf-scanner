#  CSRF Scanner Project  

This project demonstrates how to *detect Cross-Site Request Forgery (CSRF) vulnerabilities* in web applications.  
It includes a Python crawler to identify missing CSRF tokens and a Proof of Concept (PoC) exploit.  

---

##  Files Included  
- *crawler.py* → Python crawler that scans forms for missing CSRF tokens  
- *report.txt* → Output of the crawler (list of possible CSRF-vulnerable forms)  
- *poc.html* → Proof of Concept HTML form that simulates a CSRF attack  
- *proof.png* → Screenshot proof of the scanner running  
- *README.md* → Documentation for the project  

---

##  How to Run the Crawler  
1. Clone this repository or download the files  
2. Run the crawler with:  
   ```bash
   python crawler.py 
