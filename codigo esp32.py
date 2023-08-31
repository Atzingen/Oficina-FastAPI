import dht
import machine
import time
import urequests
import network

# Configuração das constantes para os pinos
DHT_PIN = 2     # Pino do sensor DHT11 (pode ser alterado para outro pino)
POT_PIN = 36    # Pino do potenciômetro (pode ser alterado para outro pino)

# Configuração das credenciais de rede Wi-Fi
WIFI_SSID = "CEPAD"
WIFI_PASSWORD = "Cepad@123"

# Conexão à rede Wi-Fi
def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Conectando à rede Wi-Fi...")
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print("Conectado à rede Wi-Fi:", sta_if.ifconfig())

# Configuração do sensor DHT11
dht_pin = machine.Pin(DHT_PIN, machine.Pin.IN)
dht_sensor = dht.DHT11(dht_pin)

# Configuração do potenciômetro
pot_pin = machine.ADC(machine.Pin(POT_PIN))
pot_pin.atten(machine.ADC.ATTN_11DB)

# Função para ler o sensor DHT11 e retornar os dados como uma tupla (temperatura, umidade)
def read_dht_sensor():
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    return temperature, humidity

# Função para ler o valor do potenciômetro e retornar o valor normalizado entre 0 e 1
def read_potentiometer():
    pot_value = pot_pin.read()
    normalized_value = pot_value / 4095.0
    return normalized_value

# Função para enviar os dados do sensor de temperatura para a API
def send_temperature_data_to_api(temperature):
    api_url = f"http://192.168.0.105:8000/insert_sensor/1/{temperature}"
    response = urequests.get(api_url)
    print("Código de status da resposta:", response.status_code)
    print("Resposta da API:", response.text)
    response.close()

# Função para enviar os dados do potenciômetro para a API
def send_potentiometer_data_to_api(pot_value):
    api_url = f"http://192.168.0.105:8000/insert_sensor/2/{pot_value}"
    response = urequests.get(api_url)
    print("Código de status da resposta:", response.status_code)
    print("Resposta da API:", response.text)
    response.close()

# Conecta à rede Wi-Fi
connect_wifi()

# Loop principal
while True:
    try:
        # Ler o sensor de temperatura e enviar os dados para a API
        temperature, humidity = read_dht_sensor()
        print("\n\nTemperatura:", temperature, "Umidade:", humidity)
        send_temperature_data_to_api(temperature)

        # Aguardar um segundo antes de ler o potenciômetro
        time.sleep(1)

        # Ler o potenciômetro e enviar os dados para a API
        pot_value = read_potentiometer()
        print("\n\nValor do Potenciômetro:", pot_value)
        send_potentiometer_data_to_api(pot_value)
        
    except Exception as e:
        print("Erro ao ler o sensor ou enviar dados para a API:", e)
    time.sleep(1)  # Aguarda 1 segundo antes de fazer uma nova leitura e envio dos dados

