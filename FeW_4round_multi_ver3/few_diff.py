# 解析するラウンド数
round = 4

# S-Boxの確率2^-2の伝播に関する制約式の係数
freq2 = [
[1,1,0,0,1,0,0,0],
[0,0,0,0,1,1,1,0],
[-1,0,1,-1,0,0,0,0],
[1,0,0,1,-1,0,0,1],
[-1,1,0,0,0,-1,0,-1],
[0,0,-1,-1,0,1,0,-1],
[0,-1,0,-1,0,0,-1,1],
[-1,0,0,0,-1,0,1,1],
[-1,-1,0,1,-1,0,0,0],
[0,-1,-1,1,0,0,0,-1],
[-1,-1,0,0,1,-1,0,0],
[0,0,0,-1,-1,-1,-1,-1],
[1,1,-1,-1,0,0,0,0],
[1,0,1,0,-1,0,1,-1],
[0,1,0,1,0,-1,-1,0],
[0,0,1,1,0,1,-1,-1],
[0,0,-1,-1,0,-1,1,1],
[1,0,0,1,1,0,-1,0],
[0,1,0,0,1,0,-1,0],
[0,0,1,0,1,0,1,1],
[-1,1,-1,1,0,1,0,0],
[0,0,1,-1,0,1,0,1],
[0,1,0,-1,0,0,0,-1],
[1,0,0,-1,0,0,1,-1],
[0,0,1,0,1,0,-1,-1],
[0,1,0,-1,0,0,1,0],
[0,0,-1,0,0,1,1,-1]
]
# S-Boxの確率2^-2の伝播がアクティブな時に1となる変数
q_freq2=[
'Q2_0_0','Q2_0_1','Q2_0_2','Q2_0_3','Q2_0_4','Q2_0_5','Q2_0_6','Q2_0_7',
'Q2_1_0','Q2_1_1','Q2_1_2','Q2_1_3','Q2_1_4','Q2_1_5','Q2_1_6','Q2_1_7',
'Q2_2_0','Q2_2_1','Q2_2_2','Q2_2_3','Q2_2_4','Q2_2_5','Q2_2_6','Q2_2_7',
'Q2_3_0','Q2_3_1','Q2_3_2','Q2_3_3','Q2_3_4','Q2_3_5','Q2_3_6','Q2_3_7',
'Q2_4_0','Q2_4_1','Q2_4_2','Q2_4_3','Q2_4_4','Q2_4_5','Q2_4_6','Q2_4_7',
'Q2_5_0','Q2_5_1','Q2_5_2','Q2_5_3','Q2_5_4','Q2_5_5','Q2_5_6','Q2_5_7',
'Q2_6_0','Q2_6_1','Q2_6_2','Q2_6_3','Q2_6_4','Q2_6_5','Q2_6_6','Q2_6_7',
'Q2_7_0','Q2_7_1','Q2_7_2','Q2_7_3','Q2_7_4','Q2_7_5','Q2_7_6','Q2_7_7',
'Q2_8_0','Q2_8_1','Q2_8_2','Q2_8_3','Q2_8_4','Q2_8_5','Q2_8_6','Q2_8_7',
'Q2_9_0','Q2_9_1','Q2_9_2','Q2_9_3','Q2_9_4','Q2_9_5','Q2_9_6','Q2_9_7',
'Q2_10_0','Q2_10_1','Q2_10_2','Q2_10_3','Q2_10_4','Q2_10_5','Q2_10_6','Q2_10_7',
'Q2_11_0','Q2_11_1','Q2_11_2','Q2_11_3','Q2_11_4','Q2_11_5','Q2_11_6','Q2_11_7',
'Q2_12_0','Q2_12_1','Q2_12_2','Q2_12_3','Q2_12_4','Q2_12_5','Q2_12_6','Q2_12_7',
'Q2_13_0','Q2_13_1','Q2_13_2','Q2_13_3','Q2_13_4','Q2_13_5','Q2_13_6','Q2_13_7',
'Q2_14_0','Q2_14_1','Q2_14_2','Q2_14_3','Q2_14_4','Q2_14_5','Q2_14_6','Q2_14_7',
'Q2_15_0','Q2_15_1','Q2_15_2','Q2_15_3','Q2_15_4','Q2_15_5','Q2_15_6','Q2_15_7',
'Q2_16_0','Q2_16_1','Q2_16_2','Q2_16_3','Q2_16_4','Q2_16_5','Q2_16_6','Q2_16_7',
'Q2_17_0','Q2_17_1','Q2_17_2','Q2_17_3','Q2_17_4','Q2_17_5','Q2_17_6','Q2_17_7',
'Q2_18_0','Q2_18_1','Q2_18_2','Q2_18_3','Q2_18_4','Q2_18_5','Q2_18_6','Q2_18_7',
'Q2_19_0','Q2_19_1','Q2_19_2','Q2_19_3','Q2_19_4','Q2_19_5','Q2_19_6','Q2_19_7',
'Q2_20_0','Q2_20_1','Q2_20_2','Q2_20_3','Q2_20_4','Q2_20_5','Q2_20_6','Q2_20_7',
'Q2_21_0','Q2_21_1','Q2_21_2','Q2_21_3','Q2_21_4','Q2_21_5','Q2_21_6','Q2_21_7',
'Q2_22_0','Q2_22_1','Q2_22_2','Q2_22_3','Q2_22_4','Q2_22_5','Q2_22_6','Q2_22_7',
'Q2_23_0','Q2_23_1','Q2_23_2','Q2_23_3','Q2_23_4','Q2_23_5','Q2_23_6','Q2_23_7',
'Q2_24_0','Q2_24_1','Q2_24_2','Q2_24_3','Q2_24_4','Q2_24_5','Q2_24_6','Q2_24_7',
'Q2_25_0','Q2_25_1','Q2_25_2','Q2_25_3','Q2_25_4','Q2_25_5','Q2_25_6','Q2_25_7',
'Q2_26_0','Q2_26_1','Q2_26_2','Q2_26_3','Q2_26_4','Q2_26_5','Q2_26_6','Q2_26_7',
'Q2_27_0','Q2_27_1','Q2_27_2','Q2_27_3','Q2_27_4','Q2_27_5','Q2_27_6','Q2_27_7',
'Q2_28_0','Q2_28_1','Q2_28_2','Q2_28_3','Q2_28_4','Q2_28_5','Q2_28_6','Q2_28_7',
'Q2_29_0','Q2_29_1','Q2_29_2','Q2_29_3','Q2_29_4','Q2_29_5','Q2_29_6','Q2_29_7',
'Q2_30_0','Q2_30_1','Q2_30_2','Q2_30_3','Q2_30_4','Q2_30_5','Q2_30_6','Q2_30_7',
'Q2_31_0','Q2_31_1','Q2_31_2','Q2_31_3','Q2_31_4','Q2_31_5','Q2_31_6','Q2_31_7'
]
# S-Boxの確率2^-3の伝播に関する制約式の係数
freq3 = [
[0,1,1,1,0,1,0,0],
[1,0,1,0,0,1,1,0],
[-1,-1,1,0,1,0,1,1],
[0,0,0,0,1,1,1,1],
[0,-1,0,0,-1,-1,1,-1],
[1,-1,-1,0,0,-1,1,0],
[1,0,1,1,0,-1,0,-1],
[-1,1,0,-1,-1,-1,0,0],
[0,-1,-1,-1,0,1,-1,0],
[1,-1,1,-1,-1,0,0,0],
[1,1,0,0,-1,1,0,-1],
[1,1,1,0,1,0,0,1],
[1,1,0,1,0,-1,-1,0],
[-1,0,-1,-1,0,-1,-1,1],
[1,1,-1,-1,-1,0,-1,0],
[-1,-1,-1,1,0,0,1,1],
[0,0,-1,-1,-1,-1,1,1],
[-1,1,0,0,-1,0,-1,1],
[1,0,1,-1,0,-1,-1,1],
[0,0,0,1,1,0,1,1],
[0,1,1,1,-1,0,-1,0],
[0,-1,-1,1,1,-1,0,-1],
[1,-1,0,-1,0,-1,-1,-1],
[0,0,0,1,1,1,0,1],
[-1,-1,1,1,0,0,-1,1],
[-1,1,0,1,1,-1,1,0],
[-1,0,0,1,-1,1,-1,-1],
[-1,1,-1,0,1,0,-1,-1],
[-1,-1,1,-1,0,0,-1,-1],
[-1,1,1,0,0,1,0,1],
[1,-1,-1,1,-1,0,-1,1],
[1,0,1,1,0,0,1,0],
[0,1,0,1,0,1,1,1],
[-1,1,-1,-1,0,-1,0,0],
[0,0,1,1,0,1,-1,1],
[1,0,0,1,1,1,1,0],
[-1,0,-1,-1,-1,0,1,-1],
[1,1,0,-1,1,-1,1,-1],
[-1,0,1,1,1,1,0,0],
[1,1,0,1,-1,0,0,-1],
[-1,-1,0,1,1,0,0,1],
[1,-1,0,-1,0,1,1,1],
[0,-1,1,-1,-1,0,0,-1]
]
# S-Boxの確率2^-3の伝播がアクティブな時に1となる変数
q_freq3=[
'Q3_0_0','Q3_0_1','Q3_0_2','Q3_0_3','Q3_0_4','Q3_0_5','Q3_0_6','Q3_0_7',
'Q3_1_0','Q3_1_1','Q3_1_2','Q3_1_3','Q3_1_4','Q3_1_5','Q3_1_6','Q3_1_7',
'Q3_2_0','Q3_2_1','Q3_2_2','Q3_2_3','Q3_2_4','Q3_2_5','Q3_2_6','Q3_2_7',
'Q3_3_0','Q3_3_1','Q3_3_2','Q3_3_3','Q3_3_4','Q3_3_5','Q3_3_6','Q3_3_7',
'Q3_4_0','Q3_4_1','Q3_4_2','Q3_4_3','Q3_4_4','Q3_4_5','Q3_4_6','Q3_4_7',
'Q3_5_0','Q3_5_1','Q3_5_2','Q3_5_3','Q3_5_4','Q3_5_5','Q3_5_6','Q3_5_7',
'Q3_6_0','Q3_6_1','Q3_6_2','Q3_6_3','Q3_6_4','Q3_6_5','Q3_6_6','Q3_6_7',
'Q3_7_0','Q3_7_1','Q3_7_2','Q3_7_3','Q3_7_4','Q3_7_5','Q3_7_6','Q3_7_7',
'Q3_8_0','Q3_8_1','Q3_8_2','Q3_8_3','Q3_8_4','Q3_8_5','Q3_8_6','Q3_8_7',
'Q3_9_0','Q3_9_1','Q3_9_2','Q3_9_3','Q3_9_4','Q3_9_5','Q3_9_6','Q3_9_7',
'Q3_10_0','Q3_10_1','Q3_10_2','Q3_10_3','Q3_10_4','Q3_10_5','Q3_10_6','Q3_10_7',
'Q3_11_0','Q3_11_1','Q3_11_2','Q3_11_3','Q3_11_4','Q3_11_5','Q3_11_6','Q3_11_7',
'Q3_12_0','Q3_12_1','Q3_12_2','Q3_12_3','Q3_12_4','Q3_12_5','Q3_12_6','Q3_12_7',
'Q3_13_0','Q3_13_1','Q3_13_2','Q3_13_3','Q3_13_4','Q3_13_5','Q3_13_6','Q3_13_7',
'Q3_14_0','Q3_14_1','Q3_14_2','Q3_14_3','Q3_14_4','Q3_14_5','Q3_14_6','Q3_14_7',
'Q3_15_0','Q3_15_1','Q3_15_2','Q3_15_3','Q3_15_4','Q3_15_5','Q3_15_6','Q3_15_7',
'Q3_16_0','Q3_16_1','Q3_16_2','Q3_16_3','Q3_16_4','Q3_16_5','Q3_16_6','Q3_16_7',
'Q3_17_0','Q3_17_1','Q3_17_2','Q3_17_3','Q3_17_4','Q3_17_5','Q3_17_6','Q3_17_7',
'Q3_18_0','Q3_18_1','Q3_18_2','Q3_18_3','Q3_18_4','Q3_18_5','Q3_18_6','Q3_18_7',
'Q3_19_0','Q3_19_1','Q3_19_2','Q3_19_3','Q3_19_4','Q3_19_5','Q3_19_6','Q3_19_7',
'Q3_20_0','Q3_20_1','Q3_20_2','Q3_20_3','Q3_20_4','Q3_20_5','Q3_20_6','Q3_20_7',
'Q3_21_0','Q3_21_1','Q3_21_2','Q3_21_3','Q3_21_4','Q3_21_5','Q3_21_6','Q3_21_7',
'Q3_22_0','Q3_22_1','Q3_22_2','Q3_22_3','Q3_22_4','Q3_22_5','Q3_22_6','Q3_22_7',
'Q3_23_0','Q3_23_1','Q3_23_2','Q3_23_3','Q3_23_4','Q3_23_5','Q3_23_6','Q3_23_7',
'Q3_24_0','Q3_24_1','Q3_24_2','Q3_24_3','Q3_24_4','Q3_24_5','Q3_24_6','Q3_24_7',
'Q3_25_0','Q3_25_1','Q3_25_2','Q3_25_3','Q3_25_4','Q3_25_5','Q3_25_6','Q3_25_7',
'Q3_26_0','Q3_26_1','Q3_26_2','Q3_26_3','Q3_26_4','Q3_26_5','Q3_26_6','Q3_26_7',
'Q3_27_0','Q3_27_1','Q3_27_2','Q3_27_3','Q3_27_4','Q3_27_5','Q3_27_6','Q3_27_7',
'Q3_28_0','Q3_28_1','Q3_28_2','Q3_28_3','Q3_28_4','Q3_28_5','Q3_28_6','Q3_28_7',
'Q3_29_0','Q3_29_1','Q3_29_2','Q3_29_3','Q3_29_4','Q3_29_5','Q3_29_6','Q3_29_7',
'Q3_30_0','Q3_30_1','Q3_30_2','Q3_30_3','Q3_30_4','Q3_30_5','Q3_30_6','Q3_30_7',
'Q3_31_0','Q3_31_1','Q3_31_2','Q3_31_3','Q3_31_4','Q3_31_5','Q3_31_6','Q3_31_7'
]
# S-Boxの入出力
var = [
['X0_0','X0_1','X0_2','X0_3','Y0_0','Y0_1','Y0_2','Y0_3'],
['X0_4','X0_5','X0_6','X0_7','Y0_4','Y0_5','Y0_6','Y0_7'],
['X0_8','X0_9','X0_10','X0_11','Y0_8','Y0_9','Y0_10','Y0_11'],
['X0_12','X0_13','X0_14','X0_15','Y0_12','Y0_13','Y0_14','Y0_15'],
['X0_16','X0_17','X0_18','X0_19','Y0_16','Y0_17','Y0_18','Y0_19'],
['X0_20','X0_21','X0_22','X0_23','Y0_20','Y0_21','Y0_22','Y0_23'],
['X0_24','X0_25','X0_26','X0_27','Y0_24','Y0_25','Y0_26','Y0_27'],
['X0_28','X0_29','X0_30','X0_31','Y0_28','Y0_29','Y0_30','Y0_31'],
['X1_0','X1_1','X1_2','X1_3','Y1_0','Y1_1','Y1_2','Y1_3'],
['X1_4','X1_5','X1_6','X1_7','Y1_4','Y1_5','Y1_6','Y1_7'],
['X1_8','X1_9','X1_10','X1_11','Y1_8','Y1_9','Y1_10','Y1_11'],
['X1_12','X1_13','X1_14','X1_15','Y1_12','Y1_13','Y1_14','Y1_15'],
['X1_16','X1_17','X1_18','X1_19','Y1_16','Y1_17','Y1_18','Y1_19'],
['X1_20','X1_21','X1_22','X1_23','Y1_20','Y1_21','Y1_22','Y1_23'],
['X1_24','X1_25','X1_26','X1_27','Y1_24','Y1_25','Y1_26','Y1_27'],
['X1_28','X1_29','X1_30','X1_31','Y1_28','Y1_29','Y1_30','Y1_31'],
['X2_0','X2_1','X2_2','X2_3','Y2_0','Y2_1','Y2_2','Y2_3'],
['X2_4','X2_5','X2_6','X2_7','Y2_4','Y2_5','Y2_6','Y2_7'],
['X2_8','X2_9','X2_10','X2_11','Y2_8','Y2_9','Y2_10','Y2_11'],
['X2_12','X2_13','X2_14','X2_15','Y2_12','Y2_13','Y2_14','Y2_15'],
['X2_16','X2_17','X2_18','X2_19','Y2_16','Y2_17','Y2_18','Y2_19'],
['X2_20','X2_21','X2_22','X2_23','Y2_20','Y2_21','Y2_22','Y2_23'],
['X2_24','X2_25','X2_26','X2_27','Y2_24','Y2_25','Y2_26','Y2_27'],
['X2_28','X2_29','X2_30','X2_31','Y2_28','Y2_29','Y2_30','Y2_31'],
['X3_0','X3_1','X3_2','X3_3','Y3_0','Y3_1','Y3_2','Y3_3'],
['X3_4','X3_5','X3_6','X3_7','Y3_4','Y3_5','Y3_6','Y3_7'],
['X3_8','X3_9','X3_10','X3_11','Y3_8','Y3_9','Y3_10','Y3_11'],
['X3_12','X3_13','X3_14','X3_15','Y3_12','Y3_13','Y3_14','Y3_15'],
['X3_16','X3_17','X3_18','X3_19','Y3_16','Y3_17','Y3_18','Y3_19'],
['X3_20','X3_21','X3_22','X3_23','Y3_20','Y3_21','Y3_22','Y3_23'],
['X3_24','X3_25','X3_26','X3_27','Y3_24','Y3_25','Y3_26','Y3_27'],
['X3_28','X3_29','X3_30','X3_31','Y3_28','Y3_29','Y3_30','Y3_31'],
['X4_0','X4_1','X4_2','X4_3','Y4_0','Y4_1','Y4_2','Y4_3'],
['X4_4','X4_5','X4_6','X4_7','Y4_4','Y4_5','Y4_6','Y4_7'],
['X4_8','X4_9','X4_10','X4_11','Y4_8','Y4_9','Y4_10','Y4_11'],
['X4_12','X4_13','X4_14','X4_15','Y4_12','Y4_13','Y4_14','Y4_15'],
['X4_16','X4_17','X4_18','X4_19','Y4_16','Y4_17','Y4_18','Y4_19'],
['X4_20','X4_21','X4_22','X4_23','Y4_20','Y4_21','Y4_22','Y4_23'],
['X4_24','X4_25','X4_26','X4_27','Y4_24','Y4_25','Y4_26','Y4_27'],
['X4_28','X4_29','X4_30','X4_31','Y4_28','Y4_29','Y4_30','Y4_31'],
['X5_0','X5_1','X5_2','X5_3','Y5_0','Y5_1','Y5_2','Y5_3'],
['X5_4','X5_5','X5_6','X5_7','Y5_4','Y5_5','Y5_6','Y5_7'],
['X5_8','X5_9','X5_10','X5_11','Y5_8','Y5_9','Y5_10','Y5_11'],
['X5_12','X5_13','X5_14','X5_15','Y5_12','Y5_13','Y5_14','Y5_15'],
['X5_16','X5_17','X5_18','X5_19','Y5_16','Y5_17','Y5_18','Y5_19'],
['X5_20','X5_21','X5_22','X5_23','Y5_20','Y5_21','Y5_22','Y5_23'],
['X5_24','X5_25','X5_26','X5_27','Y5_24','Y5_25','Y5_26','Y5_27'],
['X5_28','X5_29','X5_30','X5_31','Y5_28','Y5_29','Y5_30','Y5_31'],
['X6_0','X6_1','X6_2','X6_3','Y6_0','Y6_1','Y6_2','Y6_3'],
['X6_4','X6_5','X6_6','X6_7','Y6_4','Y6_5','Y6_6','Y6_7'],
['X6_8','X6_9','X6_10','X6_11','Y6_8','Y6_9','Y6_10','Y6_11'],
['X6_12','X6_13','X6_14','X6_15','Y6_12','Y6_13','Y6_14','Y6_15'],
['X6_16','X6_17','X6_18','X6_19','Y6_16','Y6_17','Y6_18','Y6_19'],
['X6_20','X6_21','X6_22','X6_23','Y6_20','Y6_21','Y6_22','Y6_23'],
['X6_24','X6_25','X6_26','X6_27','Y6_24','Y6_25','Y6_26','Y6_27'],
['X6_28','X6_29','X6_30','X6_31','Y6_28','Y6_29','Y6_30','Y6_31'],
['X7_0','X7_1','X7_2','X7_3','Y7_0','Y7_1','Y7_2','Y7_3'],
['X7_4','X7_5','X7_6','X7_7','Y7_4','Y7_5','Y7_6','Y7_7'],
['X7_8','X7_9','X7_10','X7_11','Y7_8','Y7_9','Y7_10','Y7_11'],
['X7_12','X7_13','X7_14','X7_15','Y7_12','Y7_13','Y7_14','Y7_15'],
['X7_16','X7_17','X7_18','X7_19','Y7_16','Y7_17','Y7_18','Y7_19'],
['X7_20','X7_21','X7_22','X7_23','Y7_20','Y7_21','Y7_22','Y7_23'],
['X7_24','X7_25','X7_26','X7_27','Y7_24','Y7_25','Y7_26','Y7_27'],
['X7_28','X7_29','X7_30','X7_31','Y7_28','Y7_29','Y7_30','Y7_31'],
['X8_0','X8_1','X8_2','X8_3','Y8_0','Y8_1','Y8_2','Y8_3'],
['X8_4','X8_5','X8_6','X8_7','Y8_4','Y8_5','Y8_6','Y8_7'],
['X8_8','X8_9','X8_10','X8_11','Y8_8','Y8_9','Y8_10','Y8_11'],
['X8_12','X8_13','X8_14','X8_15','Y8_12','Y8_13','Y8_14','Y8_15'],
['X8_16','X8_17','X8_18','X8_19','Y8_16','Y8_17','Y8_18','Y8_19'],
['X8_20','X8_21','X8_22','X8_23','Y8_20','Y8_21','Y8_22','Y8_23'],
['X8_24','X8_25','X8_26','X8_27','Y8_24','Y8_25','Y8_26','Y8_27'],
['X8_28','X8_29','X8_30','X8_31','Y8_28','Y8_29','Y8_30','Y8_31'],
['X9_0','X9_1','X9_2','X9_3','Y9_0','Y9_1','Y9_2','Y9_3'],
['X9_4','X9_5','X9_6','X9_7','Y9_4','Y9_5','Y9_6','Y9_7'],
['X9_8','X9_9','X9_10','X9_11','Y9_8','Y9_9','Y9_10','Y9_11'],
['X9_12','X9_13','X9_14','X9_15','Y9_12','Y9_13','Y9_14','Y9_15'],
['X9_16','X9_17','X9_18','X9_19','Y9_16','Y9_17','Y9_18','Y9_19'],
['X9_20','X9_21','X9_22','X9_23','Y9_20','Y9_21','Y9_22','Y9_23'],
['X9_24','X9_25','X9_26','X9_27','Y9_24','Y9_25','Y9_26','Y9_27'],
['X9_28','X9_29','X9_30','X9_31','Y9_28','Y9_29','Y9_30','Y9_31'],
['X10_0','X10_1','X10_2','X10_3','Y10_0','Y10_1','Y10_2','Y10_3'],
['X10_4','X10_5','X10_6','X10_7','Y10_4','Y10_5','Y10_6','Y10_7'],
['X10_8','X10_9','X10_10','X10_11','Y10_8','Y10_9','Y10_10','Y10_11'],
['X10_12','X10_13','X10_14','X10_15','Y10_12','Y10_13','Y10_14','Y10_15'],
['X10_16','X10_17','X10_18','X10_19','Y10_16','Y10_17','Y10_18','Y10_19'],
['X10_20','X10_21','X10_22','X10_23','Y10_20','Y10_21','Y10_22','Y10_23'],
['X10_24','X10_25','X10_26','X10_27','Y10_24','Y10_25','Y10_26','Y10_27'],
['X10_28','X10_29','X10_30','X10_31','Y10_28','Y10_29','Y10_30','Y10_31'],
['X11_0','X11_1','X11_2','X11_3','Y11_0','Y11_1','Y11_2','Y11_3'],
['X11_4','X11_5','X11_6','X11_7','Y11_4','Y11_5','Y11_6','Y11_7'],
['X11_8','X11_9','X11_10','X11_11','Y11_8','Y11_9','Y11_10','Y11_11'],
['X11_12','X11_13','X11_14','X11_15','Y11_12','Y11_13','Y11_14','Y11_15'],
['X11_16','X11_17','X11_18','X11_19','Y11_16','Y11_17','Y11_18','Y11_19'],
['X11_20','X11_21','X11_22','X11_23','Y11_20','Y11_21','Y11_22','Y11_23'],
['X11_24','X11_25','X11_26','X11_27','Y11_24','Y11_25','Y11_26','Y11_27'],
['X11_28','X11_29','X11_30','X11_31','Y11_28','Y11_29','Y11_30','Y11_31'],
['X12_0','X12_1','X12_2','X12_3','Y12_0','Y12_1','Y12_2','Y12_3'],
['X12_4','X12_5','X12_6','X12_7','Y12_4','Y12_5','Y12_6','Y12_7'],
['X12_8','X12_9','X12_10','X12_11','Y12_8','Y12_9','Y12_10','Y12_11'],
['X12_12','X12_13','X12_14','X12_15','Y12_12','Y12_13','Y12_14','Y12_15'],
['X12_16','X12_17','X12_18','X12_19','Y12_16','Y12_17','Y12_18','Y12_19'],
['X12_20','X12_21','X12_22','X12_23','Y12_20','Y12_21','Y12_22','Y12_23'],
['X12_24','X12_25','X12_26','X12_27','Y12_24','Y12_25','Y12_26','Y12_27'],
['X12_28','X12_29','X12_30','X12_31','Y12_28','Y12_29','Y12_30','Y12_31'],
['X13_0','X13_1','X13_2','X13_3','Y13_0','Y13_1','Y13_2','Y13_3'],
['X13_4','X13_5','X13_6','X13_7','Y13_4','Y13_5','Y13_6','Y13_7'],
['X13_8','X13_9','X13_10','X13_11','Y13_8','Y13_9','Y13_10','Y13_11'],
['X13_12','X13_13','X13_14','X13_15','Y13_12','Y13_13','Y13_14','Y13_15'],
['X13_16','X13_17','X13_18','X13_19','Y13_16','Y13_17','Y13_18','Y13_19'],
['X13_20','X13_21','X13_22','X13_23','Y13_20','Y13_21','Y13_22','Y13_23'],
['X13_24','X13_25','X13_26','X13_27','Y13_24','Y13_25','Y13_26','Y13_27'],
['X13_28','X13_29','X13_30','X13_31','Y13_28','Y13_29','Y13_30','Y13_31'],
['X14_0','X14_1','X14_2','X14_3','Y14_0','Y14_1','Y14_2','YX1414_3'],
['X14_4','X14_5','X14_6','X14_7','Y14_4','Y14_5','Y14_6','Y14_7'],
['X14_8','X14_9','X14_10','X14_11','Y14_8','Y14_9','Y14_10','Y14_11'],
['X14_12','X14_13','X14_14','X14_15','Y14_12','Y14_13','Y14_14','Y14_15'],
['X14_16','X14_17','X14_18','X14_19','Y14_16','Y14_17','Y14_18','Y14_19'],
['X14_20','X14_21','X14_22','X14_23','Y14_20','Y14_21','Y14_22','Y14_23'],
['X14_24','X14_25','X14_26','X14_27','Y14_24','Y14_25','Y14_26','Y14_27'],
['X14_28','X14_29','X14_30','X14_31','Y14_28','Y14_29','Y14_30','Y14_31'],
['X15_0','X15_1','X15_2','X15_3','Y15_0','Y15_1','Y15_2','Y15_3'],
['X15_4','X15_5','X15_6','X15_7','Y15_4','Y15_5','Y15_6','Y15_7'],
['X15_8','X15_9','X15_10','X15_11','Y15_8','Y15_9','Y15_10','Y15_11'],
['X15_12','X15_13','X15_14','X15_15','Y15_12','Y15_13','Y15_14','Y15_15'],
['X15_16','X15_17','X15_18','X15_19','Y15_16','Y15_17','Y15_18','Y15_19'],
['X15_20','X15_21','X15_22','X15_23','Y15_20','Y15_21','Y15_22','Y15_23'],
['X15_24','X15_25','X15_26','X15_27','Y15_24','Y15_25','Y15_26','Y15_27'],
['X15_28','X15_29','X15_30','X15_31','Y15_28','Y15_29','Y15_30','Y15_31'],
['X16_0','X16_1','X16_2','X16_3','Y16_0','Y16_1','Y16_2','Y16_3'],
['X16_4','X16_5','X16_6','X16_7','Y16_4','Y16_5','Y16_6','Y16_7'],
['X16_8','X16_9','X16_10','X16_11','Y16_8','Y16_9','Y16_10','Y16_11'],
['X16_12','X16_13','X16_14','X16_15','Y16_12','Y16_13','Y16_14','Y16_15'],
['X16_16','X16_17','X16_18','X16_19','Y16_16','Y16_17','Y16_18','Y16_19'],
['X16_20','X16_21','X16_22','X16_23','Y16_20','Y16_21','Y16_22','Y16_23'],
['X16_24','X16_25','X16_26','X16_27','Y16_24','Y16_25','Y16_26','Y16_27'],
['X16_28','X16_29','X16_30','X16_31','Y16_28','Y16_29','Y16_30','Y16_31'],
['X17_0','X17_1','X17_2','X17_3','Y17_0','Y17_1','Y17_2','Y17_3'],
['X17_4','X17_5','X17_6','X17_7','Y17_4','Y17_5','Y17_6','Y17_7'],
['X17_8','X17_9','X17_10','X17_11','Y17_8','Y17_9','Y17_10','Y17_11'],
['X17_12','X17_13','X17_14','X17_15','Y17_12','Y17_13','Y17_14','Y17_15'],
['X17_16','X17_17','X17_18','X17_19','Y17_16','Y17_17','Y17_18','Y17_19'],
['X17_20','X17_21','X17_22','X17_23','Y17_20','Y17_21','Y17_22','Y17_23'],
['X17_24','X17_25','X17_26','X17_27','Y17_24','Y17_25','Y17_26','Y17_27'],
['X17_28','X17_29','X17_30','X17_31','Y17_28','Y17_29','Y17_30','Y17_31'],
['X18_0','X18_1','X18_2','X18_3','Y18_0','Y18_1','Y18_2','Y18_3'],
['X18_4','X18_5','X18_6','X18_7','Y18_4','Y18_5','Y18_6','Y18_7'],
['X18_8','X18_9','X18_10','X18_11','Y18_8','Y18_9','Y18_10','Y18_11'],
['X18_12','X18_13','X18_14','X18_15','Y18_12','Y18_13','Y18_14','Y18_15'],
['X18_16','X18_17','X18_18','X18_19','Y18_16','Y18_17','Y18_18','Y18_19'],
['X18_20','X18_21','X18_22','X18_23','Y18_20','Y18_21','Y18_22','Y18_23'],
['X18_24','X18_25','X18_26','X18_27','Y18_24','Y18_25','Y18_26','Y18_27'],
['X18_28','X18_29','X18_30','X18_31','Y18_28','Y18_29','Y18_30','Y18_31'],
['X19_0','X19_1','X19_2','X19_3','Y19_0','Y19_1','Y19_2','Y19_3'],
['X19_4','X19_5','X19_6','X19_7','Y19_4','Y19_5','Y19_6','Y19_7'],
['X19_8','X19_9','X19_10','X19_11','Y19_8','Y19_9','Y19_10','Y19_11'],
['X19_12','X19_13','X19_14','X19_15','Y19_12','Y19_13','Y19_14','Y19_15'],
['X19_16','X19_17','X19_18','X19_19','Y19_16','Y19_17','Y19_18','Y19_19'],
['X19_20','X19_21','X19_22','X19_23','Y19_20','Y19_21','Y19_22','Y19_23'],
['X19_24','X19_25','X19_26','X19_27','Y19_24','Y19_25','Y19_26','Y19_27'],
['X19_28','X19_29','X19_30','X19_31','Y19_28','Y19_29','Y19_30','Y19_31'],
['X20_0','X20_1','X20_2','X20_3','Y20_0','Y20_1','Y20_2','Y20_3'],
['X20_4','X20_5','X20_6','X20_7','Y20_4','Y20_5','Y20_6','Y20_7'],
['X20_8','X20_9','X20_10','X20_11','Y20_8','Y20_9','Y20_10','Y20_11'],
['X20_12','X20_13','X20_14','X20_15','Y20_12','Y20_13','Y20_14','Y20_15'],
['X20_16','X20_17','X20_18','X20_19','Y20_16','Y20_17','Y20_18','Y20_19'],
['X20_20','X20_21','X20_22','X20_23','Y20_20','Y20_21','Y20_22','Y20_23'],
['X20_24','X20_25','X20_26','X20_27','Y20_24','Y20_25','Y20_26','Y20_27'],
['X20_28','X20_29','X20_30','X20_31','Y20_28','Y20_29','Y20_30','Y20_31'],
['X21_0','X21_1','X21_2','X21_3','Y21_0','Y21_1','Y21_2','Y21_3'],
['X21_4','X21_5','X21_6','X21_7','Y21_4','Y21_5','Y21_6','Y21_7'],
['X21_8','X21_9','X21_10','X21_11','Y21_8','Y21_9','Y21_10','Y21_11'],
['X21_12','X21_13','X21_14','X21_15','Y21_12','Y21_13','Y21_14','Y21_15'],
['X21_16','X21_17','X21_18','X21_19','Y21_16','Y21_17','Y21_18','Y21_19'],
['X21_20','X21_21','X21_22','X21_23','Y21_20','Y21_21','Y21_22','Y21_23'],
['X21_24','X21_25','X21_26','X21_27','Y21_24','Y21_25','Y21_26','Y21_27'],
['X21_28','X21_29','X21_30','X21_31','Y21_28','Y21_29','Y21_30','Y21_31'],
['X22_0','X22_1','X22_2','X22_3','Y22_0','Y22_1','Y22_2','Y22_3'],
['X22_4','X22_5','X22_6','X22_7','Y22_4','Y22_5','Y22_6','Y22_7'],
['X22_8','X22_9','X22_10','X22_11','Y22_8','Y22_9','Y22_10','Y22_11'],
['X22_12','X22_13','X22_14','X22_15','Y22_12','Y22_13','Y22_14','Y22_15'],
['X22_16','X22_17','X22_18','X22_19','Y22_16','Y22_17','Y22_18','Y22_19'],
['X22_20','X22_21','X22_22','X22_23','Y22_20','Y22_21','Y22_22','Y22_23'],
['X22_24','X22_25','X22_26','X22_27','Y22_24','Y22_25','Y22_26','Y22_27'],
['X22_28','X22_29','X22_30','X22_31','Y22_28','Y22_29','Y22_30','Y22_31'],
['X23_0','X23_1','X23_2','X23_3','Y23_0','Y23_1','Y23_2','Y23_3'],
['X23_4','X23_5','X23_6','X23_7','Y23_4','Y23_5','Y23_6','Y23_7'],
['X23_8','X23_9','X23_10','X23_11','Y23_8','Y23_9','Y23_10','Y23_11'],
['X23_12','X23_13','X23_14','X23_15','Y23_12','Y23_13','Y23_14','Y23_15'],
['X23_16','X23_17','X23_18','X23_19','Y23_16','Y23_17','Y23_18','Y23_19'],
['X23_20','X23_21','X23_22','X23_23','Y23_20','Y23_21','Y23_22','Y23_23'],
['X23_24','X23_25','X23_26','X23_27','Y23_24','Y23_25','Y23_26','Y23_27'],
['X23_28','X23_29','X23_30','X23_31','Y23_28','Y23_29','Y23_30','Y23_31'],
['X24_0','X24_1','X24_2','X24_3','Y24_0','Y24_1','Y24_2','Y24_3'],
['X24_4','X24_5','X24_6','X24_7','Y24_4','Y24_5','Y24_6','Y24_7'],
['X24_8','X24_9','X24_10','X24_11','Y24_8','Y24_9','Y24_10','Y24_11'],
['X24_12','X24_13','X24_14','X24_15','Y24_12','Y24_13','Y24_14','Y24_15'],
['X24_16','X24_17','X24_18','X24_19','Y24_16','Y24_17','Y24_18','Y24_19'],
['X24_20','X24_21','X24_22','X24_23','Y24_20','Y24_21','Y24_22','Y24_23'],
['X24_24','X24_25','X24_26','X24_27','Y24_24','Y24_25','Y24_26','Y24_27'],
['X24_28','X24_29','X24_30','X24_31','Y24_28','Y24_29','Y24_30','Y24_31'],
['X25_0','X25_1','X25_2','X25_3','Y25_0','Y25_1','Y25_2','Y25_3'],
['X25_4','X25_5','X25_6','X25_7','Y25_4','Y25_5','Y25_6','Y25_7'],
['X25_8','X25_9','X25_10','X25_11','Y25_8','Y25_9','Y25_10','Y25_11'],
['X25_12','X25_13','X25_14','X25_15','Y25_12','Y25_13','Y25_14','Y25_15'],
['X25_16','X25_17','X25_18','X25_19','Y25_16','Y25_17','Y25_18','Y25_19'],
['X25_20','X25_21','X25_22','X25_23','Y25_20','Y25_21','Y25_22','Y25_23'],
['X25_24','X25_25','X25_26','X25_27','Y25_24','Y25_25','Y25_26','Y25_27'],
['X25_28','X25_29','X25_30','X25_31','Y25_28','Y25_29','Y25_30','Y25_31'],
['X26_0','X26_1','X26_2','X26_3','Y26_0','Y26_1','Y26_2','Y26_3'],
['X26_4','X26_5','X26_6','X26_7','Y26_4','Y26_5','Y26_6','Y26_7'],
['X26_8','X26_9','X26_10','X26_11','Y26_8','Y26_9','Y26_10','Y26_11'],
['X26_12','X26_13','X26_14','X26_15','Y26_12','Y26_13','Y26_14','Y26_15'],
['X26_16','X26_17','X26_18','X26_19','Y26_16','Y26_17','Y26_18','Y26_19'],
['X26_20','X26_21','X26_22','X26_23','Y26_20','Y26_21','Y26_22','Y26_23'],
['X26_24','X26_25','X26_26','X26_27','Y26_24','Y26_25','Y26_26','Y26_27'],
['X26_28','X26_29','X26_30','X26_31','Y26_28','Y26_29','Y26_30','Y26_31'],
['X27_0','X27_1','X27_2','X27_3','Y27_0','Y27_1','Y27_2','Y27_3'],
['X27_4','X27_5','X27_6','X27_7','Y27_4','Y27_5','Y27_6','Y27_7'],
['X27_8','X27_9','X27_10','X27_11','Y27_8','Y27_9','Y27_10','Y27_11'],
['X27_12','X27_13','X27_14','X27_15','Y27_12','Y27_13','Y27_14','Y27_15'],
['X27_16','X27_17','X27_18','X27_19','Y27_16','Y27_17','Y27_18','Y27_19'],
['X27_20','X27_21','X27_22','X27_23','Y27_20','Y27_21','Y27_22','Y27_23'],
['X27_24','X27_25','X27_26','X27_27','Y27_24','Y27_25','Y27_26','Y27_27'],
['X27_28','X27_29','X27_30','X27_31','Y27_28','Y27_29','Y27_30','Y27_31'],
['X28_0','X28_1','X28_2','X28_3','Y28_0','Y28_1','Y28_2','Y28_3'],
['X28_4','X28_5','X28_6','X28_7','Y28_4','Y28_5','Y28_6','Y28_7'],
['X28_8','X28_9','X28_10','X28_11','Y28_8','Y28_9','Y28_10','Y28_11'],
['X28_12','X28_13','X28_14','X28_15','Y28_12','Y28_13','Y28_14','Y28_15'],
['X28_16','X28_17','X28_18','X28_19','Y28_16','Y28_17','Y28_18','Y28_19'],
['X28_20','X28_21','X28_22','X28_23','Y28_20','Y28_21','Y28_22','Y28_23'],
['X28_24','X28_25','X28_26','X28_27','Y28_24','Y28_25','Y28_26','Y28_27'],
['X28_28','X28_29','X28_30','X28_31','Y28_28','Y28_29','Y28_30','Y28_31'],
['X29_0','X29_1','X29_2','X29_3','Y29_0','Y29_1','Y29_2','Y29_3'],
['X29_4','X29_5','X29_6','X29_7','Y29_4','Y29_5','Y29_6','Y29_7'],
['X29_8','X29_9','X29_10','X29_11','Y29_8','Y29_9','Y29_10','Y29_11'],
['X29_12','X29_13','X29_14','X29_15','Y29_12','Y29_13','Y29_14','Y29_15'],
['X29_16','X29_17','X29_18','X29_19','Y29_16','Y29_17','Y29_18','Y29_19'],
['X29_20','X29_21','X29_22','X29_23','Y29_20','Y29_21','Y29_22','Y29_23'],
['X29_24','X29_25','X29_26','X29_27','Y29_24','Y29_25','Y29_26','Y29_27'],
['X29_28','X29_29','X29_30','X29_31','Y29_28','Y29_29','Y29_30','Y29_31'],
['X30_0','X30_1','X30_2','X30_3','Y30_0','Y30_1','Y30_2','Y30_3'],
['X30_4','X30_5','X30_6','X30_7','Y30_4','Y30_5','Y30_6','Y30_7'],
['X30_8','X30_9','X30_10','X30_11','Y30_8','Y30_9','Y30_10','Y30_11'],
['X30_12','X30_13','X30_14','X30_15','Y30_12','Y30_13','Y30_14','Y30_15'],
['X30_16','X30_17','X30_18','X30_19','Y30_16','Y30_17','Y30_18','Y30_19'],
['X30_20','X30_21','X30_22','X30_23','Y30_20','Y30_21','Y30_22','Y30_23'],
['X30_24','X30_25','X30_26','X30_27','Y30_24','Y30_25','Y30_26','Y30_27'],
['X30_28','X30_29','X30_30','X30_31','Y30_28','Y30_29','Y30_30','Y30_31'],
['X31_0','X31_1','X31_2','X31_3','Y31_0','Y31_1','Y31_2','Y31_3'],
['X31_4','X31_5','X31_6','X31_7','Y31_4','Y31_5','Y31_6','Y31_7'],
['X31_8','X31_9','X31_10','X31_11','Y31_8','Y31_9','Y31_10','Y31_11'],
['X31_12','X31_13','X31_14','X31_15','Y31_12','Y31_13','Y31_14','Y31_15'],
['X31_16','X31_17','X31_18','X31_19','Y31_16','Y31_17','Y31_18','Y31_19'],
['X31_20','X31_21','X31_22','X31_23','Y31_20','Y31_21','Y31_22','Y31_23'],
['X31_24','X31_25','X31_26','X31_27','Y31_24','Y31_25','Y31_26','Y31_27'],
['X31_28','X31_29','X31_30','X31_31','Y31_28','Y31_29','Y31_30','Y31_31']
]
# S-Boxがアクティブな時に1となる変数
q_sbox = [
'Q0_0','Q0_1','Q0_2','Q0_3','Q0_4','Q0_5','Q0_6','Q0_7',
'Q1_0','Q1_1','Q1_2','Q1_3','Q1_4','Q1_5','Q1_6','Q1_7',
'Q2_0','Q2_1','Q2_2','Q2_3','Q2_4','Q2_5','Q2_6','Q2_7',
'Q3_0','Q3_1','Q3_2','Q3_3','Q3_4','Q3_5','Q3_6','Q3_7',
'Q4_0','Q4_1','Q4_2','Q4_3','Q4_4','Q4_5','Q4_6','Q4_7',
'Q5_0','Q5_1','Q5_2','Q5_3','Q5_4','Q5_5','Q5_6','Q5_7',
'Q6_0','Q6_1','Q6_2','Q6_3','Q6_4','Q6_5','Q6_6','Q6_7',
'Q7_0','Q7_1','Q7_2','Q7_3','Q7_4','Q7_5','Q7_6','Q7_7',
'Q8_0','Q8_1','Q8_2','Q8_3','Q8_4','Q8_5','Q8_6','Q8_7',
'Q9_0','Q9_1','Q9_2','Q9_3','Q9_4','Q9_5','Q9_6','Q9_7',
'Q10_0','Q10_1','Q10_2','Q10_3','Q10_4','Q10_5','Q10_6','Q10_7',
'Q11_0','Q11_1','Q11_2','Q11_3','Q11_4','Q11_5','Q11_6','Q11_7',
'Q12_0','Q12_1','Q12_2','Q12_3','Q12_4','Q12_5','Q12_6','Q12_7',
'Q13_0','Q13_1','Q13_2','Q13_3','Q13_4','Q13_5','Q13_6','Q13_7',
'Q14_0','Q14_1','Q14_2','Q14_3','Q14_4','Q14_5','Q14_6','Q14_7',
'Q15_0','Q15_1','Q15_2','Q15_3','Q15_4','Q15_5','Q15_6','Q15_7',
'Q16_0','Q16_1','Q16_2','Q16_3','Q16_4','Q16_5','Q16_6','Q16_7',
'Q17_0','Q17_1','Q17_2','Q17_3','Q17_4','Q17_5','Q17_6','Q17_7',
'Q18_0','Q18_1','Q18_2','Q18_3','Q18_4','Q18_5','Q18_6','Q18_7',
'Q19_0','Q19_1','Q19_2','Q19_3','Q19_4','Q19_5','Q19_6','Q19_7',
'Q20_0','Q20_1','Q20_2','Q20_3','Q20_4','Q20_5','Q20_6','Q20_7',
'Q21_0','Q21_1','Q21_2','Q21_3','Q21_4','Q21_5','Q21_6','Q21_7',
'Q22_0','Q22_1','Q22_2','Q22_3','Q22_4','Q22_5','Q22_6','Q22_7',
'Q23_0','Q23_1','Q23_2','Q23_3','Q23_4','Q23_5','Q23_6','Q23_7',
'Q24_0','Q24_1','Q24_2','Q24_3','Q24_4','Q24_5','Q24_6','Q24_7',
'Q25_0','Q25_1','Q25_2','Q25_3','Q25_4','Q25_5','Q25_6','Q25_7',
'Q26_0','Q26_1','Q26_2','Q26_3','Q26_4','Q26_5','Q26_6','Q26_7',
'Q27_0','Q27_1','Q27_2','Q27_3','Q27_4','Q27_5','Q27_6','Q27_7',
'Q28_0','Q28_1','Q28_2','Q28_3','Q28_4','Q28_5','Q28_6','Q28_7',
'Q29_0','Q29_1','Q29_2','Q29_3','Q29_4','Q29_5','Q29_6','Q29_7',
'Q30_0','Q30_1','Q30_2','Q30_3','Q30_4','Q30_5','Q30_6','Q30_7',
'Q31_0','Q31_1','Q31_2','Q31_3','Q31_4','Q31_5','Q31_6','Q31_7' 
]

