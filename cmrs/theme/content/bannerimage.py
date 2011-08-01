import transaction
from AccessControl import ClassSecurityInfo
from zope.interface import implements

from Products.Archetypes.atapi import registerType
from Products.ATContentTypes.content.base import ATCTContent
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName

from cmrs.theme.config import PROJECTNAME
from cmrs.theme.interfaces.bannerimage import IBannerImage

from schemata import BannerImageSchema

class BannerImage(ATCTContent):
    """An image for the banner"""

    security = ClassSecurityInfo()

    implements(IBannerImage)

    meta_type = 'BannerImage'
    _at_rename_after_creation = True

    schema = BannerImageSchema

registerType(BannerImage, PROJECTNAME)
