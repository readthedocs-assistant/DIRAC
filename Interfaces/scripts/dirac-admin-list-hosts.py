#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :   dirac-admin-list-users
# Author : Adrian Casajus
########################################################################
__RCSID__   = "$Id$"
__VERSION__ = "$Revision: 1.1 $"
from DIRACEnvironment import DIRAC
from DIRAC.Core.Base import Script

Script.registerSwitch( "e", "extended", "Show extended info" )

from DIRAC.Interfaces.API.DiracAdmin                         import DiracAdmin

Script.parseCommandLine( ignoreErrors = True )
args = Script.getPositionalArgs()

diracAdmin = DiracAdmin()
exitCode = 0
errorList = []
extendedInfo = False

for unprocSw in Script.getUnprocessedSwitches():
  if unprocSw[0] in ( 'e', 'extended' ):
    extendedInfo = True

if not extendedInfo:
  result = diracAdmin.csListHosts()
  for host in result[ 'Value' ]:
    print " %s" % host
else:
  result = diracAdmin.csDescribeHosts()
  print diracAdmin.pPrint.pformat( result[ 'Value' ] )

for error in errorList:
  print "ERROR %s: %s" % error

DIRAC.exit(exitCode)