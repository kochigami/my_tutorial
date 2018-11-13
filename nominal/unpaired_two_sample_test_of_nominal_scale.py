#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy.stats import chi2_contingency
import scipy.stats as stats
from scipy.stats.contingency import expected_freq

class UnpairedTwoSampleTestOfNominalScale:
    def test(self, data):
        # check data length
        if len(data.keys()) != 2:
            print "len(data.keys()) should be two"
            sys.exit()
        elif len(data[(data.keys())[0]]) != len(data[(data.keys())[1]]):
            print "len(data[(data.keys())[0]]) and len(data[(data.keys())[1]]) should be same"
            sys.exit()
        else:
            """
            Is there any difference between the number of people who satisfies Condition1 and Yes (a) and that of people who satisfies Condition2 and Yes (c)?
            data = {"Condition1": [a, b], "Condition2": [c, d]}
            OrderedDict([('Illness', [52, 8]), ('Healty', [48, 42])])

                            Yes   No   Total <= sum_row
              --------------------------------------
              Condition1     a     b    a+b
              Condition2     c     d    c+d
              --------------------------------------
              Total         a+c   b+d    n (= a+b+c+d)
               ^
               |_ sum_column 

            """
            data_exp = expected_freq([data[(data.keys())[0]], data[(data.keys())[1]]])
            
            # select the way of calculation based on the minimum expected data (fisher's test or chi-square test)
            """
            fisher test is used in a certain condition (Cochran's rule); 
            see http://aoki2.si.gunma-u.ac.jp/lecture/Cross/warning.html and
                http://drmagician.exblog.jp/22086293/
            """
            if min(min(data_exp[0]), min(data_exp[1])) < 5: 
                # use fisher's test
                oddsratio, p = stats.fisher_exact([data[(data.keys())[0]], data[(data.keys())[1]]])
                return p
            else:
                # use chi-square test                
                chi2, p, dof, expected = chi2_contingency([data[(data.keys())[0]], data[(data.keys())[1]]])
                return p
                
if __name__ == '__main__':
    pass
