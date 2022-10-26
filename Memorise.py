import time
from selenium import webdriver
import threading
import os
from maskpass import askpass

input("YOU MUST COMPLY WITH THE FOLLOWING TO RUN THE BOT")
input("\n\nRules and safety features for using memorise bot - by Sachit Sharma v1.0\nRules:\n\n1) Do not share ANY CODE WITH ANYBODY FOR ANY REASON unless officially allowed to.\n2) DO NOT modify or delete the bot software.\n3) Do not use the bot for long periods of time!\n4) Make no attempts at manipulating the .exe file as you will be unsucessfull.\n5) Do not share the knowledge about this bot in any capacity, This includes functional details, how good the bot is, how it may operate and aything in the like.\n6) Do not brag about your points using this bot.\n7) Only use this bot on a different account from your main as otherwise it's considered cheating.\n8) Do not tell anyone you have the bot.\n\n\nSafety features:\n\n1) The bot has no way to send me any information.\n2) The bot is going to be ran on a new account so any harm would be minimal anyway.\n3) I know how the bot runs and all the details so I can see if someone has been using the bot for a long time.\n4) I have created a website and depending on what is on the website (which I can control) the bot runs or it doesn't.\n5) I have fine control over everythong including what accounts can use the bot, which courses you can run, if you have access to threads and version control\n6) Point 5 essentially means if you break a rule I can revoke your access from my bot using a remote website.\n\nPress enter to continue.")
os.system("cls")

name = "noskallontral"
debugging = False
version = "2.2"

def setup():
    input("We had an issue opening the chrome webdriver so you need to do the following:\n\n\n")
    print("1) You need to have / download chrome. To do so search 'chrome' on your current browser and click the correct link and download it\n2) Look at the top right and press the 3 dots.\n3) Hover over help then press about chrome.\n4) Now find the version number and either remember it or write it down somewhere as we will need it shortly.\n5) Now open https://chromedriver.chromium.org/downloads in a new tab and press the version you have and download it for your os (operating system).\n6) Open file explorer and open your downloads folder and then right-click the chromedriver file and the press extract all...\n7) In the text box type in C:\Program Files (x86) and then press extract.\nRun the program and it should now work, if it doesn't talk to me.\n\n")

def show_v_data(v, *args, inp = False):
    print(f"Version '{v}': ")
    if inp: 
        for i, arg in enumerate(args):
            print(f"{i+1}) {arg}")
        input("")
    else:
        for i, arg in enumerate(args):
            print(f"{i+1}) {arg}")
        print("\n") 

def login(driver, name, password, debugging):
    driver.get("https://app.memrise.com/signin")
    search = driver.find_element("id","username")
    search.send_keys(name)
    search = driver.find_element("id","password")
    search.send_keys(password)
    search = driver.find_element("xpath", '//button[@data-testid = "signinFormSubmit"]')
    search.click()
    time.sleep(5)
    if debugging: print("Logged in (hopefully)...")

def open_review(driver, link):
    driver.get(link)
    time.sleep(4)

def get_ques(driver): 
    try: return driver.find_element("xpath", '//h2').text
    except: return -1

def ans_ques(driver, debugging, que, ans, current_ques):
    try:
        t = []
        try: search = driver.find_elements("xpath", '//div[@class = "sc-dkrFOg eHBPun sc-9xkdxd-1 ikXQbJ"]')
        except: return -1
        for s in search:
            try:t.append(s.text[2:].lower())
            except Exception: t = ["" for _ in range(4)]         
        try: ind = que.index(current_ques)
        except: que.append(current_ques)
        for i in range(4):
            if ans[ind].lower() == t[i].lower():
                search = search[i]
                search.click() 
    except Exception: 
        if debugging: print(que)

def do_quiz(driver, debugging, que, ans, link):
    while True:
        open_review(driver, link)
        while True:
            current_ques = get_ques(driver)
            try:
                if current_ques == -1: break
                elif current_ques != prev_ques: ans_ques(driver, debugging, que, ans, current_ques)
            except Exception: ans_ques(driver, debugging, que, ans, current_ques)
            prev_ques = current_ques

