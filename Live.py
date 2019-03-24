from pycbc import noise
import pycbc.psd
from pycbc.waveform import get_td_waveform
import time
import pylab
import matplotlib.pyplot as plt

flow = 30.0
delta_f = 1.0 / 16
flen = int(2048 / delta_f) + 1
# noinspection PyUnresolvedReferences
psd = pycbc.psd.aLIGOZeroDetHighPower(flen, delta_f, flow)
delta_t = 1.0 / 4096
tsamples = int(32 / delta_t)
n_ts = pycbc.noise.noise_from_psd(tsamples, delta_t, psd, seed=127)
hp, hc = get_td_waveform(approximant="SEOBNRv4_opt", mass1=32, mass2=56, delta_t=1.0/4096, f_lower=30)
# print(hp[:10])
n_ts = list(n_ts)
# print("Noises : ", n_ts[:10])
noises = []
plus_p = list(hp)
wave = []

for i in n_ts:
    noises.append(i*10**3.17)

for i in range(len(hp)):
    wave.append(noises[i]+plus_p[i])


fig = plt.figure()
ax = fig.add_subplot(212)
bx = fig.add_subplot(211)
fig.show()
i = 0
x, y, ny = [], [], []

for i in range(len(hp)):
    x.append(i)
    y.append(hp[i])
    ny.append(noises[i])

    ax.plot(x, y, color='b')
    bx.plot(x, ny, color='r')
    fig.canvas.draw()

    # ax.set_xlim(left=max(0, i - 50), right=i + 50)

    time.sleep(0.000000005)
