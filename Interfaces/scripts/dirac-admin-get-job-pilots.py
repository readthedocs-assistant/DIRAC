#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :   dirac-admin-get-job-pilots
# Author : Stuart Paterson
########################################################################
__RCSID__   = "$Id$"
__VERSION__ = "$Revision: 1.1 $"
from DIRACEnvironment import DIRAC
from DIRAC.Core.Base import Script
from DIRAC.Interfaces.API.DiracAdmin                         import DiracAdmin

Script.parseCommandLine( ignoreErrors = True )
args = Script.getPositionalArgs()

def usage():
  print 'Usage: %s <JobID> [<JobID>]' %(Script.scriptName)
  DIRAC.exit(2)

if len(args) < 1:
  usage()

diracAdmin = DiracAdmin()
exitCode = 0
errorList = []

for job in args:

  try:
    job = int(job)
  except Exception,x:
    errorList.append( ('Expected integer for jobID', job) )
    exitCode = 2
    continue

  result = diracAdmin.getJobPilots(job)
  if not result['OK']:
    errorList.append( (job, result['Message']) )
    exitCode = 2

for error in errorList:
  print "ERROR %s: %s" % error

DIRAC.exit(exitCode)
