# Bots

Make web scrapers and bots powered by Selenium without all of the boilerplate.

## Getting started

1. `pip install litebot`
2. Download [Chromedriver](https://chromedriver.chromium.org/downloads) (the version corresponding to your version of Chrome) and unzip it.
3. Move it into to your `PATH` so it can be found by your OS. E.g. `/usr/local/bin` (Mac/Linux) or somewhere else (Windows... look it up)

```
from litebot.bot import Bot

bot = Bot()
bot.driver.get('https://www.google.com')
bot.click_btn('sign up')
bot.download_file('https://www.example.com/image.jpg', 'images/downloaded_img.jpg')
bot.scroll(x=100, y=200)
```
