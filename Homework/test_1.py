import yaml
import time

with open("testdata.yaml") as f:
	testdata = yaml.safe_load(f)


def test_step1(log_xpath, pass_xpath, btn_xpath, result_xpath, site):
	input1 = site.find_element("xpath", log_xpath)
	input1.send_keys("test")
	input2 = site.find_element("xpath", pass_xpath)
	input2.send_keys("test")
	btn = site.find_element("xpath", btn_xpath)
	btn.click()
	err_lable = site.find_element("xpath", result_xpath)
	assert err_lable.text == "401"

def test_step2(site, log_xpath, pass_xpath, btn_xpath, result_login):
	input1 = site.find_element("xpath", log_xpath)
	input1.send_keys(testdata["login"])
	input2 = site.find_element("xpath", pass_xpath)
	input2.send_keys(testdata["password"])
	btn = site.find_element("xpath", btn_xpath)
	btn.click()
	login = site.find_element("xpath", result_login)
	assert login.text == "Blog"

def test_step3(site, log_xpath, pass_xpath, btn_xpath, btn_new_post, title, btn_save, result_post):
	input1 = site.find_element("xpath", log_xpath)
	input1.send_keys(testdata["login"])
	input2 = site.find_element("xpath", pass_xpath)
	input2.send_keys(testdata["password"])
	btn = site.find_element("xpath", btn_xpath)
	btn.click()
	btn_new_post = site.find_element("xpath", btn_new_post)
	btn_new_post.click()
	input3 = site.find_element("xpath", title)
	input3.send_keys(testdata["title"])
	btn_save = site.find_element("xpath", btn_save)
	btn_save.click()
	time.sleep(testdata["sleep_time"])
	post = site.find_element("xpath", result_post)
	assert post.text == testdata["title"]

