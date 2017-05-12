# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/5/9 下午3:18'
"""

import re
import requests
import time

from PIL import Image

try:
    import cookielib
except:
    import http.cookiejar as cookielib

# 构造requests headers
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

# 使用登录cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie未能加载")


def get_xsrf():
    """
    获取xsrf code
    :return: xsrf code
    """
    response = requests.get("https://www.zhihu.com", headers=headers)
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text)
    if match_obj:
        print(match_obj.group(1))
    else:
        return ""


def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    im = Image.open('captcha.jpg')
    im.show()
    im.close()
    captcha = input("请输入验证码：\n")
    return captcha


def zhihu_login(account, password):
    """
    知乎登录
    :param account: 
    :param password: 
    :return: 
    """
    if re.match("^1\d{10}$", account):
        print("手机号码登录 \n")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf": get_xsrf(),
            "phone_num": account,
            "password": password
        }
    else:
        if "@" in account:
            print("邮箱登录 \n")
        else:
            print("你的账号输入有问题，请重新登录")
            return 0
        post_url = 'https://www.zhihu.com/login/email'
        post_data = {
            '_xsrf': get_xsrf(),
            'password': password,
            'email': account
        }

    # 不需要验证码直接登录成功
    login_page = session.post(post_url, post_data, headers=headers)
    login_code = login_page.json()
    if login_code['r'] == 1:
        # 不输入验证码登录失败
        # 使用需要输入验证码的方式登录
        post_data["captcha"] = get_captcha()
        login_page = session.post(post_url, post_data, headers=headers)
        login_code = login_page.json()
        print(login_code['msg'])
    # 保存 cookies 到文件，
    # 下次可以使用 cookie 直接登录，不需要输入账号和密码
    session.cookies.save()


def is_login():
    """
    通过查看用户个人信息来判断是否已经登录
    :return: 
    """
    url = "https://www.zhihu.com/settings/profile"
    response = session.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return True
    else:
        return False


if __name__ == '__main__':
    if is_login():
        print("您已经登录！")
    else:
        account = input("请输入用户名：\n")
        password = input("请输入密码：\n")
        zhihu_login(account, password)
