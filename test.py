#!/usr/bin/env python
import unittest
import app
import os

from dotenv import load_dotenv
load_dotenv()


class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, os.getenv("BACKEND_AUTH_USR"))

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, s.getenv("BACKEND_AUTH_PSW"))

    def test_hello_name(self):
        name = 'Simon'
        rv = self.app.get(f'/hello/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"{name}", 'utf-8'), rv.data)

if __name__ == '__main__':
    unittest.main()