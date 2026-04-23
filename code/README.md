# 📄 Title Cleaning and Deduplication for Systematic Search Records

This script prepares a master dataset for screening by combining raw search results from **Scopus** and **Web of Science (WoS)**. It standardizes titles, removes duplicates within and across databases, and exports a single deduplicated file.

---

## 🎯 Purpose

Supports transparency and reproducibility in the **identification stage** by:

- standardizing title fields  
- normalizing titles for comparison  
- removing internal duplicates (Scopus, WoS)  
- identifying cross-database overlap  
- merging unique records into a master dataset  

---

## 📥 Input

- `scopus_raw_2026-02-13.csv`  
- `wos_raw_2026-02-13.xls`  

---

## 📤 Output

- `master_deduplicated.csv` — dataset ready for screening  

---

## ⚙️ Pipeline

1. Load Scopus and WoS datasets  
2. Standardize title fields (`Article Title` → `Title`)  
3. Normalize titles (lowercase, clean characters, normalize spacing)  
4. Remove duplicates within each database  
5. Identify overlap across databases  
6. Merge Scopus with unique WoS records  
7. Export final dataset and summary statistics  

---

## 🧰 Dependencies

```bash
pip install pandas xlrd
