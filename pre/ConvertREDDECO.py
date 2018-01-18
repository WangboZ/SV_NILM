from nilmtk.dataset_converters import convert_redd, convert_eco
#convert redd and eco to h5
convert_redd('/net/linse8/no_backup_01/s1183/data/low_freq', '/net/linse8/no_backup_01/s1183/data/redd.h5')
convert_eco('/net/linse8/no_backup_01/s1183/data/eco', '/net/linse8/no_backup_01/s1183/data/eco.h5')