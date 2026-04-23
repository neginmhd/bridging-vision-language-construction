# 📄 Title Cleaning and Deduplication for Systematic Search Records

This script prepares the master dataset for screening by combining raw search results from **Scopus** and **Web of Science (WoS)**. It standardizes titles, removes duplicates within and across databases, and exports a single deduplicated dataset.

---

## 🎯 Purpose

The script supports transparency and reproducibility in the **identification stage** of the systematic search. It:

- loads raw records from Scopus and WoS  
- standardizes title fields  
- normalizes titles for consistent comparison  
- removes internal duplicates within each database  
- identifies overlap across databases  
- merges unique records into a master dataset  
- exports a clean file for screening  

---

## 📥 Input Files

Place the following files in the working directory:

- `scopus_raw_2026-02-13.csv`  
- `wos_raw_2026-02-13.xls`  

---

## 📤 Output

- `master_deduplicated.csv` — final dataset ready for screening  

---

## ⚙️ Pipeline

### 1. Load Data
Raw datasets are imported using `pandas`.

### 2. Standardize Fields
WoS column `Article Title` is renamed to `Title` for consistency.

### 3. Normalize Titles
Titles are cleaned to create a comparison key (`title_key`):
- lowercase conversion  
- whitespace trimming  
- removal of special characters (except `-` and `'`)  
- normalization of spacing  

### 4. Remove Internal Duplicates
Duplicates are removed separately within:
- Scopus  
- WoS  

### 5. Detect Cross-Database Overlap
- Shared records are identified using normalized titles  
- Scopus entries are labeled:
  - `Scopus`  
  - `Scopus, WoS` (if overlap exists)  
- Overlapping WoS records are excluded  
- Unique WoS records are retained and labeled `WoS`  

### 6. Merge Datasets
Scopus (deduplicated) + unique WoS records are combined into a master dataset.

### 7. Export and Summary
The script saves the final dataset and prints:
- duplicates removed (Scopus and WoS)  
- overlap between databases  
- total records removed  
- final dataset size  

---

## 🧰 Dependencies

Install required packages:

```bash
pip install pandas xlrd
