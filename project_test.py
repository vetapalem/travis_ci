from selenium import webdriver as wb
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import action_chains as ac


from webdriver_manager.chrome import ChromeDriverManager as ch


import unittest as ut,time as tt


class test_yhu(ut.TestCase):
    

    def setUp(self) -> None:
             
        self.dri= wb.Chrome(service=Service(executable_path=ch().install()))


    def test_dr(self):
        self.dri.get(url=r'https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_draganddrop')
        self.dri.maximize_window()
        tt.sleep(5)


    def  tearDown(self) -> None:
             
        self.dri.quit()




if __name__ == "__main__":
    ut.main(verbosity=2)