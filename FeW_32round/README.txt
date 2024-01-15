'few_diff_freq2_raw.txt', 'few_diff_freq3_raw.txt':
7つの数字は左から4つがDDTの入力側4bit、5から8番目が出力側4bit、最後の数字が定数。不等式の演算子等辺は全て「>=0」。

'few_diff_freq2.txt', 'few_diff_freq3.txt':
sage.math.orgで生成した制約式の係数。

'few_diff_freq2_gen.txt', 'few_diff_freq3_gen.txt':
few_diff.pyで生成した、各差分確率の制約式。各制約式は、対応するS-BoxがActiveな時にQ=1となって有効となる。

'few_diff_q_gen.txt':
各S-Boxにつき、2^-2/2^-3の差分伝播のうち必ずどちらか1つが、Activeであることを示す制約式。

'few_diff_xtoy_gen.txt', 'few_diff_wtoz_gen.txt', 'few_diff_ztox_gen.txt':
xtoyはF関数の冒頭で8bitずつ入れ替える部分の制約式。wtozはL1/L2通過前後の制約式。ztoxは段間の制約式。

'few_diff_obj_gen.txt', 'few_diff_input_gen.txt', 'few_diff_binary_gen.txt':
objは目的関数。inputは入力差分がゼロとならないための制約式。binaryは制約式に登場するすべてのbinary変数の宣言。

'few_diff.py':
目的関数、制約式、変数宣言の生成。

'few_diff_lp_gen.py':
LPファイルの生成。

'few32.lp':
32-roundのパス探索。