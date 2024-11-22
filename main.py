from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from datetime import date

DEBUG = True
url = 'http://ecodata.kz:3838/app_dg_map_ru/'

chromedriver_path = './chromedriver'
service = Service(executable_path=chromedriver_path)

coordinates = [(966, 216)]  # Исходные координаты для начала перемещения
levels = [] 

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Без графического интерфейса
# options.add_argument("--no-sandbox")``
# options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1366,768") 


driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()

water_bodies = [
    {
        'name': 'р.Ертис - с.Абылайкит',
        'pre_cord': None,
        'pre_instruction':None,
        'coord': (778, 39), 
        'water_level': 0,
    },     
     
    {
        'name': 'р.Абылайкит - с.Самсоновка',
        'pre_cord': None,
        'pre_instruction':None,
        'coord': (689, 251),
        'water_level': 0,
    }, 

    {
        'name': 'р.Ульби - г. Риддер',
        'pre_cord': (647,305),
        'pre_instruction': None,
        'coord': (821, 134),
        'water_level': 0, 
    },   
    
    {
        'name': 'р. Шаровка - с. Шаровка',
        'pre_cord': None, 
        'pre_instruction': None,
        'coord': (727, 213),
        'water_level': 0,
     },

    {

        'name': 'р. Кара Ертис - с. Боран',
        'pre_cord': (737, 342),
        'pre_instruction': [Keys.DOWN] * 6 + [Keys.RIGHT] * 3,
        'coord': (788, 431),
        'water_level': 0,
     },
     
     {
         'name': 'р. Бас Теректы - с. Мойылды', 
         'pre_cord': (753, 441),
         'pre_instruction': None, 
         'coord': (815, 307),
         'water_level': 0,
    },
    {
        'name': 'р. Калжыр - с. Калжыр',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (585, 393),
        'water_level': 0,
    },   
    
    {
        'name': 'р. Улкен Бокен - с. Джумба',
        'pre_cord': None, 
        'pre_instruction': None,
        'coord': (144, 151),
        'water_level': 0,
    },

    {
        'name': 'р. Кайынды - с. Миролюбовка',
        'pre_cord': None, 
        'pre_instruction': None,
        'coord': (325, 251),
        'water_level': 0,
    }, 
    {
        'name': 'вдхр. Буктырма - с. Куйган',
        'pre_cord': None, 
        'pre_instruction': None, 
        'coord': (305, 350),
        'water_level': 0,
    },
    {
        'name': 'вдхр. Буктырма - с. Аксуат',
        'pre_cord': None,
        'pre_instruction': None, 
        'coord': (348, 478),
        'water_level': 0,
    }, 
    {
        'name': 'р. Куршим - с. Маралды',
        'pre_cord': None, 
        'pre_instruction': None,
        'coord': (530, 326  ),
        'water_level': 0,
    },
    {
        'name': 'р. Куршим - с. Бирлик',
        'pre_cord': None, 
        'pre_instruction': None,
        'coord': (376, 367),
        'water_level': 0,
    },

    {
        'name': 'р. Нарын - с. Улкен Нарын',
        'pre_cord': (491, 399),
        'pre_instruction': None,
        'coord': (501, 203),
        'water_level':0
    },
    {
        'name': 'вдхр. Буктырма - с. Хайрузовка',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (470, 251),
        'water_level':0,
    },
    {
        'name': 'р. Нарын - с. Кокбастау',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (526, 251),
        'water_level': 0,
    },
    {
        'name': 'р. Буктырма - с. Барлык',
        'pre_cord': None,
        'pre_instruction': None, 
        'coord': (618, 233),
        'water_level':0,
    },
    {
        'name': 'р. Буктырма - с. Берель',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (852, 248),
        'water_level': 0,
    },

    {
        'name': 'р. Аксу - с. Аксу',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (512, 250),
        'water_level':0
    },

    {
        'name': 'р. Урыль - с. Урыль',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (680, 290),
        'water_level': 0
    },

    {
        'name': 'р. Черновая - с. Черновое (Аккайнар)',
        'pre_cord': None,
        'pre_instruction': None, 
        'coord': (597, 296),
        'water_level': 0
    },
    {
        'name': 'р. Сарымсакты - с. Катон-Карагай',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (544, 316),
        'water_level':0
    },

    {
        'name': 'р. Акберел (Aкбулкак) – с. Берел',
        'pre_cord': (633, 350),
        'pre_instruction': None,
        'coord': (682, 246),
        'water_level': 0,
    },

    {
        'name': 'р. Буктырма - с. Лесная Пристань',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (310, 125),
        'water_level':0
    },

    {
        'name': 'р. Левая Березовка - с. Средигорное',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (323, 351),
        'water_level': 0,
    },

    {
        'name': 'р. Тургысын - с. Кутиха',
        'pre_cord': (404, 365),
        'pre_instruction': None,
        'coord': (268, 236),
        'water_level': 0
    },
    
    {
        'name': 'вдхр. Буктырма - с. Заводинка',
        'pre_cord': None, 
        'pre_instruction': None, 
        'coord': (220, 317),
        'water_level':0
    },

    {
        'name': 'вдхр. Буктырма - с. Селезневка',
        'pre_cord': None,
        'pre_instruction': None, 
        'coord': (165,335),
        'water_level':0
    },

    {
        'name': 'р. Хамир - с. Малеевск',
        'pre_cord': (251,377),
        'pre_instruction': None,
        'coord': (340, 249),
        'water_level': 0
    },
    
    {
        'name': 'р. Березовка - с. Соловьево',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (342,325),
        'water_level':0
    },

    {
        'name': 'р. Смолянка - с. Северное',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (118, 280),
        'water_level': 0
    },

    {
        'name': 'р. Ульби - с. Ульби-Перевальное',
        'pre_cord': (257,289),
        'pre_instruction': None,
        'coord': (122,216),
        'water_level': 0,
    },

    {
        'name': 'р. Глубочанка - с. Белокаменка',
        'pre_cord': (289, 284),
        'pre_instruction': None,
        'coord': (153,220),
        'water_level':0
    },

    {
        'name': 'р. Красноярка - с. Предгорное',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (121,241),
        'water_level': 0,
    },

    {
        'name': 'р. Улан - с. Герасимовка',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (216, 334),
        'water_level': 0,
    },
    {
        'name': 'р. Дресвянка - с. Отрадное',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (185, 328),
        'water_level': 0,
    },
    {
        'name': 'р. Сибе - с. Алгабас',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (242,500),
        'water_level':0,
    },
    {
        'name': 'р. Жартас - с. Гагарино',
        'pre_cord': (318, 512),
        'pre_instruction': None,
        'coord': (114,278),
        'water_level': 0,
    },
    {
        'name': 'р. Тайынты - с. Акбулан',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (395,458),
        'water_level': 0,
    },

    {
        'name': 'р. Киши Ульби - с. Горная Ульбинка',
        'pre_cord': (459,523),
        'pre_instruction': None,
        'coord': (373,326),
        'water_level': 0,
    },
    {
        'name': 'р. Ертис - с. Уварова',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (278,307),
        'water_level':0
    },
    {
        'name': 'р. Оба - с. Верхуба',
        'pre_cord': (455,331),
        'pre_instruction': None,
        'coord': (284,185),
        'water_level':0
    },
    {
        'name':'р. Малая Убинка - с. Быструха',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (413,405),
        'water_level':0
    },
    {
        'name': 'р. Оба - с. Каракожа',
        'pre_cord': (398,252),
        'pre_instruction': None,
        'coord': (398,151),
        'water_level':0,
    },
    {
        'name': 'р. Оба - г. Шемонаиха',
        'pre_cord':None,
        'pre_instruction':None,
        'coord':(185,301),
        'water_level':0
    },
    {
        'name': 'вдхр. Буктырма - п. Тугыл',
        'pre_cord': (350,310),
        'pre_instruction': [Keys.DOWN] * 9,
        'coord': (609,383),
        'water_level':0,
    },
    {
        'name': 'р. Кандысу - с. Сарыолен',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (589,505),
        'water_level':0,
    },

]

