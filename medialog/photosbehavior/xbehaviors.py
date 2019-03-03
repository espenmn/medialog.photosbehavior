from zope import schema
from zope.interface import Interface
from zope.interface import alsoProvides
from z3c.form import interfaces
from plone.namedfile.field import NamedImage
from collective.z3cform.datagridfield import DataGridFieldFactory 
from collective.z3cform.datagridfield import DictRow
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.autoform.directives import widget
from plone.namedfile.field import NamedImage
from collective.z3cform.datagridfield import DataGridFieldFactory 
from collective.z3cform.datagridfield import DictRow
from plone.autoform.interfaces import IFormFieldProvider

from z3c.form.browser.multi import MultiWidget

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('medialog.photosbehavior')


class IImagePair(model.Schema):

    image = NamedImage(
        title=_(u"image", default=u"image"),
        required = False,
        description=_(u"help_image",
            default=u"Choose an image")
    )
    
    title = schema.TextLine(
        title=_(u'image_title', 'Image Title'),
        required=False
    )
    
    description = schema.TextLine(
        title=_(u'image_description', 'Image Description'),
        required=False
    )
    

class IPhotosBehavior(model.Schema):
    """Adds settings to medialog.controlpanel
        """
    model.fieldset(
        'photos',
        label=_(u'Photos'),
            fields=[
                    'image_pairs',
            ],
    )
    
    widget(image_pairs=DataGridFieldFactory)
    image_pairs = schema.List(
        title = _(u"image_pairs", 
            default=u"Photos"),
        value_type=DictRow(schema=IImagePair),
    )

alsoProvides(IPhotosBehavior, IFormFieldProvider)
