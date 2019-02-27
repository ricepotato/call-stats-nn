# -*- coding: utf-8 -*-

import logging
#import tensorflow as tf

log = logging.getLogger('csn.model')
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

class Model(object):
    def __init__(self):
        pass

    def _build_net(self):
        pass

    def get_accuracy(self):
        pass

    def train(self):
        log.info('train')