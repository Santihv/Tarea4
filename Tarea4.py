'''
Tarea #3
IE0405: Modelos Probabilísticos de Señales y Sistemas
Santiago Hernández Vargas
B73737
'''

import numpy as np
from scipy import signal
from scipy import integrate
import matplotlib.pyplot as plt
import csv

with open('bits10k.csv') as datos:
  reader = csv.reader(datos)
  bits = [int(i[0]) for i in reader]

  '''
  1) Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.
  '''
  
  #Definir parámetros de la simulación
  f = 5000 #Hz
  T = 1/f #Segundos
  p = 50 #Cantidad de puntos por periodo
  tp = np.linspace(0,T,p) #Vector de valores del tiempo/T
  seno = np.sin(2 * np.pi * f * tp) #Onda senoidal generada
  
  #Visualizar la onda senoidal
  plt.plot(tp,seno)
  plt.xlabel('Tiempo t (s)')
  plt.ylabel('Amplitud')
  plt.title('Onda senoidal en un periodo')
  plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
  plt.savefig('onda.png')

  #Frecuencia de muestreo
  fs = p/T #250 kHz

  #Tiempo total
  t = np.linspace(0,len(bits)*T,len(bits)*p)

  #Inicializar señal modulada Tx
  senial = np.zeros(t.shape)
  
  #Crear la señal modulada
  for k,b in enumerate(bits):
    if b == 1:
      senial[k*p:(k+1)*p] = seno
    else:
      senial[k*p:(k+1)*p] = -1*seno

  #Visualización de los bits
  pb = 10 #Número de primeros bits que queremos ver
  plt.figure()
  plt.plot(senial[0:pb*p])
  plt.xlabel('Cantidad de puntos temporales (50/T)')
  plt.ylabel('Amplitud')
  plt.title('Primeros {} bits modulados por BPSK'.format(pb))
  plt.savefig('señal.png')

  '''
  2) Calcular la potencia promedio de la señal modulada generada.
  '''

  #Potencia instantánea
  Pinst = senial**2

  #Potencia promedio a partir de la potencia instantánea
  Pprom = integrate.trapz(Pinst, t) / (len(bits) * T) #Watt
  print('Potencia promedio de la señal: Pprom = ',Pprom)

  '''
  3) Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.
  '''

  #Definir los valores de relación señal a ruido
  SNR = [i for i in range(-2,3+1)] #SNR[dB] = 10*log10(Pprom/Pn)


  #Inicializar una lista para guardar los valores de BER
  valores_BER = []
  
  #El for es para variar el SNR y graficar todos los canales de una vez
  for snr in SNR:
    #Potencia del ruido para SNR y potencia de la señal dadas
    Pn = Pprom / (10**(snr / 10))

    #Desviación estándar del ruido (Pn = sigma^2)
    sigma = np.sqrt(Pn)

    #Crear ruido
    ruido = np.random.normal(0, sigma, senial.shape)

    #Simular "el canal": señal recibida
    Rx = senial + ruido

    #Visualización de los primeros bits recibidos
    plt.figure()
    plt.plot(Rx[0:pb*p])
    plt.xlabel('Cantidad de puntos temporales (50/T)')
    plt.ylabel('Amplitud')
    plt.title('Señal recibida después del canal AWGN con SNR = {} dB'.format(snr))
    plt.savefig('Rx_SNR={}dB.png'.format(snr))

    '''
    4) Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.
    '''

    #Este condicional es para que la PSD antes del canal se grafique solo una vez
    if snr == -2:
      #Antes del canal ruidoso
      fw, PSD = signal.welch(senial, fs, nperseg=1024)
      plt.figure()
      plt.semilogy(fw, PSD)
      plt.xlabel('Frecuencia (Hz)')
      plt.ylabel('Densidad espectral de potencia (W/Hz)')
      plt.title('PSD de la señal antes del canal AWGN')
      plt.savefig('PSD_antes.png')

    #Después del canal ruidoso
    fw, PSD = signal.welch(Rx, fs, nperseg=1024)
    plt.figure()
    plt.semilogy(fw, PSD)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Densidad espectral de potencia (W/Hz)')
    plt.title('PSD de la señal después del canal AWGN con SNR = {} dB'.format(snr))
    plt.savefig('PSD_después_SNR={}dB.png'.format(snr))

    '''
    5) Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.
    '''
    
    # Pseudo-energía de la onda original
    Es = np.sum(seno**2)

    # Inicialización del vector de bits recibidos
    bitsRx = np.zeros(np.array(bits).shape)

    # Decodificación de la señal por detección de energía
    for k, b in enumerate(bits):
        Ep = np.sum(Rx[k*p:(k+1)*p] * seno)
        if Ep > Es/2:
            bitsRx[k] = 1
        else:
            bitsRx[k] = 0

    err = np.sum(np.abs(bits - bitsRx))
    BER = err/len(bits) * 100 #En porcentaje
    
    #Guardar los BER para luego graficarlos
    valores_BER.append(BER)

    print('Hay un total de {} errores en {} bits para una tasa de error de {}% con un SNR de {} dB.'.format(err, len(bits), BER, snr))


  '''
  6) Graficar BER versus SNR.
  '''

  plt.figure()
  plt.plot(SNR,valores_BER)
  plt.xlabel('Relación señal a ruido (SNR)')
  plt.ylabel('Relación error por bit (BER)')
  plt.title('BER contra SNR')
  plt.savefig('BER_vs_SNR.png')