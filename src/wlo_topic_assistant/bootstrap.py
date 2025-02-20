""" Download the required model after installation. """

import os
import pickle

import nltk

from wlo_topic_assistant._version import __version__
from wlo_topic_assistant.topic_assistant import TopicAssistant
from wlo_topic_assistant.topic_assistant2 import TopicAssistant2


def main():
    print("Downloading NLTK stopwords model")
    nltk.download('stopwords')

    print("Caching topic assistant models")
    path = "data"
    os.makedirs(path, exist_ok=True)
    for cls in [TopicAssistant, TopicAssistant2]:
        with open(f"{path}/{cls.__name__}_{__version__}.pkl", "wb+") as f:
            pickle.dump(cls(), f)


if __name__ == "__main__":
    main()
