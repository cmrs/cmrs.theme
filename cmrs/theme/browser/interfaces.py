from plone.theme.interfaces import IDefaultPloneLayer

class ICmrsSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "cmrs" theme, this interface must be its layer
       (in theme/viewlets/configure.zcml).
    """
