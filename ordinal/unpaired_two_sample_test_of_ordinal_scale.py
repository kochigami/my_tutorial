#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys
import numpy

'''
Mann-Whitney test
'''

class UnpairedTwoSampleTestOfOrdinalScale:
    def test(self, data):
        """
        data = {'Children':  [20, 18, 15, 13, 10, 6],
                'Adults': [17, 16, 12, 9, 8, 6, 4, 2]}
        # https://kusuri-jouhou.com/statistics/mann.html
        => comparison of two median

        # use mannwhitneyu() from scipy
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
        # however, alternative keyword cannnot be used
        # TypeError: mannwhitneyu() got an unexpected keyword argument 'alternative'
        """
        if len(data.keys()) != 2:
            print "Please check the contents of your data."
            print "The number of data type should be two."
            sys.exit()
        result = stats.mannwhitneyu(data[(data.keys())[0]], data[(data.keys())[1]], use_continuity=True)
        print "median ({}): {}".format((data.keys())[0], numpy.median(data[(data.keys())[0]]))
        print "median ({}): {}".format((data.keys())[1], numpy.median(data[(data.keys())[1]]))
        print "U value: {}".format(result[0]) 
        print "p value: {}".format(result[1])
        return result[1]
