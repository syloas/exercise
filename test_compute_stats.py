import unittest
from unittest.mock import mock_open, patch, Mock
import compute_stats_refactor


class TestStats(unittest.TestCase):

    def test_read_ints(self):
        with patch('compute_stats_refactor.open', mock_open(read_data="346\n921")):
            result = compute_stats_refactor.read_ints()
            self.assertEqual(result, [346, 921])

    def test_count(self):
        with patch('compute_stats_refactor.read_ints', Mock(return_value=[346, 921])):
            result = compute_stats_refactor.count()
            self.assertEqual(result, 2)

    def test_summation(self):
        with patch('compute_stats_refactor.read_ints', Mock(return_value=[346, 921])):
            result = compute_stats_refactor.summation()
            self.assertEqual(result, 1267)

    def test_average(self):
        with patch('compute_stats_refactor.read_ints', Mock(return_value=[346, 921, 966, 350])):
            result = compute_stats_refactor.average()
            self.assertEqual(result, 646)

    def test_minimum(self):
        with patch('compute_stats_refactor.read_ints', Mock(return_value=[346, 921, 966, 350])):
            result = compute_stats_refactor.minimum()
            self.assertEqual(result, 346)

    def test_maximum(self):
        with patch('compute_stats_refactor.read_ints', Mock(return_value=[346, 921, 966, 350])):
            result = compute_stats_refactor.maximum()
            self.assertEqual(result, 966)

