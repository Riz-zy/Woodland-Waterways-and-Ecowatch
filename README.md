# Depth vs. Development: Evaluating Lake Capacity Designations

**Author:** Rishikesh Narayan Tekavade  
**Context:** AMOD 5640Y Research Project  
**Date:** December 2025

## 📄 Project Overview
This project evaluates the validity of Ontario’s "At Capacity" lake designation system using a reproducible Python-based analytical pipeline. Focusing on 31 lakes (61 sites) in Haliburton County, the study integrates water chemistry data (2022–2024) with morphometric and development metrics to determine if administrative capacity status aligns with observed trophic conditions.

The analysis challenges the effectiveness of mass-balance models in morphologically complex regions, suggesting that binary capacity designations often mask the ecological reality of deep-lake resilience and shallow-lake vulnerability.

## 🧪 Methodology
This repository contains a Python 3.10 workflow designed for auditability and scalability in environmental data science. The pipeline includes:

* **Data Harmonization:** An automated script using `os`, `pathlib`, and `re` to standardize heterogeneous file naming conventions and directory structures.
* **Preprocessing:** Cleaning and merging data using `pandas` and `openpyxl`, including the resolution of lake naming inconsistencies and outlier detection.
* **Statistical Analysis:** * OLS regression for short-term trajectory analysis.
    * ANCOVA models to isolate the effects of depth vs. administrative status.
    * Feature engineering for drainage ratios and hydrologic classification.

## 📊 Key Findings
* **Morphometry Dominates:** Maximum depth is the primary driver of phosphorus variability ($p<0.005$), while "At Capacity" status showed no significant predictive power ($p=0.99$) once morphometry was accounted for.
* **Resilience:** Deeper lakes exhibited greater resilience to nutrient loading, while shallow systems showed higher vulnerability.
* **Hotspots Identified:** Despite regional stability, localized enrichment hotspots were identified in Gull, Stocking, and Kashagawigamog lakes, likely driven by legacy loading and climate factors.

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Data Manipulation:** `pandas`, `numpy`
* **Statistics:** `scipy`, `statsmodels`, `scikit-learn`
* **Visualization:** `matplotlib`, `seaborn`

## 📂 Data Sources
The primary dataset was compiled by the Woodland Waterways and EcoWatch (WWEW) program and the U-Links Centre for Community-Based Research.
