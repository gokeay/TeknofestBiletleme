from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

# excelden istenilen veriyi al
yolcuBilgisiExcelKopyasi = "Gökay	Özcan	19.07.2002	38398628254	haytaa002@gmail.com	5443299229	Erkek"
gender = "erkek"

link = "https://www.turkishairlines.com/tr-int/ucak-bileti/rezervasyon/"
service = Service('C:/Users/gokay/Desktop/YAZILIM/webApp/biletlemeOtomasyon/msedgedriver.exe')
# driver = webdriver.Chrome(service=service)
driver = webdriver.Edge(service=service)
driver.get(link)

# formun olduğu siteye geldik mi
wait = WebDriverWait(driver, 300)
url_condition = EC.url_contains("yolcu-bilgileri")
wait.until(url_condition)

# script = generate_script(yolcuBilgisiExcelKopyasi)

# formu otomatik doldur
wait = WebDriverWait(driver, 300)
formKutulari = wait.until(EC.presence_of_element_located((By.ID, "firstname_0")))
wait.until(formKutulari)
# script = 'document.getElementById("firstname_0").value = "Gökay"; document.getElementById("surname_0").value = "Özcan"; document.getElementById("birthdate_0").value = "19/07/2002";'
# script = 'document.querySelector("#passengerTitleId_0 > div:nth-child(1) > label").click(); document.querySelector("#firstname_0").value = "Gökay"; document.querySelector("#surname_0").value = "Özcan"; document.querySelector("#birthdate_0").value = "19/07/2002"; document.querySelector("#passengerInfoValidationContextId_0 > div:nth-child(3) > div.col-12.col-md-12.col-lg-2.col-xl-2.mb-10-mbl.mb-10 > div > div > fieldset > label").click(); document.querySelector("#identity_0").value = "38398628254"; document.querySelector("#email").value = "ozcan301gokay@gmail.com"; document.querySelector("#regionCodes").value = "TR_90"; document.querySelector("#phonenumber").value = "5443299229";'
# driver.execute_script(script)

# Radio Buttons
male_radio_button = driver.find_element(By.ID, "MR")
female_radio_button = driver.find_element(By.ID, "MS")

# Checkbox seçimi
checkbox = driver.find_element(By.ID, "tc1_0")

# Buttons
countryCodeButton = driver.find_element(By.XPATH, ("/html/body/div[2]/div/div[1]/section/div[1]/form/div/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div/div/button"))

# Text Inputs
first_name_input = driver.find_element(By.ID, "firstname_0")
last_name_input = driver.find_element(By.ID, "surname_0")
birthdate_input = driver.find_element(By.ID, "birthdate_0")
email = driver.find_element(By.ID, "email")

checkbox.click()
male_radio_button.click() if gender == "erkek" else female_radio_button.click()
first_name_input.send_keys("John")
last_name_input.send_keys("Doe")
birthdate_input.send_keys("01/01/1990")
email.send_keys("ozcan301gokay@gmail.com")
countryCodeButton.click()
# wait = WebDriverWait(driver, 300)
# formKutulari = wait.until(EC.presence_of_element_located((By.ID, "firstname_0")))
# wait.until(formKutulari)


# time.sleep(10)

# devam butonuna tıkla ve yolcu bilgileri sayfasından koltuk seçimi sayfasına geç
# devam_butonu = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/section/fixed-price-bar-general/div[1]/div/div[2]/div[4]/div/button")
# devam_butonu.click()
# time.sleep(1)


# devam butonuna tıkla ve sonraki sayfaya ()
wait = WebDriverWait(driver, 300)
url_condition = EC.url_contains("seat-selection")
wait.until(url_condition)

# devam butonuna tıkla ve sonraki sayfaya (ek hizmetler) geç
wait = WebDriverWait(driver, 300)
devam_butonu = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/fixed-price-bar-general/div[1]/div/div[2]/div[4]/div/button")))
devam_butonu.click()
time.sleep(1)


# devam butonuna tıkla ve sonraki sayfaya (ödeme) geç
wait = WebDriverWait(driver, 300)
devam_butonu = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/fixed-price-bar-general/div[1]/div/div[2]/div[4]/div/button")))
devam_butonu.click()
time.sleep(5)


# sayfayı kart seçimi için aşağı kaydır
wait = WebDriverWait(driver, 300)
url_condition = EC.url_contains("odeme")
wait.until(url_condition)
driver.execute_script("window.scrollBy(0, 300);")  # 500 piksel aşağı kaydırır
time.sleep(1)


