# Tarea 4: Procesos aleatorios
## Santiago Hernández Vargas B73737

### 1) Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

Dado que se tienen 10000 bits en total se opta por mostrar los resultados con los primeros 10, los cuales son: `[0 1 0 1 0 1 1 0 1 0]`

Para poder modular la información primero es necesario generar la onda portadora, la cual es una onda senoidal de amplitud unitaria con los siguientes parámetros:

Parámetro | Símbolo | Valor | Unidad
--------- | ------- | ----- | ------
Frecuencia de la portadora | f | 5000 | Hz
Periodo de la onda | T | 1/f = 0,2 | ms
Puntos por periodo | p | 50 | -
Frecuencia de muestreo | fs | p/T = 250 | kHz

La onda generada sería la siguiente:

![Onda senoidal generada](https://github.com/Santihv/Tarea4/blob/master/onda.png)

Los bits proporcionados serán modulados mediante la codificación por cambio binario de fase o BPSK (*Binary phase shift keying*), que es un esquema de modulación de dos fases donde los ceros y unos en un mensaje binario son representados por dos fases diferentes en la señal portadora, donde un 1 implica un desfase de 0° y un 0 un desfase de 180° (o -180°, que sería equivalente) ([Gaussian Waves](https://www.gaussianwaves.com/2010/04/bpsk-modulation-and-demodulation-2/#:~:text=Binary%20Phase%20Shift%20Keying%20(BPSK)%20is%20a%20two%20phase%20modulation,for%20binary%200.), 2010). Matemáticamente se expresa:

<img src="https://render.githubusercontent.com/render/math?math=s_1(t) = \sin(2 \pi f t)">

<img src="https://render.githubusercontent.com/render/math?math=s_0(t) = \sin(2 \pi f t \pm \pi) = - \sin(2 \pi f t)">

por la propiedad de imparidad de la función seno. De esta manera, la onda con los primeros 10 bits codificados en BPSK se vería de la siguiente manera:

![Primeros 10 bits codificados en BPSK](https://github.com/Santihv/Tarea4/blob/master/señal.png)

### 2) Calcular la potencia promedio de la señal modulada generada.

Para calcular la potencia promedio de la señal primero es necesario calcular la potencia instantánea, donde esta sería el cuadrado de la señal:

<img src="https://render.githubusercontent.com/render/math?math=P(t) = \sin^2(2 \pi f t)">

La potencia promedio sería el promedio de la suma de cada uno de los valores cuadráticos medios de las potencias, que es lo mismo a la integral de *P(t)* desde *-T* a *T* entre dos veces el periodo:

<img src="https://render.githubusercontent.com/render/math?math=P_{prom} = \frac{1}{2T} \displaystyle\int_{-T}^{T} P(t) dt = \frac{1}{2T} \displaystyle\int_{-T}^{T} \sin^2(2 \pi f t) dt">

Este proceso de integración se efectuó con `integrate.trapz` perteneciente a la librería `scipy` y se obtuvo **Pprom = 0,49000098 W**.

### 3) Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.

Para generar el ruido se necesita establecer su potencia, la cual se expresa como función del *SNR*:

<img src="https://render.githubusercontent.com/render/math?math=P_n = \frac{P_{prom}}{10^{\frac{SNR}{10}}} = \sigma^2">

Como el ruido es AWGN este se genera con una distribución gaussiana de números aleatorios cuya desviación estándar corresponde a la raíz cuadrada de su potencia. Posteriormente, para simular que la señal emitida es distorsionada por el ruido este se le suma a la señal BPSK antes generada. Las ondas ruidosas generadas para los distintos valores de SNR se muestran a continuación:

![Rx con SNR = -2 dB](https://github.com/Santihv/Tarea4/blob/master/Rx_SNR%3D-2dB.png)

![Rx con SNR = -1 dB](https://github.com/Santihv/Tarea4/blob/master/Rx_SNR%3D-1dB.png)

![Rx con SNR = 0 dB](https://github.com/Santihv/Tarea4/blob/master/Rx_SNR%3D0dB.png)

![Rx con SNR = 1 dB](https://github.com/Santihv/Tarea4/blob/master/Rx_SNR%3D1dB.png)

![Rx con SNR = 2 dB](https://github.com/Santihv/Tarea4/blob/master/Rx_SNR%3D2dB.png)

![Rx con SNR = 3 dB](https://github.com/Santihv/Tarea4/blob/master/Rx_SNR%3D3dB.png)

### 4) Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.

El espectro de densidad de potencia de una señal aleatoria describe cómo se distribuye la potencia en todas las frecuencias. Para obtenerlo se utilizó el método de Welch del módulo `signal` de `scipy`. El gráfico de la PSD de la señal antes de pasar por el canal AWGN sería:

![PSD de la señal antes del canal AWGN](https://github.com/Santihv/Tarea4/blob/master/PSD_antes.png)

La PSD de la señal después de pasar por el canal AWGN para cada *SNR* requerido se muestra gráficamente a continuación:

![PSD de la señal después del canal AWGN con SNR = -2 dB](https://github.com/Santihv/Tarea4/blob/master/PSD_despu%C3%A9s_SNR%3D-2dB.png)

![PSD de la señal después del canal AWGN con SNR = -1 dB](https://github.com/Santihv/Tarea4/blob/master/PSD_despu%C3%A9s_SNR%3D-1dB.png)

![PSD de la señal después del canal AWGN con SNR = 0 dB](https://github.com/Santihv/Tarea4/blob/master/PSD_despu%C3%A9s_SNR%3D0dB.png)

![PSD de la señal después del canal AWGN con SNR = 1 dB](https://github.com/Santihv/Tarea4/blob/master/PSD_despu%C3%A9s_SNR%3D1dB.png)

![PSD de la señal después del canal AWGN con SNR = 2 dB](https://github.com/Santihv/Tarea4/blob/master/PSD_despu%C3%A9s_SNR%3D2dB.png)

![PSD de la señal después del canal AWGN con SNR = 3 dB](https://github.com/Santihv/Tarea4/blob/master/PSD_despu%C3%A9s_SNR%3D3dB.png)

De estos resultados se aprecia cómo antes de pasar por el canal ruidoso la potencia se distribuye en todos los armónicos de la onda portadora, mientras que después de pasar por el canal solo se distribuye en la frecuencia fundamental mientras que los armónicos son mayormente atenuados al aumentar el SNR.

### 5) Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.

La decodificación de la señal se lleva a cabo por el método de detección de energía. Para esto se calcula lo que se llamará como *pseudo energía* como la suma (no integral) de cada punto en un periodo de la onda portadora al cuadrado (la cual sería conocida en un sistema real) y la energía en cada periodo de la onda recibida *Rx* de la misma manera. Si la energía en un periodo de Rx es mayor a la mitad de la pseudo energía entonces se decodifica como un 1, si no se decodificará como un 0. La relación de errores por bit *BER* (*bit error rate*) corresponde a la relación porcentual entre la cantidad de errores en la señal recibida respecto de la enviada y la cantidad de bits totales, que en este caso son 10000. Los resultados para cada valor de *SNR* se muestran en el siguiente cuadro:

SNR | Errores | BER 
--------- | ------- | ----- 
-2 dB | 11 | 0,11% 
-1 dB | 3 | 0,03% 
 0 dB | 1 | 0,01% 
 1 dB | 0 | 0%
 2 dB | 0 | 0%
 3 dB | 0 | 0%
 
 ### 6) Graficar BER versus SNR.
 
 La representación gráfica de los datos anteriores sería:
 
 ![BER contra SNR](https://github.com/Santihv/Tarea4/blob/master/BER_vs_SNR.png)
