# -*- coding: utf-8 -*-

"""
<<<<<<< HEAD
a py of something usually(?) is used
=======
a py of usually(?) used things
>>>>>>> 2aad22e4739a22557b78eb60368651108f714d25
"""


class Common:
    """
    main
    """

    def __init__(self):
        self.pi = 3.141592653589793
        self.e = 2.718281828459045
        self.true = 1
        self.false = 0
<<<<<<< HEAD
        self.NeedModuleList = ["xml", "requests", "myqr", "sys", "os"]
=======
        self.NeedModuleList = ["xml", "requests", "myqr", "sys", "os", "math"]
>>>>>>> 2aad22e4739a22557b78eb60368651108f714d25

    class VariablePlus:
        """
        a class of variable include name、value and more...
        to make the class successful run, u must give "name"!
        """

        def __init__(self, name, value = "", uuid = ""):
            self.information = self
            self.name = name
            self.value = value
            self.uuid = uuid

    def AnalysiskXml(self, XmlPath) -> list:
        """
            use this function to analysis xml
            please input xml-path
            if some value is none, also return ""
            return all things, and don`t nest
            you should installed xml(one of the Python build-in module)
        """
        
        try:
            import xml.etree.ElementTree as ET
        except Exception:
            raise Exception("import module:\"xml\" fail")
        tree = ET.parse(XmlPath)
        root = tree.getroot()
        R = []
        for i in root.iter():
            K_n = (
            "tag:"+str(i.tag),
            "attrib:"+str(i.attrib),
            "text:"+str(i.text),
            "tail:"+str(i.tail)
            )
            R.append(i)
            
        return R

    def BetterAnalysiskXml(self, XmlPath):
        """
        use this function to analysis xml
        please input xml-path
        if some value is none, also return " "
        return all things, and nest
        ==============================================
        I do not know how to write this code
        If you want to use it
        Please write it by yourself and AnalysiskXml()
        At last: FUCK YOU!
        """

        pass

    def GetWebInformation(self, url:str, output=True) -> list:
        """
        make sure that you installed "requests"
        output:whether output or not(True or False)
        Raise0_Return1_Error:raise error or return error(0 or 1)
        """

        try:
            import requests as rq
        except Exception:
            raise Exception("import module:\"requests\" fail")
        try:
            web = rq.get(url=url)
            if web.status_code == 200 and output and url[0:4] in [
                "https",
                "Http",
                "Https",
                "http"
                ]:
                print("http-web loading and getting successful")
                print("return code-nunber:"+str(web.status_code))
            texts = web.text.split(";")
            return texts
        except Exception:
                raise Exception("connect error")

    def CreatObjects(self, number:int, Type=0, name="obj"):
        """
        creat "number" objects
        give "type" a real value, such as []、{}、""
        """

        T = str(type(Type))[8:-2]+"()"
        for i in range(1, number+1):
            Run_Code = name+str(i)+" = "+T
            exec("global "+name+str(i))
            exec(Run_Code)

    def CreatOtherPathObjects(self, number:int, classpath:list, name="obj") -> list:
        """"
        creat "number" objects
        ClassPath:please input a list of the path:
        [{from}XXXX, {import}XXXX], {from}XXXX if none, use \"\"
        """
        
        try:
            if classpath[0]:
                exec("from {} import{}".format(classpath[0], classpath[1]))
            else:
                exec("import {}".format(classpath[1]))
        except Exception:
            raise Exception("import module fail")
        R = []
        for i in range(1,number+1):
            exec("global {}".format(name+str(i)))
            exec(name+str(i)+" = "+classpath[1]+"()")
            exec("R.append({})".format(name+str(i)))
        return R

    def GenerateQRcode(self,
        text:str,
        textname:str,
        size:int,
        bgp="",
        colorized=False,
        save_dir="",
        level="H",
        contrast=1.0,
        brightness=1.0
        ):
        """
        input words, return you a QRcode!
        make sure that you installed "myqr"
        only allow:0~9,a~z,A~Z, .,:;~-+/\|{}'"=<>[]()*&^`%$#@!?_ [space]
        text:something which you want to save in QRcode
        textname:the name of QRcode
        size:the size of QRcode, between 1 and 40
        level:fault-tolerance level, in {L, M ,Q, H}, H is the highest and default
        bgp:background picture, the background-path of QRcode
        colorized:the bgp is Colored(True) or black-and-white(False, default)
        save_dir:the save-path of QRcode, default is work-path
        contrast:contrast ratio, the number more higher the contrast ratio more higher, default is 1.0
        brightness:the number more higher the brightness more higher, default is 1.0
        """

        try:
            from MyQR import myqr
        except Exception:
            raise Exception("import module:\"MyQR.myqr\" fail")
        allowstr = r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;~-\+/\|{}'\"=<>[]()\*&^`%$#@!\?_ "
        for i in text:
            if i not in allowstr:
                raise Exception("name:text is not legal!")
        try:
            myqr.run(words=text,
            save_name=textname,
            version=size,
            picture=bgp,
            colorized=colorized,
            save_dir=save_dir,
            contrast=contrast,
            brightness=brightness
            )
        except Exception:
            raise Exception("running fail")

    def SystemBasic(self, ErrorReturn="", Alist=[], *argvs) -> dict:
        """
        make sure that you installed "sys"
        you can use this method to get some imformation about the system and the program
        this method allow two ways to set
        1: Alist: give the method a list, including [platform, argv, path, modules,  over]
        2: *argvs:(platform, argv, path, modules, over)
        if you want to use "over" and set return value, set the "ErrorReturn"
        """

        try:
            import sys
        except Exception:
            raise Exception("import module:\"sys\" fail")
        R = {}
        if Alist:
            if "platform" in Alist:
                R["platform"] = sys.platform()
            if "argv" in Alist:
                R["argv"] = sys.argv()
            if "path" in Alist:
                R["path"] = sys.path()
            if "modules" in Alive:
                R["modules"] = sys.modules()
            if "over" in Alist and ErrorReturn:
                R["over"] = sys.exit(ErrorReturn)
            else:
                R["over"] = sys.exit()
        else:
            if "platform" in argvs:
                R["platform"] = sys.platform()
            if "argv" in argvs:
                R["argv"] = sys.argv()
            if "path" in argvs:
                R["path"] = sys.path()
            if "modules" in argvs:
                R["modules"] = sys.modules()
            if "over" in argvs and ErrorReturn:
                R["over"] = sys.exit(ErrorReturn)
            else:
                R["over"] = sys.exit()
        return R

    def OsBasic(self, Alist:list) -> dict:
        """
        make sure that you installed "os"
        use this method to get imformation about files
        ————————————————————————————————————————————————
        How to input argvs?
        [[x1, x1.2, x1.3], [x2, x2.1, x2.2, x2.3...]...]
        x1,x2 mean the name of the methods
        x1.2,x1.3,x2.1,x2.2... mean the argvs of what methods you use

        the lists of methods can be upset, but each argvs of lists must not be upset!
        the position of the parameter must be correct

        total methods:
        [
            [path],
            [get_cwd],
            [chdir, -path-],
            [rename, -filepath, chname-],
            [is_file_exist, -filepath-],
            [isfile, -filepath-],
            [isdir, -filepath-],
            [get_environ],
            [makedirs, -filepath-]
        ]
        """

        try:
            import os
        except:
            raise Exception("import module:\"os\" fail")
        R = {}
        for i in Alist:
            if i[0] == "path":
                R["file"] = os.path.dirname(__file__)
            if i[0] == "get_cwd":
                R["get_cwd"] = os.getcwd()
            if i[0] == "chdir":
                try:
                    os.chdir(i[1])
                    R["chdir"] = True
                except:
                    R["chdir"] = False
                    pass
            if i[0] == "rename":
                try:
                    os.rename(i[1], i[2])
                    R["rename"] = True
                except:
                    R["rename"] = False
                    pass
            if i[0] == "is_file_exist":
                R["is_file_exist"] = os.path.exists(i[1])
            if i[0] == "isfile":
                R["isfile"] = os.path.isfile(i[1])
            if i[0] == "isdir":
                R["isdir"] = os.path.isdir(i[1])
            if i[0] == "get_environ":
                for k, v in os.environ.items():
                    R["get_environ"] = [k, v]
            if i[0] == "makedirs":
                R["makedirs"] = os.makedirs(i[1])
        return R

    def MathBasic(self, Alist, PubNum="") -> dict:
        """
        use this method to calculate
        use "PubNum" to set a number which can be used in the whole methods

        if you seted the "PubNum", you need not input "-number-" when you use methods which need three or more argvs, use "" instead
        the lists of methods can be upset, but each argvs of lists must not be upset!
        the position of the parameter must be correct
        
        Alist = [
            [ceil, -number-]
            [floor, -number-]
            [pow. -number, PowerNumber-]
<<<<<<< HEAD
            [rooting, -number, times, FloatLong-]
=======
>>>>>>> 2aad22e4739a22557b78eb60368651108f714d25
        ]
        """

        R = {}
        Key = False
        if (type(PubNum) is int)or(type(PubNum) is float):
                Key = True
        for i in Alist:
            if i[0] == "ceil":
                if Key:
                    if PubNum < 0:
                        R["ceil"] = int(PubNum)
                    else:
                        R["ceil"] = int(PubNum)+1
                else:
                    if i[1] < 0:
                        R["ceil"] = int(i[1])
                    else:
                        R["ceil"] = int(i[1])+1
            if i[0] == "floor":
                if Key:
                    if PubNum < 0:
                        R["floor"] = int(PubNum)-1
                    else:
                        R["floor"] = int(PubNum)
                else:
                    if i[1] < 0:
                        R["floor"] = int(i[1])-1
                    else:
                        R["floor"] = int(i[1])
            if i[0] == "pow":
                if Key:
                    R["pow"] = PubNum ** i[2]
                else:
                    R["pow"] = i[1] ** i[2]
