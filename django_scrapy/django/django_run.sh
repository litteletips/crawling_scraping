# 
docker run --rm \
--mount type=bind,src=/Users/yaroten/Library/Mobile\ Documents/com~apple~CloudDocs/git/crawling_scraping/django_scrapy/django,dst=/opt/apps \
django2.2 \
django-admin startproject django_project .