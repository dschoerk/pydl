import unittest
from pathlib import Path
import src as pydl

class Testcases(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)

        self.testurl = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'

    '''def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)'''

    def test_download_success(self):
        pydl.get(self.testurl)
        [p.unlink() for p in Path('.').glob('*.png')] # delete any downloaded png files

    def test_download_localpath(self):
        pydl.get(self.testurl, localpath='test.png')
        Path('test.png').unlink()

    def test_md5_fail(self):
        with self.assertRaises(Exception):
            pydl.get(self.testurl, md5='')

    def test_md5_success(self):
        local_file = 'tmp'
        pydl.get(self.testurl, localpath=local_file)
        md5 = pydl.md5_from_file(local_file)
        Path(local_file).unlink()

        pydl.get(self.testurl, localpath=local_file, md5=md5)
        Path(local_file).unlink()





if __name__ == '__main__':
    unittest.main()