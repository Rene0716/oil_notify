import unittest
from unittest.mock import patch
import oil_notify

class TestMyModule(unittest.TestCase):
    def test_get_data(self):
        # print(f'url:{oil_notify.url}')
        data = oil_notify.get_data(oil_notify.url)
        self.assertTrue(len(data) > 0)

    @patch('oil_notify.requests.post')
    def test_postToLine(self, mock_post):
        token = oil_notify.token
        data = oil_notify.data
        
        # 創建模擬的 Response 對象
        mock_response=oil_notify.requests.Response()
        mock_response.status_code = 200
        mock_response._content = b'Success'  # _content 是模擬 HTTP response 的內容
        
        mock_post.return_value = mock_response

        resp = oil_notify.postToLine(token, data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.text, 'Success')

if __name__ == '__main__':
    unittest.main()