try:
    driver.get(url)

    # driver.maximize_window()

    sleep(5)  # Ждем, чтобы страница полностью загрузилась
    
    cycle_var = True
    zoom_in_button = None
    while cycle_var:
    
    # Находим элемент <a> с классом leaflet-control-zoom-in и кликаем на него
        try:
            zoom_in_button = driver.find_element(By.CLASS_NAME, 'leaflet-control-zoom-in')
        except NoSuchElementException: 
            pass 

        if zoom_in_button:
            cycle_var = False
    zoom_in_button.click()  # Кликаем на элемент для увеличения масштаба
    sleep(1)
    zoom_in_button.click()

    # sleep(3)  # Ждем немного, чтобы увидеть эффект клика

    actions = ActionChains(driver)
    actions.move_by_offset(736,500).perform()
    
    # Перемещаем курсор на заданные координаты

    for _ in range(14):
        actions.send_keys(Keys.ARROW_RIGHT).perform()
        sleep(.3)

    actions.send_keys(Keys.ARROW_UP).perform() 
    sleep(.3)

    zoom_in_button.click()
    actions.move_by_offset(-736,-500)

    for body in water_bodies: 
        
        if body['pre_cord']:
            pre_x, pre_y = body['pre_cord']
            actions.move_by_offset(pre_x, pre_y).perform()
            sleep(.4)
            actions.click().perform() 
            sleep(.4)
            actions.move_by_offset(-pre_x, -pre_y)

        if body['pre_instruction']:
            for move in body['pre_instruction']:
                actions.send_keys(move).perform()
                sleep(.3)

        x,y = body['coord']
        actions.move_by_offset(x,y).perform()
        sleep(.3) 
        actions.click().perform() 
        sleep(.3)
        try:
            row_element = driver.find_element(By.XPATH, "//td[font[text()='Фактический уровень, см']]/following-sibling::td")
            print(row_element)
            table_value = row_element.text 
            body['water_level'] = table_value
            print(table_value)

        except Exception as e:
            print(f"Couldnt find a water level value for {body['name']}", e)

        actions.move_by_offset(-x,-y)
        


        
        
    print('Закончил выполнение скрипта')
    print('Спаршенные значения:', [body['water_level'] for body in water_bodies], len(water_bodies))
    
    # if DEBUG:
    #     sleep(555)  # Задержка для наблюдения результата
    # else:
    #     sleep(10)
    for body in water_bodies:
        body['date'] = date.today()


    df = pd.DataFrame(water_bodies)
    df = df[['name', 'water_level', 'date']]
    df.to_csv('hydroposts1.csv', index=False, encoding='utf-8-sig')

finally:
    word = input()
    if word == 'close':
        driver.quit()
    else:
        driver.quit()