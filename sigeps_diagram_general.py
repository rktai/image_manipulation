import numpy as np
import matplotlib.pyplot as plt

# dummy parameters
fy = 1731
Emod = 197880
eps_y = 0.0087
fu = 1931
eps_u = 0.044

# Constitutive relation
def constitutive_relation(eps):
    if eps >= 0 and eps <= eps_y:
        return Emod * eps
    elif eps > eps_y and eps <= eps_u:
        return fy + (fu - fy) / (eps_u - eps_y) * (eps - eps_y)
    elif eps > eps_u:
        return 0
    else:
        raise Exception("eps value in func_width not valid")

# returns list of stress from list of strains and defined function
def eps_to_sig(lst_eps, func):
    lst_sig = []
    for i in range(len(lst_eps)):
        sig = func(lst_eps[i])
        lst_sig.append(sig)
    return lst_sig

# Create segmented lists sig and eps per contour
n_steps = 2
eps_begin = 0
eps_end = 0.33 * eps_y
lst_eps1 = list(np.linspace(eps_begin, eps_end, n_steps))
lst_sig1 = eps_to_sig(lst_eps1, constitutive_relation)

n_steps = 2
eps_begin = 0.33 * eps_y
eps_end = 0.67 * eps_y
lst_eps2 = list(np.linspace(eps_begin, eps_end, n_steps))
lst_sig2 = eps_to_sig(lst_eps2, constitutive_relation)

n_steps = 2
eps_begin = 0.67 * eps_y
eps_end = 1 * eps_y
lst_eps3 = list(np.linspace(eps_begin, eps_end, n_steps))
lst_sig3 = eps_to_sig(lst_eps3, constitutive_relation)


n_steps = 2
eps_begin = eps_y
eps_end = eps_u
lst_eps4 = list(np.linspace(eps_begin, eps_end, n_steps))
lst_sig4 = eps_to_sig(lst_eps4, constitutive_relation)

n_steps = 1000
eps_begin = eps_u
eps_end = 1.5 * eps_u
lst_eps5 = list(np.linspace(eps_begin, eps_end, n_steps))
lst_sig5 = eps_to_sig(lst_eps5, constitutive_relation)

##### plot diagram
# Initiate figure
fig = plt.figure(figsize=(8, 4))
ax1 = fig.add_subplot(111)

# Plot lines
ax1.plot(lst_eps1, lst_sig1, color = "#0000ff")
ax1.plot(lst_eps2, lst_sig2, color = "#00ffff")
ax1.plot(lst_eps3, lst_sig3, color = "#00ff00")
ax1.plot(lst_eps4, lst_sig4, color = "#ffff00")
ax1.plot(lst_eps5, lst_sig5, color = "#ff0000")

# Label settings
ylabel = r'$\sigma$' + ' [N/mm' + r'$^2$' +  ']'
ax1.set_ylabel(ylabel)

xlabel = r'$\epsilon$' + ' [-]'
ax1.set_xlabel(xlabel)

# Set limits for axes
ax1.set_xlim(0, 1.25*eps_u)
ax1.set_ylim(0, 1.1 * fu)

# Set ticks
ax1.tick_params(bottom=True, top=True, left=True, right=True, direction='in')
ax1.locator_params(axis="x", nbins=6)
# ax1.locator_params(axis="y", nbins=6)

# Set gridlines
ax1.grid(color = 'grey', linestyle = '--', linewidth = 0.5)

# Adjust subplot
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.99, top=0.99)

plt.show()
