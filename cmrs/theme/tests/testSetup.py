import unittest2 as unittest

from zope.component import getSiteManager

from plone.app.testing import PLONE_INTEGRATION_TESTING
from plone.app.testing import ploneSite
from plone.app.testing import applyProfile
from plone.browserlayer.utils import registered_layers

from base import CMRS_THEME_INTEGRATION_TESTING

class TestInstallation(unittest.TestCase):
    """Ensure product is properly installed"""
    layer = CMRS_THEME_INTEGRATION_TESTING

    def setUp(self):                                
        self.portal = self.layer['portal'] 

    def testSkinLayer(self):
        portal_skins = getattr(self.portal, 'portal_skins')
        assert 'cmrs' in portal_skins.getSkinSelections()
