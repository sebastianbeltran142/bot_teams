# LIBRERÍAS
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import unicodedata as un
import pyautogui as pg
import time as tm
#Configuraciones varias y opcionales
now = datetime.now()
print(datetime.now(),'Gracias por ejecutar este script creado por HDTC. Puede cerrar el proceso con Ctrl + C en cualquier momento. Ver: 10.0.0')
print(datetime.now(),'Script ejecutado por el usuario')


# URL TEAMS para configurar en pestaña 1
url1 = 'https://teams.microsoft.com/_#/conversations/'
print(datetime.now(), 'Abriendo página web', url1)
broswer = webdriver.FirefoxOptions()

broswer.add_argument('--Private')
print(datetime.now(), 'Preparando navegador')
driver = webdriver.Firefox(executable_path='C:\\project\\python\\teamsbot\\driver\\geckodriver.exe', options=broswer)
driver.maximize_window()

def inicio_sesion_teams():
    driver.get(url1)
    print(datetime.now(), 'Cargando página web. Un momento, por favor...')
    complete_cargue = '//*[@id="i0116"]'
    element = WebDriverWait(driver,10).until(
        ec.presence_of_element_located((By.XPATH,complete_cargue))
    )
    print(datetime.now(), 'Navegador web iniciada')
    return element
inicio_sesion_teams() 
print(datetime.now(), 'Página web', url1, 'cargada correctamente')

# Autenticación sesión por el usuario
def test_teams_start():
    tm.sleep(1)

    driver.find_element(By.NAME,"loginfmt").send_keys("14ct222227@educacioncpe.gov.co")
    driver.find_element(By.ID, "idSIButton9").click()
    print(datetime.now(),"Proceso ejecutado user")
    tm.sleep(1.5)

    driver.find_element(By.NAME,"passwd").send_keys("Educacion2015")
    driver.find_element(By.ID,"idSIButton9").click()
    tm.sleep(1.5)

    driver.find_element(By.ID,"idBtn_Back").click()
    print(datetime.now(),"Proceso ejecutado pass")
    print(datetime.now(),"Inicio de sesión terminada, procedimiento para resetear cuenta")
test_teams_start()

def configure_sesion():
    element = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "#control-input"))
    )
    return element
configure_sesion()

def prepare_sesion():
    driver.find_element(By.CSS_SELECTOR,"#personDropdown").click()
    tm.sleep(1)
    driver.find_element(By.CLASS_NAME,"ts-sym.profile-action.profile-set-presence-button").click()
    tm.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"body > div.popover.minwidth-md.maxwidth-md.popover.app-default-menu.settings-presence-popover.am-fade.bottom > ul > li:nth-child(10) > button").click()
    tm.sleep(1)

    driver.find_element(By.ID,"app-bar-86fcd49b-61a2-4701-b771-54728cd291fb").click()
    print(datetime.now(),"Proceso de preparación de la cuenta terminada")
    tm.sleep(15)
    print('Sistema listo para el envío de mensajes. Se debe tener en cuenta el rendimiento del equipo vis conectividad')

prepare_sesion()


def chat(msg_nvo_finish: str):
    for a in range(100000000):
        chat_nvo = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/left-rail/div/div/left-rail-chat-tabs/div/div/div[1]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[1]/a/span[4]/div').text
        user = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/left-rail/div/div/left-rail-chat-tabs/div/div/div[1]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[1]/a/span[2]/span').text
        msg_nvo = chat_nvo
        trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
        msg_nvo = un.normalize('NFKC', un.normalize('NFKD', msg_nvo).translate(trans_tab))
        msg_nvo_finish = msg_nvo.lower()

        # Contiene mensajes
        if msg_nvo_finish.__contains__('hola'):
            try:
                print(datetime.now(),'⚡⚡⚡ usuario "',user,'" dice:...', msg_nvo_finish)
                driver.find_element(By.CLASS_NAME, 'cle-item').click()
                pg.typewrite('(smilerobot) Estimado(a) usuario(a), bienvenido al chat de la mesa de servicios. Le saluda Dani Bot de HDTC. En un momento, uno de nuestros agentes lo contactara con gusto')
                # pg.hotkey('ctrl','v')
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Mensaje enviado exitoso.')
                tm.sleep(2)
            except:
                pass
        elif msg_nvo_finish.__contains__('gracias'):
            try:
                print(datetime.now(),'⚡⚡⚡ usuario "',user,'" dice:...', msg_nvo_finish)
                driver.find_element(By.CLASS_NAME, 'cle-item').click()
                pg.typewrite('(handshake) A usted por contactarnos. Recuerda que le escribio Dani Bot de HDTC y que tenga un excelente dia')
                # pg.hotkey('ctrl','v')
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Mensaje enviado exitoso.')
                tm.sleep(2)
            except:
                pass
        tm.sleep(1)
    
print(datetime.now(),"⚡⚡⚡ Estoy escuchando mensajes")

chat(str)


print(now, "Cierre inesperado del servicio, favor reiniciar o solicitar soporte técnico. Grupo HD TEC-CO SAS.")

driver.quit()