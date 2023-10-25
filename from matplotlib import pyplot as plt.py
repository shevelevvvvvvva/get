import matplotlib.pyplot as plt
import numpy as np


data_array = np.loadtxt('/home/b03-301/Downloads/data.txt', dtype=int)
data_settings = np.loadtxt('/home/b03-301/Downloads/settings.txt', dtype=float)

data_time = np.linspace(0, data_settings[0], data_array.size) * 1000
data_array = data_array * data_settings[1]

fig, ax = plt.subplots()

ax.minorticks_on()
ax.grid(which = 'minor', color = 'grey', ls = ':')
ax.grid('major')

ax.plot(data_time, data_array, color = 'red', ls = '-', linewidth = 0.5, marker = 'd', markersize = 1, label = 'U(t)')

ax.set_xlim(np.min(data_time), np.max(data_time)+2)
ax.set_ylim(np.min(data_array), np.max(data_array)+0.5)

ax.set_xlabel('Время, c')
ax.set_ylabel('Напряжение, В')

plt.text(8.5,1.25, 'Время зарядки: 5,72 с')
plt.text(8.5,1.1, 'Время разряки: 7,74 с')
ax.set_title('Процесс зарядки и разрядки конденсатора')

ax.legend()

plt.show()
fig.savefig('/home/b03-301/Downloads/fig.png')
fig.savefig('/home/b03-301/Downloads/fig.svg')