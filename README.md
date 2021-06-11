# Discord-QR-Token-Grabber
Discord Token Grabber via QR code

### About
A Python script that automatically generates a fake Nitro QR code that grabs the Discord token and username when scanned then sends it back to a specified Discord Webhook.

## **Setup Guide:**
You will first need to make a discord Webhook(https://www.youtube.com/watch?v=fKksxz2Gdnc) and paste you webhook in line 12

Install requirements :
```
pip3 install -r requirements.txt
```
Then if steps above were succesful after launching the python file by doing ```python Discord-QR```, it will then create a fake discord nitro QR code in the same directory. Copy that image and send it to a friend. Once they scan it you get there discord token sent to you via the webhook.

**Requirements:**\
Python3, Windows(x64), google chrome
## Troubleshoot
1. Make sure your chromedriver.exe file is the same version as your Chrome web browser version
2. Download the latest version chromedriver.exe here: https://chromedriver.chromium.org/downloads
3. Then replace the chromedriver.exe file in the folder.
