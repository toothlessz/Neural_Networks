import numpy as np 

# famous data
P_trust = 0.95
t_critical_student = 2.26
number_drills = 20
number_stoutnes = 24

# for hi_square
decrease_of_freedom = number_stoutnes - 1
level_main = 0.05
hi_critical_23_005 = 35.5  # 23 and 0.05
hi_critical_11_005 = 19.7

# X_values data
drills = np.asarray([
    [14.8, 9.6, 15.7, 9.1, 8.7, 7.7, 16.1, 10.7, 25, 14.1, 10.9, 8.4, 18.4, 8.7, 16.9, 20.4, 11.3, 11.4, 19, 13.1, 20.5, 17.5, 12.3, 7.5],
    [0.16, 0.56, 0.13, 0.15, 0.88, 0.12, 0.17, 0.11, 0.16, 0.14, 0.11, 0.12, 0.14, 0.68, 0.18, 0.18, 0.94, 0.12, 0.17, 0.11, 0.62, 0.16, 0.12, 0.38],
    [15.6, 10.4, 15.7, 22.6, 10.1, 11.5, 18.8, 12.9, 19, 20.6, 13.6, 10.2, 14.6, 7.2, 13.4, 20.1, 9.5, 8.6, 16.2, 10.8, 7.8, 19.1, 13, 7.9],
    [15.8, 7.8, 13.5, 17.4, 9.2, 10.5, 13.8, 8.9, 11.8, 21.7, 14, 12.2, 14.9, 12.6, 15.9, 17.8, 11.1, 10.5, 19.2, 13.2, 4.4, 19.4, 13.1, 4.1],
    [0.15, 0.6, 0.14, 0.17, 0.83, 0.69, 0.18, 0.12, 0.19, 0.19, 0.13, 0.11, 0.16, 0.17, 0.13, 0.13, 0.56, 0.8, 0.13, 0.81, 0.65, 0.16, 0.12, 0.58],
    [17.4, 9.7, 14.5, 17.5, 9.9, 14.9, 20.6, 14.3, 16.1, 16, 11.7, 11.3, 18.9, 5.8, 20.5, 7.7, 8.4, 14.2, 14.8, 9.7, 6.4, 16.5, 11.9, 5.9],
    [14.9, 9.9, 15.1, 14.4, 10.1, 7.3, 17, 11.4, 16.5, 21.1, 13.8, 7.7, 17.1, 9.6, 17.2, 13.8, 8.9, 11.6, 16.4, 10.9, 6.6, 15.4, 11.4, 7.6], 
    [15.4, 9.7, 12.4, 14.6, 11.7, 16.3, 17, 9.4, 23.9, 18.4, 12.7, 10.2, 15.4, 10.1, 18.6, 23.4, 14.9, 12.7, 16.1, 10.7, 10.1, 14.3, 10.9, 5.1], 
    [0.12, 0.12, 0.13, 0.17, 0.11, 0.7, 0.14, 0.12, 0.11, 0.16, 0.12, 0.13, 0.16, 0.94, 0.2, 0.22, 0.11, 0.14, 0.17, 0.11, 0.36, 0.11, 0.93, 0.45], 
    [0.14, 0.89, 0.19, 0.14, 0.98, 0.11, 0.18, 0.89, 0.12, 0.21, 0.13, 0.97, 0.17, 0.11, 0.19, 0.13, 0.11, 0.13, 0.18, 0.12, 0.44, 0.18, 0.13, 0.25],
    [13.7, 11.1, 15.8, 12.2, 12.3, 11, 13.9, 11.5, 14.6, 19.5, 13.1, 8.2, 15.4, 9.3, 17.5, 14.9, 8.6, 11.9, 15.9, 10.5, 5.7, 13.1, 10.5, 7.7],
    [14.8, 15.6, 13.9, 17.6, 12.3, 13.3, 17.1, 9.2, 16.5, 15.6, 11.5, 8.2, 15.6, 8.6, 16.7, 15.4, 11.9, 11.2, 18.4, 12.6, 6.6, 21.7, 14, 3.8],
    [0.17, 0.12, 0.14, 0.14, 0.11, 0.99, 0.14, 0.142, 0.15, 0.16, 0.12, 0.1, 0.16, 0.84, 0.14, 0.15, 0.78, 0.88, 0.19, 0.13, 0.57, 0.17, 0.12, 0.08],
    [11.8, 6.6, 13.5, 12.9, 11.8, 8.2, 20.4, 11.3, 21.9, 14.6, 11.1, 9.1, 15.3, 9.3, 16.8, 14.4, 8.5, 11.3, 17.8, 12.1, 9.1, 14.8, 11.2, 7.2],
    [14.1, 12, 16, 11.7, 8.8, 14.4, 16.8, 10.2, 15.2, 12.6, 10.3, 11.9, 17.7, 6.4, 17.3, 15.8, 9.4, 11.6, 16.9, 11.3, 6, 19, 12.9, 5.2],
    [17.3, 9, 13.7, 23.6, 9, 9.6, 15.5, 12.1, 11.7, 18.5, 12.7, 12.6, 15.9, 8.7, 14.9, 16.5, 10.1, 9.7, 16.1, 10.7, 4.3, 21.3, 13.9, 5.9],
    [0.18, 0.88, 0.14, 0.18, 0.14, 0.12, 0.19, 0.84, 0.16, 0.18, 0.13, 0.11, 0.14, 0.85, 0.17, 0.19, 0.82, 0.12, 0.18, 0.12, 0.65, 0.16, 0.12, 0.84],
    [0.17, 0.96, 0.16, 0.14, 0.74, 0.9, 0.13, 0.12, 0.13, 0.18, 0.12, 0.15, 0.2, 0.99, 0.13, 0.17, 0.15, 0.84, 0.16, 0.12, 0.65, 0.16, 0.12, 0.51],
    [0.12, 0.14, 0.16, 0.15, 0.91, 0.1, 0.17, 0.11, 0.15, 0.17, 0.12, 0.98, 0.14, 0.74, 0.16, 0.15, 0.99, 0.12, 0.12, 0.69, 0.05, 0.17, 0.12, 0.5], 
    [15.4, 11.8, 11.8, 20.7, 10.3, 11.5, 15.4, 11.4, 16.4, 14.3, 11, 10, 17.7, 10.9, 18.1, 17.9, 10.1, 12.3, 12.6, 7.9, 6.1, 16.7, 12, 5.6]
])

# generated data from function generate_normal_distribution()
normal_distribution = np.asarray([15.3, 14.3, 15.3, 16.0, 13.5, 14.5, 16.0, 13.4, 14.0, 14.6,  14.0, 14.2, 15.8, 13.9, 15.5, 15.5, 15.3, 15.5, 15.4, 16.4, 16.1, 14.3,  16.0, 13.4 ])

# result from comparison with data from table and generated normal distribution.
# every number belong to data from table. 
# 1 - distribution is normal
# 0 - distribution isn't normal
y_train = np.asarray([1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1])