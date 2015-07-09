from zope import schema
from zope.interface import Interface
from z3c.form import interfaces

from collective.z3cform.datagridfield import DataGridFieldFactory 
from collective.z3cform.datagridfield import DictRow

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('medialog.photosbehavior')


class IImagePair(form.Schema):
      
    image_scale = schema.Choice(
        title=_(u"imagesize", default=u"image Size"),
        vocabulary = 'medialog.photosbehavior.ImageSizeVocabulary',
        required = True,
        description=_(u"help_imagesize",
            default=u"Set  size for image")
    )
    
    title = schema.TextLine(
        title=_(u'image_title', 'Image Title'),
        required=False
    )
    
    description = schema.TextLine(
        title=_(u'image_description', 'Image Description'),
        required=False
    )
    


class IPhotosBehaviorSettings(form.Schema):
    """Adds settings to medialog.controlpanel
        """
    form.fieldset(
        'photos',
        label=_(u'Photos'),
            fields=[
                    'image_pairs',
            ],
    )
    
    multiField = schema.List(
		value_type=schema.Int(default=42))
	multiWidget.field = multiField
    
    form.widget(content_pairs=DataGridFieldFactory)
    image_pairs = schema.List(
        title = _(u"image_pairs", 
            default=u"Photos"),
        value_type=DictRow(schema=IImagePair),
    )
    
                
