import logging
logger = logging.getLogger('root')
logger_2 = logging.getLogger('main')
logger_3 = logging.getLogger('utils')
sub_sub_1 = logging.getLogger('sub_1')


logger_2.setLevel('INFO')
sub_sub_1.setLevel('DEBUG')

cus_hand = logging.StreamHandler()
logger_2.addHandler(cus_hand)
formatter = logging.Formatter(fmt='%(logname)s | %(levelname)s | %(name)s | (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')

#print(logger,logger_2,logger_3,logger_2.parent)