"""
This is the one place where you set the path structure of the LO code.
The info is stored in the dict Ldir.

All paths are pathlib.Path objects.

This program is meant to be loaded as a module by Lfun which then adds more
entries to the Ldir dict based on which model run you are working on.

Users should copy this to LO_user/get_lo_info.py, edit as needed, and make it into
their own GitHub repo.

"""
import os
from pathlib import Path

# defaults that should work on all machines
parent = Path(__file__).absolute().parent.parent
LO = parent / 'LO'
LOo = parent / 'LO_output'
LOu = parent / 'LO_user'
data = parent / 'LO_data'


# These are places where the ROMS history files are kept
roms_out = Path('a1/fsoares/LiveOcean/LO_roms')
roms_out1 = parent / 'LO_roms' # placeholder
roms_out2 = parent / 'BLANK'
roms_out3 = parent / 'BLANK'
roms_out4 = parent / 'BLANK'



HOME = Path.home()
try:
    HOSTNAME = os.environ['HOSTNAME']
except KeyError:
    HOSTNAME = 'BLANK'
    
# debugging
# print('** from get_lo_info.py **')
# print('HOME = ' + str(HOME))
# print('HOSTNAME = ' + HOSTNAME)


Ldir0 = dict()

Ldir0['parent'] = parent
Ldir0['LO'] = LO
Ldir0['LOo'] = LOo
Ldir0['LOu'] = LOu
Ldir0['data'] = data
Ldir0['roms_out'] = roms_out
Ldir0['roms_out1'] = roms_out1
Ldir0['roms_out2'] = roms_out2
Ldir0['roms_out3'] = roms_out3
Ldir0['roms_out4'] = roms_out4



