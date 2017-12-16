from __future__ import print_function, division, absolute_import
import sys
import os
import unittest
import doctest
import importlib
import glob


testRoot = os.path.dirname(os.path.abspath(__file__))
if testRoot not in sys.path:
    sys.path.append(testRoot)

testModules = glob.glob(os.path.join(testRoot, "test*.py"))
modulesWithDocTests = ["drawBot.misc", "testExport"]  # TODO: doctest discovery

loader = unittest.TestLoader()
suite = unittest.TestSuite()
for path in testModules:
    moduleName, ext = os.path.splitext(os.path.basename(path))
    suite.addTest(loader.loadTestsFromName(moduleName))

for moduleName in modulesWithDocTests:
    m = importlib.import_module(moduleName)
    suite.addTest(doctest.DocTestSuite(m))

unittest.TextTestRunner(verbosity=1).run(suite)
# TODO: call sys.exit() with result code if we're not in DB
