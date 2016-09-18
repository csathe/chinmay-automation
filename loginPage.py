from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import selectors_store_room, elements_store_room, values_store_room
from selenium.webdriver.support.ui import Select

class LP:

    def fvb(self,browser):

        try:

            # wait checks until elements have been located
            fn = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                EC.presence_of_element_located((selectors_store_room.id, elements_store_room.first_name_box)))
            ln = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                EC.presence_of_element_located((selectors_store_room.id, elements_store_room.last_name_box)))

            mobile_number = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                EC.presence_of_element_located((selectors_store_room.id, elements_store_room.mobile_number_box)))
            mobile_number_again = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                EC.presence_of_element_located((selectors_store_room.id, elements_store_room.reenter_mobile_number_box)))

            new_password = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                EC.presence_of_element_located((selectors_store_room.id, elements_store_room.new_pwd)))

            birthday_month = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                EC.presence_of_element_located((selectors_store_room.id, elements_store_room.bday_month)))

            birthday_day = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                EC.presence_of_element_located((selectors_store_room.id, elements_store_room.bday_day)))

            birthday_year = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                EC.presence_of_element_located((selectors_store_room.id, elements_store_room.bday_year)))

            m = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                EC.presence_of_element_located((selectors_store_room.id, elements_store_room.male)))
            fm = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                EC.presence_of_element_located((selectors_store_room.id, elements_store_room.female)))

            # enter text in boxes, select dropdown options etc.
            fn.send_keys(values_store_room.fn_text)
            ln.send_keys(values_store_room.ln_text)
            mobile_number.send_keys(values_store_room.m_num)
            mobile_number_again.send_keys(values_store_room.m_num)
            new_password.send_keys(values_store_room.np)


            Select( (birthday_month) ).select_by_visible_text(values_store_room.mon)
            Select((birthday_day)).select_by_visible_text(values_store_room.day)
            Select((birthday_year)).select_by_visible_text(values_store_room.year)

            m.click()
            fm.click()

        except:
            print("Can't load page, possibly no connection, or browser error. ")


    def get_text(self, browser):

        try:

            # get the text from particlar page elements and return it for assertion tests

            t_and_c_text = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                        EC.presence_of_element_located((selectors_store_room.css, elements_store_room.tc_text_css)))

            ct = WebDriverWait(browser, values_store_room.timeoutinSeconds).until(
                EC.presence_of_element_located((selectors_store_room.xpath, elements_store_room.ct_xpath)))

            return t_and_c_text.text, ct.text

        except:
            print("Can't load page, possibly no connection, or browser error. ")






