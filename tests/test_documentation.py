from satella.coding.predicates import x
from satella.coding.sequences import choose

from tests.base import LoggedInTestCase


class TestCalculators(LoggedInTestCase):
    def test_view_project(self):
        resp = self.client.get('/v1/projects')
        self.assertEqual(resp.status_code, 200)
        choose(x['id'] == 1, resp.data)

        resp = self.client.get('/v1/projects/1/items')
        self.assertEqual(resp.status_code, 200)
        self.assertGreaterEqual(len(resp.data), 1)
