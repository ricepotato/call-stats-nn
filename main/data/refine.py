# -*- coding: utf-8 -*-
import os
import logging
import json

log = logging.getLogger('csn.nn')
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

data_path = os.path.dirname(__file__)

target_obj = {
    'doc_downloader':'doc_downloader_stats.json',
    'gandcrab':'gandcrab_stats.json',
    'java_adwind':'java_adwind_stats.json',
    'js_downlaoder':'js_downloader_stats.json'
    'js_gandcrab':'js_gandcrab_stats.json'
    'ransom_gen_stats':'ransom_gen_stats.json'
}

def refine(virus_name, obj):
    apistats = obj[virus_name]
    
    for task_id, process in apistats.items():
        stats_res = {}
        for pid, calls in process.items():
            for apiname, count in calls.items():
                stats_res[apiname] = stats_res.get(apiname, 0) + count


def main():
    log.info('refine data')

if __name__ == "__main__":
    main()