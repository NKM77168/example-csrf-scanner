import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()

def log(message):
    """
    Print message to terminal and save it into report.txt
    """
    print(message)
    with open("report.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

def crawl(url, depth=2):
    """
    Crawl the target website and check forms for CSRF token protection.
    """
    if depth == 0 or url in visited:
        return
    visited.add(url)

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find forms
        for form in soup.find_all("form"):
            action = form.get("action")
            inputs = [i.get("name") for i in form.find_all("input") if i.get("name")]

            log(f"[+] Form found at {url} -> action='{action}'")

            # Check for CSRF token
            if not any("csrf" in str(i).lower() for i in inputs):
                log(f"    [!] Possible missing CSRF token at {url}")

        # Crawl links
        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link['href'])
            if full_url.startswith("http"):
                crawl(full_url, depth-1)

    except Exception as e:
        log(f"[x] Error at {url}: {e}")

if __name__ == "__main__":
    target = "http://testphp.vulnweb.com"  # 🔹 Replace with your test target
    log(f"[*] Starting CSRF scan on {target}")
    crawl(target, depth=2)
    log("[*] Scan finished. Results saved to report.txt")