<<<<<<< HEAD
            if i[0] == "rooting":
                if Key:
                    if PubNum == 0:
                        R["rooting"] = 0
                    elif ((PubNum > 0)and(i[2]>0))or((i[2]%2)==1):
                        FloatLong = 0
                        Rslt = 0
                        while FloatLong <= i[3]:
                            for j in range(0, 10):
                                Rslt += 1 / (10 ** FloatLong)
                                if (Rslt ** i[2])**2 == PubNum**2:
                                    break
                                elif (Rslt ** i[2])**2 > PubNum**2:
                                    Rslt -= 1 / (10 ** FloatLong)
                                    break
                            FloatLong += 1
                            if (Rslt ** i[2])**2 == PubNum**2:
                                break
                        if PubNum > 0:
                            R["rooting"] = int(Rslt * (10**i[3])) / (10**i[3])
                        else:
                            R["rooting"] = int(Rslt * (10**i[3])) / (10**i[3])*-1
                    else:
                        raise Exception("input wrong")
                else:
                    if i[1] == 0:
                        R["rooting"] = 0
                    elif ((i[1] > 0)and(i[2]>0))or((i[2]%2)==1):
                        FloatLong = 0
                        Rslt = 0
                        while FloatLong <= i[3]:
                            for j in range(0, 10):
                                Rslt += 1 / (10 ** FloatLong)
                                if (Rslt ** i[2])**2 == i[1]**2:
                                    break
                                elif (Rslt ** i[2])**2 > i[1]**2:
                                    Rslt -= 1 / (10 ** FloatLong)
                                    break
                            FloatLong += 1
                            if (Rslt ** i[2])**2 == i[1]**2:
                                break
                        if i[1] > 0:
                            R["rooting"] = int(Rslt * (10**i[3])) / (10**i[3])
                        else:
                            R["rooting"] = int(Rslt * (10**i[3])) / (10**i[3])* -1
                    else:
                        raise Exception("input wrong")
        return R

a = Common()
print(a.MathBasic([["rooting", -50, 3, 5]]))
=======
                

>>>>>>> 2aad22e4739a22557b78eb60368651108f714d25
