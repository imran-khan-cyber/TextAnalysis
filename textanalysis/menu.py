from textanalysis import TextAnalysis

class menuoptions:
    """ Assist users for menu options to perform Text Analysis Operations. """

    def startmenu(self):
        # Create instantiation (object)
        m = TextAnalysis.TextAnalysis()
        while True:
            print "           TEXT  ANALYSIS"
            print
            print " 1. Default Auto Text"
            print " 2. User Input Data Text"
            print " 3. File Data Text"
            print " 4. Exit"
            print
            opt = input("Enter Options (1-4) : ")
            if opt == 1:
                m.setautomatic()
            elif opt == 2:
                m.setreadinput()
            elif opt == 3:
                m.setfiledata()
            elif opt ==4:
                break
            else:
                print "Invalid Option! Try again..."
                continue
            m.display()
            m.analyzetext()
            m.showresult()

        del m

