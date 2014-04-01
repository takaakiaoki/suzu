import os
import sys

import json

# initial profile data 
config_default = {
        'version':0,
        'lastdir':''
        }

class Error(Exception):
    def __init__(self, mesg):
        Exception.__init__(self)
        self.mesg = mesg

    def __str__(self):
        return str(self.mesg)

def pathinfo():
    """ get profile directory path
        if SUZUPROFDIR is defined use it
        windows: APPDATA\suzu
        unixs: HOME/.suzu
        @return path infomation of profile data, otherwize None
    """
    info = {}
    pdir = None
    if 'SUZUPROFDIR' in os.environ:
        pdir = os.environ['SUZUPROFDIR']
    elif sys.platform == 'win32':
        try:
            pdir = os.path.join(os.environ['APPDATA'], 'suzu')
        except KeyError:
            pdir = None
    else:
        try:
            pdir = os.path.join(os.environ['HOME'], '.suzu')
        except KeyError:
            pdir = None

    if pdir:
        info['profiledir'] = pdir
        info['config'] = os.path.join(pdir, 'config.json')

        return info

    return None

def initialize():
    """ 1. if pathinfo['profiledir'] does not exist dig it.
        2. if pathinfo['config'] does not exist, create it.
        returns pinfo
    """
    pinfo = pathinfo()

    if not pinfo:
        raise Error('cannot decide profile directory, $SUZUPROFILEDIR, $APPDATA, or $HOME should be configured.')

    # dig profdir
    if not os.path.isdir(pinfo['profiledir']):
        os.mkdir(pinfo['profiledir'])

    # test dir
    if not os.path.isdir(pinfo['profiledir']):
        raise Error('profile directory {} does not exist, nor cannot create'.format(pinfo['profiledir']))

    # test profile data file
    if not os.path.isfile(pinfo['config']):
        with open(pinfo['config'], 'w') as stream:
            json.dump(config_default, stream, indent=2, sort_keys=True)

    # test file (do not care on the contents)
    if not os.path.isfile(pinfo['config']):
        raise Error('config file {} does not exist, nor cannot create'.format(pinfo['config']))

    return pinfo

def load_config(stream):
    return json.load(stream)

def dump_config(d, stream):
    json.dump(d, stream, indent=2, sort_keys=True)

if __name__ == '__main__':
    p = initialize()

    print(p)
