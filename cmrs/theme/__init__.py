from zope.i18nmessageid import MessageFactory

# global imports not good, but no time
from Products.Archetypes import atapi
from Products.CMFCore import utils

from config import PROJECTNAME, ADD_PERMISSIONS

courseMessageFactory = MessageFactory('cmrs.theme')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    from content.bannerimage import BannerImage
    from content.sectionfolder import SectionFolder
    from content.sectionimage import SectionImage
    from content.sectionimagefolder import SectionImageFolder

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(PROJECTNAME),
        PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (PROJECTNAME, atype.portal_type),
            content_types=(atype, ),
            permission=ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
            ).initialize(context)
