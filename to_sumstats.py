#editer haozhou
#version V1.0
#date 20240204


import pandas as pd
import argparse
import sys
import time
import subprocess

def process_rmvp(sum, output):
    # 构建文件名
    tmp_file = f"{sum.rsplit('.csv', 1)[0]}.{output}.tmp"


    # sed 和 awk 命令组合
    cmd2 = f"sed 's/\"//g;s/,/\t/g' {sum} | awk -v OFS='\t' '{{if($8 != \"NA\")print $1,$2,$3,$4,$5,$6,$7,$8,$6/$7}}' | sed '1d' > {tmp_file}"
    subprocess.run(cmd2, shell=True, check=True)

    # 最后的 sed 命令，添加标题
    cmd3 = f"sed -i '1i SNP\tCHROM\tPOS\tA1\tA2\tEffect\tSE\tP\tZ' {tmp_file}"
    subprocess.run(cmd3, shell=True, check=True)

    return tmp_file  # 返回处理后的文件名，可用作输出文件



def munge_sumstats(args):
    START_TIME = time.time()
    
    # 处理输入文件并获取输出文件名
    output_tmp = process_rmvp(sum=args.rmvp_sum, output=args.out)
    print("Processed sumstats file:", args.out + ".tmp")

    try:
        # 读取处理后的数据
        dat = pd.read_csv(output_tmp, delim_whitespace=True, header=0, na_values=['.', 'NA'])
        dat1 = dat[['SNP', 'A1', 'A2', 'P','Z']]

        # 确保必要的列存在
        for c in ['SNP', 'A1', 'A2', 'P','Z']:
            if c not in dat1.columns:
                raise ValueError(f'Column {c} is required but not found.')

        # 处理样本大小
        if args.N:
            dat1.loc[:, 'N'] = args.N #加上新列

        # 输出处理后的数据
        out_fname = args.out + '.sumstats'
        dat1.to_csv(out_fname + '.gz', sep="\t", index=False, float_format='%.3f', compression='gzip')
        print(f'Output written to {out_fname}.gz')

    except Exception as e:
        print('Error:', e)
    finally:
        print('Total time elapsed:', round(time.time() - START_TIME, 2), 'seconds')

#try, except, 和 finally 用于处理可能导致程序中断或错误的异常情况。try 块包含可能引发异常的代码，except 块用于处理异常，而 finally 块中的代码无论是否发生异常都会执行。


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rmvp_sum', required=True, help="Input filename.")
    parser.add_argument('--out', required=True, help="Output filename prefix.")
    parser.add_argument('--N', type=float, help="Sample size.")
    args = parser.parse_args()
    munge_sumstats(args)

