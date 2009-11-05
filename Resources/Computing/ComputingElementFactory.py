########################################################################
# $HeadURL$
# File :   ComputingElementFactory.py
# Author : Stuart Paterson
########################################################################

"""  The Computing Element Factory has one method that instantiates a given Computing Element
     from the CEUnique ID specified in the JobAgent configuration section.
"""
from DIRAC.Resources.Computing.ComputingElement          import ComputingElement, getCEConfigDict
from DIRAC                                               import S_OK, S_ERROR, gLogger, gConfig

__RCSID__ = "$Id$"

import sys,types

class ComputingElementFactory:

  #############################################################################
  def __init__(self,ceUniqueID):
    """ Standard constructor
    """
    self.log = gLogger
    self.ceUniqueID = ceUniqueID
    self.log = gLogger.getSubLogger( self.ceUniqueID )

  #############################################################################
  def getCE(self):
    """This method returns the CE instance corresponding to the supplied
       CEUniqueID.  If no corresponding CE is available, this is indicated.
    """
    self.ceType = self.ceUniqueID
    ceConfigDict = getCEConfigDict( self.ceUniqueID )
    self.log.info('CEConfigDict',ceConfigDict)
    if 'CEType' in ceConfigDict:
      self.ceType = ceConfigDict['CEType']
    subClassName = "%sComputingElement" % (self.ceType)

    try:
      ceSubClass = __import__('DIRAC.Resources.Computing.%s' % subClassName,globals(),locals(),[subClassName])
    except Exception, x:
      msg = 'ComputingElementFactory could not import DIRAC.Resources.Computing.%s' % ( subClassName )
      self.log.exception()
      self.log.warn( msg )
      return S_ERROR( msg )

    try:
      ceStr = 'ceSubClass.%s( "%s" )' % ( subClassName, self.ceUniqueID )
      computingElement = eval( ceStr )
    except Exception, x:
      msg = 'ComputingElementFactory could not instantiate %s()' %(subClassName)
      self.log.exception()
      self.log.warn( msg )
      return S_ERROR( msg )

    return S_OK( computingElement )

#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#
