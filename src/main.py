from machine import Pin, ADC, I2C
from lcd_i2c import LcdI2C
import time


i2c = I2C(0, scl=Pin(26), sda=Pin(25), freq=400000)
print("I2C:", [hex(a) for a in i2c.scan()]) 

lcd = LcdI2C(i2c, addr=0x27)
lcd.linha(0, "Iniciando...")


botao = Pin(27, Pin.IN, Pin.PULL_UP)

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

pot = ADC(Pin(35))
pot.atten(ADC.ATTN_11DB)


led_amarelo = Pin(19, Pin.OUT)
led_vermelho = Pin(21, Pin.OUT)
led_verde = Pin(22, Pin.OUT)

PRECO_BASE = 1.00


def apagar_leds():
    led_vermelho.off()
    led_amarelo.off()
    led_verde.off()


while True:

    horario_pico = not botao.value()
    luz = ldr.read()
    demanda = pot.read()

    preco = PRECO_BASE

    if demanda > 3000:
        preco *= 1.40
        demanda_txt = "Alta"
    elif demanda > 1500:
        preco *= 1.15
        demanda_txt = "Media"
    else:
        demanda_txt = "Baixa"

    if horario_pico:
        preco *= 1.30

    if luz > 3000:
        preco *= 0.80
        solar_txt = "Alta"
    elif luz < 1000:
        preco *= 1.10
        solar_txt = "Baixa"
    else:
        solar_txt = "Media"


    apagar_leds()

    if preco < 1.00:
        led_verde.on()
        estado = "DESCONTO"
    elif preco < 1.50:
        led_amarelo.on()
        estado = "NORMAL"
    else:
        led_vermelho.on()
        estado = "ACRESCIMO"

    lcd.linha(0, estado + " R$" + "{:.2f}".format(preco))
    lcd.linha(1, "S:" + solar_txt + " D:" + demanda_txt)

    print("-----------------------")
    print("Preço: R$", round(preco, 2))
    print("Estado:", estado)
    print("Horário Pico:", horario_pico)
    print("Solar:", solar_txt, "| LDR:", luz)
    print("Demanda:", demanda_txt, "| Pot:", demanda)

    time.sleep(0.5)