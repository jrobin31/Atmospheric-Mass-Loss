
# coding: utf-8

# In[ ]:

Here we calculate the proportionality constant for Equation 14 of Owen & Jackson 2012 MNRAS 425, 2931


# In[1]:

from astropy import units as u
import numpy as np
l_x = 1e30 * u.erg / u.second
a_au = 0.1 * u.au
Z = 1
m_dot_earth = 10**10.6 * u.g / u.second

#Printing these will display the corresponding units 
print ('Values we get from Fig. 5:')
print (l_x)
print (a_au)
print (m_dot_earth)

#Astropy units will convert AU units to cgs units (cm)
a_cm = a_au.to(u.cm)
print('Convert orbital radius to cm:')
print (a_cm)

#Now it's time to calculate the proportionality constant by multiplying the 
#right-hand side of the equation to get an exact value
prop_constant = m_dot_earth * Z**0.77 * a_au**2 / l_x
print ('Proportionality constant for Eq. 14 (auto unit conversion):')
#When we print, we can use the .cgs attribute from astropy.units to force 
#the code to do unit cancelation and print the result in cgs units
print (prop_constant.cgs)


# In[3]:

l_x_quasar = 1e46 * u.erg / u.second
Z = 1
m_dot_earth = 0.1 * (5.1e18 * u.kg) / (1e8 * u.year) 

#Now it's time to calculate the a_au by rearranging equation 14
a_au = np.sqrt(l_x_quasar * prop_constant / m_dot_earth / Z**0.77)

#When we print, we can use the .pc attribute from astropy.units to force 
#the code to do unit cancelation and print the result in parsecs
print (a_au.to(u.pc))


# In[ ]:



