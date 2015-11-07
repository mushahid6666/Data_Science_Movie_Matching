
class stringfix():
    def findslashes(self,str):
        fslash = '/'
        bslash = "\\"
        result = str.find(fslash)
        if (result == -1):
            result = str.find(bslash)
            if (result == -1):
                return str
            else:
                bslashindex = str.index(bslash)
                str = str[0:bslashindex]
                return str
        else:
            fslashindex = str.index(fslash)
            str = str[0:fslashindex]
            result = str.find(bslash)
            if (result == -1):
                return str
            else:
                bslashindex = str.index(bslash)
                str = str[0:bslashindex]
                return str


    def findbraces(self,str):
        opbrac = '('
        clbrac = ')'
        result = str.find(opbrac)
        if (result == -1):
            result = str.find(clbrac)
            if (result == -1):
                return str
            else:
                clbracindex = str.index(clbrac)
                str = str[0:clbracindex]
                return str
        else:
            opbracindex = str.index(opbrac)
            str = str[0:opbracindex]
            result = str.find(clbrac)
            if (result == -1):
                return str
            else:
                clbracindex = str.index(clbrac)
                str = str[0:clbracindex]
                return str


    def findcomma(self,str):
        comma = ','
        result = str.find(comma)
        if (result == -1):
            return str
        else:
            str = '"' + str + '"'
            return str


    def removeallspaces(self,str):
        str = str.strip()
        str = str.replace(" ", "_")
        return str


    def removeallcolons(self,str):
        print(str)
        str = str.replace(":", '_')
        return str

