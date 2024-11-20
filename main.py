from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from datetime import date

DEBUG = False
url = 'http://ecodata.kz:3838/app_dg_map_ru/'

chromedriver_path = './chromedriver'
service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service)
coordinates = [(966, 216)]  # Исходные координаты для начала перемещения
levels = [] 

water_bodies = [
    {
        'name': 'р.Ертис - с.Абылайкит',
        'pre_cord': None,
        'pre_instruction':None,
        'coord': (973, 177), 
        'water_level': 0,
    },     
     
    {
        'name': 'р.Абылайкит - с.Самсоновка',
        'pre_cord': None,
        'pre_instruction':None,
        'coord': (953, 397),
        'water_level': 0,
    }, 

    {
        'name': 'р.Ульби - г. Риддер',
        'pre_cord': (922,414),
        'pre_instruction': None,
        'coord': (1090, 282),
        'water_level': 0, 
    },   
    
    {
        'name': 'р. Шаровка - с. Шаровка',
        'pre_cord': None, 
        'pre_instruction': None,
        'coord': (1118, 365),
        'water_level': 0,
     },

    {

        'name': 'р. Кара Ертис - с. Боран',
        'pre_cord': (1120, 499),
        'pre_instruction': [Keys.DOWN] * 6 + [Keys.RIGHT] * 3,
        'coord': (1174, 578),
        'water_level': 0,
     },
     
     {
         'name': 'р. Бас Теректы - с. Мойылды', 
         'pre_cord': (1133, 593),
         'pre_instruction': None, 
         'coord': (1200, 460),
         'water_level': 0,
    },
    {
        'name': 'р. Калжыр - с. Калжыр',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (971, 538),
        'water_level': 0,
    },   
    
    {
        'name': 'р. Улкен Бокен - с. Джумба',
        'pre_cord': None, 
        'pre_instruction': None,
        'coord': (530, 298),
        'water_level': 0,
    },

    {
        'name': 'р. Кайынды - с. Миролюбовка',
        'pre_cord': None, 
        'pre_instruction': None,
        'coord': (683, 405),
        'water_level': 0,
    }, 
    {
        'name': 'вдхр. Буктырма - с. Куйган',
        'pre_cord': None, 
        'pre_instruction': None, 
        'coord': (667, 495),
        'water_level': 0,
    },
    {
        'name': 'вдхр. Буктырма - с. Аксуат',
        'pre_cord': None,
        'pre_instruction': None, 
        'coord': (702, 619),
        'water_level': 0,
    }, 
    {
        'name': 'р. Куршим - с. Маралды',
        'pre_cord': None, 
        'pre_instruction': None,
        'coord': (882, 474),
        'water_level': 0,
    },
    {
        'name': 'р. Куршим - с. Бирлик',
        'pre_cord': None, 
        'pre_instruction': None,
        'coord': (735, 521),
        'water_level': 0,
    },

    {
        'name': 'р. Нарын - с. Улкен Нарын',
        'pre_cord': (822, 580),
        'pre_instruction': None,
        'coord': (850, 351),
        'water_level':0
    },
    {
        'name': 'вдхр. Буктырма - с. Хайрузовка',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (820, 398),
        'water_level':0,
    },
    {
        'name': 'р. Нарын - с. Кокбастау',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (877,403),
        'water_level': 0,
    },
    {
        'name': 'р. Буктырма - с. Барлык',
        'pre_cord': None,
        'pre_instruction': None, 
        'coord': (972, 384),
        'water_level':0,
    },
    {
        'name': 'р. Буктырма - с. Берель',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (1207, 403),
        'water_level': 0,
    },

    {
        'name': 'р. Аксу - с. Аксу',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (904, 391),
        'water_level':0
    },

    {
        'name': 'р. Урыль - с. Урыль',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (1071, 436),
        'water_level': 0
    },

    {
        'name': 'р. Черновая - с. Черновое (Аккайнар)',
        'pre_cord': None,
        'pre_instruction': None, 
        'coord': (993, 441),
        'water_level': 0
    },
    {
        'name': 'р. Сарымсакты - с. Катон-Карагай',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (937, 459),
        'water_level':0
    },

    {
        'name': 'р. Акберел (Aкбулкак) – с. Берел',
        'pre_cord': (966, 505),
        'pre_instruction': None,
        'coord': (1072, 392),
        'water_level': 0,
    },

    {
        'name': 'р. Буктырма - с. Лесная Пристань',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (712, 279),
        'water_level':0
    },

    {
        'name': 'р. Левая Березовка - с. Средигорное',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (719, 488),
        'water_level': 0,
    },

    {
        'name': 'р. Тургысын - с. Кутиха',
        'pre_cord': (783, 516),
        'pre_instruction': None,
        'coord': (660, 381),
        'water_level': 0
    },
    
    {
        'name': 'вдхр. Буктырма - с. Заводинка',
        'pre_cord': None, 
        'pre_instruction': None, 
        'coord': (615, 459),
        'water_level':0
    },

    {
        'name': 'вдхр. Буктырма - с. Селезневка',
        'pre_cord': None,
        'pre_instruction': None, 
        'coord': (553,478),
        'water_level':0
    },

    {
        'name': 'р. Хамир - с. Малеевск',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (713,396),
        'water_level': 0
    },
    
    {
        'name': 'р. Березовка - с. Соловьево',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (712,473),
        'water_level':0
    },

    {
        'name': 'р. Смолянка - с. Северное',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (489, 419),
        'water_level': 0
    },

    {
        'name': 'р. Ульби - с. Ульби-Перевальное',
        'pre_cord': (545,432),
        'pre_instruction': None,
        'coord': (424,361),
        'water_level': 0,
    },

    {
        'name': 'р. Глубочанка - с. Белокаменка',
        'pre_cord': (491, 422),
        'pre_instruction': None,
        'coord': (388,362),
        'water_level':0
    },

    {
        'name': 'р. Красноярка - с. Предгорное',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (327,408),
        'water_level': 0,
    },

    {
        'name': 'р. Улан - с. Герасимовка',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (368, 483),
        'water_level': 0,
    },
    {
        'name': 'р. Дресвянка - с. Отрадное',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (328, 477),
        'water_level': 0,
    },
    {
        'name': 'р. Сибе - с. Алгабас',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (386,642),
        'water_level':0,
    },
    {
        'name': 'р. Жартас - с. Гагарино',
        'pre_cord': (447,657),
        'pre_instruction': None,
        'coord': (258,425),
        'water_level': 0,
    },
    {
        'name': 'р. Тайынты - с. Акбулан',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (466,600),
        'water_level': 0,
    },

    {
        'name': 'р. Киши Ульби - с. Горная Ульбинка',
        'pre_cord': (521,642),
        'pre_instruction': None,
        'coord': (451,477),
        'water_level': 0,
    },
    {
        'name': 'р. Ертис - с. Уварова',
        'pre_cord': None,
        'pre_instruction': None,
        'coord': (350,450),
        'water_level':0
    },
    {
        'name': 'р. Оба - с. Верхуба',
        'pre_cord': (547,475),
        'pre_instruction': None,
        'coord': (363,341),
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
        'pre_cord': (636,400),
        'pre_instruction': None,
        'coord': (473,303),
        'water_level':0,
    },
    {
        'name': 'р. Оба - г. Шемонаиха',
        'pre_cord':None,
        'pre_instruction':None,
        'coord':(257,450),
        'water_level':0
    },
    {
        'name': 'вдхр. Буктырма - п. Тугыл',
        'pre_cord': (285,511),
        'pre_instruction': [Keys.DOWN] *6,
        'coord': (687,761),
        'water_level':0,
    },
    {
        'name': 'р. Кандысу - с. Сарыолен',
        'pre_cord': (660,805),
        'pre_instruction': [Keys.DOWN],
        'coord': (668,811),
        'water_level':0,
    },

]

try:
    driver.get(url)

    driver.maximize_window()

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

        except Exception as e:
            print(f"Couldnt find a water level value for {body['name']}", e)

        actions.move_by_offset(-x,-y)
        


        
        
    print('Закончил выполнение скрипта')
    print('Спаршенные значения:', [body['water_level'] for body in water_bodies], len(water_bodies))
    
    if DEBUG:
        sleep(555)  # Задержка для наблюдения результата
    else:
        sleep(10)
    for body in water_bodies:
        body['date'] = date.today()


    df = pd.DataFrame(water_bodies)
    df = df[['name', 'water_level', 'date']]
    df.to_csv('hydroposts1.csv', index=False, encoding='utf-8-sig')

finally:
    driver.quit()
