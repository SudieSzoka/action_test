import requests
import json

def sendTextmessage(webhook, content):

    headers = {"Content-Type": "application/json; charset=utf-8",}
    payload_message = {"msg_type": "text",
        "content": {"text": content}}
    # print(payload_message)
    requests.post(url=webhook, data=json.dumps(payload_message), headers=headers)

if __name__ == "__main__":
    # webhook 是一串以“https://open.feishu.cn/open-apis/bot/v2/hook”开头的字符串
    # 需要替换成自己的
    webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/50f62927-674c-47e7-aac2-98092d28cc19"
    content = "你好，Action！"
    sendTextmessage(webhook, content)
