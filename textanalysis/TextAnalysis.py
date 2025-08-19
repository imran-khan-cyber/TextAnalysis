class TextAnalysis:
    """ To perform Text Analysis operations of count the occurrences of an
    alphabetic characters and display the histogram pattern based on it."""

    # Constructor Function.
    def __init__(self):
        self.text = " "
        self.result = {}


    def setautomatic(self):
        self.text = """This section provides essential information on C,  C++ and 
                       programming  libraries. quicydoc img   marks help chapters 
                       available locally (some of the internal links may be to
                       internet pages) world icon  marks help chapters 
                       retrieved from the internet (slower loading & less 
                       reliable lines."""


    def setreadinput(self):
        intext = " "
        print "Enter a Text below (Null to stop) : \n"
        while True:
            tmptext = raw_input()
            if len(tmptext) == 0:
                break
            intext += tmptext

        self.text = intext


    def setfiledata(self):
        filename = raw_input("Enter a File path : ")
        with open(filename,"r") as f:
            self.text = f.read()

    def display(self):
        print self.text
        print


    def analyzetext(self):
        self.result.clear()
        tmptext = self.text.upper()
        for c in tmptext:
            if c.isalpha():
                if self.result.has_key(c):
                    self.result[c] += 1
                else :
                    self.result[c] = 1

        print self.result


    def showresult(self):
        for k,v in self.result.iteritems():
            print "{}  {:2d}  {}".format(k, v, "*" * v)