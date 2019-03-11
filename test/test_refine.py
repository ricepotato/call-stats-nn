# -*- coding: utf-8 -*-

import os
import sys
import unittest
import logging
import json

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                        '..', 'main', 'data'))
tmp_path = os.path.join(os.path.dirname(__file__), 'tmp')

sys.path.insert(0, base_path)

from refine import refine, api_index

log = logging.getLogger('csn.test')
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

try:
    os.mkdir(tmp_path)
except Exception as e:
    log.warning('mkdir tmp path=%s, %s',tmp_path, e)

test_obj = {
    "java_adwind": {
        "2867201": {
            "3562": {
                "LdrUnloadDll": 1, 
                "DeviceIoControl": 20, 
                "NtTerminateProcess": 3, 
                "NtQueryInformationFile": 1880, 
                "NtQueryValueKey": 5
            }, 
            "3683": {
                "FindFirstFileExW": 3, 
                "SetFileInformationByHandle": 1, 
                "DeviceIoControl": 1, 
                "NtQueryInformationFile":3
            }            
            },
        "2867200": {
            "3560": {
                "LdrUnloadDll": 1, 
                "DeviceIoControl": 20, 
            }, 
            "3688": {
                "LdrUnloadDll": 1, 
                "LdrGetDllHandle": 2, 
            }
        }
    }
}

class TestRefine(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_refine(self):
        res_obj = refine('java_adwind', test_obj)
        # api call 수가 모든 pid 의 call 수를 모두 합친것과 같아야 한다.
        self.assertEqual(res_obj['2867201']['LdrUnloadDll'], 1)
        self.assertEqual(res_obj['2867201']['DeviceIoControl'], 21)
        self.assertEqual(res_obj['2867201']['NtQueryInformationFile'], 1883)
        self.assertEqual(res_obj['2867201']['NtQueryValueKey'], 5)

        self.assertEqual(res_obj['2867200']['LdrUnloadDll'], 2)
        self.assertEqual(res_obj['2867200']['LdrGetDllHandle'], 2)
        self.assertEqual(res_obj['2867200']['DeviceIoControl'], 20)

        #log.info(res_obj)

    def test_api_index(self):
        test_csv_path = os.path.join(os.path.dirname(__file__), 'test_csv.csv')
        with open(test_csv_path, 'w') as f:
            f.write('apiname1,apiname2,apiname3')

        res = api_index(test_csv_path)

        # csv 파싱 하여 결과가 3이어야 한다.
        self.assertEqual(len(res), 3)
        # index 에 맞는 문자열이 출력되어야 한다.
        self.assertEqual(res['apiname1'], 0)
        self.assertEqual(res['apiname2'], 1)
        self.assertEqual(res['apiname3'], 2)

    def test_data_check(self):
        index_filepath = os.path.join(base_path, 'apiname_index.csv')
        res = api_index(index_filepath)
        self.assertEqual(res['AssignProcessToJobObject'], 0)
        self.assertEqual(res['CIFrameElement_CreateElement'], 4)


if __name__ == "__main__":
    unittest.main()