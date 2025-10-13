import unittest
import tempfile
import os
from word_counter import count_words

class TestWordCounter(unittest.TestCase):
    """单元测试类，测试 word_counter.py 的核心功能"""
    
    def test_basic_word_count(self):
        """测试基本的词频统计功能"""
        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("Hello world! Hello Python. Python is great.")
            temp_name = f.name
        
        # 执行统计
        result = count_words(temp_name)
        os.unlink(temp_name)  # 删除临时文件
        
        # 转换为字典便于断言
        result_dict = dict(result)
        
        # 验证结果
        self.assertEqual(result_dict.get('hello'), 2)
        self.assertEqual(result_dict.get('world'), 1)
        self.assertEqual(result_dict.get('python'), 2)
        self.assertEqual(result_dict.get('is'), 1)
        self.assertEqual(result_dict.get('great'), 1)
    
    def test_case_insensitivity(self):
        """测试大小写不敏感特性"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("Hello HELLO hello")
            temp_name = f.name
        
        result = count_words(temp_name)
        os.unlink(temp_name)
        
        self.assertEqual(dict(result).get('hello'), 3)
    
    def test_punctuation_removal(self):
        """测试标点符号去除功能"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("don't won't hello! world? test... example,")
            temp_name = f.name
        
        result = count_words(temp_name)
        os.unlink(temp_name)
        
        result_dict = dict(result)
        self.assertEqual(result_dict.get('dont'), 1)
        self.assertEqual(result_dict.get('wont'), 1)
        self.assertEqual(result_dict.get('hello'), 1)
        self.assertEqual(result_dict.get('world'), 1)
        self.assertEqual(result_dict.get('test'), 1)
        self.assertEqual(result_dict.get('example'), 1)
    
    def test_empty_file(self):
        """测试空文件处理"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            temp_name = f.name  # 空文件
        
        result = count_words(temp_name)
        os.unlink(temp_name)
        
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()