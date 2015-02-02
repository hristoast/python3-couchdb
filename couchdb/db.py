import http.client
import json

from .common import *

__all__ = ['Couch']


class Couch:
    def __init__(self, host=DEFAULT_COUCH_HOST, options=None, port=DEFAULT_COUCH_PORT):
        self.host = host
        self.options = options
        self.port = port

    def connect(self):
        return http.client.HTTPConnection(self.host, self.port)  # No close()

    # db ops
    def create_db(self, db_name):
        r = self._put(''.join([SEP, db_name, SEP]), '')
        return r

    def delete_db(self, db_name):
        r = self._delete(''.join([SEP, db_name, SEP]))
        return r

    def list_dbs(self):
        return self._get(SEP + ALL_DBS)

    def info_db(self, db_name):
        r = self._get(''.join([SEP, db_name, SEP]))
        return r

    # doc ops
    def get_doc_key(self, db_name, doc_id, key):
        doc = self.open_doc(db_name, doc_id)
        return json.loads(doc)[key]

    def get_doc_rev(self, db_name, doc_id):
        doc = self.open_doc(db_name, doc_id)
        return json.loads(doc)['_rev']

    def list_docs(self, db_name):
        r = self._get(''.join([SEP, db_name, SEP, ALL_DOCS]))
        return r

    def open_doc(self, db_name, doc_id):
        r = self._get(''.join([SEP, db_name, SEP, doc_id]))
        return r

    def save_doc(self, db_name, body, doc_id=None):
        if doc_id:
            r = self._put(''.join([SEP, db_name, SEP, doc_id]), body)
        else:
            r = self._post(''.join([SEP, db_name, SEP]), body)
        return r

    def delete_doc(self, db_name, doc_id, rev_id):
        data = '{{"_rev":"{}"}}'.format(rev_id)
        r = self._put(''.join([SEP, db_name, SEP, doc_id]), data)
        return r

    # print versions of db ops
    def print_create_db(self, db_name):
        r = self._put(''.join([SEP, db_name, SEP]), '')
        _fancy_print(r)

    def print_delete_db(self, db_name):
        r = self._delete(''.join([SEP, db_name, SEP]))
        _fancy_print(r)

    def print_list_dbs(self):
        _fancy_print(self._get(SEP + ALL_DBS))

    def print_info_db(self, db_name):
        r = self._get(''.join([SEP, db_name, SEP]))
        _fancy_print(r)

    # print versions of doc ops
    def print_list_docs(self, db_name):
        r = self._get(''.join([SEP, db_name, SEP, ALL_DOCS]))
        _fancy_print(r)

    def print_open_doc(self, db_name, doc_id):
        r = self._get(''.join([SEP, db_name, SEP, doc_id]))
        _fancy_print(r)

    def print_save_doc(self, db_name, body, doc_id=None):
        if doc_id:
            r = self._put(''.join([SEP, db_name, SEP, doc_id]), body)
        else:
            r = self._post(''.join([SEP, db_name, SEP]), body)
        _fancy_print(r)

    def print_delete_doc(self, db_name, doc_id, rev_id):
        data = '{{"_rev":"{}"}}'.format(rev_id)
        r = self._put(''.join([SEP, db_name, SEP, doc_id]), data)
        _fancy_print(r)

    # etc
    def couch_index(self):
        r = self._get(SEP)
        return r

    def print_couch_index(self):
        r = self._get(SEP)
        _fancy_print(r)

    # http methods
    def _get(self, uri):
        c = self.connect()
        headers = {'Accept': 'application/json'}
        c.request('GET', uri, None, headers)
        response_str = c.getresponse().read().decode('utf-8')
        c.close()
        return response_str

    def _post(self, uri, body):
        c = self.connect()
        headers = {'Content-type': 'application/json'}
        c.request('POST', uri, body, headers)
        response_str = c.getresponse().read().decode('utf-8')
        c.close()
        return response_str

    def _put(self, uri, body):
        c = self.connect()
        if len(body) > 0:
            headers = {'Content-type': 'application/json'}
            c.request('PUT', uri, body, headers)
        else:
            c.request('PUT', uri, body)
        response_str = c.getresponse().read().decode('utf-8')
        c.close()
        return response_str

    def _delete(self, uri):
        c = self.connect()
        c.request('DELETE', uri)
        response_str = c.getresponse().read().decode('utf-8')
        c.close()
        return response_str


def _fancy_print(s):
    """Fancy printing for json. Accepts strings."""
    print(json.dumps(json.loads(s), indent=4, sort_keys=True))