def get_course():
    courses = [
    [['music', 'maths', 'technology', 'drama', 'RE', 'My favourite day is Monday/', 'Tuesday.', 'On Mondays/Tuesdays I study...', 'Why?', 'in the morning', 'we study', 'I don’t study', 'in the afternoon', 'Because...', 'Opinions', 'Do you like art?', 'Yes, I like art (a lot).', 'Do you like science?', 'science', 'art', 'I study...', 'PE', 'What is your favourite day?', 'No, I don’t like art (at all).', 'What do you study?', 'geography', 'Spanish', 'French', 'ICT', 'history', 'English'], ["música", "matemáticas", "tecnología", "teatro", "religion", "Mi día favorito es el lunes/", "el martes.", "Los lunes/martes estudio...", "¿Por qué?", "por la mañana", "estudiamos", "no estudio", "por la tarde", "Porque...", "Opiniones", "¿Te gusta el dibujo?", "Sí, me gusta (mucho) el dibujo.", "¿Te gustan las ciencias?", "ciencias", "dibujo", "Estudio...", "educación física", "¿Cuál es tu día favorito?","No, no me gusta (nada) el dibujo.", "¿Qué estudias?", "geografía", "español", "francés", "informática","historia", "inglés"], "https://app.memrise.com/aprender/speed?course_id=2190903?recommendation_id=41918db8-977c-4108-a3c1-05f53d8afcba&key=ba712366-dad0-406d-8b6a-182157fb7e43"],
    [['When is your birthday?', 'But', 'My birthday is the ... of ...', 'A fish', 'A guinea pig', 'No (tengo) I don’t have', 'Very', 'Also/Aswell', 'My', 'Your', 'He/She has', 'A bit', 'Do you have any pets?', 'And', 'I am ... years old', 'A horse', 'A rabbit', 'Quite', 'A cat', 'A dog'],["¿Cuándo es tu cumpleaños?","pero","Mi cumpleaños es el ... de ...","Un pez","Una cobaya","no","muy","también","Mi / mis","Tu / tus","Tiene","Un poco","¿Tienes mascotas?","y","Tengo... años","Un caballo","Un conejo","bastante","Un gato","Un perro"],"https://app.memrise.com/aprender/speed?course_id=6082030?recommendation_id=910dfce9-50f3-42c1-aeda-07cc3a633050"],
    [['Drama', 'RE', 'Technology', 'I don’t study', 'In the morning', 'Why?', 'In the afternoon', 'On Mondays/Tuesdays', 'What do you study?', 'Spanish', 'Science', 'Art', 'PE', 'French', 'ICT', 'English', 'History', 'Geography', 'Maths', 'Music'],["El teatro","La religión","La tecnología","No estudio","Por la mañana","¿Por qué?","Por la tarde","Los lunes/martes ...","¿Qué estudias?","El español","Las ciencias","El dibujo","La educación física","El francés","La Informática","El inglés","La historia","La geografía","Las matemáticas","La música"],"https://app.memrise.com/aprender/speed?course_id=6139018?recommendation_id=0efd635d-5eff-4f14-a22a-a4b6bfd3762f"],
    [['What is he/she/it like?', 'I live in ...', 'Where do you live?', 'How old are you?', 'January', 'Three', 'What are they like?', 'Two', 'One', 'Four', 'Five', 'Eight', 'Six', 'Seven', 'Nine', 'Ten', 'Yellow', 'Blue', 'Orange', 'Brown'],["¿Cómo es?","Vivo en ...","¿Dónde vives?","¿Cuántos años tienes?","enero","Tres","¿Cómo son?","Dos","Uno","Cuatro","Cinco","Ocho","Seis","Siete","Nueve","Diez","Amarillo","Azul","Naranja","Marrón"],"https://app.memrise.com/aprender/speed?course_id=6098500?recommendation_id=d2f2c0d3-68ed-4681-872c-c74b6777095f"],
    [['You are', 'I am', 'Fun/Funny', 'Fantastic', 'Generous', 'Clever', 'Great', 'Nice', 'Cool', 'Sincere', 'Silly/Stupid', 'You have', 'I have', 'A sister', 'Calm', 'A brother', 'A step/half brother', 'A step/half sister', 'I am an only child (girl)', 'I am an only child (boy)'],["Eres","Soy","Divertido/a","Fenomenal","Generoso/a","Listo/a","Genial","Simpático/a","Guay","Sincero/a","Tonto/a","Tienes","Tengo","Una hermana","Tranquilo/a","Un hermano","Un hermanastro","Una hermanastra","Soy hija única","Soy hijo único"],"https://app.memrise.com/aprender/speed?course_id=5814212?recommendation_id=488bb45e-9b0b-4305-96f4-65d17181bc87"],
    [['Spain', 'I visited monuments', 'Scotland', 'I bought a t-shirt', 'I took photos', 'I danced', 'I rode a bike', 'I sent a text message', 'I relaxed on the beach', 'I swam in the sea', 'aeroplane', 'Last year', 'I sunbathed', 'What did you do on your summer holidays?','We went to', 'Car', 'Where did you go?', 'I went to', 'Coach', 'France'],['España','Visité monumentos','Escocia','Compré una camiseta','Saqué fotos','Bailé','Monté en bici(cleta)','Mandé SMS','Descansé en la playa','Nadé en el mar','avión','El año pasado','Tomé el sol','¿Qué hiciste en tus vacaciones de verano?', "Fuimos a ...", "coche", "¿Adónde fuiste?", "Fui a ...", "autocar", "Francia"],"https://app.memrise.com/aprender/speed?course_id=6062979?recommendation_id=0a168b63-cd1a-4640-b848-2c20a5d6f7fd&key=c5347d15-f1db-4cc5-bb1d-89443e73cff9"],
    [['I ate paella', 'I drank a lemonade', 'I met a cute boy/girl', 'I went out with my brother/sister', 'I wrote texts', 'I saw a castle', 'Then', 'Later', 'How annoying!', 'How tasty/delicious!', 'Afterwards', 'In the morning', 'Another day', 'On the first day', 'In the afternoon', 'What luck/How lucky!', 'On the last day', 'What a shame/pity!', 'I didn’t go on holiday', 'Who did you go with?'],
    ["Comí paella", "Bebí una limonada", "guapo/guapa", "salí con mi hermano/a", "Escribí SMS", "Vi un castillo", "Luego", "Más tarde", "¡Qué rollo!", "¡Qué rico!", "Después", "por la mañana", "otro día", "el primer día", "por la tarde", "¡Qué suerte!", "el último día", "¡Qué lástima!", "no fui de vacaciones", "¿Con quién fuiste?"],"https://app.memrise.com/aprender/speed?course_id=6075549?recommendation_id=6fb2f87e-79ec-4ba8-a617-40b1eb85527c"]]
    
    while True:
        try: 
            c_num = int(input("Enter course num:\n1) Viva 1 module 3\n2) Parkside Year 7 Module 1 Vocab Test 2\n3) Parkside Y7 Module 3 Vocab' Test 1\n4) Parkside Y7 Module 1 Vocab' Test 3\n5) Parkside Year 7 Vocab Test 1 2020\n6) Parkside Y8 Vocabulary Test 1\n7) Parkside Y8 Module 1 Vocab' Test 2\nCourse number: ")) - 1
            c_inf = courses[c_num] 
            que = c_inf[0]
            ans = c_inf[1]
            link = c_inf[2]
            break
        except ValueError: print("\n\nEnter valid input!\n\n")
        except IndexError: print("\n\nEnter valid input!\n\n")
    return que, ans, link, c_num

