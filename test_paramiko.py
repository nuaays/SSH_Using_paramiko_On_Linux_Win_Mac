
import os, sys, platform
sys.path.append( os.path.dirname( os.path.abspath(__file__) ) )
import Lib
import Crypto, paramiko
import shutil, glob, zipfile, tempfile, optparse, ConfigParser

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.header import Header
from email.mime.image import MIMEImage
from email.Utils import COMMASPACE, formatdate
from email import Encoders


print platform.architecture()
print platform.node()
print platform.platform()
print platform.processor()
print platform.python_build()
print platform.python_compiler()
print platform.python_branch()  
print platform.python_implementation()  
print platform.python_revision()  
print platform.python_version()  
print platform.python_version_tuple() 
print "-----------------------"
print platform.release()
print platform.system()   #Darwin #Linux #Windows
print "----------------------"
print platform.version()
print platform.uname()
print "----------------------"

 
"""
ClearUp *.pyc
"""
print "============================================================================================"
#clear *.pycos.path.realpath(__file__)
for root, dirs, files in os.walk( os.path.dirname(__file__) ):
	[os.remove( os.path.join(root, name) ) for name in files if name.endswith(".pyc") ]
	#for name in files:
	#	filename = os.path.realpath( os.path.join(root, name) )
	#	if filename.endswith(".pyc"):
	#		os.remove(filename)



"""
SSH To AWS Linux using paramiko
"""
paramiko.util.log_to_file('test.log')
ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('54.*.*.*',port=22,username='ec2****',password='***',compress=True)
stdin, stdout, stderr = ssh.exec_command('hostname;uptime;whoami')
print stdout.read()
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print ssh.exec_command('w')[1].read()
ssh.close()






