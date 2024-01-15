# few_diff.pyで生成された各txtファイルを接続して，LPファイルを生成
file = [
    'few_diff_input_gen.txt',
    'few_diff_xtoy_gen.txt',
    'few_diff_freq2_revgen.txt',
    'few_diff_freq3_revgen.txt',
    'few_diff_q_gen.txt',
    'few_diff_wtoz_gen.txt',
    'few_diff_ztox_gen.txt',
    'few_diff_or_y_gen.txt'   
]

with open('few9.lp','w') as new_file:
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