# 32次元の行ベクトル生成
def vector_gen(vector):
    array = [0 for a in range(32)]
    for i in range(32):
        array[i] = vector + str(i)
    return array
# 33*32の行列生成
def var_gen(var):
    array = [[0 for a in range(32)] for b in range(33)]
    for i in range(33):
        for j in range(32):
            array[i][j] = var + str(i) + '_' + str(j)
    return array

#各中間変数の設定
l = vector_gen('L')
x = var_gen('X')
y = var_gen('Y')
t = var_gen('T')
u = var_gen('U')
v = var_gen('V')

# 目的関数を生成する関数
def obj():
    obj = ''
    for i in range(round*8):
        obj = obj + '2 ' + q_freq2[i] + ' + 3 ' + q_freq3[i] + ' + '
    obj = obj.rstrip(' + ')
    return obj
with open('few_diff_obj_gen.txt','w') as f:
    tmp = obj()
    print(tmp, file=f)

# 入力が非零であるための制約式を生成する関数
def non_zero_diff_input():
    input = ''
    for i in range(32):
        input = input + l[i] + ' + '
    for j in range(32):
        input = input + x[0][j] + ' + '
    input = input.rstrip(' + ') + ' >= 1'
    return input
with open('few_diff_input_gen.txt','w') as f:
    tmp = non_zero_diff_input()
    print(tmp, file=f)

