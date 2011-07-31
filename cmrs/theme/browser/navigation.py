from plone.app.portlets.portlets.navigation import Renderer as base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Renderer(base):
    _template = ViewPageTemplateFile('templates/navigation.pt')
    recurse = ViewPageTemplateFile('templates/navigation_recurse.pt')
