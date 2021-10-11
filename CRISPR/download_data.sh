#!/bin/bash

#/bin/bash

# download supplementary tables 18 and 19 from Doench et al. 2016
wget https://static-content.springer.com/esm/art%3A10.1038%2Fnbt.3437/MediaObjects/41587_2016_BFnbt3437_MOESM8_ESM.zip
unzip 41587_2016_BFnbt3437_MOESM8_ESM.zip -x '__MACOSX/*'
mv 'SuppTables/STable 18 CD33_OffTargetdata.xlsx' data/offtarget
mv 'SuppTables/STable 19 FractionActive_dlfc_lookup.xlsx' data/offtarget
rm -rf ./SuppTables

# download supplementary table from Tsai et al. 2015
wget https://static-content.springer.com/esm/art%3A10.1038%2Fnbt.3117/MediaObjects/41587_2015_BFnbt3117_MOESM22_ESM.xlsx
mv 41587_2015_BFnbt3117_MOESM22_ESM.xlsx data/offtarget

# run script to filter CD33 data
python filter_s_table_18.py -d './data/offtarget/STable 18 CD33_OffTargetdata.xlsx' -o './data/offtarget/CD33_data_postfilter.xlsx'

# run script to filter Tsai et al. data
python filter_tsai.py -d './data/offtarget/41587_2015_BFnbt3117_MOESM22_ESM.xlsx' -o './data/offtarget/Supplementary Table 10.xlsx'
