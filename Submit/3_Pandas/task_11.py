# 課題11： age_dfの'age'カラムの値に対して'age_group'カラムを追加して、
# 
# - 0 ~ 18までを'kids'
# - 19 ~ 65までを'adult'
# - 65 ~ 99までを'elderly'
# 
# と分類し表示せよ（変数名はage_df）


age_df = numeric_df.rename(columns={0: 'age'}, inplace=False)
# 以下よりコードを記入してください  ##############################


# 出力  #################################################
display(age_df)
