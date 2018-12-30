import fastunit as unittest
import requests,time


class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def test_b_run(self):
        r = requests.get("http://www.baidu.com")
        print(2,r)
        assert(False)
        time.sleep(2)


if __name__ == '__main__':

    unittest.main()