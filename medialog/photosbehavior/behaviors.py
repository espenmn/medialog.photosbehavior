# -*- coding: utf-8 -*-
from plone.app.contenttypes import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
 
from collective.z3cform.datagridfield import DataGridFieldFactory 
from collective.z3cform.datagridfield import DictRow

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('medialog.photosbehavior')

#https://github.com/collective/collective.z3cform.datagridfield/issues/31

try:
    from zope.globalrequest import getRequest
    getRequest  # pyflakes
except ImportError:
    # Fake it
    getRequest = object


@provider(IFormFieldProvider)
class IPhoto(model.Schema):

    image = namedfile.NamedBlobImage(
        title=_(u"Photo"),
        description=u"",
        required=False,
    )

    image_title = schema.TextLine(
        title=_(u"Photo Title"),
        description=u"",
        required=False,
    )

    image_description = schema.TextLine(
        title=_(u"Photo Description"),
        description=u"",
        required=False,
    )

@provider(IFormFieldProvider)
class IPhotosBehavior(model.Schema):
    """Adds settings to medialog.controlpanel
    
    def image():
    
        """
    model.fieldset(
        'photos',
        label=_(u'Photos'),
            fields=[
                    'image_pairs',
            ],
    )
    
    image_pairs = schema.Tuple(
        title = _(u"image_pairs", 
            default=u"Photos"),
        value_type= DictRow(schema=IPhoto)
    )
    

@implementer(IPhotosBehavior)
@adapter(IDexterityContent)
class PhotosBehavior(object):

    def __init__(self, context):
        self.context = context

    #code from contentreewidget utils
    def closest_content(context=None):
        """Try to find a usable context, with increasing agression"""
        # Normally, we should be given a useful context (e.g the page)
        c = context
        c = _valid_context(c)
        if c is not None:
            return c
        # Subforms (e.g. DataGridField) may not have a context set, find out
        # what page is being published
        c = getattr(getRequest(), 'PUBLISHED', None)
        c = _valid_context(c)
        if c is not None:
            return c
        # During widget traversal nothing is being published yet, use getSite()
        c = getSite()
        c = _valid_context(c)
        if c is not None:
            return c
        raise ValueError('Cannot find suitable context to bind to source')
        
    
    def context(self):
        context = self.request.PARENTS[0]