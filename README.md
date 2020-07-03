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
