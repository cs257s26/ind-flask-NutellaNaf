from app import *
import unittest
import dotenv

class TestApp(unittest.TestCase):
    def test_home_route(self):
        #sets up a special test app
        self.app = app.test_client() 

        #test app returns TestResponse object
        response = self.app.get('/', follow_redirects=True) 
        
        #TestResponse has webpage in .data
        self.assertEqual(b'Please look at the README.md to learn what routes to go to!', response.data) 
 
    # Tests for Nafees' user story route (top 5 of a section)
    def test_user_story_route(self):
        self.app = app.test_client() 

        response = self.app.get('/training_hours', follow_redirects=True) 
        
        self.assertEqual(b'<p> 2820.0 in row 4 </p><p> 2160.0 in row 2 </p><p> 1928.0 in row 6 </p><p> 1709.0 in row 18 </p><p> 1361.0 in row 5 </p>', response.data)

    def test_user_story_route_non_numeric(self):
        self.app = app.test_client() 

        response = self.app.get('/Model name', follow_redirects=True) 
        
        self.assertEqual(b'This is not a valid page! Please review README.md for valid paths and usage.', response.data) 

    def test_user_story_route_invalid_col(self):
        self.app = app.test_client() 

        response = self.app.get('/nafees', follow_redirects=True) 
        
        self.assertEqual(b'This is not a valid page! Please review README.md for valid paths and usage.', response.data)

    # Tests for Nafees' top n columns route

    def test_top_n_in_column_route(self):
        self.app = app.test_client() 

        response = self.app.get('/2/training_hours', follow_redirects=True) 
        
        self.assertEqual(b'<p>2820.0 in row 4 </p><p>2160.0 in row 2 </p>', response.data)

    def test_top_n_in_column_route_invalid_n(self):
        self.app = app.test_client() 

        response = self.app.get('/90/training_hours', follow_redirects=True) 
        
        self.assertEqual(b'This is not a valid page! Please review README.md for valid paths and usage.', response.data)

    def test_top_n_in_column_route_non_numeric(self):
        self.app = app.test_client() 

        response = self.app.get('/2/Model name', follow_redirects=True) 
        
        self.assertEqual(b'This is not a valid page! Please review README.md for valid paths and usage.', response.data) 

    def test_top_n_column_route_invalid_col(self):
        self.app = app.test_client() 

        response = self.app.get('/2/nafees', follow_redirects=True) 
        
        self.assertEqual(b'This is not a valid page! Please review README.md for valid paths and usage.', response.data)

    # Tests for Nafees' fetch all rows in column route
    def test_fetch_all_col_route(self):
        self.app = app.test_client() 

        response = self.app.get('/all/training_hours', follow_redirects=True) 

        valid_string = b"<p> 355.2 in row 1 </p><p> 2160 in row 2 </p><p> 1200 in row 3 </p><p> 2820 in row 4 </p><p> 1361 in row 5 </p><p> 1928 in row 6 </p><p> Not disclosed in row 7 </p><p> Not disclosed in row 8 </p><p> Not disclosed in row 9 </p><p> Not disclosed in row 10 </p><p> Not disclosed in row 11 </p><p> 480 in row 12 </p><p> 74.4 in row 13 </p><p> 648 in row 14 </p><p> 489.6 in row 15 </p><p> Not specified in row 16 </p><p> Not specified in row 17 </p><p> 1709 in row 18 </p><p> Not specified in row 19 </p><p> Not specified in row 20 </p><p> Not specified in row 21 </p><p> 240 in row 22 </p><p> 1000 in row 23 </p><p> Not specified in row 24 </p><p> Not specified in row 25 </p><p> Not specified in row 26 </p><p> Not specified in row 27 </p>"
        
        self.assertEqual(valid_string, response.data)

    def test_fetch_all_col_route_non_numeric(self):
        self.app = app.test_client() 

        response = self.app.get('/all/Model name', follow_redirects=True) 
        
        valid_string = b"""<p> GPT-3 in row 1 </p><p> GPT-4 in row 2 </p><p> PaLM in row 3 </p><p> BLOOM in row 4 </p><p> DeepSeek-V3 in row 5 </p><p> Llama 3.1 in row 6 </p><p> Claude 3 Opus in row 7 </p><p> Claude 3 Sonnet in row 8 </p><p> Claude 3 Haiku in row 9 </p><p> Gemini 1.0 Ultra in row 10 </p><p> Gemini 1.5 Pro in row 11 </p><p> T5 in row 12 </p><p> GShard in row 13 </p><p> Switch in row 14 </p><p> XLM in row 15 </p><p> Chinchilla in row 16 </p><p> GLaM in row 17 </p><p> Falcon 180B in row 18 </p><p> Mistral 7B in row 19 </p><p> Mixtral 8x7B in row 20 </p><p> Qwen 72B in row 21 </p><p> Yi-34B in row 22 </p><p> Grok 3 in row 23 </p><p> Gopher in row 24 </p><p> OPT-175B in row 25 </p><p> Gemma 7B in row 26 </p><p> Vicuna 7B in row 27 </p>"""

        self.assertEqual(valid_string, response.data) 

    def test_fetch_all_col_route_invalid_col(self):
        self.app = app.test_client() 

        response = self.app.get('/all/nafees', follow_redirects=True) 
        
        self.assertEqual(b'This is not a valid page! Please review README.md for valid paths and usage.', response.data)

if __name__ == '__main__':
    unittest.main()