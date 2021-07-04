# Axie project Automation

# Description: These methods will make the setup so that the bot can open the necessary websites in Google Chrome.

# Created and Developed by Joussef Abdul Salam (GitHub: programmerdoge)
# Date: 7/4/2021
# License: MIT License

from selenium import webdriver

PATH = "C:\\Program Files (x86)\\chromedriver.exe"  # PATH environment variable for Chrome webdriver


class Access:
    """
    The Access class creates a blueprint to access any website.
    - Parameter:
        -> url: The URL of the website you want to access.
    """

    def __init__(self, url=""):
        """
        Constructor method that initializes the Access object with the URL of
        the website that wants to be accessed.
        """

        self.url = url
        self.driver = webdriver.Chrome(PATH)

    def setURL(self, url):
        """
        Setter method for the url member of the Access object.
        """
        self.url = url

    def getURL(self):
        """
        Getter method to know which URL does the object currently have.
        """
        return self.url

    def enterSite(self):
        """
        Method to go to the site managed by the bot.
        """
        try:
            self.driver.get(self.url)
        except Exception:
            print("Error: Not a valid website, please check the URL.\n")
            self.driver.close()


########### Testing ##########

accessor = Access("https://www.google.com")
accessor.enterSite()

accessor2 = Access()
accessor2.setURL("whatever")
accessor2.enterSite()
