 
from __future__ import print_function
import nilmtk
from nilmtk.utils import print_dict
from nilmtk import DataSet
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
from matplotlib.pylab import plt


# import dataset
dataset = DataSet('/net/linse8/no_backup_01/s1183/data/ukdale.h5')

# set window
dataset.set_window("2014-06-01", "2014-07-01")



# house 1
BUILDING = 1
elec = dataset.buildings[BUILDING].elec
# appliance kettle
kettle= elec['kettle']
# arguments for get_activations
MIN_OFF=0
MIN_ON=12
ON_POWER=10
#get activations and print the number of activations
activations1 = kettle.get_activations(min_off_duration=MIN_OFF, min_on_duration=MIN_ON,on_power_threshold=ON_POWER)
print("Number of activations =", len(activations1))

# plot activations
for i in range(15):
  #activations[i].plot()
   activations1.plot()
   plt.savefig('building1kettle'+str(i))
   plt.close()
  