from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações do Selenium
options = Options()
options.add_argument("--user-data-dir=./whatsapp_data")  # Mantém login ativo
options.add_argument("--profile-directory=Default")  # Usa o perfil padrão
options.add_argument("--no-sandbox")  
options.add_argument("--disable-dev-shm-usage")  

# Inicializa o ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")
input("📌 Escaneie o QR Code e pressione ENTER para continuar...")

# Define contato e mensagem
contato = "Nome do Contato ou Número"
mensagem = "Olá! Isso é um teste automatizado."

# Encontra a barra de pesquisa e digita o contato
search_box = driver.find_element("xpath", "//div[@contenteditable='true']")
search_box.send_keys(contato)
time.sleep(2)
search_box.send_keys("\n")
time.sleep(2)

# Encontra a caixa de mensagem e envia a mensagem
msg_box = driver.find_element("xpath", "//div[@contenteditable='true']")
msg_box.send_keys(mensagem)
msg_box.send_keys("\n")

print("✅ Mensagem enviada com sucesso!")

# Fecha o navegador após alguns segundos
time.sleep(5)
driver.quit()
