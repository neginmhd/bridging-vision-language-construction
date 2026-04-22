import pandas as pd

# LOAD BOTH DATASETS
df_scopus = pd.read_csv("scopus_raw_2026-02-13.csv")
df_wos = pd.read_excel("wos_raw_2026-02-13.xls", engine="xlrd")

print(f"Scopus loaded: {len(df_scopus)} records")
print(f"WoS loaded: {len(df_wos)} records")

# STANDARDIZE COLUMN NAMES
df_wos = df_wos.rename(columns={'Article Title': 'Title'})

# DEFINE THE NORMALIZATION FUNCTION
def clean_titles(series):
    """Clean titles (convert to lowercase, strip extra whitespace, and remove special characters except hyphens (-) and apostrophes (')).
    This creates a normalized version for duplicate detection."""
    return (
        series.astype(str)
        .str.lower()
        .str.strip()
        .str.replace(r"[^\w\s'\-]", '', regex=True)
        .str.replace(r'\s+', ' ', regex=True)
    )

# CHECK INTERNAL DUPLICATES - SCOPUS
scopus_raw_count = len(df_scopus)
df_scopus['title_key'] = clean_titles(df_scopus['Title'])
df_scopus = df_scopus.drop_duplicates(subset='title_key', keep='first').reset_index(drop=True)
scopus_internal_duplicates = scopus_raw_count - len(df_scopus)

print(f"\nScopus: {scopus_internal_duplicates} duplicates removed, {len(df_scopus)} records remaining")

# CHECK INTERNAL DUPLICATES - WOS
wos_raw_count = len(df_wos)
df_wos['title_key'] = clean_titles(df_wos['Title'])
df_wos = df_wos.drop_duplicates(subset='title_key', keep='first').reset_index(drop=True)
wos_internal_duplicates = wos_raw_count - len(df_wos)

print(f"WoS: {wos_internal_duplicates} duplicates removed, {len(df_wos)} records remaining")

# CHECK OVERLAP BETWEEN DATABASES
scopus_keys = set(df_scopus['title_key'])
wos_keys = set(df_wos['title_key'])
overlap = scopus_keys & wos_keys

# Mark Scopus records that have overlaps
df_scopus['source'] = df_scopus['title_key'].apply(lambda x: 'Scopus, WoS' if x in overlap else 'Scopus')

# KEEP ONLY WOS TITLES NOT IN SCOPUS
df_wos_unique = df_wos[~df_wos['title_key'].isin(scopus_keys)].reset_index(drop=True)
df_wos_unique['source'] = 'WoS'

# COMBINE DATASETS
df_master = pd.concat([df_scopus, df_wos_unique], ignore_index=True, sort=False)
print(f"\nCombined dataset: {len(df_master)} records")

# SAVE MASTER DATASET
output_path = "master_deduplicated.csv"
df_master.to_csv(output_path, index=False)
print(f"Master dataset saved to: {output_path}")

# SUMMARY
total_removed = scopus_internal_duplicates + wos_internal_duplicates + len(overlap)
print("\nSummary:")
print(f"  Scopus internal duplicates: {scopus_internal_duplicates}")
print(f"  WoS internal duplicates: {wos_internal_duplicates}")
print(f"  Overlap between databases: {len(overlap)}")
print(f"  Total records removed: {total_removed}")
print(f"  Total records ready for screening: {len(df_master)}")