# 確率2^-2の差分伝播に関する制約式を生成する関数
def freq2_x_to_y(i0, i1, i2, i3, o0, o1, o2, o3, q):
    ineq = ''
    input = [i0, i1, i2, i3, o0, o1, o2, o3]
    for i in range(27):
        c = 0
        for j in range(8):
            if freq2[i][j] > 1:
                ineq = ineq + str(freq2[i][j]) + ' ' + input[j] + ' + '
            elif freq2[i][j] == 1:
                ineq = ineq + input[j] + ' + '
            elif freq2[i][j] < -1:
                ineq = ineq.rstrip(' + ') + ' - ' + str((-1)*freq2[i][j]) + ' ' + input[j] + ' + '
            elif freq2[i][j] == -1:
                c = c + 1
                ineq = ineq.rstrip(' + ') + ' - ' + input[j] + ' + '
        ineq = ineq.rstrip(' + ') + ' - ' + q + ' >= ' + str((-1)*c) + '\n'
    return ineq
with open('few_diff_freq2_gen.txt', 'w') as f:
    for i in range(round*8):
        tmp = freq2_x_to_y(var[i][0],var[i][1],var[i][2],var[i][3],var[i][4],var[i][5],var[i][6],var[i][7],q_freq2[i]).lstrip().replace('\n -','\n-')
        print(tmp, file=f)

