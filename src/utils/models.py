from datetime import datetime
from flask_mongoengine import MongoEngine
from mongoengine.fields import DateTimeField
from mongoengine.document import Document
dc = MongoEngine()


class BaseDocument(Document):
    meta = {
        'abstract': True
    }

    created_on = DateTimeField(default=datetime.now())
    updated_on = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_on:
            self.created_on = datetime.now()
        self.updated_on = datetime.now()
        return super(BaseDocument, self).save(*args, **kwargs)


class ReprMixin(object):
    """Provides a string representible form for objects."""

    __repr_fields__ = ['id', 'name']

    def __repr__(self):
        fields =  {f:getattr(self, f, '<BLANK>') for f in self.__repr_fields__}
        pattern = ['{0}={{{0}}}'.format(f) for f in self.__repr_fields__]
        pattern = ' '.join(pattern)
        pattern = pattern.format(**fields)
        return '<{} {}>'.format(self.__class__.__name__, pattern)
