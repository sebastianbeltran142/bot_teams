# Librerías para tener en cuenta
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import unicodedata as un
import pyautogui as pg
import time as tm

#Configuraciones varias y opcionales
now = datetime.now()
print(datetime.now(),'Gracias por ejecutar este script creado por HDTC. Puede cerrar el proceso con Ctrl + C en cualquier momento. Ver: 1.1.0')
print(datetime.now(),'Script ejecutado por el usuario')


# URL TEAMS para configurar en pestaña 1
url1 = 'https://teams.microsoft.com/_#/conversations/'
print(datetime.now(), 'Abriendo página web', url1)
broswer = webdriver.FirefoxOptions()

broswer.add_argument('--Private')
print(datetime.now(), 'Preparando navegador')
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=broswer)
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
    for a in range(9999999999):
        chat_nvo = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/left-rail/div/div/left-rail-chat-tabs/div/div/div[1]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[1]/a/span[4]/div').text
        user = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/left-rail/div/div/left-rail-chat-tabs/div/div/div[1]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[1]/a/span[2]/span').text
        msg_nvo = chat_nvo
        trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
        msg_nvo = un.normalize('NFKC', un.normalize('NFKD', msg_nvo).translate(trans_tab))
        msg_nvo_finish = msg_nvo.lower()

        # Cajón de mensajería instantánea
        if msg_nvo_finish.__contains__('hola'):
            try:
                print(datetime.now(),'⚡⚡⚡ usuario "',user,'" dice:...', msg_nvo_finish)
                driver.find_element(By.CLASS_NAME, 'cle-item').click()
                pg.typewrite('(hi) Bienvenido al soporte de la mesa de servicios de la empresa, le escribe Dani (smilerobot). Estas son las opciones *super flash* que me fueron configurados:')
                tm.sleep(2.2)
                pg.hotkey('enter')
                pg.typewrite('(keycapone)(keycapasterisk) Clave wifi invitados de la semana.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycaptwo)(keycapasterisk) Cambiar clave del correo Outlook.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycapthree)(keycapasterisk) Desbloquear cuenta de integratic.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycapfour)(keycapasterisk) Hablar con un representante de la mesa de servicios.')
                tm.sleep(3)
                pg.hotkey('enter')
                tm.sleep(1)
                pg.typewrite('(keyboard) Digite cualquiera de las opciones disponibles incluyendo el asterisco.')
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Mensaje enviado exitoso.')
                tm.sleep(2)
            except:
                pass

        elif msg_nvo_finish.__contains__('buenos'):
            try:
                print(datetime.now(),'⚡⚡⚡ usuario "',user,'" dice:...', msg_nvo_finish)
                driver.find_element(By.CLASS_NAME, 'cle-item').click()
                pg.typewrite('(hi) Bienvenido al soporte de la mesa de servicios de la empresa, le escribe Dani (smilerobot). Estas son las opciones *super flash* que me fueron configurados:')
                tm.sleep(2.2)
                pg.hotkey('enter')
                pg.typewrite('(keycapone)(keycapasterisk) Clave wifi invitados de la semana.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycaptwo)(keycapasterisk) Cambiar clave del correo Outlook.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycapthree)(keycapasterisk) Desbloquear cuenta de integratic.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycapfour)(keycapasterisk) Hablar con un representante de la mesa de servicios.')
                tm.sleep(3)
                pg.hotkey('enter')
                tm.sleep(1)
                pg.typewrite('(keyboard) Seleccione cualquiera de las opciones disponibles.')
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Mensaje enviado exitoso.')
                tm.sleep(2)
            except:
                pass

        elif msg_nvo_finish.__contains__('buenas'):
            try:
                print(datetime.now(),'⚡⚡⚡ usuario "',user,'" dice:...', msg_nvo_finish)
                driver.find_element(By.CLASS_NAME, 'cle-item').click()
                pg.typewrite('(hi) Bienvenido al soporte de la mesa de servicios de la empresa, le escribe Dani (smilerobot). Estas son las opciones *super flash* que me fueron configurados:')
                tm.sleep(2.2)
                pg.hotkey('enter')
                pg.typewrite('(keycapone)(keycapasterisk) Clave wifi invitados de la semana.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycaptwo)(keycapasterisk) Cambiar clave del correo Outlook.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycapthree)(keycapasterisk) Desbloquear cuenta de integratic.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycapfour)(keycapasterisk) Hablar con un representante de la mesa de servicios.')
                tm.sleep(3)
                pg.hotkey('enter')
                tm.sleep(1)
                pg.typewrite('(keyboard) Seleccione cualquiera de las opciones disponibles.')
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Mensaje enviado exitoso.')
                tm.sleep(2)
            except:
                pass

        if msg_nvo_finish.__contains__('0*'):
            try:
                print(datetime.now(),'⚡⚡⚡ usuario "',user,'" selecciona la opción:...', msg_nvo_finish)
                driver.find_element(By.CLASS_NAME, 'cle-item').click()
                pg.typewrite(';) De acuerdo, se ha enviado de nuevo a las opciones iniciales. Estas son las opciones *super flash* que me fueron configurados:')
                tm.sleep(2.2)
                pg.hotkey('enter')
                pg.typewrite('(keycapone)(keycapasterisk) Clave wifi invitados de la semana.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycaptwo)(keycapasterisk) Cambiar clave del correo Outlook.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycapthree)(keycapasterisk) Desbloquear cuenta de integratic.')
                pg.hotkey('shift','enter')
                pg.typewrite('(keycapfour)(keycapasterisk) Hablar con un representante de la mesa de servicios.')
                tm.sleep(3)
                pg.hotkey('enter')
                tm.sleep(1)
                pg.typewrite('(keyboard) Digite cualquiera de las opciones disponibles incluyendo el asterisco.')
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Mensaje enviado exitoso.')
                tm.sleep(2)
            except:
                pass

        elif msg_nvo_finish.__contains__('1*'):
            try:
                print(datetime.now(),'⚡⚡⚡ usuario "',user,'" selecciona la opción:...', msg_nvo_finish)
                driver.find_element(By.CLASS_NAME, 'cle-item').click()
                pg.typewrite(';) De acuerdo, la clave de wifi de la semana es pepitoperez*, espero funcione')
                tm.sleep(1)
                pg.hotkey('enter')
                pg.typewrite(':) Si ha sido satisfactoria la respuesta entregada, puede agradecerme en cualquier momento, de lo contrario, digite (keycapzero)(keycapasterisk) para volver al menu principal, o (keycapfour)(keycapasterisk) para hablar con un representante de la mesa de servicios.')
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Mensaje enviado exitoso.')
                tm.sleep(2)
            except:
                pass

        elif msg_nvo_finish.__contains__('2*'):
            try:
                print(datetime.now(),'⚡⚡⚡ usuario "',user,'" selecciona la opción:...', msg_nvo_finish)
                driver.find_element(By.CLASS_NAME, 'cle-item').click()
                pg.typewrite(';) De acuerdo, para cambiar la clave de Outlook ingrese en la opción cambiar contrasena y luego cambia la clave. Este video muestra el procedimiento para cambio, por favor de click en el siguiente enlace')
                tm.sleep(2)
                pg.hotkey('enter')
                tm.sleep(1)
                pg.typewrite('https://www.youtube.com/watch?v=TNTY71tWW1k&t=3s')
                pg.hotkey('enter')
                tm.sleep(1)
                pg.typewrite(':) Si ha sido satisfactoria la respuesta entregada, puede agradecerme en cualquier momento, de lo contrario, digite (keycapzero)(keycapasterisk) para volver al menu principal, o (keycapfour)(keycapasterisk) para hablar con un representante de la mesa de servicios.')
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Mensaje enviado exitoso.')
                tm.sleep(2)
            except:
                pass

        elif msg_nvo_finish.__contains__('3*'):
            try:
                print(datetime.now(),'⚡⚡⚡ usuario "',user,'" selecciona la opción:...', msg_nvo_finish)
                driver.find_element(By.CLASS_NAME, 'cle-item').click()
                pg.typewrite(';) De acuerdo, Se ha notificado al profesional para el desbloqueo de la cuenta integratic. Por favor, intente acceder dentro de dos minutos')
                tm.sleep(1.5)
                pg.hotkey('enter')
                pg.typewrite(':) Si ha sido satisfactoria la respuesta entregada, puede agradecerme en cualquier momento, de lo contrario, digite (keycapzero)(keycapasterisk) para volver al menu principal, o (keycapfour)(keycapasterisk) para hablar con un representante de la mesa de servicios.')
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Mensaje enviado exitoso.')
                tm.sleep(2)
            except:
                pass


        elif msg_nvo_finish.__contains__('4*'):
            try:
                print(datetime.now(),'⚡⚡⚡ usuario "',user,'" selecciona la opción:...', msg_nvo_finish)
                driver.find_element(By.CLASS_NAME, 'cle-item').click()
                pg.typewrite(';) De acuerdo, se ha notificado a los profesionales de la mesa de servicios, por favor, estar pendiente En caso de finalizar, por favor agradecer al finalizar el servicio con el agente que atienda su solicitud')
                tm.sleep(2.5)
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Mensaje enviado exitoso.')
                tm.sleep(2)
            except:
                pass

        elif msg_nvo_finish.__contains__('gracias'):
            try:
                print(datetime.now(),'⚡⚡⚡ usuario "',user,'" dice:...', msg_nvo_finish)
                driver.find_element(By.CLASS_NAME, 'cle-item').click()
                pg.typewrite('(thanks) Agradecemos a usted por contactarnos. Recuerda que le escribio Dani Bot (smilerobot) deseandole un excelente dia productvo. Al finalizar el servicio, por favor lo invito a realizar la encuesta del servicio y regalenos (star)(star)(star)(star)(star)')
                tm.sleep(3)
                pg.hotkey('enter')
                pg.typewrite('Chat cerrado (handshake)')
                tm.sleep(0.5)
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Mensaje enviado exitoso.')
                tm.sleep(2)
            except:
                pass

        elif msg_nvo_finish.__contains__('/bot_ver'):
            try:
                print(datetime.now(),'⚡⚡⚡ Operador "',user,'" ejecutó comando', msg_nvo_finish)
                pg.typewrite('HDTC Bot para TEAMS Ver: 1.1.0')
                tm.sleep(0.5)
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Procedimiento realizado con éxito.')
            except:
                pass

        elif msg_nvo_finish.__contains__('/help'):
            try:
                print(datetime.now(),'⚡⚡⚡ Operador "',user,'" ejecutó comando', msg_nvo_finish)
                pg.typewrite('Contacte al soporte técnico Profesional HDTC 3125596416 o escibir al correo electronico serviciohdtecco@gmail.com. Bot en actualizaciones')
                tm.sleep(1)
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Procedimiento realizado con éxito.')
            except:
                pass

        elif msg_nvo_finish.__contains__('/test'):
            try:
                print(datetime.now(),'⚡⚡⚡ Operador "',user,'" ejecutó comando', msg_nvo_finish)
                pg.typewrite('Agente bot despierto')
                tm.sleep(0.5)
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Procedimiento realizado con éxito.')
            except:
                pass

        elif msg_nvo_finish.__contains__('/reset'):
            try:
                print(datetime.now(),'⚡⚡⚡ Operador "',user,'" ejecutó comando', msg_nvo_finish)
                driver.refresh()
                tm.sleep(16)
                pg.typewrite('servicio remoto reseteada')
                tm.sleep(0.5)
                pg.hotkey('enter')
                print(datetime.now(),'⚡⚡⚡ Procedimiento realizado con éxito.')
            except:
                pass

        elif msg_nvo_finish.__contains__('/quit'):
            try:
                print(datetime.now(),'⚡⚡⚡ Operador "',user,'" ejecutó comando', msg_nvo_finish)
                pg.typewrite('Se ejecuta el apagado del bot por solicitud del operador')
                tm.sleep(0.5)
                pg.hotkey('enter')
                tm.sleep(2)
                driver.quit()
                print(datetime.now(),'⚡⚡⚡ Procedimiento realizado con éxito. Es necesario reiniciar la aplicación.')
                break
            except:
                pass

        tm.sleep(1)
    
print(datetime.now(),"⚡⚡⚡ Estoy escuchando mensajes")

chat(str)


print(now, "Cierre inesperado del servicio, favor reiniciar o solicitar soporte técnico con el profesional. Grupo HD TEC-CO SAS.")

driver.quit()
