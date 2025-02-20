""" Download the required model after installation. """

import logging
import nltk

log = logging.getLogger(__name__)

def main():
    print("Downloading NLTK stopwords model")
    nltk.download('stopwords')

if __name__ == "__main__":
    main()