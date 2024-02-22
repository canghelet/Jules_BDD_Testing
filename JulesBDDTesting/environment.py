from pages.forgot_password_page import Forgot_password_page
from pages.signin_page import Sign_in_page
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.forgot_password_page = Forgot_password_page()
    context.signin_page = Sign_in_page()

def after_all(context):
    context.browser.close()

