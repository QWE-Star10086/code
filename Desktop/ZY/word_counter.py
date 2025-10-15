import sys
import string
from collections import Counter
def process_text(text):
    """处理文本：转换为小写并去除标点符号"""
    # 作用为转换为小写，忽略大小写差异
    text = text.lower()
    
    # 创建翻译表并去除所有标点符号
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    
    return text

def count_words(file_path):
    """统计文件中的词频并返回结果"""
    try:
        # 以UTF-8编码形式打开文件
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # 处理文本
        processed_content = process_text(content)
        
        # 分割为单词列表
        words = processed_content.split()
        
        # 统计词频
        word_counts = Counter(words)
        
        return word_counts
        
    except FileNotFoundError:
        print(f"错误：找不到文件 '{file_path}'", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"错误：文件 '{file_path}' 不是有效的UTF-8编码文件", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"处理文件时出错：{str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    # 检查是否提供了文件路径参数
    if len(sys.argv) != 2:
        print("用法：python word_counter.py <文件路径>", file=sys.stderr)
        sys.exit(1)
        
    file_path = sys.argv[1]
    
    # 统计词频
    word_counts = count_words(file_path)
    
    # 输出前20个最常见的词
    print("出现频率最高的前20个词：")
    print("------------------------")
    for word, count in word_counts.most_common(20):
        print(f"{word}: {count}次")

if __name__ == "__main__":
    main()
