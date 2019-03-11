# -*- coding: utf-8 -*-
import os
import logging
import json

log = logging.getLogger('csn.nn')
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

data_path = os.path.dirname(__file__)

API_INDEX_FILENAME = 'apiname_index.csv'

label_obj = {
    'doc_downloader':0,
    'gandcrab':1,
    'java_adwind':2,
    'js_downloader':3,
    'js_gandcrab':4,
    'ransom_gen':5
}

target_obj = {
    'doc_downloader':'doc_downloader_stats.json',
    'gandcrab':'gandcrab_stats.json',
    'java_adwind':'java_adwind_stats.json',
    'js_downloader':'js_downloader_stats.json',
    'js_gandcrab':'js_gandcrab_stats.json',
    'ransom_gen':'ransom_gen_stats.json'
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
        #api_index_dict[idx] = apiname
        api_index_dict[apiname] = idx

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

def dump_data(virusname, obj):
    path = os.path.join(data_path, '{}_refine.json'.format(virusname))
    try:
        log.info('dump data virusname=%s', virusname)
        with open(path, 'w') as f:
            f.write(json.dumps(obj, indent=4))
    except Exception as e:
        log.error('dump_data error. %s', e)
        return None
    
    return path

def dump_data_csv(virusname, line):
    dump_path = os.path.join(data_path, '{}_data.csv'.format(virusname))
    try:
        with open(dump_path, 'a') as f:
            f.write(line)
        return True
    except Exception as e:
        log.error('dump_data error. %s', e)
        return False

def make_data(virusname, rf_filepath, ai_obj):
    try:
        with open(rf_filepath, 'r') as f:
            data = f.read()
    except Exception as e:
        log.error('make_data error. %s', e)
        return None


    res_dict = {}
    rf_obj = json.loads(data)
    for task_id, obj in rf_obj.items():
        for apiname, count in obj.items():
            try:
                res_dict[ai_obj[apiname]] = count
            except KeyError as e:
                log.debug('key %s is not in api index.', apiname)

        call_csv = []
        for idx in range(0, len(ai_obj)):
            call_csv.append(str(res_dict.get(idx, 0)))
        
        call_csv.append('\n')
        line = ",".join(call_csv)
        dump_data_csv(virusname, line)


def main():
    log.info('refine data')
    csv_file = os.path.join(data_path, API_INDEX_FILENAME)
    ai_obj = api_index(csv_file)
    if not ai_obj:
        log.error('api_index error')
        return 0

    #rf_path_list = []
    for virusname, json_filename in target_obj.items():
        json_path = os.path.join(data_path, json_filename)
        if not os.path.exists(json_path):
            log.error('path not exists %s', json_path)
            continue
        try:
            with open(json_path, 'r') as f:
                data = f.read()
        except Exception as e:
            log.error('open error filepath=%s e=%s', json_path, e)
            continue

        json_obj = json.loads(data)
        res_dict = refine(virusname, json_obj)
        refine_path = dump_data(virusname, res_dict)
        #rf_path_list.append(refine_path)
        make_data(virusname, refine_path, ai_obj)


if __name__ == "__main__":
    main()