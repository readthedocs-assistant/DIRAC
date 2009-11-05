#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :   dirac-admin-add-user
# Author : Adrian Casajus
########################################################################
__RCSID__   = "$Id$"
__VERSION__ = "$Revision: 1.1 $"
from DIRACEnvironment import DIRAC
from DIRAC.Core.Base import Script

Script.registerSwitch( "p:", "property=", "Add property to the user <name>=<value>" )

from DIRAC.Interfaces.API.DiracAdmin                         import DiracAdmin

args = Script.getPositionalArgs()

def usage():
  print 'Usage: %s [<options>] <username> <DN> <groups>+' %(Script.scriptName)
  DIRAC.exit(2)


diracAdmin = DiracAdmin()
exitCode = 0
errorList = []

if len(args) < 3:
  usage()

userProps = {}
for unprocSw in Script.getUnprocessedSwitches():
  if unprocSw[0] in ( "p", "property" ):
    prop = unprocSw[1]
    pl = prop.split( "=" )
    if len( pl ) < 2:
      errorList.append( ( "in arguments", "Property %s has to include a '=' to separate name from value" % prop ) )
      exitCode = 255
    else:
      pName = pl[0]
      pValue = "=".join( pl[1:] )
      print "Setting property %s to %s" % ( pName, pValue )
      userProps[ pName ] = pValue

userProps[ 'DN' ] = args[1]
userProps[ 'groups' ] = args[2:]

if not diracAdmin.csRegisterUser( args[0], userProps ):
  errorList.append( ( "add user", "Cannot register user %s" % args[0] ) )
  exitCode = 255
else:
  result = diracAdmin.csCommitChanges()
  if not result[ 'OK' ]:
    errorList.append( ( "commit", result[ 'Message' ] ) )
    exitCode = 255

for error in errorList:
  print "ERROR %s: %s" % error

DIRAC.exit(exitCode)