from haystack import indexes
from .models import Blog


class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True,
        use_template=True,
        template_name="search/blog_text.txt"
    )
    title = indexes.CharField(model_attr='title')
    #description = indexes.CharField(model_attr='description')
    short_description = indexes.CharField(model_attr='short_description')
    # add autocomplete
    description_auto = indexes.EdgeNgramField(model_attr='description')

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
