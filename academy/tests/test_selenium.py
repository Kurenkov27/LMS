from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver

from academy.models import Student, Lecturer, Group


class SeleniumTest(StaticLiveServerTestCase):

    NUMBER_OF_GROUPS = 5

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(5)

    def setUp(self) -> None:
        self.student = Student.objects.create(first_name='John', last_name='Doe', email='JD@gmail.com')
        self.lecturer = Lecturer.objects.create(first_name='Adam', last_name='Smith', email='ASmith@gmail.com')
        #self._create_groups(self.NUMBER_OF_GROUPS)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_unsuccessful_login(self):
        self.selenium.get(self.live_server_url)

        login_url = self.selenium.find_element_by_id('login')
        login_url.click()

        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('test')

        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('test')

        submit_btn = self.selenium.find_element_by_id('submit_login')
        submit_btn.submit()

        error = self.selenium.find_element_by_id('invalid_login_message')
        expected_error = "Your username and password do not match! Please try again"
        self.assertEqual(error.text, expected_error)


def test_sign_up(self):
    self.selenium.get(self.live_server_url)
    login_url = self.selenium.find_element_by_id('login')
    login_url.click()
    sign_up_btn = self.selenium.find_element_by_id('sign_up')
    sign_up_btn.click()
    email_input = self.selenium.find_element_by_name('email')
    email_input.send_keys('test@lms.com')
    username_input = self.selenium.find_element_by_name('username')
    username_input.send_keys('test')
    password_input = self.selenium.find_element_by_name('password1')
    password_input.send_keys('as79fssdfm97s')
    password_input = self.selenium.find_element_by_name('password2')
    password_input.send_keys('as79fssdfm97s')
    submit_btn = self.selenium.find_element_by_tag_name('button')
    submit_btn.submit()
    notification = self.selenium.find_element_by_id('notification')
    expected_notification = 'Please confirm your email address to complete the registration.'
    self.assertEqual(notification.text, expected_notification)


def test_check_group_pagination(self):
    self.selenium.get(self.live_server_url)
    groups_url = self.selenium.find_element_by_id('groups')
    groups_url.click()
    pagination = self.selenium.find_element_by_class_name('pagination')
    self.assertTrue(bool(pagination))


def test_pagination_hide_for_single_page(self):
    Group.objects.all().delete()
    self.selenium.get(self.live_server_url)
    groups_url = self.selenium.find_element_by_id('groups')
    groups_url.click()
    with self.assertRaisesMessage(NoSuchElementException):
        self.selenium.find_element_by_class_name('page-link')


def test_contact_us(self):
    self.selenium.get(self.live_server_url)
    contact_url = self.selenium.find_element_by_id('contact')
    contact_url.click()
    email_input = self.selenium.find_element_by_name('name')
    email_input.send_keys('Mario Baker')
    email_input = self.selenium.find_element_by_name('email')
    email_input.send_keys('test@lms.com')
    username_input = self.selenium.find_element_by_name('message')
    username_input.send_keys('test')
    submit_btn = self.selenium.find_element_by_tag_name('button')
    submit_btn.submit()
    notification = self.selenium.find_element_by_id('notification')
    expected_notification = ' Your message was sent! '
    self.assertEqual(notification.text, expected_notification)


def test_no_pagination_for_students(self):
    Group.objects.all().delete()
    self.selenium.get(self.live_server_url)
    students_url = self.selenium.find_element_by_id('students')
    students_url.click()
    with self.assertRaisesMessage(NoSuchElementException):
        self.selenium.find_element_by_class_name('page-link')


def test_no_pagination_for_lecturers(self):
    Group.objects.all().delete()
    self.selenium.get(self.live_server_url)
    lecturers_url = self.selenium.find_element_by_id('lecturers')
    lecturers_url.click()
    with self.assertRaisesMessage(NoSuchElementException):
        self.selenium.find_element_by_class_name('page-link')