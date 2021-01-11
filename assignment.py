import pandas as pd


WIPS=pd.read_csv('WIPS.txt',delimiter='\t')

print(WIPS)

dfProjPostingData=pd.read_csv('dfProjPostingData.txt',delimiter='\t')

categories=pd.read_csv('catergories.txt',delimiter='\t')

print(categories)


dfProjPostingData.rename(columns={'DisplayValue':'accountid','ProjCategoryRelation':'CategoryId'},inplace=True)

print(dfProjPostingData)

new_Wips_PostingData=pd.merge(WIPS,dfProjPostingData)
print(new_Wips_PostingData)

new_categoris_PostingData=pd.merge(categories,new_Wips_PostingData)

print(new_categoris_PostingData)

new_categoris_PostingData_groupby=new_categoris_PostingData.groupby(['dataAreaId','accountid','CategoryId','CategoryName']
).sum()[['AmountMst']].round(decimals=2).reset_index()

print(new_categoris_PostingData_groupby)




new_categoris_PostingData_groupby.rename(columns={'dataAreaId':'Legal entity code','accountid':'Account','CategoryId':'Reference','CategoryName':'Text','AmountMst':'Amount'},inplace=True)

print(new_categoris_PostingData_groupby)

new_categoris_PostingData_groupby['Date']=pd.to_datetime('today')
new_categoris_PostingData_groupby['link']=''
new_categoris_PostingData_groupby['Transactiontype']=70
new_categoris_PostingData_groupby['Transactionamount']=new_categoris_PostingData_groupby['Amount']
new_categoris_PostingData_groupby['Currencycode']=''
print(new_categoris_PostingData_groupby)

new_categoris_PostingData_groupby[['Legal entity code','Account','Amount','Date','Reference','Text','link','Transactiontype','Transactionamount','Currencycode']].to_csv('result.csv')




