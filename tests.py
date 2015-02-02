import http.client
import json
import unittest

from couchdb import Couch


TEST_DB_NAME = 'test_db_name'
TEST_DOC_ID = 'test_doc'


class CouchTests(unittest.TestCase):
    def setUp(self):
        self.couch = Couch()

    def test_01_connect(self):
        c = self.couch.connect()
        c.close()
        self.assertIsInstance(
            c, http.client.HTTPConnection)

    def test_02_create_db(self):
        self.assertTrue('ok' in self.couch.create_db(TEST_DB_NAME))

    def test_03_create_db_again(self):
        self.assertTrue('error' in self.couch.create_db(TEST_DB_NAME))

    def test_04_add_doc(self):
        doc = self.couch.couch_index()
        self.assertTrue(
            'ok' in self.couch.save_doc(TEST_DB_NAME, doc, TEST_DOC_ID))

    def test_05_add_doc_again(self):
        doc = self.couch.couch_index()
        self.assertTrue(
            'error' in self.couch.save_doc(TEST_DB_NAME, doc, TEST_DOC_ID))

    def test_06_get_rev(self):
        doc = self.couch.open_doc(TEST_DB_NAME, TEST_DOC_ID)
        self.rev = json.loads(doc)['_rev']

    def test_07_delete_doc(self):
        global rev
        rev = self.couch.get_doc_rev(TEST_DB_NAME, TEST_DOC_ID)
        self.assertTrue(
            'ok' in self.couch.delete_doc(TEST_DB_NAME, TEST_DOC_ID, rev))

    def test_08_delete_doc_again(self):
        global rev
        self.assertTrue(
            'error' in self.couch.delete_doc(TEST_DB_NAME, TEST_DOC_ID, rev))

    def test_09_delete_db(self):
        self.assertTrue('ok' in self.couch.delete_db(TEST_DB_NAME))

    def test_10_delete_db_again(self):
        self.assertTrue('error' in self.couch.delete_db(TEST_DB_NAME))


if __name__ == '__main__':
    unittest.main()
