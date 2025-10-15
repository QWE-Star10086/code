# 导入function.py中的函数
from function import show_messages, show_sent_messages
send_messages = ["jjk", "oop", "yyo"]
sent_messages = []
# 使用导入的函数
show_messages(send_messages, sent_messages)
show_sent_messages(sent_messages)
