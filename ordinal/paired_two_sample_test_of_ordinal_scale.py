#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
from scipy.stats import wilcoxon
from scipy.stats import ranksums
import sys
import itertools
import math
import numpy

'''
signed rank sum test
signed test
'''

class PairedTwoSampleTestOfOrdinalScale:
    '''
    calc_ave:
    calculate average order
    
    [ex]
    diff:  [-1, +31, +23, +2, -5, +5]
    order: [1, 6, 5, 2, 3.5, 3.5]
    3.5 = (3 + 4) / 2
    (i: 3, count: 2) 
    '''
    def calc_ave(self, order, count, i):
        tmp_sum = 0.0
        for j in range(count):
            tmp_sum += i+1+j
        for j in range(count):
            order.append(tmp_sum / float(count))

    def test(self, data, mode="signed_rank_sum_test"):
        '''
        signed rank sum test
        '''
        """
        data = {'Product_A': [25, 62, 58, 26, 42, 18, 11, 33, 50, 34]
                'Product_B': [26, 31, 35, 24, 47, 13, 11, 21, 42, 18]}
        """
        if mode == "signed_rank_sum_test":
            x = data[data.keys()[0]]
            y = data[data.keys()[1]]
            if len(x) != len(y):
                print "Please check the contents of your data."
                print "The number of data type should be two."
                sys.exit()
            else:
                statistic, p = ranksums(data[data.keys()[0]], data[data.keys()[1]])

        elif mode == "signed_test":
            '''
            signed test
            '''
            """
            data = {'Cusine_A': [5, 3, 4, 4, 3, 4, 4, 1, 3, 3, 5, 3]
                    'Cusine_B': [3, 5, 3, 3, 5, 2, 2, 1, 4, 2, 2, 3]}
            # https://kusuri-jouhou.com/statistics/fugou.html
            """
            x = data[(data.keys())[0]]
            y = data[(data.keys())[1]]
            # note: nx == ny
            nx = len(data[(data.keys())[0]])
            if len(x) != len(y):
                print "Please check the contents of your data."
                print "The number of data type should be two."
                sys.exit()
            else:
                statistic, p = wilcoxon(data[data.keys()[0]], data[data.keys()[1]])
                print "median ({}) = {}".format((data.keys())[0], numpy.median(x))
                print "median ({}) = {}".format((data.keys())[1], numpy.median(y))
                print "p value: {}".format(p)
                return p

        else:
            print "Please choose mode: 'signed_test' or 'signed_rank_test'"
