## django requirement
We need to use django < 3.0 to work with Solr. Otherwise,  
we'll hit issue with "import six", which django 3.x already  
dropped support. So django 2.2 is used in Pipfile for the 
virtual environment.

## Patching django-haystack
I hit the following issue with django-haystack when doing the search. 
AttributeError: 'list' object has no attribute 'split'

Below is a link online that seems to be related.
https://github.com/django-haystack/django-haystack/issues/1200

Based on the solution provided by rifuso on Oct 23 2019 in the 
link, I made the following change and it works. 
app_label, model_name = raw_result[DJANGO_CT].split('.')
=> 
app_label, model_name = raw_result[DJANGO_CT][0].split('.')


## Install solr on MacOS
brew update
brew install solr

## Start Solr and create a core of blog
solr start
solr create_core -c blog
NOTE: This will use a default schema for blog core.

## Update index
python manage.py update_index

## Rebuild index
pythong manage.py rebuild_index

## Start server
python manage.py runserver 

After the above steps, we can do search at url address
at localhost:8000/blog/blog-search

