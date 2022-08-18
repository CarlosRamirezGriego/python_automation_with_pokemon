from .system_enums import TargetBrowser
from selenium import webdriver

class BrowserFactory:

    name: str = ""
    browser: TargetBrowser = TargetBrowser.Chrome
    driver = ""

    def __init__(self, tb: str):
        self.name = "NoName"
        self.browser = TargetBrowser
        self.SetBrowserByString(tb)


    def SetBrowserByString(self, targetBrowser: str):
        if targetBrowser.upper() == "GC":
            self.browser = TargetBrowser.Chrome
            self.driver = webdriver.Chrome()
        elif targetBrowser.upper() == "FF":
            self.browser = TargetBrowser.FF
            self.driver = webdriver.Firefox()
        else:
            self.browser = TargetBrowser.Chrome
            self.driver = webdriver.Chrome()


    def SetBrowserByEnum(self, targetBrowser: TargetBrowser):
        if targetBrowser == TargetBrowser.Chrome:
            self.browser = TargetBrowser.Chrome
            self.driver = webdriver.Chrome()
        elif targetBrowser == TargetBrowser.FF:
            self.browser = TargetBrowser.FF
            self.driver = webdriver.Firefox()
        else:
            self.browser = TargetBrowser.Chrome
            self.driver = webdriver.Chrome()

    def RefreshBrowser(self):
        self.driver.refresh()


    def MaximizeBrowser(self):
        self.driver.maximize_window()


    def NavigateToThisPage(self, url: str):
        self.driver.get(url)
