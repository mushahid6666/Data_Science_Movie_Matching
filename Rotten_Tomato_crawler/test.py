def findslashes(str):
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

str = "mushahid\asjdd/"
print findslashes(str)
