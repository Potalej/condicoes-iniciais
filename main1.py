import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider
from src.ler import ler_valores_iniciais
from src.mecanica import energia_cinetica, energia_potencial

dados = ler_valores_iniciais('data/vi/teste.txt')

T = energia_cinetica(dados['massas'], dados['momentos'])
V = energia_potencial(dados['G'], dados['massas'], dados['posicoes'])
H = T + V

def f(fator_potencial, fator_cinetica):
  return fator_cinetica**2 * T + (1/fator_potencial) * V

# fator_potencial = np.linspace(0.5, 1.5, 100)

# Define initial parameters
init_potencial = 1
init_cinetica = 1

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
# line, = ax.plot(fator_potencial, f(fator_potencial, 1), lw=2)
ax.set_xlabel('Time [s]')

# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
amp_cinetica = Slider(
    ax=axfreq,
    label='Cinetica',
    valmin=0.1,
    valmax=2,
    valinit=init_cinetica,
    valstep=0.5
)

# Make a vertically oriented slider to control the amplitude
axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
amp_potencial = Slider(
    ax=axamp,
    label="Potencial",
    valmin=0.1,
    valmax=2,
    valinit=init_potencial,
    orientation="vertical",
    valstep=0.5
)


# The function to be called anytime a slider's value changes
def update(val, quem):
  if quem == 1:
    # coloca a energia potencial em funcao da cinetica
    valor_cinetica  = val
    valor_potencial = V / (H - valor_cinetica**2 * T)
    amp_potencial.set_val(valor_potencial)
  else:
    # coloca a energia cinetica em funcao da potencial
    valor_potencial  = val
    valor_cinetica = abs((H - V/valor_potencial) / T)**0.5
    amp_cinetica.set_val(valor_cinetica)

  R, P = dados['posicoes'], dados['momentos']

  ax.clear()
  R_1, P_1 = [], []
  for a in range(len(dados['massas'])):
    Ra = [R[a][0]/valor_potencial, R[a][1]/valor_potencial]
    ax.scatter(Ra[0],Ra[1])

  # ax.set_xlim(amp_cinetica.valmin,amp_cinetica.valmax)
  # ax.set_ylim(f(amp_potencial.valmin,amp_cinetica.valmin),f(amp_potencial.valmax,amp_cinetica.valmax))
  # line.set_ydata(f(amp_potencial.val, amp_cinetica.val))
  fig.canvas.draw_idle()


# register the update function with each slider
amp_cinetica.on_changed(lambda x: update(x,1))
amp_potencial.on_changed(lambda x: update(x,2))

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
plt.show()