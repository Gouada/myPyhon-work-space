
import unittest
from testSteps.guineenewsStartPageTestSteps import GuineenewsStartPageTest
from testSteps.jeuneAfriqueStartPageTestSteps import JeuneAfriqueStartPageTestSteps

tc1 = unittest.TestLoader().loadTestsFromTestCase(GuineenewsStartPageTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(JeuneAfriqueStartPageTestSteps)

tSuite = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(tSuite)