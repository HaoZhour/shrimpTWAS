

# Shrimp TWAS Analysis

## Overview

This document outlines the steps for Transcriptome-Wide Association Study (TWAS) analysis using the Fusion package. Please follow the instructions below:

1. **GWAS Analysis with rMVP:**
   Perform a Genome-Wide Association Study (GWAS) analysis using rMVP, and generate the corresponding GWAS Summary file. Here we recommend using rMVP for GWAS analysis as it produces a Summary file that is compatible with to_sumstats.py.

2. **Conversion to Sumstats Format:**
   Utilize the `to_sumstats.py` script to convert the generated GWAS Summary file into the required sumstats format. Use the following parameters:
   ```bash
   python to_sumstats.py --rmvpsum <input_summary_file> --out <output_file_suffix> --N <sample_size>


3. **TWAS Analysis with Fusion:**
   - Use the following command to input the files into the Fusion package:
     ```bash
     Rscript FUSION.assoc.R \
        --sumstats <input_sumstats_file> \
        --weights <RDat.list> \
        --force_model top1 \
        --weights_dir ./ \
        --ref_ld_chr <input_LD files> \
        --chr <input_chr number> \
        --max_impute 0.9 \
        --min_r2pred 0.5 \
        --out <output_file> 
 
     ```
   - Perform TWAS calculations separately for each chromosome.

4. **Results:**
   - Generate and analyze the corresponding TWAS results.

## Additional Information

For more details or assistance, please refer to the Fusion documentation.

## Contact

If you have any questions or need further assistance, feel free to contact us.

Haozhou：zhouhao@ysfri.ac.cn
Shengluan：luansheng@ysfri.ac.cn