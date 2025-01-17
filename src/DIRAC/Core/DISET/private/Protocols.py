from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__RCSID__ = "$Id$"

from DIRAC.Core.DISET.private.Transports import PlainTransport, SSLTransport

gProtocolDict = {
    "dip": {
        "transport": PlainTransport.PlainTransport,
        "sanity": PlainTransport.checkSanity,
        "delegation": PlainTransport.delegate,
    },
    "dips": {
        "transport": SSLTransport.SSLTransport,
        "sanity": SSLTransport.checkSanity,
        "delegation": SSLTransport.delegate,
    },
}

gDefaultProtocol = "dips"
