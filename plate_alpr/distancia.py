#coding: utf-8

import sys
import time
import signal
import RPi.GPIO as GPIO
from cancela import Cancela
from camera  import Camera 
class Detector():
    
    def __init__(self): 
        #Define a numeracao dos pinos de acordo com a placa
        GPIO.setmode(GPIO.BOARD)
        #TRIGGER estao no  pino 7  e ECHO no pino 11
        self.PIN_TRIGGER = 7
        self.PIN_ECHO = 11     
        # Variaveis para auxiliar no controle do loop principal
        #sampling_rate: taxa de amostragem em hz, isto é, em média, quantas leituras do sonar serão feitas por segundo
        #speed_of_sound: velocidade do som no ar a 30ºC em m/s
        #max_distance: distancia maxima permitida para medição
        #max_delta_t: um valor maximo para a variavel delta_t, baseado na distancia maxima max_distance
        self.sampling_rate = 20.0
        self.speed_of_sound = 349.10
        self.max_distance = 4
        self.max_delta_t = self.max_distance/self.speed_of_sound
        self.distance = 0
        self.start_t = 0
        self.ent_t = 0
        #Define PIN_TRIGGER como saida digital e PIN_ECHO como entrada digital
        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)
        #Inicializa  o  PIN_TRIGGER em nivel lógico baixo
        GPIO.output(self.PIN_TRIGGER, False)
        time.sleep(1)


    #chamar m�todo em loop.
    def distance_car(self): 
        #Gera um pulso de 10ms em PIN_TRIGGER
        #Essa acao vai resultar na transmissao de ondas ultrassonicas pelo
        #transmissor do módulo sonar.
        GPIO.output(self.PIN_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.PIN_TRIGGER, False)
        #Atualiza a variável start_t enquanto ECHO está em nível lógico baixo.
        # Quando ECHO trocar de estado, start_t manterá seu valor, marcando
        # o momento da borda de subida de ECHO. Este é o momento em que as ondas
        # sonoras acabaram de ser enviadas pelo transmissor.
        while GPIO.input(self.PIN_ECHO) == 0:
            self.start_t = time.time()
        # Atualiza a variável end_t enquando ECHO está em alto. Quando ECHO
        # voltar ao nível baixo, end_t vai manter seu valor, marcando o tempo
        # da borda de descida de ECHO, ou o momento em que as ondas refletidas
        # por um objeto foram captadas pelo receptor. Caso o intervalo de tempo
        # seja maior que max_delta_t, o loop de espera também será interrompido.
        while GPIO.input(self.PIN_ECHO) == 1 and time.time() - self.start_t < self.max_delta_t:
           self.end_t = time.time()
        # Se a diferença entre end_t e start_t estiver dentro dos limites impostos,
        # atualizamos a variável delta_t e calculamos a distância até um obstáculo.
        # Caso o valor de delta_t não esteja nos limites determinados definimos a
        # distância como -1, sinalizando uma medida mal-sucedida.
        if self.end_t - self.start_t < self.max_delta_t:
            delta_t = self.end_t -self.start_t
            self.distance = 100*(0.5 * delta_t * self.speed_of_sound)
            if self.distance > 15 or self.distance < 10:
                self.distance = -1 
        else:
            self.distance = -1
        #imprime o valor da distancia arredondado para 2 casas decimais
        self.distance = (round(self.distance, 2))
        #delay para manter a taxa de amostragem
        time.sleep(1/self.sampling_rate)
        return self.distance




    #Funcao para finalizar o acesso a GPIO do RPI de forma segura
    def clean():
        GPIO.cleanup()


    #Funcaoo para finalizar o programa de forma segura com CTRL+C
    def sigint_handler(signum, instant):
        clean()
        sys.exit()
    #Ativar a captura do sinal SIGINT (CTRL+Ci)
    signal.signal(signal.SIGINT, sigint_handler)


"""
detector = Detector()
cancela = Cancela()
Alpr = 1
while True:
    if detector.distance_car() != -1:
        print("Captura Foto")
        camera = Camera()
        camera.captura_img()
        print("Alpr analisa foto, 1 para abrir cancela, 0 para fechar ")
        if Alpr  == 1:
            print("Abre cancela")
            cancela.abre_cancela()
            #time.sleep(1)
        else:
            print("Mantem cancela Fechada")
            cancela.fecha_cancela()
        while detector.distance_car() != -1:
            print ("Mantenha cancela aberta")
            cancela.mantem_aberta()
        else:
            print("fecha cancela")
            cancela.fecha_cancela()
            continue
    else:
        print("Mantenha cancela fechada")
        cancela.fecha_cancela()
"""





