import requests
import subprocess
import time


def wait_for_hub():
    while True:
        try:
            response = requests.get("http://selenium-hub:4444/wd/hub/status")
            if response.status_code == 200 and response.json()["value"]["ready"]:
                print("Selenium Hub is ready")
                return
        except:
            pass
        print("Selenium Hub is not ready yet, retrying in 5 seconds...")
        time.sleep(5)


if __name__ == "__main__":
    try:
        wait_for_hub()
        subprocess.run(["behave", "./src/features", "-f",
                       "behave_html_formatter:HTMLFormatter", "-o", "/usr/home/www/index.html"])
    except FileNotFoundError:
        print("Error: starting behave")
