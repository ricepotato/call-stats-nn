# -*- coding: utf-8 -*-

import logging

log = logging.getLogger('csn.nn')
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def main():
    log.info('nn main')

if __name__ == "__main__":
    main()