# 確率2^-3の差分伝播に関する制約式を生成する関数
def freq3_x_to_y(i0, i1, i2, i3, o0, o1, o2, o3, q):
    ineq = ''
    input = [i0, i1, i2, i3, o0, o1, o2, o3]
    for i in range(43):
        c = 0
        for j in range(8):
            if freq3[i][j] > 1:
                ineq = ineq + str(freq3[i][j]) + ' ' + input[j] + ' + '
            elif freq3[i][j] == 1:
                ineq = ineq + input[j] + ' + '
            elif freq3[i][j] < -1:
                ineq = ineq.rstrip(' + ') + ' - ' + str((-1)*freq3[i][j]) + ' ' + input[j] + ' + '
            elif freq3[i][j] == -1:
                c = c + 1
                ineq = ineq.rstrip(' + ') + ' - ' + input[j] + ' + '
        ineq = ineq.rstrip(' + ') + ' - ' + q + ' >= ' + str((-1)*c) + '\n'
    return ineq
with open('few_diff_freq3_gen.txt', 'w') as f:
    for i in range(round*8):
        tmp = freq3_x_to_y(var[i][0],var[i][1],var[i][2],var[i][3],var[i][4],var[i][5],var[i][6],var[i][7],q_freq3[i]).lstrip().replace('\n -','\n-')
        print(tmp, file=f)

