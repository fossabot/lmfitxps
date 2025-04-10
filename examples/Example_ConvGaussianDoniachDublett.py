import numpy as np
import matplotlib.pyplot as plt
import lmfit
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from lmfitxps import models
import matplotlib as mpl

exec_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
dublett = models.ConvGaussianDoniachDublett(prefix='dublett_', independent_vars=["x"])
bg=models.TougaardBG(independent_vars=["x","y"], prefix='tougaard_')
fit_model=dublett+bg
data = np.genfromtxt(exec_dir + '/examples/clean_Au_4f.csv', delimiter=',', skip_header=0)
x = data[:, 0]
y = data[:, 1]
output_dir = os.path.join(exec_dir, 'examples/', 'plots')
os.makedirs(output_dir, exist_ok=True)

fig, (ax1, ax2) = plt.subplots(nrows=2,gridspec_kw={'height_ratios': [1, 1]}, sharex=True)
fig.patch.set_facecolor('#FCFCFC')

params = lmfit.Parameters()
params.add('tougaard_B', value=148.969)
params.add('tougaard_C', value=144.506, vary=False)
params.add('tougaard_D', value=268.598, vary=False)
params.add('tougaard_C_d', value=0.281, vary=False)
params.add('tougaard_extend', value=30)
params.add('dublett_amplitude', value=np.max(y))
params.add('dublett_sigma', value=0.2126)
params.add('dublett_gamma', value=0.04)
params.add('dublett_gaussian_sigma', value=0.0892)
params.add('dublett_center', value=92.2273)
params.add('dublett_soc', value=3.67127)
params.add('dublett_height_ratio', value=0.7)
params.add('dublett_fct_coster_kronig', value=1.04)

result = fit_model.fit(y, params, y=y, x=x, weights=1 /(np.sqrt(y)))
comps = result.eval_components(x=x, y=y)
print(result.fit_report())

cmap = mpl.colormaps['tab20']
ax1.plot(x, result.best_fit, label='Best Fit', color=cmap(0))
ax1.plot(x, y, 'x', markersize=4, label='Data Points', color=cmap(2))

ax1.plot(x, comps['tougaard_'], label='Tougaard background', color='black')
ax1.plot(x, comps['dublett_'] + comps['tougaard_'], color=cmap(4), label="Doniach-Dublett")

ax1.fill_between(x, comps['dublett_'] + comps['tougaard_'], comps['tougaard_'], alpha=0.5,color=cmap(5))
ax1.legend()
ax1.set_xlabel('bin. energy in eV')
ax1.set_ylabel('intensity in arb. units')
# Set ticks only inside
ax1.tick_params(axis='x', which='both',top=True, direction='in')
ax1.tick_params(axis='y', which='both', right=True,direction='in')
ax2.tick_params(axis='x', which='both',top=True, direction='in')
ax2.tick_params(axis='y', which='both', right=True, direction='in')

ax1.set_yticklabels([])
ax1.set_title(f'ConvGaussian DoniachDublett using kin. energy scale')
fig.subplots_adjust(hspace=0)
ax1.set_xlim(np.min(x), np.max(x))
# Residual plot
residual = result.residual
ax2.plot(x, residual)
ax2.set_xlabel('kin. energy in eV')
ax2.set_ylabel('Residual')

plot_filename = os.path.join(output_dir, f'plot_dublett_kin.png')
fig.savefig(plot_filename, dpi=300)
plt.close(fig)


dublett = models.ConvGaussianDoniachDublett(prefix='dublett_', independent_vars=["x"])
bg=models.TougaardBG(independent_vars=["x","y"], prefix='tougaard_')
fit_model=dublett+bg
data = np.genfromtxt(exec_dir + '/examples/clean_Au_4f.csv', delimiter=',', skip_header=0)
x = 180-data[:, 0]
y = data[:, 1]
output_dir = os.path.join(exec_dir, 'examples/', 'plots')
os.makedirs(output_dir, exist_ok=True)

fig2, (ax21, ax22) = plt.subplots(nrows=2,gridspec_kw={'height_ratios': [1, 1]}, sharex=True)
fig2.patch.set_facecolor('#FCFCFC')

params = lmfit.Parameters()
params.add('tougaard_B', value=148.969)
params.add('tougaard_C', value=144.506, vary=False)
params.add('tougaard_D', value=268.598, vary=False)
params.add('tougaard_C_d', value=0.281, vary=False)
params.add('tougaard_extend', value=30)
params.add('dublett_amplitude', value=np.max(y))
params.add('dublett_sigma', value=0.2126)
params.add('dublett_gamma', value=0.04, min=0)
params.add('dublett_gaussian_sigma', value=0.0892)
params.add('dublett_center', value=87.663)
params.add('dublett_soc', value=3.67127)
params.add('dublett_height_ratio', value=0.7)
params.add('dublett_fct_coster_kronig', value=1.04)



result = fit_model.fit(y, params, y=y, x=x, weights=1 /(np.sqrt(y)))
comps = result.eval_components(x=x, y=y)
print(result.fit_report())
cmap = mpl.colormaps['tab20']
ax21.plot(x, result.best_fit, label='Best Fit', color=cmap(0))
ax21.plot(x, y, 'x', markersize=4, label='Data Points', color=cmap(2))

ax21.plot(x, comps['tougaard_'], label='Tougaard background', color='black')
ax21.plot(x, comps['dublett_'] + comps['tougaard_'], color=cmap(4), label="Doniach-Dublett")

ax21.fill_between(x, comps['dublett_'] + comps['tougaard_'], comps['tougaard_'], alpha=0.5,color=cmap(5))
ax21.legend()
ax21.set_xlabel('bin. energy in eV')
ax21.set_ylabel('intensity in arb. units')
# Set ticks only inside
ax21.tick_params(axis='x', which='both',top=True, direction='in')
ax21.tick_params(axis='y', which='both', right=True,direction='in')
ax22.tick_params(axis='x', which='both',top=True, direction='in')
ax22.tick_params(axis='y', which='both', right=True, direction='in')

ax21.set_yticklabels([])
ax21.set_title(f'ConvDoniachDublettModel using bin. energy scale')
fig2.subplots_adjust(hspace=0)
ax21.set_xlim(np.min(x), np.max(x))
# Residual plot
residual = result.residual
ax22.plot(x, residual)
ax22.set_xlabel('bin. energy in eV')
ax22.set_ylabel('residual')
ax22.set_xlim(np.max(x), np.min(x))
plot_filename = os.path.join(output_dir, f'plot_dublett_bin.png')
fig2.savefig(plot_filename, dpi=300)
plt.close(fig2)