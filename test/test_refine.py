# -*- coding: utf-8 -*-

import os
import sys
import unittest
import logging

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                        '..', 'main', 'data'))

sys.path.insert(0, base_path)

from refine import refine


log = logging.getLogger('csn.test')
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

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
                "LdrUnloadDll": 1, 
                "LdrGetDllHandle": 2, 
                "NtOpenFile": 1, 
                "FindFirstFileExW": 3, 
                "SetFileInformationByHandle": 1, 
                "NtQueryValueKey": 1
            }            
            },
        "2867200": {
            "3560": {
                "LdrUnloadDll": 1, 
                "DeviceIoControl": 20, 
                "NtSetInformationFile": 519, 
                "GetSystemWindowsDirectoryW": 1, 
                "NtClose": 1646, 
                "NtCreateSection": 1, 
                "NtOpenKey": 3, 
                "LdrGetProcedureAddress": 2, 
                "LdrLoadDll": 1, 
                "NtTerminateProcess": 3, 
                "NtQueryInformationFile": 1880, 
                "NtQueryValueKey": 5
            }, 
            "3688": {
                "LdrUnloadDll": 1, 
                "LdrGetDllHandle": 2, 
                "NtOpenFile": 1, 
                "FindFirstFileExW": 3, 
                "SetFileInformationByHandle": 1, 
                "NtQueryValueKey": 1
            }
        }
    }
}

class TestRefine(unittest.TestCase):
    def setUp(self):
        self.model = Model()

    def tearDown(self):
        pass

    def test_refine(self):
        res_obj = refine(test_obj, 'java_adwind')

if __name__ == "__main__":
    unittest.main()