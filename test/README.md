# Tests

## Define variables
export usuario=user1
export senha=12345678
export link='https://global.hoymiles.com/platform/login'

## Download chromedrive
wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

### old version
wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip

## Unzip to path
unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
