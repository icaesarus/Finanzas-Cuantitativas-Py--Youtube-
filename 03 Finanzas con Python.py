import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis,chi2

x_size=10**6
degrees_freedom = 500
type_random_variable= 'student'

if type_random_variable =='normal':
    x= np.random.standard_normal(size=x_size)
    x_str= type_random_variable
elif type_random_variable =='exponential':
    x= np.random.standard_exponential(size=x_size)
elif type_random_variable =='student':
    x= np.random.standard_t(size=x_size, df=degrees_freedom)
    x_str = type_random_variable + ' (df= ' + str(degrees_freedom)+ ')'

plt.figure()
plt.hist(x, bins=500)
plt.title('Histogram ' + x_str)
          
plt.show()
x_mean= np.mean(x)
x_stdev= np.std(x)
x_skew = skew(x)
x_kurt = kurtosis(x)
x_median = np.percentile(x,50)

#codigo nueco metido
