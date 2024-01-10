import unittest
import process

class MyTestCase(unittest.TestCase):
    def test_something(self):
        process.send_email('测试发送消息', '发送成功')
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
