import unittest2
from Combination import Combination
import os
from sparktestingbase.testcase import SparkTestingBaseTestCase
import shutil


class CombinationTest(SparkTestingBaseTestCase):
    # Come back to - Could not call own setUp method that needs to be called before every class
    # def setUp(self):
    #     super(SparkTestingBaseTestCase, self).setUp()
    #     sc = super(SparkTestingBaseTestCase).sc


    def testRun(self):
        baseFolder = "/target"
        self.combination = Combination(self.sc)
        inputFolder = os.path.dirname(__file__) + "/resources/persons.csv"
        outputFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + baseFolder + "/run"
        self.deleteTestFolder(outputFolder)
        self.combination.run(inputFolder, outputFolder)


    def createTestFolder(self, directory):
        if os.path.exists(directory):
            shutil.rmtree(directory)

        os.makedirs(directory)

    def deleteTestFolder(self, directory):
        if os.path.exists(directory):
            shutil.rmtree(directory)


