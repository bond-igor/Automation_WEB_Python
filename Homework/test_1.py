import yaml, time
from testpage import OperationsHelper, check_id
import logging


with open("testdata.yaml") as f:
	testdata = yaml.safe_load(f)


def test_step_1(browser):
    logging.info("Тест 1 запущен")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'

def test_step2(browser):
	logging.info("Тест 2 запущен")
	testpage = OperationsHelper(browser, testdata['address'])
	testpage.go_to_site()
	testpage.enter_login(testdata["login"])
	testpage.enter_pass(testdata["password"])
	testpage.click_login_button()

	assert testpage.get_text_blog() == "Blog"


def test_step3(browser):
	# залогинится
	logging.info("Тест 3 запущен")
	testpage = OperationsHelper(browser, testdata['address'])
	testpage.go_to_site()
	try:
		testpage.enter_login(testdata["login"])
		testpage.enter_pass(testdata["password"])
		testpage.click_login_button()
	except:
		pass
	# создания поста
	testpage.click_new_post_btn()
	testpage.enter_title_post("new title")
	testpage.enter_content_post("content")
	testpage.click_save_btn()

	time.sleep(3)

	# Проверка наличия названия поста на странице
	assert testpage.get_res_create_text() == "new title"

def test_step_4(browser):
	logging.info("Тест 4 запущен")
	testpage = OperationsHelper(browser, testdata['address'])
	testpage.go_to_site()
	#добавим модуль try/except что бы тест можно было запускать отдельно от других
	try:
		testpage.enter_login(testdata['login'])
		testpage.enter_pass(testdata['password'])
		testpage.click_login_button()
	except:
		pass
	testpage.contact_contact_link()
	time.sleep(testdata['sleep_time'])
	testpage.enter_contact_name("ivan")
	testpage.enter_contact_mail("test@mail.ru")
	testpage.enter_contact_content("Hello World")
	time.sleep(testdata['sleep_time'])
	testpage.click_contact()
	time.sleep(testdata['sleep_time'])
	assert testpage.get_alert_text() == 'Form successfully submitted'

def test_step5(required_id, token):
	logging.info("Тест 5 запущен")
	assert required_id in check_id(token)

