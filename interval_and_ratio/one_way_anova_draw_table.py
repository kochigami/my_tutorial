#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from one_way_anova import OneWayAnova


class OneWayAnovaDrawTable:
    '''
    draw_table: function for draw Analysis variance of table by matplotlib.
    data_list:
    mode: string. between or within. choose one based on your test.
    '''
    def draw_table(self, data_list, mode="CR", threshold=0.05, comparison_mode="holm"):
        # set column
        columns = ("Sum of Squares", "Dof", "Mean Square", "F", "P") 
        # set row based on your test type
        if mode == "CR":
            rows = ["Between Groups", "Within Groups", "Total"]
        elif mode == "RB":
            rows = ["Between Groups", "Subject", "Error", "Total"]
        else:
            print "Please choose mode 'CR' or 'RB'."
            return False

        # initialization for draw table
        fig, ax = plt.subplots()

        # FIXME: calculate anova
        one_way_anova_class = OneWayAnova()
        data_list = one_way_anova_class.one_way_anova(data_list, mode, threshold, comparison_mode)

        # set information for table
        # cellText: data text inside each cell
        # cellLoc: data text location inside each cell
        # rowLabels: string list. table row label
        # colLabels: string list. table column label
        # bbox: float list. [left, bottom, width, height]. adjustment to fit table inside plot area
        # % left: right is +, left is -. bottom: up is +, down is -, width/ height: size ratio 
        # loc: table location relative to plot area
        ax.table(cellText=data_list,
                 cellLoc='center',
                 rowLabels=rows,
                 colLabels=columns,
                 bbox=[0.11, 0.0, 1.0, 0.7],
                 loc="center left")
        # set x, y axis display off 
        ax.axis("off")
        # show a table
        plt.show()

if __name__ == '__main__':
    pass
