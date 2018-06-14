from Acquisition import aq_inner
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implements, Interface
#from Products.CMFCore.utils import getToolByName

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter

#from AccessControl import getSecurityManager


class PhotosViewlet(ViewletBase):
    render = ViewPageTemplateFile('photosviewlet.pt')


    def getphotos(self):
        return self.context.image_pairs

    def javascript(self):
        """get the settings into the javascript"""

        return """<script>$(function () {
            $("#slider").responsiveSlides({
            });
            });
        </script>"""
