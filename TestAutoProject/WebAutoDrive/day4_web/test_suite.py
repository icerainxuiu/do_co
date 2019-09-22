from day4_web.case import test_add_num, test_sub_num
from day4_web import test_frame_switch

import unittest


suit = unittest.TestLoader().discover("./case/", pattern="test*.py")


# suit = unittest.TestSuite()
#
# suit.addTest(unittest.makeSuite(test_sub_num.TestSub))
# suit.addTest(unittest.makeSuite(test_add_num.TestAdd))
# suit.addTest(unittest.makeSuite(test_frame_switch.TestFrameSwitch))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suit)