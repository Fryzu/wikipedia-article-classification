import os

BASE_PATH = os.path.dirname(os.path.dirname(
    os.path.abspath(os.path.dirname(__file__))))

DATA_DIR = os.path.join(BASE_PATH, "data")

CATEGORIES_PATH = os.path.join(DATA_DIR, "wikipedia_topics_nowikidata.csv")
