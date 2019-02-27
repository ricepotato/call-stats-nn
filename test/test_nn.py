# -*- coding: utf-8 -*-

import os
import sys
import unittest
import logging

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                        '..', 'main'))

sys.path.insert(0, base_path)

from model import Model


log = logging.getLogger('csn.test')
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

class TestNn(unittest.TestCase):
    def setUp(self):
        self.model = Model()

    def tearDown(self):
        pass

    def test_nn(self):
        log.info('test_nn')
        self.model.train()

if __name__ == "__main__":
    unittest.main()