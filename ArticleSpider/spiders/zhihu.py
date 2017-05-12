# -*- coding: utf-8 -*-
import scrapy
import re
import json
import time

from PIL import Image


class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/']
    headers = {
        "Host": "www.zhihu.com",
        "Referer": "https://www.zhihu.com/",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }

    def parse(self, response):
        pass

    def start_requests(self):
        return [scrapy.Request("https://www.zhihu.com/#signin", headers=self.headers, callback=self.login)]

    def login(self, response):
        """
        登录
        :param response: 
        :return: 
        """
        response_text = response.text
        match_obj = re.match('.*name="_xsrf" value="(.*?)"', response_text, re.DOTALL)
        xsrf = ''
        if match_obj:
            xsrf = match_obj.group(1)

        if xsrf:
            post_data = {
                "_xsrf": xsrf,
                "phone_num": "18951855817",
                "password": "tracy584563542"
            }
            t = str(int(time.time() * 1000))
            captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
            yield scrapy.Request(captcha_url, headers=self.headers, meta={"post_data": post_data},
                                 callback=self.login_after_captcha)

    def login_after_captcha(self, response):
        with open("captcha.jpg", "wb") as f:
            f.write(response.body)
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
        captcha = input("请输入验证码：\n")
        post_data = response.meta.get("post_data", {})
        post_data["captcha"] = captcha
        post_url = "https://www.zhihu.com/login/phone_num"
        return [scrapy.FormRequest(
            url=post_url,
            formdata=post_data,
            headers=self.headers,
            callback=self.check_login
        )]

    def check_login(self, response):
        """
        验证服务器的返回数据判断登录是否成功
        :param response: 
        :return: 
        """
        text_json = json.loads(response.text)
        if 'msg' in text_json and text_json['msg'] == '登陆成功':
            # 从继承的Spider类中拿的内容，恢复到正确执行
            for url in self.start_urls:
                yield scrapy.Request(url, dont_filter=True, headers=self.headers)
