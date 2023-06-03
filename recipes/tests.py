from django.test import TestCase
from .selPath import SELENIUM_DIRS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless") #sera usado no actions
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

class petracker_tests(TestCase):
    def test(self):
        driver.get("http://127.0.0.1:8000/")
        self.run_tests(driver)
    
    def register(self, driver):
        register = driver.find_element(By.NAME, "sign-up")
        register.click()
        register_username = driver.find_element(By.NAME, "username")
        register_username.send_keys("miles morales")
        register_email = driver.find_element(By.NAME, "email")
        register_email.send_keys("spiderman@gmail.com")
        register_password = driver.find_element(By.NAME, "password")
        register_password.send_keys("gwen&miles")
        register_button = driver.find_element(By.NAME, "register")
        time.sleep(1)
        register_button.click()

    def login(self, driver):
        login_username = driver.find_element(By.NAME, "username")
        login_username.send_keys("miles morales")
        login_password = driver.find_element(By.NAME, "password")
        login_password.send_keys("gwen&miles")
        login_button = driver.find_element(By.NAME, "login")
        time.sleep(1)
        login_button.click()

    def register_pet(self, driver):
        time.sleep(1)
        register_pet_button = driver.find_element(By.LINK_TEXT, "+")
        register_pet_button.click()
        register_pet_name = driver.find_element(By.NAME, "name")
        register_pet_name.send_keys("Peter Porker")
        register_pet_breed = driver.find_element(By.NAME, "breed")
        register_pet_breed.send_keys("Spider Pig")
        register_pet_age = driver.find_element(By.NAME, "age")
        register_pet_age.send_keys("3")
        register_pet_description = driver.find_element(By.NAME, "description")
        register_pet_description.send_keys("This is astounding! Am I a spider with the limitations of a pig? Or a pig with the proportionate strength and agility of a spider? I've become something greater than either spider or pig... I've become a Spider-Ham!")
        register_pet_phone = driver.find_element(By.NAME, "phone")
        register_pet_phone.send_keys("12345678910")
        register_pet_email = driver.find_element(By.NAME, "email")
        register_pet_email.send_keys("spiderman@gmail.com")
        driver.find_element(By.NAME, "photo").send_keys("C:/Users/virna/OneDrive/Área de Trabalho/FDS_PETracker(3.0)/PETracker/files/spider_pig.jpg") #ver dps como alterar isso por causa do actions
        register_pet_button_create = driver.find_element(By.NAME, "create")
        register_pet_button_create.click()
        
    def acessing_home(self, driver):
        pet_profile_button = driver.find_element(By.NAME, "pet_profile")
        pet_profile_button.click()
        time.sleep(1)

    def alergy(self, driver):
        alergy_input = driver.find_element(By.NAME, "title")
        alergy_input.send_keys("Tylenol")
        alergy_input_button = driver.find_element(By.NAME, "add")
        alergy_input_button.click()
        time.sleep(1)
        driver.find_element(By.ID, "ab").click()
        time.sleep(1)
        driver.find_element(By.ID, "del-al").click()
        time.sleep(1)
        
    def background_color(self, driver):
        background_color_select = driver.find_element(By.ID, "id_background_color")
        background_color_select.click()
        Select(background_color_select).select_by_value('#978DCC')
        background_color_select_button = driver.find_element(By.NAME, "add_color")
        background_color_select_button.click()
        time.sleep(1)
        
        background_color_select = driver.find_element(By.ID, "id_background_color")
        background_color_select.click()
        Select(background_color_select).select_by_value('#FAA42B')
        background_color_select_button = driver.find_element(By.NAME, "add_color")
        background_color_select_button.click()
        time.sleep(1)
        
        background_color_select = driver.find_element(By.ID, "id_background_color")
        background_color_select.click()
        Select(background_color_select).select_by_value('#00B7D9')
        background_color_select_button = driver.find_element(By.NAME, "add_color")
        background_color_select_button.click()
        time.sleep(1)

        background_color_select = driver.find_element(By.ID, "id_background_color")
        background_color_select.click()
        Select(background_color_select).select_by_value('#4FD881')
        background_color_select_button = driver.find_element(By.NAME, "add_color")
        background_color_select_button.click()
        time.sleep(1)

    def calendar(self, driver):
        calendar_nav_button = driver.find_element(By.ID, "calendar")
        calendar_nav_button.click()
        new_event_button = driver.find_element(By.NAME, "button_new_event")
        new_event_button.click()
        event_title = driver.find_element(By.ID, "id_title")
        event_title.send_keys("Walk to The Park With Peter Porker")
        event_description = driver.find_element(By.ID, "id_description")
        event_description.send_keys("He needs to check if any super vilain is trying to commit crimes. Thanos can be there. Who knows? He's inevitable!")
        event_start_time = driver.find_element(By.ID, "id_start_time")
        event_start_time.send_keys("13062023")
        event_start_time.send_keys(Keys.TAB)
        event_start_time.send_keys("1620")
        event_end_time = driver.find_element(By.ID, "id_end_time")
        event_end_time.send_keys("13062023")
        event_end_time.send_keys(Keys.TAB)
        event_end_time.send_keys("2007")
        event_color_select = driver.find_element(By.ID, "id_colorSelected")
        event_color_select.send_keys("purple")
        event_save_button = driver.find_element(By.ID, "save-event")
        time.sleep(1)
        event_save_button.click()
        time.sleep(1)
        #falta terminar esse, mas n faço ideia de como
        back_button = driver.find_element(By.ID, "back_button")
        back_button.click()
        time.sleep(1)

    def checklist(self, driver):
        checklist_nav_button = driver.find_element(By.ID, "kanban") 
        checklist_nav_button.click()
        new_task = driver.find_element(By.ID, "task")
        new_task.send_keys("Defeat Thanos")
        new_task_responsible = driver.find_element(By.ID, "responsible")
        new_task_responsible.send_keys("Peter Porker")
        new_task_due_date = driver.find_element(By.ID, "due-date")
        new_task_due_date.send_keys(13062023)
        add_task_button = driver.find_element(By.ID, "add-task")
        add_task_button.click()
        
        move_task_r = driver.find_element(By.ID, "right-td-btn")
        move_task_r.click()
        time.sleep(1)
        
        move_task_r2 = driver.find_element(By.ID, "right-ip-btn")
        move_task_r2.click()
        time.sleep(1)
        move_task_l = driver.find_element(By.ID, "left-d-btn")
        move_task_l.click()
        time.sleep(1)
        move_task_r2 = driver.find_element(By.ID, "right-ip-btn")
        move_task_r2.click()
        time.sleep(1)
        move_task_r3 = driver.find_element(By.ID, "right-d-btn")
        move_task_r3.click()
        time.sleep(1)
        show_history = driver.find_element(By.ID, "show")
        show_history.click()
        time.sleep(1)
        hide_history = driver.find_element(By.ID, "hide")
        hide_history.click()
        time.sleep(1)
        show_history = driver.find_element(By.ID, "show")
        show_history.click()
        time.sleep(1)
        redo_task = driver.find_element(By.ID, "restore-h-btn")
        redo_task.click()
        time.sleep(1)
        delete_task = driver.find_element(By.ID, "delete-td-btn")
        delete_task.click()
        time.sleep(1)
        
        back_button = driver.find_element(By.ID, "back_button")
        back_button.click()
        time.sleep(2)

    def medicine(self, driver):
        medicine_nav_button = driver.find_element(By.ID, "medicine")
        medicine_nav_button.click()

        plan_medicine = driver.find_element(By.ID, "id_medicine")
        plan_medicine.send_keys("Zolmitriptan")
        plan_details = driver.find_element(By.ID, "id_details")
        plan_details.send_keys("After defeating Thanos, Peter got sick. Since Porker is alergic to Tylenol, he'll take Zolmitriptan's pills for 3 days instead")
        plan_times_per_day = driver.find_element(By.ID, "id_time_per_day")
        plan_times_per_day.send_keys("1")
        time.sleep(1)
        plan_add_button = driver.find_element(By.ID, "add-plan")
        plan_add_button.click()
        time.sleep(1)
        driver.find_element(By.ID, "mpd").click()
        time.sleep(1)
        driver.find_element(By.ID, "back_button").click()
        time.sleep(3)
        driver.find_element(By.ID, "mpd").click()
        time.sleep(1)
        delete_med_plan = driver.find_element(By.ID, "del-med-plan")
        delete_med_plan.click()
        time.sleep(1)

        driver.quit()

        #shift + tab volta a linha

    def run_tests(self, driver):
        self.register(driver)
        self.login(driver)
        self.register_pet(driver)
        self.acessing_home(driver)
        self.alergy(driver)
        self.background_color(driver)
        self.calendar(driver)
        self.checklist(driver)
        self.medicine(driver)
# register
# login
# create pet
# select pet
# pet_home
#