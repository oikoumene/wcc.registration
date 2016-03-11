from collective.grok import gs
from wcc.registration import MessageFactory as _

@gs.importstep(
    name=u'wcc.registration', 
    title=_('wcc.registration import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.registration.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