def validify(PATH, c_num):
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    driver.get("https://mem-bot.netlify.app/limiter.html")
    time.sleep(4)
    search = driver.find_elements("xpath","//p1")
    names = []
    courses_allowed = []
    for element in search:
        z, y, change_threads_allowed = element.text.split(" - ")
        names.append(z)
        courses_allowed.append(y)
    for i, n in enumerate(names):
        if n == name:
            courses_allowed = courses_allowed[i].split(", ")
            change_threads_allowed = True if change_threads_allowed == "True" else False
            search = driver.find_element("xpath", "//p2").text   
            versions_allowed = search.split(", ") 
            driver.close()
            for v in versions_allowed: 
                if v == version:
                    for course in courses_allowed:
                        if int(course) == int(c_num)+1: return True, change_threads_allowed
                    else: print("Error -69\nCourse either DNE or no access to course.")
                    return False, change_threads_allowed
            else: print("Error 69.69\nVersion unsupported.")
            return False, change_threads_allowed

def get_input(change_threads_allowed):
    thread_num = 1
    os.system("cls")
    password = askpass(prompt="Enter your password (Dont worry I have no way to communicate with anyone or do anything bad) ")
    if change_threads_allowed: thread_num = int(input("How many threads do you want? "))
    return thread_num, password

def main():
    que, ans, link, c_num = get_course()
    run, change_threads_allowed = validify(PATH, c_num)
    if run:
        thread_num, password = get_input(change_threads_allowed)
        if thread_num == 0: return 0
        threads = []
        drivers = []
        for i in range(thread_num):
            drivers.append(webdriver.Chrome(PATH))
            threads.append(threading.Thread(target=do_quiz, args=(drivers[i], debugging, que, ans, link)))
            login(drivers[i], name, password, debugging)
            threads[i].start()

try: 
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.close()
    run = True
except Exception: 
    os.system("cls") 
    setup()
try: 
    if run:
        os.system("cls")
        print("CHANGE LOG\n﹉﹉﹉﹉﹉\n")
        show_v_data("Oh Pea Update / 2.0", "Added Threading (being able to run the same course consecultively.")
        show_v_data("Chalky Kukiz / 2.1", "Better code structure. (don't worry about it)", "The password is hidden when you enter it.", "The changelog menu has been added.")
        show_v_data("Mapel Sirap / 2.2","Changed the website domain and how the website looks significantly.", "Added a 'setup.'","Added a new course.","Gave all the Versions awesome names",inp = True)
        os.system("cls")
        main()
except: pass