# S-Boxの状態変数Qに関する制約式を生成する関数
def q():
    cstr = ''
    for i in range(round*8):
        cstr = cstr + q_freq2[i] + ' + ' + q_freq3[i] + ' - ' + q_sbox[i] +' = 0\n'
    return cstr
with open('few_diff_q_gen.txt','w') as f:
    tmp = q()
    print(tmp, file=f)

# S-Boxがアクティブな時，状態変数Qが1となるための制約式を生成する関数
def or_xy():
    cstr = ''
    for m in range(round):
        for n in range(8):
            cstr = cstr +\
                 '- ' + x[m][n*4] + ' - ' + x[m][n*4+1] + ' - ' + x[m][n*4+2] + ' - ' + x[m][n*4+3] + ' - ' + y[m][n*4] + ' - ' + y[m][n*4+1] + ' - ' + y[m][n*4+2] + ' - ' + y[m][n*4+3] + ' + 8 ' + q_sbox[m*8+n] + ' >= 0\n' +\
                 '- ' + x[m][n*4] + ' - ' + x[m][n*4+1] + ' - ' + x[m][n*4+2] + ' - ' + x[m][n*4+3] + ' - ' + y[m][n*4] + ' - ' + y[m][n*4+1] + ' - ' + y[m][n*4+2] + ' - ' + y[m][n*4+3] + ' + 8 ' + q_sbox[m*8+n] + ' <= 7\n'
    return cstr
