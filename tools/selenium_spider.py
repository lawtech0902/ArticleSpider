# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/6/22 下午4:49'
"""
import time

from selenium import webdriver
from scrapy.selector import Selector

# browser = webdriver.Chrome(executable_path="/Users/lawtech/TempSpace/chromedriver")

# Selenium动态网页请求
# browser.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.13.bgHDMS&id=539418030842&cm_id=140105335569ed55e27b&abbucket=5")
# t_selector = Selector(text=browser.page_source)
# print(t_selector.css(".tm-promo-price .tm-price::text").extract())

# Selenium完成知乎模拟登录
# browser.get("https://www.zhihu.com/#signin")
# browser.find_element_by_css_selector(".view-signin input[name='account']").send_keys("584563542@qq.com")
# browser.find_element_by_css_selector(".view-signin input[name='password']").send_keys("tracy584563542")
# browser.find_element_by_css_selector(".view_signin button.sign-button").click()

# Selenium完成微博模拟登录
# browser.get("https://www.weibo.com")
# time.sleep(10)
# browser.find_element_by_css_selector("#loginname").send_keys("584563542@qq.com")
# browser.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys("tracy584563542")
# browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()

# Selenium模拟鼠标下拉
# browser.get("https://www.oschina.net/blog")
# for i in range(3):
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(3)

# 设置ChromeDriver不加载图片
# chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_opt.add_experimental_option("prefs", prefs)
# browser = webdriver.Chrome(executable_path="/Users/lawtech/TempSpace/chromedriver", chrome_options=chrome_opt)
# browser.get("https://www.taobao.com")

# phantomjs, 无界面的浏览器， 多进程情况下phantomjs性能会下降很严重
# browser = webdriver.PhantomJS(executable_path="/Users/lawtech/TempSpace/phantomjs-2.1.1-macosx/bin/phantomjs")
# browser.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.13.bgHDMS&id=539418030842&cm_id=140105335569ed55e27b&abbucket=5")
# t_selector = Selector(text=browser.page_source)
# print(t_selector.css(".tm-promo-price .tm-price::text").extract())
# browser.quit()

# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
# display.start()
#
# browser = webdriver.Chrome(executable_path="/Users/lawtech/TempSpace/chromedriver")
# browser.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.13.bgHDMS&id=539418030842&cm_id=140105335569ed55e27b&abbucket=5")

