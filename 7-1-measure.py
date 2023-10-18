import RPi.GPIO as GPIO
from matplotlib import pyplot 
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

leds=[2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)

bits = len(dac)
levels = 2**bits

#перевод в двоичную
def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

#алгоритм последовательного приближения
def adc():
    value_res = 0
    temp_value = 0
    for i in range(bits):
        pow2 = 2 **(bits - i - 1)
        temp_value = value_res + pow2
        signal = decimal2binary(temp_value)
        GPIO.output(dac, signal)
        time.sleep(0.01)
        compVal = GPIO.input(comp)
        if compVal ==0:
            value_res = value_res + pow2

    return value_res    

try:
    value = 0
    data = []
    data1 = []
    count = 0
    print ('начало зарядки ')
    start_time = time.time()
    while value < 206:
        value = adc()
        print(value, ' ', value / 256 * 3.3)
        data1.append(value)
        data.append(value / 256 * 3.3)
        count += 1
        GPIO.output(leds, decimal2binary(value))
    GPIO.setup (troyka, GPIO.OUT, initial = GPIO.LOW) 

    count = 0
    print ('начало разрядки ')
    while value > 177:
        value = adc()
        print(value, ' ', value / 256 * 3.3)
        data1.append(value)
        data.append(value / 256 * 3.3)
        count += 1
        GPIO.output(leds, decimal2binary(value))

    time_of = time.time() - start_time

    #запись в файл
    with open('data.txt', 'w') as f:
        for i in data1:
             f.write(str(i) + '\n')

    with open('settings.txt', 'w') as f:
        f.write('частота дискретизации ' + str(count / time_of ) + 'изм в секунду' +'\n')
        f.write('шаг квантования АЦП ' + str(3.3 / 256) + 'вольт' + '\n')

    print ('продолжительность ', time_of,  'период', time_of / count, 'частота дискретизации', count / time_of , 'шаг квантования АЦП ', (3.3 / 256))  
     

    #графики      
    pyplot.plot(data)
    pyplot.xlabel('iterations')
    pyplot.ylabel('voltage')
    pyplot.show()

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup() 