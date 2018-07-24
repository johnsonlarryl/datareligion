from pyspark.sql import SparkSession
import logging


class WordCount:

    def __init__(self, sc):
        self.sc = sc
        self.logger = logging.getLogger("py4j")

    def run(self):
        self.logger.warn("We are running our job!")


def main():
    sc = SparkSession.builder.appName("WordCount").getOrCreate()
    wc = WordCount(sc)
    wc.run()

if __name__ == "__main__":
    main()
