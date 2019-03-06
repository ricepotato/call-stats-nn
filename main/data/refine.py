# -*- coding: utf-8 -*-
import os
import logging
import json

log = logging.getLogger('csn.nn')
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

data_path = os.path.dirname(__file__)

API_INDEX_FILENAME = 'apiname_index.csv'

target_obj = {
    'doc_downloader':'doc_downloader_stats.json',
    'gandcrab':'gandcrab_stats.json',
    'java_adwind':'java_adwind_stats.json',
    'js_downlaoder':'js_downloader_stats.json',
    'js_gandcrab':'js_gandcrab_stats.json',
    'ransom_gen_stats':'ransom_gen_stats.json'
}



def api_index(csv_filepath):
    
    if not os.path.exists(csv_filepath):
        log.error('api name index csv file not exist. %s', csv_filepath)
        return None

    try:
        with open(csv_filepath, 'r') as f:
            csv_data = f.read()
    except Exception as e:
        log.error('file open error %s', e)
        return None

    api_index_list = csv_data.split(',')
    log.debug('api_index_list length=%d', len(api_index_list))
    api_index_dict = {}
    for idx, apiname in enumerate(api_index_list):
        api_index_dict[idx] = apiname

    return api_index_dict
        

def refine(virus_name, obj):
    apistats = obj[virus_name]
    
    res_dict = {}
    for task_id, process in apistats.items():
        stats_res = {}
        for pid, calls in process.items():
            for apiname, count in calls.items():
                stats_res[apiname] = stats_res.get(apiname, 0) + count
        res_dict[task_id] = stats_res

    return res_dict



def main():
    log.info('refine data')
    csv_file = os.path.join(data_path, API_INDEX_FILENAME)
    api_index = api_index(csv_file)
    if not api_index:
        log.error('api_index error')
        return 0

    for virusname, json_filename in target_obj:
        json_path = os.path.join(data_path, 'json_data', json_filename)
        if not os.path.exists(json_path):
            log.error('path not exists %s', json_path)
            continue

        with open(json_path, 'r') as f:
            json_obj = f.read(json_path)
            res_dict = refine(virusname, json_obj)


if __name__ == "__main__":
    main()