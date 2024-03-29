from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from pathlib import Path
print('Hello world!')
# Selenium - Automatizando tarefas no navegador


# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
print(ROOT_FOLDER)

# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'aula315' / 'drivers' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    # Dorme por 10 segundos
    sleep(10)
