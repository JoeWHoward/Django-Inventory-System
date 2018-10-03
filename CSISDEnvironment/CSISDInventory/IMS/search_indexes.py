import datetime
from haystack import indexes
from IMS.models import Campus, Teacher, Device

class CampusIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    content_auto = indexes.EdgeNgramField(model_attr='name')
    
    def get_model(self):
        return Campus
    def index_queryset(self, using=None):
        # Used when the entire index for model is updated
        return self.get_model().objects.all()
    
class TeacherIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    content_auto = indexes.EdgeNgramField(model_attr='name')
    
    def get_model(self):
        return Teacher
    def index_queryset(self, using=None):
        # Used when the entire index for model is updated
        return self.get_model().objects.all()
    
class DeviceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    content_auto = indexes.EdgeNgramField(model_attr='name')
    
    def get_model(self):
        return Device
    def index_queryset(self, using=None):
        # Used when the entire index for model is updated
        return self.get_model().objects.all()