with open('few_diff_or_xy_gen.txt','w') as f:
    tmp = or_xy()
    print(tmp, file=f)

# F関数後半にある線形処理部と段間の接続に関する制約式を生成する関数
def y_to_x():
    cstr = ''
    for i in range(round):
        if i == 0:
            for j in range(32):
                if 0 <= j < 8:
                    cstr = cstr +\
                    y[i][j] + ' + ' + y[i][(j+1)%16] + ' + ' + y[i][(j+5)%16] + ' + ' +\
                    y[i][(j+9)%16] + ' + ' + y[i][(j+12)%16] + ' + ' + l[j] +\
                    ' - 2 ' + t[i][j] + ' - 2 ' + u[i][j] + ' - 2 ' + v[i][j] + ' - ' + x[i+1][j] +\
                    ' = 0\n'
                elif 8 <= j < 16:
                    cstr = cstr +\
                    y[i][j] + ' + ' + y[i][(j+1)%16] + ' + ' + y[i][(j+5)%16] + ' + ' +\
                    y[i][(j+9)%16] + ' + ' + y[i][(j+12)%16] + ' + ' + l[j] +\
                    ' - 2 ' + t[i][j] + ' - 2 ' + u[i][j] + ' - 2 ' + v[i][j] + ' - ' + x[i+1][j+16] +\
                    ' = 0\n'
                elif 16 <= j < 24:
                    cstr = cstr +\
                    y[i][j] + ' + ' + y[i][(j+4)%16+16] + ' + ' + y[i][(j+7)%16+16] + ' + ' +\
                    y[i][(j+11)%16+16] + ' + ' + y[i][(j+15)%16+16] + ' + ' + l[j] +\
                    ' - 2 ' + t[i][j] + ' - 2 ' + u[i][j] + ' - 2 ' + v[i][j] + ' - ' + x[i+1][j] +\
                    ' = 0\n'
                elif 24 <= j < 32:
                    cstr = cstr +\
                    y[i][j] + ' + ' + y[i][(j+4)%16+16] + ' + ' + y[i][(j+7)%16+16] + ' + ' +\
                    y[i][(j+11)%16+16] + ' + ' + y[i][(j+15)%16+16] + ' + ' + l[j] +\
                    ' - 2 ' + t[i][j] + ' - 2 ' + u[i][j] + ' - 2 ' + v[i][j] + ' - ' + x[i+1][j-16] +\
                    ' = 0\n'
        else:
            for j in range(32):
                if 0 <= j < 8:
                    cstr = cstr +\
                    y[i][j] + ' + ' + y[i][(j+1)%16] + ' + ' + y[i][(j+5)%16] + ' + ' +\
                    y[i][(j+9)%16] + ' + ' + y[i][(j+12)%16] + ' + ' + x[i-1][j] +\
                    ' - 2 ' + t[i][j] + ' - 2 ' + u[i][j] + ' - 2 ' + v[i][j] + ' - ' + x[i+1][j] +\
                    ' = 0\n'
                elif 8 <= j < 16:
                    cstr = cstr +\
                    y[i][j] + ' + ' + y[i][(j+1)%16] + ' + ' + y[i][(j+5)%16] + ' + ' +\
                    y[i][(j+9)%16] + ' + ' + y[i][(j+12)%16] + ' + ' + x[i-1][j+16] +\
                    ' - 2 ' + t[i][j] + ' - 2 ' + u[i][j] + ' - 2 ' + v[i][j] + ' - ' + x[i+1][j+16] +\
                    ' = 0\n'
                elif 16 <= j < 24:
                    cstr = cstr +\
                    y[i][j] + ' + ' + y[i][(j+4)%16+16] + ' + ' + y[i][(j+7)%16+16] + ' + ' +\
                    y[i][(j+11)%16+16] + ' + ' + y[i][(j+15)%16+16] + ' + ' + x[i-1][j] +\
                    ' - 2 ' + t[i][j] + ' - 2 ' + u[i][j] + ' - 2 ' + v[i][j] + ' - ' + x[i+1][j] +\
                    ' = 0\n'
                elif 24 <= j < 32:
                    cstr = cstr +\
                    y[i][j] + ' + ' + y[i][(j+4)%16+16] + ' + ' + y[i][(j+7)%16+16] + ' + ' +\
                    y[i][(j+11)%16+16] + ' + ' + y[i][(j+15)%16+16] + ' + ' + x[i-1][j-16] +\
                    ' - 2 ' + t[i][j] + ' - 2 ' + u[i][j] + ' - 2 ' + v[i][j] + ' - ' + x[i+1][j-16] +\
                    ' = 0\n'
    return cstr
