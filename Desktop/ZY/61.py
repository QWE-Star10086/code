def show_messages(send_messages,sent_messages):
    while send_messages:
        ms=send_messages.pop()
        sent_messages.append(ms)
def show_sent_messages(sent_messages):
        for sent_message in sent_messages:
             print(f"Hello {sent_message}")
send_messages=["jjk","oop","yyo"]
sent_messages=[]
show_messages(send_messages,sent_messages)
show_sent_messages(sent_messages)