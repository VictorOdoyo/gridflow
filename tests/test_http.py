import unittest
import numpy as np

import threading,json
from http.server import ThreadingHTTPServer
from urllib.request import urlopen,Request
from urllib.error import HTTPError
from gridflow.server import Handler
class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),Handler);cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start();cls.url=f'http://127.0.0.1:{cls.server.server_port}'
    @classmethod
    def tearDownClass(cls):cls.server.shutdown();cls.server.server_close();cls.thread.join()
    def test_assets_and_examples(self):
        for path in ['/','/app.js','/style.css','/api/examples']:
            with urlopen(self.url+path) as response:self.assertEqual(response.status,200);self.assertGreater(len(response.read()),10)
    def test_bad_json(self):
        with self.assertRaises(HTTPError) as error:urlopen(Request(self.url+'/api/study',data=b'{bad',headers={'Content-Type':'application/json'}))
        self.assertEqual(error.exception.code,400)
    def test_cross_origin(self):
        with self.assertRaises(HTTPError) as error:urlopen(Request(self.url+'/api/study',data=b'{}',headers={'Content-Type':'application/json','Origin':'https://example.com'}))
        self.assertEqual(error.exception.code,403)
    def test_no_file_traversal(self):
        with self.assertRaises(HTTPError):urlopen(self.url+'/../pyproject.toml')
