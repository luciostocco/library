import json
import os
import pytest
import unittest

# In order to test we need to change Working directory to the app level
# bootstrap.app needs to read the config ini file
wd = os.getcwd()
os.chdir(f'{wd}/../')

from bootstrap.app import *

# set the application to testing mode
app.testing = True
app.config['TESTING'] = True


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


class TestApi:

    def test_post_book_request(self, client):
        # send data as POST form to endpoint
        payload = {"email":  "lucio@mail.com", "title": "Book 1"}

        response = client.post('/request', data=payload)
        assert response.status_code == 200

        # check result from server with expected data
        #assert response.data == json.dumps(payload)

    def test_get_book_by_id(self, client):

        response = client.get('/')
        assert response.status_code == 200

    def test_list_books(self, client):
        # It need to be implemented
        pass

    def test_delete_book(self, client):
        # It need to be implemented
        pass


if __name__ == "__main__":
    unittest.main()