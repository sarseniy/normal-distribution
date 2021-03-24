import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
M = 10

plt.figure(figsize=(15,7))

a = []
with open('info.txt', 'r') as file:
    for line in file:
        b = line.strip()
        print(b)
        x = float(b)
        a.append(x)

dr = (max(a) - min(a)) / M
x = np.arange(min(a) - 0.05, max(a) + 0.091, 0.001)
n, bins, patches = plt.hist(a, M, weights=[1/len(a)/dr] * len(a), facecolor='gray')
sigma = 0.090834124

plt.annotate('$R_{cp}$', xy=(np.mean(a), 0),  xycoords='data',
            xytext=(np.mean(a), 0.3), textcoords='data',
            arrowprops=dict(facecolor='r'))

plt.annotate('$R_{cp} - \sigma$', xy=(np.mean(a) - sigma, 0),  xycoords='data',
            xytext=(np.mean(a) - sigma - 0.015, 0.3), textcoords='data',
            arrowprops=dict(facecolor='r', arrowstyle = '->'))

plt.annotate('$R_{cp} - 2\sigma$', xy=(np.mean(a) - 2 * sigma, 0),  xycoords='data',
            xytext=(np.mean(a) - 2 * sigma - 0.019, 0.3), textcoords='data',
            arrowprops=dict(facecolor='r', arrowstyle = '->'))

plt.annotate('$R_{cp} - 3\sigma$', xy=(np.mean(a) - 3 * sigma, 0),  xycoords='data',
            xytext=(np.mean(a) - 3 * sigma - 0.018, 0.3), textcoords='data',
            arrowprops=dict(facecolor='r', arrowstyle = '->'))

plt.annotate('$R_{cp} + \sigma$', xy=(np.mean(a) + sigma, 0),  xycoords='data',
            xytext=(np.mean(a) + sigma - 0.015, 0.3), textcoords='data',
            arrowprops=dict(facecolor='r', arrowstyle = '->'))

plt.annotate('$R_{cp} + 2\sigma$', xy=(np.mean(a) + 2 * sigma, 0),  xycoords='data',
            xytext=(np.mean(a) + 2 * sigma - 0.018, 0.3), textcoords='data',
            arrowprops=dict(facecolor='r', arrowstyle = '->'))

plt.annotate('$R_{cp} + 3\sigma$', xy=(np.mean(a) + 3 * sigma, 0),  xycoords='data',
            xytext=(np.mean(a) + 3 * sigma - 0.018, 0.3), textcoords='data',
            arrowprops=dict(facecolor='r', arrowstyle = '->'))

sred = np.mean(a)
plt.text(8.4, 4, r'$\langle R \rangle = 8,21$ кОм')
plt.text(8.4, 3.8, r'$\sigma = 0,09$ кОм')

plt.plot(x, 1 / ((2 * np.pi)**0.5 * sigma) * np.exp(-(x - np.mean(a))**2/(2 * sigma**2)), 'r')

kol = []
for i in range(0,M+1):
    kol.append(0)


for i in range(0,M+1):
    niz = min(a) + i * dr
    verh = min(a) + (i + 1) * dr
    for elem in a:
        if niz <= elem < verh:
            kol[i] += 1
            print(elem, i)

omega = []
for i in range(0, M+1):
    omega.append(kol[i]/len(a)/dr * 100)
print(omega)

print(kol)
print(min(a))

chet = 0
for elem in a:
    if np.mean(a) - 3 * sigma < elem < np.mean(a) + 3 * sigma:
        chet += 1
print(chet)
plt.xlabel('Сопротивление, $R$')
plt.ylabel('Плотность вероятности, $\omega$')
#plt.title('Histogram of $R$')
#plt.grid(True)
plt.show()
