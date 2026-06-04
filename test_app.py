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
        
        self.assertEqual(b'<h1> Top 5 Models by training_hours </h1><p> Model:BLOOM | 2820.0 </p><p> Model:GPT-4 | 2160.0 </p><p> Model:Llama 3.1 | 1928.0 </p><p> Model:Falcon 180B | 1709.0 </p><p> Model:DeepSeek-V3 | 1361.0 </p>', response.data)

    def test_user_story_route_non_numeric(self):
        self.app = app.test_client() 

        response = self.app.get('/model_name', follow_redirects=True) 
        
        self.assertEqual(b'This is not a valid page! Please review README.md for valid paths and usage.', response.data) 

    def test_user_story_route_invalid_col(self):
        self.app = app.test_client() 

        response = self.app.get('/nafees', follow_redirects=True) 
        
        self.assertEqual(b'This is not a valid page! Please review README.md for valid paths and usage.', response.data)

    # Tests for Nafees' top n columns route

    def test_top_n_in_column_route(self):
        self.app = app.test_client() 

        response = self.app.get('/2/training_hours', follow_redirects=True) 
        
        self.assertEqual(b'<h1> Top 2 Models by training_hours </h1><p> Model:BLOOM | 2820.0 </p><p> Model:GPT-4 | 2160.0 </p>', response.data)

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

        valid_string = b"""<h1> All values in training_hours </h1><ol><li> Model: GPT-3 | Value: 355.2 </li><li> Model: GPT-4 | Value: 2160.0 </li><li> Model: PaLM | Value: 1200.0 </li><li> Model: BLOOM | Value: 2820.0 </li><li> Model: DeepSeek-V3 | Value: 1361.0 </li><li> Model: Llama 3.1 | Value: 1928.0 </li><li> Model: Claude 3 Opus | Value: None </li><li> Model: Claude 3 Sonnet | Value: None </li><li> Model: Claude 3 Haiku | Value: None </li><li> Model: Gemini 1.0 Ultra | Value: None </li><li> Model: Gemini 1.5 Pro | Value: None </li><li> Model: T5 | Value: 480.0 </li><li> Model: GShard | Value: 74.4 </li><li> Model: Switch | Value: 648.0 </li><li> Model: XLM | Value: 489.6 </li><li> Model: Chinchilla | Value: None </li><li> Model: GLaM | Value: None </li><li> Model: Falcon 180B | Value: 1709.0 </li><li> Model: Mistral 7B | Value: None </li><li> Model: Mixtral 8x7B | Value: None </li><li> Model: Qwen 72B | Value: None </li><li> Model: Yi-34B | Value: 240.0 </li><li> Model: Grok 3 | Value: 1000.0 </li><li> Model: Gopher | Value: None </li><li> Model: OPT-175B | Value: None </li><li> Model: Gemma 7B | Value: None </li><li> Model: Vicuna 7B | Value: None </li></ol>"""
        
        self.assertEqual(valid_string, response.data)

    def test_fetch_all_col_route_non_numeric(self):
        self.app = app.test_client() 

        response = self.app.get('/all/model_name', follow_redirects=True) 
        
        valid_string = b"""<h1> All values in model_name </h1><ol><li> Model: GPT-3 | Value: GPT-3 </li><li> Model: GPT-4 | Value: GPT-4 </li><li> Model: PaLM | Value: PaLM </li><li> Model: BLOOM | Value: BLOOM </li><li> Model: DeepSeek-V3 | Value: DeepSeek-V3 </li><li> Model: Llama 3.1 | Value: Llama 3.1 </li><li> Model: Claude 3 Opus | Value: Claude 3 Opus </li><li> Model: Claude 3 Sonnet | Value: Claude 3 Sonnet </li><li> Model: Claude 3 Haiku | Value: Claude 3 Haiku </li><li> Model: Gemini 1.0 Ultra | Value: Gemini 1.0 Ultra </li><li> Model: Gemini 1.5 Pro | Value: Gemini 1.5 Pro </li><li> Model: T5 | Value: T5 </li><li> Model: GShard | Value: GShard </li><li> Model: Switch | Value: Switch </li><li> Model: XLM | Value: XLM </li><li> Model: Chinchilla | Value: Chinchilla </li><li> Model: GLaM | Value: GLaM </li><li> Model: Falcon 180B | Value: Falcon 180B </li><li> Model: Mistral 7B | Value: Mistral 7B </li><li> Model: Mixtral 8x7B | Value: Mixtral 8x7B </li><li> Model: Qwen 72B | Value: Qwen 72B </li><li> Model: Yi-34B | Value: Yi-34B </li><li> Model: Grok 3 | Value: Grok 3 </li><li> Model: Gopher | Value: Gopher </li><li> Model: OPT-175B | Value: OPT-175B </li><li> Model: Gemma 7B | Value: Gemma 7B </li><li> Model: Vicuna 7B | Value: Vicuna 7B </li></ol>"""

        self.assertEqual(valid_string, response.data) 

    def test_fetch_all_col_route_invalid_col(self):
        self.app = app.test_client() 

        response = self.app.get('/all/nafees', follow_redirects=True) 
        
        self.assertEqual(b'This is not a valid page! Please review README.md for valid paths and usage.', response.data)

if __name__ == '__main__':
    unittest.main()