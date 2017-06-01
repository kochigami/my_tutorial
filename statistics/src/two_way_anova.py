#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
#from scipy import stats
#import matplotlib.pyplot as plt
import numpy as np
import math
#from texttable import Texttable
from calculate_average import CalculateAverage
from calculate_variance import CalculateVariance
from analysis_of_variance import AnalysisOfVariance

class TwoWayAnova:
    def __init__(self):
        self.calculate_average = CalculateAverage()
        self.calculate_variance = CalculateVariance()
        self.analysis_of_variance = AnalysisOfVariance()
    
    def calc_two_way_anova(self, df_of_each_group, label_of_each_group, df_factor1, label_factor1, df_factor2, label_factor2, df_of_all_samples, label_of_all_samples):
        ### calculate average ###
        '''
        Calculate within_average: average (float) list of each category 
        Args:
           df_of_each_group: DataFrame of each category
           label_of_each_group: string list. label of each category
        Example:
           within_average: [2.0296623333333335, 1.9834588333333334, 2.074698666666667]
        '''
        within_average = []
        for i in range(len(label_of_each_group)):
            within_average.append(self.calculate_average.calc_average(df_of_each_group, label_of_each_group[i]))
        '''
        Calculate factor1_average: average (float) list of category of factor1 
        Args:
           df_factor1: DataFrame of factor1
           label_factor1: string list. label of factor1
        Example:
           factor1_average: [2.0296623333333335, 1.98]
        '''
        factor1_average = []
        for i in range(len(label_factor1)):
            factor1_average.append(self.calculate_average.calc_average(df_factor1, label_factor1[i]))
        '''
        Calculate factor2_average: average (float) list of category of factor2 
        Args:
           df_factor2: DataFrame of factor2
           label_factor2: string list. label of factor2
        Example:
           factor2_average: [2.0296623333333335, 1.98]
        '''
        factor2_average = []
        for i in range(len(label_factor2)):
            factor2_average.append(self.calculate_average.calc_average(df_factor2, label_factor2[i]))
        '''
        Calculate average_of_all: average (float) of all samples 
        Args:
           df_of_all_samples: DataFrame of all samples
           label_of_all_samples: string list. Normally, ["all"].
        Example:
           average_of_all: [2.0296623333333335]
        '''
        average_of_all = self.calculate_average.calc_average(df_of_all_samples, label_of_all_samples)
        
        ### calculate sample nums ###
        '''
        Calculate sample_num_per_group: float list. sample num of each category
        Args:
           df_of_each_group: DataFrame of each category
           label_of_each_group: string list. label of each category
        Example:
           sample_num_per_group: [6.0, 6.0, 6.0]
        '''
        sample_num_per_group =[]
        sample_num_per_group = self.analysis_of_variance.calc_sample_num(df_of_each_group, label_of_each_group, sample_num_per_group)
        '''
        Calculate sample_num_per_factor1: float list. sample num per factor1
        Args:
           df_factor1: DataFrame of factor1
           label_factor1: string list. label of factor1
        Example:
           sample_num_per_factor1: [6.0, 6.0, 6.0]
        '''
        sample_num_per_factor1 = []
        sample_num_per_factor1 = self.analysis_of_variance.calc_sample_num(df_factor1, label_factor1, sample_num_per_factor1)
        '''
        Calculate sample_num_per_factor2: float list. sample num per factor2
        Args:
           df_factor2: DataFrame of factor2
           label_factor2: string list. label of factor2
        Example:
           sample_num_per_factor2: [6.0, 6.0, 6.0]
        '''
        sample_num_per_factor2 = []
        sample_num_per_factor2 = self.analysis_of_variance.calc_sample_num(df_factor2, label_factor2, sample_num_per_factor2)
        '''
        Calculate total_sample_num: float list. sample num of all categories
        Args:
           df_of_all_samples: DataFrame of all samples
           label_of_all_samples: string list. Normally, ["all"].
        Example:
           total_sample_num: [18.0]
        '''
        total_sample_num = []
        total_sample_num = self.analysis_of_variance.calc_sample_num(df_of_all_samples, label_of_all_samples, total_sample_num)

        ### calculate total variance ###
        '''
        Calculate within_variance: variance (float) list of each category 
        Args:
           df_of_each_group: DataFrame of each category
           label_of_each_group: string list. label of each category
        Example:
           within_variance: [0.03470865617688887, 0.1543511475384722, 0.2957196379978889]
        '''
        within_variance = []
        for i in range(len(label_of_each_group)):
            within_variance.append(self.calculate_variance.calc_variance(df_of_each_group, label_of_each_group[i]))
        '''
        Calculate factor1_variance: variance (float) list of factor1 
        Args:
           df_factor1: DataFrame of factor1
           label_of_factor1: string list. label of factor1
        Example:
           factor1_variance: [0.03470865617688887, 0.1543511475384722, 0.2957196379978889]
        '''
        factor1_variance = []
        for i in range(len(label_factor1)):
            factor1_variance.append(self.calculate_variance.calc_variance(df_factor1, label_factor1[i]))
        '''
        Calculate factor2_variance: variance (float) list of factor2 
        Args:
           df_factor2: DataFrame of factor2
           label_of_factor2: string list. label of factor2
        Example:
           factor2_variance: [0.03470865617688887, 0.1543511475384722, 0.2957196379978889]
        '''
        factor2_variance = []
        for i in range(len(label_factor2)):
            factor2_variance.append(self.calculate_variance.calc_variance(df_factor2, label_factor2[i]))
        '''
        Calculate variance_of_all: variance (float) of all samples
        Args:
           df_of_all_samples: DataFrame of all samples
           label_of_all_samples: string list. Normally, ["all"].
        Example:
           variance_of_all: 0.162980674118
        '''
        variance_of_all = self.calculate_variance.calc_variance(df_of_all_samples, label_of_all_samples)
        
        ### calculate sum of squares ###
        '''
        Calculate sum_of_squares_of_others: total sum of squares (float) of others 
        Args:
           sample_num_per_group: calculated from "calculate sample nums" (float list)
           within_variance: calculated from "calculate variance" (float list) 
        Example:
           sum_of_squares_of_others: 2.90867665028 
        '''
        sum_of_squares_of_others = 0.0
        for i in range(len(label_of_each_group)):
            sum_of_squares_of_others += self.analysis_of_variance.calc_sum_of_squares(within_variance[i], sample_num_per_group[i])
        '''
        Calculate sum_of_squares_of_each_group: total sum of squares (float) of each group 
        Args:
           sample_num_per_group: calculated from "calculate sample nums" (float list)
           average_of_all: float.
           within_variance: calculated from "calculate variance" (float list) 
        Example:
           sum_of_squares_of_each_group: 2.90867665028 
        '''
        sum_of_squares_of_each_group = 0.0
        for i in range(len(label_of_each_group)):
            sum_of_squares_of_each_group += math.pow((within_average[i] - average_of_all), 2) * sample_num_per_group[i]
        '''
        Calculate sum_of_squares_of_factor1: total sum of squares (float) of factor1
        Args:
           sample_num_per_factor1: calculated from "calculate sample nums" (float list)
           average_of_all: float.
           factor1_variance: calculated from "calculate variance" (float list) 
        Example:
           sum_of_squares_of_factor1: 2.90867665028 
        '''
        sum_of_squares_of_factor1 = 0.0
        for i in range(len(label_factor1)):
            sum_of_squares_of_factor1 += math.pow((factor1_average[i] - average_of_all), 2) * sample_num_per_factor1[i]
        '''
        Calculate sum_of_squares_of_factor2: total sum of squares (float) of factor2
        Args:
           sample_num_per_factor2: calculated from "calculate sample nums" (float list)
           average_of_all: float.
           factor2_variance: calculated from "calculate variance" (float list) 
        Example:
           sum_of_squares_of_factor2: 2.90867665028 
        '''
        sum_of_squares_of_factor2 = 0.0
        for i in range(len(label_factor2)):
            sum_of_squares_of_factor2 += math.pow((factor2_average[i] - average_of_all), 2) * sample_num_per_factor2[i]
        '''
        Calculate sum_of_squares_of_interaction: total sum of squares (float) of interaction of factor1 and factor2
        Args:
           sum_of_squares_of_each_group: float
           sum_of_squares_of_factor1: float
           sum_of_squares_of_factor2: float
        Example:
           sum_of_squares_of_interaction: 2.90867665028 
        '''
        sum_of_squares_of_interaction = sum_of_squares_of_each_group - sum_of_squares_of_factor1 - sum_of_squares_of_factor2
        
        ### calculate dof ###
        '''
        Calculate dof_of_factor1: dof (float) of factor1 
        Args:
           sample_num_per_factor1: calculated from "calculate sample nums"
        Example:
           dof_of_factor1: 2.0
        '''
        dof_of_factor1 = len(sample_num_per_factor1) - 1.0
        '''
        Calculate dof_of_factor2: dof (float) of factor2 
        Args:
           sample_num_per_factor2: calculated from "calculate sample nums"
        Example:
           dof_of_factor2: 2.0
        '''
        dof_of_factor2 = len(sample_num_per_factor2) - 1.0
        '''
        Calculate dof_of_interaction: dof (float) of interaction 
        Args:
           dof_of_factor1
           dof_of_factor2
        Example:
           dof_of_interaction: 2.0
        '''
        dof_of_interaction = dof_of_factor1 * dof_of_factor2
        '''
        Calculate dof_of_all: total dof (float) of each category num 
        Args:           
           total_sample_num: args (float list)
        Example:
           dof_of_all: 2.0
        '''
        dof_of_all = total_sample_num[0] - 1.0
        '''
        Calculate dof_of_others: dof (float) of others 
        Args:
           dof_of_all:
           dof_of_factor1:
           dof_of_factor2:
           dof_of_interaction:
        Example:
           dof_of_others: 2.0
        '''
        dof_of_others = dof_of_all - dof_of_factor1 - dof_of_factor2 - dof_of_interaction

        ### calculate sum of squares ###
        '''
        Calculate mean_square_of_factor1: mean_square (float) of factor1
        Args:           
           sum_of_squares_of_factor1: calculated from "calculate sum of squares" (float)
           dof_of_factor1: calculated from "calculate dof" (float)
        Example:
           mean_square_of_factor1: 0.012
        '''
        mean_square_of_factor1 = 0.0
        mean_square_of_factor1 = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_factor1, dof_of_factor1)
        '''
        Calculate mean_square_of_factor2: mean_square (float) of factor2
        Args:           
           sum_of_squares_of_factor2: calculated from "calculate sum of squares" (float)
           dof_of_factor1: calculated from "calculate dof" (float)
        Example:
           mean_square_of_factor2: 0.012
        '''
        mean_square_of_factor2 = 0.0        
        mean_square_of_factor2 = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_factor2, dof_of_factor2)
        '''
        Calculate mean_square_of_interaction: mean_square (float) of interaction
        Args:           
           sum_of_squares_of_interaction: calculated from "calculate sum of squares" (float)
           dof_of_interaction: calculated from "calculate dof" (float)
        Example:
           mean_square_of_interaction: 0.012
        '''        
        mean_square_of_interaction = 0.0
        mean_square_of_interaction = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_interaction, dof_of_interaction)
        '''
        Calculate mean_square_of_others: mean_square (float) of others
        Args:           
           sum_of_squares_of_others: calculated from "calculate sum of squares" (float)
           dof_of_others: calculated from "calculate dof" (float)
        Example:
           mean_square_of_others: 0.012
        '''
        mean_square_of_others = 0.0
        mean_square_of_others = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_others, dof_of_others)

        ### calculate F ###
        '''
        Calculate F_of_factor1 value. (float)
        Args:
           mean_square_of_factor1: calculated from "calculate mean square" (float)
           mean_square_of_others: calculated from "calculate mean square" (float)
        Example: 
           F_of_factor1: 0.064
        '''
        F_of_factor1 = self.analysis_of_variance.calc_F(mean_square_of_factor1, mean_square_of_others)
        '''
        Calculate F_of_factor2 value. (float)
        Args:
           mean_square_of_factor2: calculated from "calculate mean square" (float)
           mean_square_of_others: calculated from "calculate mean square" (float)
        Example: 
           F_of_factor2: 0.064
        '''
        F_of_factor2 = self.analysis_of_variance.calc_F(mean_square_of_factor2, mean_square_of_others)
        '''
        Calculate F_of_interaction value. (float)
        Args:
           mean_square_of_interaction: calculated from "calculate mean square" (float)
           mean_square_of_others: calculated from "calculate mean square" (float)
        Example: 
           F_of_interaction: 0.064
        '''
        F_of_interaction = self.analysis_of_variance.calc_F(mean_square_of_interaction, mean_square_of_others)

        sum_of_squares = {"Factor1": sum_of_squares_of_factor1,
                          "Factor2": sum_of_squares_of_factor2,
                          "Interaction": sum_of_squares_of_interaction,
                          "Others": sum_of_squares_of_others,
                          "Total": sum_of_squares_of_factor1 + sum_of_squares_of_factor2 + sum_of_squares_of_interaction + sum_of_squares_of_others}
        
        dof = {"Factor1": dof_of_factor1,
               "Factor2": dof_of_factor2,
               "Interaction": dof_of_interaction,
               "Others": dof_of_others,
               "Total": dof_of_all}
        
        mean_squares = {"Factor1": mean_square_of_factor1,
                        "Factor2": mean_square_of_factor2,
                        "Interaction": mean_square_of_interaction,
                        "Others": mean_square_of_others}
        
        F = {"Factor1": F_of_factor1,
             "Factor2": F_of_factor2,
             "Interaction": F_of_interaction}
        
        self.analysis_of_variance.show_table(sum_of_squares, dof, mean_squares, F, analysis_type="two-way")

        '''
        Draw matplotlib table.
        Args: sum_of_squares_of_factor1
              sum_of_squares_of_factor2
              sum_of_squares_of_interaction
              sum_of_squares_of_others
              dof_of_factor1
              dof_of_factor2 
              dof_of_interaction
              dof_of_others
              dof_of_all
              mean_square_of_factor1
              mean_square_of_factor2
              mean_square_of_interaction
              mean_square_of_others
              F_of_factor1
              F_of_factor2
              F_of_interaction
        '''
        show_table_df = self.analysis_of_variance.make_df_of_two_way_anova_for_matplotlib_table(sum_of_squares_of_factor1, sum_of_squares_of_factor2, sum_of_squares_of_interaction, sum_of_squares_of_others, dof_of_factor1, dof_of_factor2, dof_of_interaction, dof_of_others, dof_of_all, mean_square_of_factor1, mean_square_of_factor2, mean_square_of_interaction, mean_square_of_others, F_of_factor1, F_of_factor2, F_of_interaction)
        self.analysis_of_variance.matplotlib_table(show_table_df)

if __name__ == '__main__':
    # data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
    #         'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
    #         'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
    #         'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]
    #     }

    data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'Crispy-normal': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
            'Normal-normal' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
            'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]
        }

    df = DataFrame(data, index = [str(i+1)  for i  in np.arange(15)])
    
    data_factor1 = {'Crispy': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                    'Normal': [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}

    data_factor2 = {'hot': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                    'normal': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                    'mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}

    df_factor1 = DataFrame(data_factor1, index = [str(i+1)  for i  in np.arange(45)])
    df_factor2 = DataFrame(data_factor2, index = [str(i+1)  for i  in np.arange(30)])

    data_all = {'all': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]
            }

    df_all = DataFrame(data_all, index = [str(i+1) for i in np.arange(90)])

    two_way_anova = TwoWayAnova()
    two_way_anova.calc_two_way_anova(df, ['Crispy-hot', 'Crispy-normal', 'Crispy-mild', 'Normal-hot', 'Normal-normal', 'Normal-mild'], df_factor1, ['Crispy', 'Normal'], df_factor2, ['hot', 'normal', 'mild'], df_all, ['all'])
