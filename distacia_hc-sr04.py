#coding: utf-8

import sys
import time
import signal
import RPi.GPIO as GPIO


#Define a numeração dos pinos de acordo com a placa
GPIO.setmode(GPIO.BOARD)

#Função para finalizar o acesso a GPIO do RPI de forma segura
def clean():
    GPIO.cleanup()
    
#Função para finalizar o programa de forma segura com CTRL+C
def sigint_handler(signum, instant):
    clean()
    sys.exit()

#Ativar a captura do sinal SIGINT (CTRL+C)
signal.signal(signal.SIGINT, sigint_handler)

#TRIGGER está no  pino 7  e ECHO no pino 11
PIN_TRIGGER = 7
PIN_ECHO = 11

"""
Variaveis para auxiliar no controle do loop principal
sampling_rate: taxa de amostragem em hz, isto é, em média, quantas leituras do sonar serão feitas por segundo
speed_of_sound: velocidade do som no ar a 30ºC em m/s
max_distance: distancia maxima permitida para medição
max_delta_t: um valor maximo para a variavel delta_t, baseado na distancia maxima max_distance
"""
sampling_rate = 20.0
speed_of_sound = 349.10
max_distance = 4.0
max_delta_t = max_distance/speed_of_sound


#Define PIN_TRIGGER como saida digital e PIN_ECHO como entrada digital
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

#Inicializa  o  PIN_TRIGGER em nivel lógico baixo
GPIO.output(PIN_TRIGGER, False)
time.sleep(1)


print("Sampling Rate: ", sampling_rate, "Hz")
print("Distancia (cm)")

#loop principal. Será executado até que seja pressionado CTRL+C
while True:
    #Gera um pulso de 10ms em PIN_TRIGGER
    #Essa ação vai resultar na transmissão de ondas ultrassônicas pelo
    #transmissor do módulo sonar.
    GPIO.output(PIN_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, False)
    
    # # Atualiza a variável start_t enquanto ECHO está em nível lógico baixo.
    # Quando ECHO trocar de estado, start_t manterá seu valor, marcando
    # o momento da borda de subida de ECHO. Este é o momento em que as ondas
    # sonoras acabaram de ser enviadas pelo transmissor.
    while GPIO.input(PIN_ECHO) == 0:
        start_t = time.time()
    
    # Atualiza a variável end_t enquando ECHO está em alto. Quando ECHO
    # voltar ao nível baixo, end_t vai manter seu valor, marcando o tempo
    # da borda de descida de ECHO, ou o momento em que as ondas refletidas
    # por um objeto foram captadas pelo receptor. Caso o intervalo de tempo
    # seja maior que max_delta_t, o loop de espera também será interrompido.
    while GPIO.input(PIN_ECHO) == 1 and time.time() - start_t < max_delta_t:
        end_t = time.time()
    
    # Se a diferença entre end_t e start_t estiver dentro dos limites impostos,
    # atualizamos a variável delta_t e calculamos a distância até um obstáculo.
    # Caso o valor de delta_t não esteja nos limites determinados definimos a
    # distância como -1, sinalizando uma medida mal-sucedida.
    if end_t - start_t < max_delta_t:
        delta_t = end_t - start_t
        distance = 100*(0.5 * delta_t * speed_of_sound)
    else:
        distance = -1
    
    #imprime o valor da distancia arredondado para 2 casas decimais
    print(round(distance, 2))
    
    #delay para manter a taxa de amostragem
    time.sleep(1/sampling_rate)



