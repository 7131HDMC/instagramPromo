from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import time
import random

# Fiz algumas modificações


class InstagramBot:
    def __init__(self, username, password, photo_url, max_comments, comments_templates):
        self.username = username
        self.password = password        
        self.max_comments = max_comments
        self.photo_url = photo_url
        self.comments_templates = comments_templates
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        options = Options()
        # options.headless = True
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"./geckodriver"
            ,options=options
        )
        """ # Coloque o caminho para o seu geckodriver aqui, lembrando que você precisa instalar o firefox e geckodriver na versão mais atual """
        # Link download do geckodriver: https://github.com/mozilla/geckodriver/releases
        # Link download Firefox https://www.mozilla.org/pt-BR/firefox/new/

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/?next=%2Fp%2FCosCnN-upZ6%2F&source=desktop_nav")
        time.sleep(3)
        # login_button = driver.find_element(By.XPATH,
        #     "//a[@href='/accounts/login/?source=auth_switcher']"
        # )
        # login_button.click()
        time.sleep(3)
        user_element = driver.find_element(By.XPATH,
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element(By.XPATH,
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)

        # msg=[
        #         "🔥🔥",
        #         "Sinistro paizão!🔥",
        #         "Bora pra cima🔥",
        #         "👏🏽👏🏽👏🏽👏🏽",
        #         "😮❤️❤️🔥🙌🏾",
        #         "👏🔥🔥 brabo irmão",
        #         "Um dia agente chega la",
        #         "🔥🔥🔥🔥🔥🔥",
        #         # "e esse ano, vai passar o carna onde?",
        #         "Voa!!!"
        #     ]
        msg = self.comments_templates.split(";")

        self.comentarios_em_foto(
            photo=self.photo_url,#"https://www.instagram.com/p/Cp-YmviueNd/",
            comments=msg,
            amount=self.max_comments
        )
        # self.comente_nas_fotos_com_a_hashtag(
        #     photo="https://www.instagram.com/p/CosCnN-upZ6/?igshid=MDJmNzVkMjY%3D"
        # )  # Altere aqui para a hashtag que você deseja usar.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        # print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def comentarios_em_foto(self, photo, comments,amount=500):
        links_de_posts = []
        driver = self.driver
        
        driver.get(photo)
        time.sleep(5)
        
# search_input = lambda: 
        # coment_icon = driver.find_element(By.XPATH, '//*[@id="mount_0_0_gr"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[2]/button')
        # coment_icon.click()



        time.sleep(2)
        count = 2
        c = 0
        for i in range(amount):  
            print(i)  
            c+=1
            if c==11:
                c=0

                # comente_input = driver.find_element(By.CSS_SELECTOR,
                #     'textarea.x1i0vuye'
                # )
                # comente_input.clear()

                # comente_input.send_keys(
                #     random.choice(comments)
                # )
                # block = driver.find_element(By.XPATH,
                # '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]'
                # )
                # if block.size() > 0:
                #     block.click()
                
                # enter.click()
                time.sleep(45)
            try:
                

                comente_input = driver.find_element(By.CSS_SELECTOR,
                    'textarea.x1i0vuye'
                )
                comente_input.clear()

                comente_input.send_keys(
                    random.choice(comments)
                )

                time.sleep(count)

                enter = driver.find_element(By.CSS_SELECTOR,"._akhn > div:nth-child(3)")
                time.sleep(count)
                enter.click()

            except Exception as ex:
                print("wiat 1h to try again!")
                print(ex)
                count+=1
                if count>=1200:
                    count=300
                # time.sleep(1600)
                # enter =             driver.find_element(By.XPATH,
                #     '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/div/div[2]/div'
                # )
                time.sleep(3000)

                # enter.click()

            time.sleep(15)



    def comente_nas_fotos_com_a_hashtag(self, hashtag=False, photo=False):
        links_de_posts = []
        driver = self.driver
        if hashtag:
            driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        else:
            driver.get(photo)

        time.sleep(5)
        # for i in range(
        #     1, 3
        # ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
        #     driver.execute_script(
        #         "window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(3)

        
        # hrefs = driver.find_elements_by_tag_name("a")
        # pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        # print(hashtag + " fotos: " + str(len(pic_hrefs)))
        # for link in pic_hrefs:
        #     try:
        #         if link.index("/p/") != -1:
        #             links_de_posts.append(link)
        #     except:
        #         pass

        # for pic_href in links_de_posts:
        #     driver.get(pic_href)
        #     driver.execute_script(
        #         "window.scrollTo(0, document.body.scrollHeight);")
        #     try:
        #         comments = [
        #             "Olha que foto massa!",
        #             "Olha que foto massa!",
        #             "Olha que foto massa!",
        #             "Olha que foto massa!",
        #         ]  # Remova esses comentários e insira os seus comentários aqui
        #         driver.find_element_by_class_name("Ypffh").click()
        #         comment_input_box = driver.find_element_by_class_name("Ypffh")
        #         time.sleep(random.randint(2, 5))
        #         self.type_like_a_person(
        #             random.choice(comments), comment_input_box)
        #         time.sleep(random.randint(3, 5))
        #         driver.find_element_by_xpath(
        #             "//button[contains(text(), 'Publicar')]"
        #         ).click()
        #         time.sleep(random.randint(3, 5))
        #     except Exception as e:
        #         print(e)
        #         time.sleep(5)


# Entre com o usuário e senha aqui
# hd = InstagramBot("haridasafiuza@gmail.com", "#Hari9180")
# hd.login()
form={'email': 'haridasafiuza@gmail.com', 'password': '#Hari9180', 'post': 'https://www.instagram.com/p/B6ZQn8sAVwhMkylGu6ATMfq5rNuPZTkKHRQmQ00/', 'comments_template': 'Linda;Linda😮😮😮', 'max_coments': 3}
insta = InstagramBot(
form["email"],
form["password"],
form["post"],
form["max_coments"],
form["comments_template"],
)
insta.login()