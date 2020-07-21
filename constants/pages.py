
#from enum import Enum

class Pages():

    startPage = {'pageTitle':'Start', 'pageUrl':'https://www.jeuneafrique.com/'}
    politiquePage = {'pageTitle':'Politique', 'pageUrl':'https://www.jeuneafrique.com/rubriques/politique/'}
    societePage = {'pageTitle': 'Societe', 'pageUrl': 'https://www.jeuneafrique.com/rubriques/societe/'}
    culturePage = {'pageTitle': 'Culture', 'pageUrl': 'https://www.jeuneafrique.com/rubriques/culture/'}
    lifestylePage = {'pageTitle': 'Lifestyle', 'pageUrl': 'https://www.jeuneafrique.com/rubriques/lifestyle/'}
    economiePage = {'pageTitle': 'Economie', 'pageUrl': 'https://www.jeuneafrique.com/rubriques/economie/'}
    sportPage = {'pageTitle': 'Sport', 'pageUrl': 'https://www.jeuneafrique.com/rubriques/sport/'}

    guineenewsStartPage={'pageTitle':'Guineenews', 'pageUrl':'https://www.guineenews.org/'}

    pagelist = {'startPage':startPage, 'politiquePage':politiquePage, 'societePage':societePage,
                'culturePage':culturePage,'lifestylePage':lifestylePage, 'economiePage':economiePage,
                'sportPage':sportPage, 'guineenewsStartPage':guineenewsStartPage}
    @classmethod
    def getPageURL(cls, page):
        try:
            if page is not None:
                #return page['pageUrl']
                return cls.pagelist[page]['pageUrl']
        except Exception as e:
            print("page is null")


    def getPageTitle(self, page):
        try:
            if page is not None:
                #return page['pageTitle']
                return self.pagelist[page]['pageTitle']
        except Exception as e:
            print("page is null")