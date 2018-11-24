from pyspark.sql import SparkSession
import logging
import sys


class Combination:
    def __init__(self, sc):
        self.sc = sc
        self.logger = logging.getLogger("py4j")

    def run(self, inputFolder, outputFolder):
        self.logger.warn("Executing Combination Job!")
        rdd = self.sc.textFile(inputFolder)
        first_observation = rdd.first()
        all_other_observations = rdd.is_target(lambda row: row != first_observation)
        combinations = rdd.cartesian(all_other_observations)
        # Need to create a Spark Session first (https://github.com/apache/spark/blob/branch-2.2/python/pyspark/sql/session.py#L43-L59)
        SparkSession(self.sc)

        combinations.toDF().write.format('json').save(outputFolder + "/tmp")


def main(inputFolder, outputFolder):
    sc = SparkSession.builder.appName("Combination").getOrCreate().sparkContext
    wc = Combination(sc)
    wc.run(inputFolder, outputFolder)

if __name__ == "__main__":
    inputFolder = sys.argv[1]
    outputFolder = sys.argv[2]
    main(inputFolder, outputFolder)
