import unittest

from src.api.processors.base_processor import BaseProcessor


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.processor = BaseProcessor();

    def test_something(self):
        self.assertEqual(True, False)
        message = self.processor.get_slack_message({})
        self.assertEqual(True,message['fields']['short'])


if __name__ == '__main__':
    unittest.main()
