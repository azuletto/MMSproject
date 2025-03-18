from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route("/")
def scrape():
    options = Options()
    options.add_argument("--headless")  # Modo sem interface gráfica
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    title = driver.title
    driver.quit()

    return jsonify({"title": title})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # A Render exige uma porta específica
