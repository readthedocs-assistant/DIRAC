# $HeadURL$
__RCSID__ = "$Id$"
""" This backend just print the log messages through the standar output
"""
from DIRAC.LoggingSystem.private.backends.BaseBackend import BaseBackend

class PrintBackend( BaseBackend ):

  def doMessage( self, messageObject ):
    print self.composeString( messageObject )

