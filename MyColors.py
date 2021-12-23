import fontstyle as fs
from colorama import Fore,Style

class NormalColors():
    def meganta(self,n):
        self.n = n
        return  (f"{Style.BRIGHT+Fore.MAGENTA}{self.n}")

    def red(self,n):
        self.n = n
        return  (f"{Style.BRIGHT+Fore.RED}{self.n}")

    def yellow(self,n):
        self.n = n
        return  (f"{Style.BRIGHT+Fore.YELLOW}{self.n}")

    def green(self,n):
        self.n = n
        return  (f"{Style.BRIGHT+Fore.GREEN}{self.n}")

    def cyan(self,n):
        self.n = n
        return  (f"{Style.BRIGHT+Fore.CYAN}{self.n}")
        
    def blue(self,n):
        self.n = n
        return  (f"{Style.BRIGHT+Fore.BLUE}{self.n}")

    def reset(self,n):
        self.n = n
        return  (f"{Style.BRIGHT+Fore.RESET}{self.n}")

class NormalBoldColors():
    def redBold(self,n):
        self.n = n
        return  (f'{Style.BRIGHT+Fore.RED}{fs.apply(self.n,"bold")}')


    def megantaBold(self,n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.MAGENTA}{fs.apply(self.n,'bold')}")

    def yellowBold(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.YELLOW}{fs.apply(self.n,'bold')}")

    def greenBold(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.GREEN}{fs.apply(self.n,'bold')}")

    def cyanBold(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.CYAN}{fs.apply(self.n,'bold')}")

    def blueBold(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.BLUE}{fs.apply(self.n,'bold')}")


class lightColors():
    def LIGHT_meganta(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTMAGENTA_EX}{self.n}")

    def LIGHT_red(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTRED_EX}{self.n}")

    def LIGHT_yellow(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTYELLOW_EX}{self.n}")

    def LIGHT_green(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}{self.n}")

    def LIGHT_cyan(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTCYAN_EX}{self.n}")

    def LIGHT_blue(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTBLUE_EX}{self.n}")

class lightColorsBold():
    def LIGHT_megantaBold(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTMAGENTA_EX}{fs.apply(self.n,'bold')}")

    def LIGHT_redBold(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTRED_EX}{fs.apply(self.n,'bold')}")

    def LIGHT_yellowBold(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTYELLOW_EX}{fs.apply(self.n,'bold')}")

    def LIGHT_greenBold(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}{fs.apply(self.n,'bold')}")

    def LIGHT_cyanBold(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTCYAN_EX}{fs.apply(self.n,'bold')}")

    def LIGHT_blueBold(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTBLUE_EX}{fs.apply(self.n,'bold')}")

class NormalItalicColors():
    def redItalic(self,n):
        self.n = n
        return  (f'{Style.BRIGHT+Fore.RED}{fs.apply(self.n,"italic")}')

    def megantaItalic(self,n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.MAGENTA}{fs.apply(self.n,'italic')}")

    def yellowItalic(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.YELLOW}{fs.apply(self.n,'italic')}")

    def greenItalic(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.GREEN}{fs.apply(self.n,'italic')}")

    def cyanItalic(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.CYAN}{fs.apply(self.n,'italic')}")

    def blueItalic(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.BLUE}{fs.apply(self.n,'italic')}")


class lightColorsItalic():
    def LIGHT_megantaItalic(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTMAGENTA_EX}{fs.apply(self.n,'italic')}")

    def LIGHT_redItalic(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTRED_EX}{fs.apply(self.n,'italic')}")

    def LIGHT_yellowItalic(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTYELLOW_EX}{fs.apply(self.n,'italic')}")

    def LIGHT_greenItalic(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}{fs.apply(self.n,'italic')}")

    def LIGHT_cyanItalic(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTCYAN_EX}{fs.apply(self.n,'italic')}")

    def LIGHT_blueItalic(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTBLUE_EX}{fs.apply(self.n,'italic')}")


class NormalBIUColors():
    def redBIU(self,n):
        self.n = n
        return  (f'{Style.BRIGHT+Fore.RED}{fs.apply(self.n,"bold/italic/underline")}')


    def megantaBIU(self,n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.MAGENTA}{fs.apply(self.n,'bold/italic/underline')}")

    def yellowBIU(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.YELLOW}{fs.apply(self.n,'bold/italic/underline')}")

    def greenBIU(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.GREEN}{fs.apply(self.n,'bold/italic/underline')}")

    def cyanBIU(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.CYAN}{fs.apply(self.n,'bold/italic/underline')}")

    def blueBIU(self, n):
            self.n = n
            return  (f"{Style.BRIGHT + Fore.BLUE}{fs.apply(self.n,'bold/italic/underline')}")

class lightColorsBIU():
    def LIGHT_megantaBIU(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTMAGENTA_EX}{fs.apply(self.n,'bold/italic/underline')}")

    def LIGHT_redBIU(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTRED_EX}{fs.apply(self.n,'bold/italic/underline')}")

    def LIGHT_yellowBIU(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTYELLOW_EX}{fs.apply(self.n,'bold/italic/underline')}")

    def LIGHT_greenBIU(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}{fs.apply(self.n,'bold/italic/underline')}")

    def LIGHT_cyanBIU(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTCYAN_EX}{fs.apply(self.n,'bold/italic/underline')}")

    def LIGHT_blueBIU(self, n):
        self.n = n
        return  (f"{Style.BRIGHT + Fore.LIGHTBLUE_EX}{fs.apply(self.n,'bold/italic/underline')}")

















