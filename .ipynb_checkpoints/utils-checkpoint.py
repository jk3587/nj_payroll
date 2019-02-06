import janitor
    
def clean_names(df):
    return janitor.clean_names(df)

def clean_columns(df):
    for col in df.select_dtypes(include=['object']).columns:
        df[col].fillna('None', inplace=True)
        df[col] = df[col].str.lower()
    for col in df.select_dtypes(include=['integer', 'float']).columns:
        #if len(df[df[col].isnull()]) > 0:
        df[col].fillna(0, inplace=True)
    return df

def agency_name_shorten(row):
    if 'elderly' in row:
        return 'division of elderly advocacy'
    else:
        return row
    
def clean_agency_name(df):
    if 'master_department_agency_desc' in df.columns:
        df['master_department_agency_desc'] = df.apply(lambda row: agency_name_shorten(row['master_department_agency_desc']), axis=1)
    return df

def clean(df):
    df = clean_names(df)
    df = clean_columns(df)
    df = clean_agency_name(df)
    return df