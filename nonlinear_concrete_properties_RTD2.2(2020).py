# Non-linear concrete properties based on MC2010 (2012) en RTD 2020 version 2.2

import math
from decimal import Decimal

# input
fcm: float = 54.6  # mean concrete compressive strength in MPa
# TODO: update script with kwargs and overwrite modelcode formulas

# calculate concrete properties
delta_f = 8  # [MPa]
fck = fcm - 8  # [MPa]

if fck <= 50.0:
    fctm = 0.3 * fck ** (2 / 3)  # [MPa]
else:
    fctm = 2.12 * math.log(1 + 0.1 * fcm)  # [MPa]

fctk_lower_5th = 0.7 * fctm  # [MPa]
fctk_upper_95th = 1.3 * fctm  # [MPa]

Gfm = 0.073 * fcm ** 0.18  # [N/mm]
Gcm = 250 * Gfm  # [N/mm]

Gfk = 0.7 * 0.073 * fcm ** 0.18  # [N/mm]
Gck = 250 * fck / fcm * 0.073 * fcm ** 0.18  # [N/mm]

Ec = 21_500 * (0.1 * fcm) ** (1 / 3)  # [N/mm2]

# print concrete properties
msg = f""""
Ec = {'%.5E' % Decimal(str(Ec))} [N/mm2] = {'%.5E' % Decimal(str(Ec * 10 ** 6))} [N/m2]

Characteristic properties:
fck = {'%.5E' % Decimal(str(fck))} [N/mm2] = {'%.5E' % Decimal(str(fck * 10 ** 6))} [N/m2]
fctk;0.05 = {'%.5E' % Decimal(str(fctk_lower_5th))} [N/mm2] = {'%.5E' % Decimal(str(fctk_lower_5th * 10 ** 6))} [N/m2]
fctk;0.95 = {'%.5E' % Decimal(str(fctk_upper_95th))} [N/mm2] = {'%.5E' % Decimal(str(fctk_upper_95th * 10 ** 6))} [N/m2]
Gfk = {'%.5E' % Decimal(str(Gfk))} [N/mm] = {'%.5E' % Decimal(str(Gfk * 1000))} [N/m]
Gfk = {'%.5E' % Decimal(str(Gck))} [N/mm] = {'%.5E' % Decimal(str(Gck * 1000))} [N/m]

Mean properties:
fcm = {'%.5E' % Decimal(str(fcm))} [N/mm2] = {'%.5E' % Decimal(str(fcm * 10 ** 6))} [N/m2] )
fctm = {'%.5E' % Decimal(str(fctm))} [N/mm2] = {'%.5E' % Decimal(str(fctm * 10 ** 6))} [N/m2] )
Gfm = {'%.5E' % Decimal(str(Gfm))} [N/mm] = {'%.5E' % Decimal(str(Gfm * 1000))} [N/m]
Gcm = {'%.5E' % Decimal(str(Gcm))} [N/mm] = {'%.5E' % Decimal(str(Gcm * 1000))} [N/m]
"""
print(msg)

# Bepalen karakteristieke punten in druk en trekdiagram


# Parabolic compression curve concrete
# fcm = 54.8 # hardcoded, deactivate if using calculated values
# # Ec =   # hardcoded, deactivate if using calculated values
# # Gc = 30120.3 # hardcoded, deactivate if using calculated values
# hc = 80 # hardcoded, deactivate if using calculated values
# alpha_c3 = -1/3*fcm/Ec # strain at 1/3 of maximum concrete compressive strength
# alpha_c = 5*alpha_c3 # strain at maximum concrete compressive strength
# alpha_u = min(alpha_c-1.5*Gcm/(hc*fcm),2.5*alpha_c) # ultimate compressive strain
# print("hc = " + '%.5E' % Decimal(str(hc)) + " [m]" )
# print("eps_c_top = " + '%.5E' % Decimal(str(alpha_c)))
# print("eps_c_ult = " + '%.5E' % Decimal(str(alpha_u)))
#
# # Hordijk tension softening
# # ftm = 2.6965E+06 # hardcoded, deactivate if using calculated values
# # Ec =   # hardcoded, deactivate if using calculated values
# # Gf = 94.4 # hardcoded, deactivate if using calculated values
# # hc =  # hardcoded, deactivate if using calculated values
# eps_t_el = ftm/Ec
# eps_t_ult =5.136*Gf/(hc*ftm)
# print("eps_t_el = " + '%.5E' % Decimal(str(eps_t_el)))
# print("eps_t_ult = " + '%.5E' % Decimal(str(eps_t_ult)))
