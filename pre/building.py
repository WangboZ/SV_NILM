from __future__ import print_function
import nilmtk
from nilmtk.utils import print_dict
from nilmtk import DataSet
dataset = DataSet('/net/linse8/no_backup_01/s1183/data/ukdale.h5')

#print apliances in the buildings

Buiding = 1
print(dataset.buildings[Buiding].elec)

elec = dataset.buildings[Buiding].elec
# plot mains
elec.mains().plot()