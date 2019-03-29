from BasePackage.Base import Base

class Wailts(Base):

    def waitA(self, T):
        self.AndroidDriver.implicitly_wait(T)

    def waitC(self,T):
        pass

    def waiForElement(self,E,PT):
        pass

    def waitForPage(self,T,E):
        pass