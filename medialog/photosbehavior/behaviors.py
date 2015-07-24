from zope import schema
from zope.interface import Interface
from zope.interface import alsoProvides
from z3c.form import interfaces
from plone.directives import form
from plone.namedfile import field as namedfile

#do I need this ?
from plone.supermodel import model
from plone.dexterity.interfaces import IDexterityContent

from collective.z3cform.datagridfield import DataGridFieldFactory 
from collective.z3cform.datagridfield import DictRow
from plone.autoform.interfaces import IFormFieldProvider

#from z3c.form.browser.multi import MultiWidget

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('medialog.photosbehavior')

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

alsoProvides(IPhoto, IFormFieldProvider)

 
class IPhotosBehavior(form.Schema):
    """Adds settings to medialog.controlpanel
        """
    form.fieldset(
        'photos',
        label=_(u'Photos'),
            fields=[
                    'image_pairs',
            ],
    )
    
    form.widget(image_pairs=DataGridFieldFactory)
    image_pairs = schema.List(
        title = _(u"image_pairs", 
            default=u"Photos"),
        value_type=DictRow(schema=IPhoto),
    )
    

alsoProvides(IPhotosBehavior, IFormFieldProvider)
