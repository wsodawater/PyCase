
import requests

class TestDEMO:

    def test_demo(self):

        # 获取access_token
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2fe8d43de24a160f&corpsecret=jf3ZvNHkSXO4zzmHfdSbRma4F17KtUghsD6E6mOa52A'
        r = requests.get(url)
        token = r.json()['access_token']

        # 添加成员
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
        # body = {
        #     "userid": "ceshiapi",
        #     "name": "测试api",
        #     "mobile": "+86 13800000001",
        #     "department": [1,2],
        # }
        # r = requests.post(url,json=body)
        # print(r.json())

        # 获取成员
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=ceshiapi"
        # r = requests.get(url)
        # print(r.json())

        #更新成员
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
        # body = {
        #     "userid": "ceshiapi",
        #     "name": "api测试人api",
        # }
        # r = requests.post(url,json=body)
        # print(r.json())

        #删除成员
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=ceshiapi"
        # r = requests.get(url)
        # print(r.json())

        # 删除成员
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=ceshiapi"
        # r = requests.get(url)
        # print(r.json())