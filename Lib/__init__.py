#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yang Sen C
# DAte  : 2014-11-19

import os, sys, platform, shutil
sys.path.append( os.path.dirname( os.path.abspath(__file__) ) )
print os.path.dirname( os.path.abspath(__file__) )

"""
"""
def import_Crypto():
    Lib_Path       = os.path.dirname( os.path.abspath(__file__) )
    Crypto_default = os.path.join( Lib_Path, "Crypto"       )
    Crypto_linux   = os.path.join( Lib_Path, "Crypto_linux" )
    Crypto_win     = os.path.join( Lib_Path, "Crypto_win"   )
    Crypto_mac     = os.path.join( Lib_Path, "Crypto_mac"   )
    
    if os.path.exists( Crypto_default ):
        shutil.rmtree( Crypto_default )

    if platform.system() == "Windows":
        shutil.copytree( Crypto_win, Crypto_default)
    elif platform.system() == "Linux":
        shutil.copytree( Crypto_linux, Crypto_default)
    elif platform.system() == "Darwin":
        shutil.copytree( Crypto_mac, Crypto_default)
    else:
        print "[ERROR] Current System:%s is not Supported!" % platform.system()
        sys.exit(1)
    pass


#Import Suited Crypto For Current System
import_Crypto()
import Crypto

#
if sys.version_info < (2, 2):
    raise RuntimeError('You need python 2.2 for this module.')

__author__  = "Yang Sen C <Sen.B.Yang@alcatel-sbell.com.cn>"
__version__ = "1.0.0"
__license__ = "GNU Lesser General Public License (LGPL)"