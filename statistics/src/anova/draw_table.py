#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from one_way_anova import OneWayAnova


class DrawTable:
    '''
    draw_table: function for draw Analysis variance of table by matplotlib.
    data_list:
    mode: string. between or within. choose one based on your test.
    '''
    def draw_table(self, data_list, mode="between"):
        # set column
        columns = ("Sum of Squares", "Dof", "Mean Square", "F") 
        # set row based on your test type
        if mode == "between":
            rows = ["Between Groups", "Within Groups", "Total"]
        elif mode == "within":
            rows = ["Between Groups", "Subject", "Error", "Total"]
        else:
            print "Please choose mode 'between' or 'within'."
            return False

        # initialization for draw table
        fig, ax = plt.subplots()

        # FIXME: calculate anova
        if mode == "between":
            one_way_anova_class = OneWayAnova()
            data_list = one_way_anova_class.one_way_anova(data_list)
        elif mode == "within":
            print "within"

        # FIXME: set data_list_for_display after calculating anova
        if mode == "within":
            print "within"

        # set information for table
        # cellText: data text inside each cell
        # cellLoc: data text location inside each cell
        # rowLabels: string list. table row label
        # colLabels: string list. table column label
        # bbox: float list. [left, bottom, width, height]. adjustment to fit table inside plot area
        # % left: right is +, left is -. bottom: up is +, down is -, width/ height: size ratio 
        # loc: table location relative to plot area
        table = ax.table(cellText=data_list,
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
    draw_table = DrawTable()
    data = {'Japanese': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'English':  [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'French' :  [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75]}
    #data_list = np.random.randint(10,90, size=(4, 4))
    
    draw_table.draw_table(data)
