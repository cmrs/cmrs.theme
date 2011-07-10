import unittest2 as unittest

from zope.component import getSiteManager

from plone.app.testing import PLONE_INTEGRATION_TESTING
from plone.app.testing import ploneSite
from plone.app.testing import applyProfile
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName

from base import CMRS_THEME_INTEGRATION_TESTING

class TestInstallation(unittest.TestCase):
    """Ensure product is properly installed"""
    layer = CMRS_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testBrowserLayerRegistered(self):
        sm = getSiteManager(self.portal)
        layers = [o.__name__ for o in registered_layers()]
        print layers
        assert 'ICmrsTheme' in layers

    def testSkinLayer(self):
        portal_skins = getattr(self.portal, 'portal_skins')
        assert 'CMRS' in portal_skins.getSkinSelections()

    def testCurrentSkinLayer(self):
        current_skin = self.portal.getCurrentSkinName()
        assert 'CMRS' == current_skin

    def testSkinLayersInstalled(self):
        """Test skin layer is installed, and keble layout folder is also installed"""
        assert 'cmrs_theme' in self.portal.portal_skins.objectIds()
        assert 'portal_logo.gif' in self.portal.portal_skins.cmrs_theme.objectIds()
        assert 'keble_default' in self.portal.portal_skins.objectIds()
        assert 'kc_logo.gif' in self.portal.portal_skins.keble_default.objectIds()

class TestReinstall(unittest.TestCase):
    """Ensure product can be reinstalled safely"""
    layer = CMRS_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testReinstall(self):
        portal_setup = getToolByName(self.portal, 'portal_setup')
        portal_setup.runAllImportStepsFromProfile('profile-cmrs.theme:default')