# kredi kartı ödemesini seç
krediKartiButton = driver.find_element(By.ID, "creditCard")
krediKartiButton.click()
time.sleep(2)


# kart bilgilerini doldur
cardNumber = driver.find_element(By.ID, "cardNumber")
cardNumber.send_keys("123570137001529")
tarih_ay = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/section[2]/div/div[2]/div[8]/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div/button")
tarih_ay.click()
time.sleep(1)
ayBilgisi = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/section[2]/div/div[2]/div[8]/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div/ul/li[13]")
ayBilgisi.click()
tarih_yil = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/section[2]/div/div[2]/div[8]/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/button")
tarih_yil.click()
time.sleep(1)
yilBilgisi = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/section[2]/div/div[2]/div[8]/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/ul/li[2]")
yilBilgisi.click()


# sayfayı adres bilgileri için aşağı kaydır
driver.execute_script("window.scrollBy(0, 500);")  # 500 piksel aşağı kaydırır
time.sleep(1)


# adres bilgilerini doldur
yasanilanBolge = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/section[2]/div/div[2]/div[8]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/button")
yasanilanBolge.click()
time.sleep(1)
ulkeTurkiye = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/section[2]/div/div[2]/div[8]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/div/ul/li[2]")
ulkeTurkiye.click()
sehir = driver.find_element(By.ID, "city")
sehir.send_keys("istanbul")
adress = driver.find_element(By.ID, "addressLine1")
adress.send_keys("istanbul")


# bitir butonuna tıkla ve sonraki sayfaya (son onay) geç
devam_butonu = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/section[2]/fixed-price-bar-payment/div[1]/div/div/div[3]/div/button")
devam_butonu.click()


# onay metni kutusunu onayla ve onayla butonuna basarak bilet alımını tamamla
# wait = WebDriverWait(driver, 300)
# onayKutusu = wait.until(EC.presence_of_element_located((By.XPATH, "onay kutusu path i")))
# onayKutusu.click()
# onaylaButonu = driver.find_element(By.XPATH, " onayla butonu path i")
# onaylaButonu.click()
# time.sleep(5)

# işlem tamamlandı sayfasına geldik mi
# wait = WebDriverWait(driver, 300)
# url_condition = EC.url_contains("teşekkürler biletiniz alındı falan filan a dair bir url kelimesi")
# wait.until(url_condition)
# time.sleep(5)

# pnr kodunu sayfadan al
# pnrKodu = driver.find_element(By.XPATH, "pnr kodu path i")
# pnrKodu = pnrKodu.text

# # pnr kodunu excele kaydet
# open("pnrKodu.txt", "w").write(pnrKodu)



# # koltuk secimi sayfasına geldik mi
# wait = WebDriverWait(driver, 300)
# url_condition = EC.url_contains("seat-selection")
# wait.until(url_condition)




# .clear(



def generate_script(yolcu_bilgisi_excel_kopyasi):

    parts = yolcu_bilgisi_excel_kopyasi.split('\t')
    gender = parts[6].lower()
    birth_date = parts[2]
    birth_date_parts = birth_date.split(".")
    day = (birth_date_parts[0].rjust(2, '0'))
    month = (birth_date_parts[1].rjust(2, '0'))

    button_id = "MR" if gender == "erkek" else "MS"
    formatted_birth_date = day + "/" + month + "/" + birth_date_parts[2]
    phone_number = parts[5]

    # Kodu görüntüle
    generated_script = f"""
    var tiklanacakDugme = document.querySelector('#{button_id}');
    if (tiklanacakDugme) {{
        tiklanacakDugme.click();
    }} else {{
        console.log('Öğe bulunamadı.');
    }}
    document.getElementById("firstname_0").value = "{parts[0]}";
    document.getElementById("surname_0").value = "{parts[1]}";

    var tiklanacakDugme2 = document.querySelector('#tc1_0');
    if (tiklanacakDugme2) {{
        tiklanacakDugme2.click();
    }} else {{
        console.log('Öğe bulunamadı.');
    }}
    document.getElementById("identity_0").value = "{parts[3]}";
    document.getElementById("email").value = "{parts[4]}";

    var dropdown = document.querySelector('#regionCodes');
    dropdown.value = "TR_90";
    var event = new Event('change', {{ bubbles: true, cancelable: true, }});
    dropdown.dispatchEvent(event);
    document.getElementById("phonenumber").value = "{phone_number}";
    """
    # document.getElementById("birthdate_0").value = "{formatted_birth_date}";

    print(generated_script)
    return generated_script

