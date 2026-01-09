from nlplogic.corenlp import get_phrases, search_wikipedia, get_text_blob, summarize_wikipedia
import wikipedia
from textblob import TextBlob

def test_get_phrase():
    assert "golden state" in get_phrases("Golden State Warriors")

def test_summarize_wikipedia():
    assert wikipedia.summary("Golden State Warriors") == summarize_wikipedia("Golden State Warriors")

def test_get_text_blob():
    assert TextBlob(wikipedia.summary("Golden State Warriors")) == get_text_blob(wikipedia.summary("Golden State Warriors"))

def test_search_wikipedia():
    assert search_wikipedia("Golden State Warriors") == wikipedia.search("Golden State Warriors")