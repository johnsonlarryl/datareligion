from pyspark.sql import SparkSession
import logging


class Combination:
    def __init__(self, sc):
        self.sc = sc
        self.logger = logging.getLogger("py4j")

    def run(self):
        self.logger.warn("We are running our job!")
        numbers = range(4)
        numbers = numbers[1:4]
        rdd = self.sc.parallelize(numbers)
        first_observation = rdd.first()
        all_other_observations = rdd.filter(lambda row: row != first_observation)
        combinations = rdd.cartesian(all_other_observations).collect()
        combinations.foreach(print)


def main():
    sc = SparkSession.builder.appName("Combination").getOrCreate().sparkContext
    wc = Combination(sc)
    wc.run()

if __name__ == "__main__":
    main()
