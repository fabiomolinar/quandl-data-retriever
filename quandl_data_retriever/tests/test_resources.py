import unittest

from quandl_data_retriever import resources

class TestForgeOne(unittest.TestCase):    
    def test_get_url(self):
        strings = [
            "https://forex.1forge.com/1.0.3/quotes?pairs=EURUSD,GBPJPY,AUDUSD&api_key=mysecretapikey",
            "https://forex.1forge.com/1.0.3/quotes?pairs=EURUSD,GBPJPY,AUDUSD",
            "/1.0.3/quotes?pairs=EURUSD,GBPJPY,AUDUSD&api_key=mysecretapikey",
            "/quotes?pairs=EURUSD,GBPJPY,AUDUSD&api_key=mysecretapikey",
            "quotes?pairs=EURUSD,GBPJPY,AUDUSD&api_key=mysecretapikey",
            "quotes?pairs=EURUSD,GBPJPY,AUDUSD",
            "/quotes?pairs=EURUSD,GBPJPY,AUDUSD",
            "quotes?pairs=EURUSD,GBPJPY,AUDUSD&"
        ]
        result = "https://forex.1forge.com/1.0.3/quotes?pairs=EURUSD,GBPJPY,AUDUSD&api_key=mysecretapikey"
        api_key = "mysecretapikey"
        forge_one = resources.ForgeOne(api_key)
        for s in strings:
            with self.subTest(msg=s):
                self.assertEqual(forge_one.get_url(s), result)

class TestQuandl(unittest.TestCase):    
    def test_get_url(self):
        strings = [
            "https://www.quandl.com/api/v3/datasets/XBRU/VAN?column_index=1&api_key=mysecretapikey",
            "https://www.quandl.com/api/v3/datasets/XBRU/VAN?column_index=1",
            "https://www.quandl.com/api/v3/datasets/XBRU/VAN?column_index=1&",
            "/api/v3/datasets/XBRU/VAN?column_index=1",
            "datasets/XBRU/VAN?column_index=1",
            "datasets/XBRU/VAN?column_index=1&api_key=mysecretapikey"
        ]
        result = "https://www.quandl.com/api/v3/datasets/XBRU/VAN?column_index=1&api_key=mysecretapikey"
        api_key = "mysecretapikey"
        quandl = resources.Quandl(api_key)
        for s in strings:
            with self.subTest(msg=s):
                self.assertEqual(quandl.get_url(s), result)

if __name__ == "__main__":
    unittest.main()