with open('few_diff_ytox_gen.txt','w') as f:
    tmp = y_to_x()
    print(tmp, file=f)

# T, U, Vの大小関係を表す制約式を生成する関数
def tuv():
    cstr = ''
    for i in range(round):
        for j in range(32):
            cstr = cstr +\
            t[i][j] + ' - ' + u[i][j] + ' >= 0\n' +\
            u[i][j] + ' - ' + v[i][j] + ' >= 0\n'
    return cstr.rstrip('\n')
with open('few_diff_tuv_gen.txt','w') as f:
    tmp = tuv()
    print(tmp, file=f)

# LPファイルの変数宣言部を生成する関数
def binary():
    binary = ''
    for i in range(round*8):
        binary = binary + q_freq2[i] + '\n'
    for i in range(round*8):
        binary = binary + q_freq3[i] + '\n'
    for i in range(round*8):
        binary = binary + q_sbox[i] + '\n'
    for i in range(32):
        binary = binary + l[i] + '\n'
    for i in range(round+1):
        for j in range(32):
            binary = binary + x[i][j] + '\n'
    for i in range(round):
        for j in range(32):
            binary = binary + y[i][j]+ '\n'
    for i in range(round):
        for j in range(32):
            binary = binary + t[i][j]+ '\n'
    for i in range(round):
        for j in range(32):
            binary = binary + u[i][j]+ '\n'
    for i in range(round):
        for j in range(32):
            binary = binary + v[i][j]+ '\n'
    return binary
with open('few_diff_binary_gen.txt','w') as f:
    tmp = binary()
    print(tmp, file=f)

# 生成された各txtファイルを格納する変数
file = [
    'few_diff_input_gen.txt',
    'few_diff_freq2_gen.txt',
    'few_diff_freq3_gen.txt',
    'few_diff_q_gen.txt',
    'few_diff_ytox_gen.txt',
    'few_diff_or_xy_gen.txt',
    'few_diff_tuv_gen.txt'   
]

# 生成された各txtファイルを接続して，LPファイルを生成
with open('few'+str(round)+'.lp','w') as new_file:
    new_file.write('Minimize\n')
    with open('few_diff_obj_gen.txt') as f:
        for line in f:
            new_file.write(line)
        new_file.write('\n')
    new_file.write('\nSubject To\n')
    for name in file:
        with open(name) as f:
            for line in f:
                new_file.write(line)
            new_file.write('\n')
    new_file.write('\nBinary\n')
    with open('few_diff_binary_gen.txt') as f:
        for line in f:
            new_file.write(line)
        new_file.write('\n')
    new_file.write('\nEND')