
def clean_prosper_data(df):
    '''
    Cleans the Prosper dataset by selecting important columns and dropping missing values.
    '''
    important_cols = ['BorrowerAPR', 'ProsperRating (Alpha)', 'IncomeRange',
                      'LoanOriginalAmount', 'DebtToIncomeRatio', 'StatedMonthlyIncome', 'Term', 'BorrowerRate', 'LoanStatus']
    df_clean = df[important_cols].dropna().reset_index(drop=True)
    return df_clean
