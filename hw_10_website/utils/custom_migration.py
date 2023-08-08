import os
import django
import configparser

from datetime import datetime
from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_10_website.settings")
django.setup()

from quotes.models import Quote, Tag, Author  # noqa

# ----------- Connection to DB ------------
current_folder = os.path.dirname(os.path.abspath(__file__))
parent_folder = os.path.dirname(current_folder)

init_file = os.path.join(parent_folder, "config.ini")


config = configparser.ConfigParser()
config.read(init_file)

mongo_user = config.get('DB', 'mongo_user')
mongodb_pass = config.get('DB', 'mongo_pass')


client = MongoClient(f"mongodb+srv://{mongo_user}:{mongodb_pass}@stepanovdb.codnmzv.mongodb.net/")
db = client.hw09_scraping
# ------------------------------------------------


authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author["fullname"],
        born_date=datetime.strptime(author["born_date"], "%B %d, %Y"),
        born_location=author["born_location"],
        description=author["description"],
        photo=author["photo_url"]
    )


quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote["quote"])))

    if not exist_quote:
        author = db.authors.find_one({"_id": quote["author"]})
        author_in_sql = Author.objects.get(fullname=author["fullname"])

        q = Quote.objects.create(quote=quote["quote"], author=author_in_sql)

        for tag in tags:
            q.tags.add(tag)
