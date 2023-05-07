
#esta version era de chatgpt3 y no me gustó



from selenium import webdriver

# Dirección de correo electrónico y contraseña de tu cuenta de WhatsApp
email = 'juanangelbasgall@hotmail.com'
password = 'asdf'

# Número de teléfono del destinatario (incluyendo el código del país)
destination_phone = '3489303607'

# Mensaje que quieres enviar
message = 'Hola, ¿cómo estás?'

# Inicializa el navegador web y abre la página de WhatsApp en línea
driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='C:\\Users\\Hans\\Desktop\\chromedriver_win32')
driver.get('https://web.whatsapp.com/')



# Espera a que se cargue la página y luego inicia sesión en tu cuenta de WhatsApp
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input').send_keys(email)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/button').click()

# Espera a que se cargue la página de chat y luego selecciona el destinatario
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="side"]/div[2]/div/label/input').send_keys(destination_phone)
driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span').click()

# Escribe el mensaje y luego envía el mensaje
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

# Cierra el navegador
driver.quit()