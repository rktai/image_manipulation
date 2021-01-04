# Based on RTD 2017 version 2.1

from decimal import Decimal

# input parameters
fcm = 74.8E+06 # concrete compressive strength [N/m2]
ftm = 4.53E+06 # mexperimental, not calculated from fcm
hc = 0.050 # crackband width [m]

print("fcm = " + '%.5E' % Decimal(str(fcm)) + " [N/m2]" )
print("hc = " + '%.5E' % Decimal(str(hc)) + " [m]" )

# calculate concrete properties
Ec =  ((2.15*10**4)*((fcm*10**-6)/10)**(1/3))*10**6 # concrete E-modulus [N/m2]
Gf =  73*(fcm*10**-6)**0.18 # concrete fracture energy in [N/m]
Gc =  250*Gf # concrete fracture energy in [N/m]
# ftm = (0.3*((fcm*10**-6)-8)**(2/3))*10**6 # concrete tensile strength [N/m2]
print("Ec = " + '%.5E' % Decimal(str(Ec)) + " [N/m2]" )
print("Gf = " + '%.5E' % Decimal(str(Gf)) + " [N/m2]" )
print("Gc = " + '%.5E' % Decimal(str(Gc)) + " [N/m2]" )
print("ftm = " + '%.5E' % Decimal(str(ftm)) + " [N/m2]" )

# Parabolic compression curve concrete
alpha_c3 = -1/3*fcm/Ec # strain at 1/3 of maximum concrete compressive strength
alpha_c = 5*alpha_c3 # strain at maximum concrete compressive strength
alpha_u = min(alpha_c-1.5*Gc/(hc*fcm),2.5*alpha_c) # ultimate compressive strain 
print("eps_c_top = " + '%.5E' % Decimal(str(alpha_c)))
print("eps_c_ult = " + '%.5E' % Decimal(str(alpha_u)))

# Hordijk tension softening
eps_t_el = ftm/Ec
eps_t_ult =5.136*Gf/(hc*ftm)
print("eps_t_el = " + '%.5E' % Decimal(str(eps_t_el)))
print("eps_t_ult = " + '%.5E' % Decimal(str(eps_t_ult)))