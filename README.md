# medical-appointment-no-shows-cleaning
Data Cleaning and Preprocessing project on the Medical Appointment No Shows dataset.
Includes handling missing values, removing duplicates, standardizing text, fixing data types, formatting dates, and cleaning column names for better data consistency and analysis.

# 🩺 Medical Appointment No Shows — Data Cleaning & Preprocessing

## 📘 Project Overview
This project focuses on **data cleaning and preprocessing** for the *Medical Appointment No Shows* dataset.  
The dataset contains information about medical appointments and whether patients showed up or not.  
The goal of this project is to prepare clean, structured, and analysis-ready data by identifying and fixing common data quality issues.

---

## 📂 Dataset Description
The dataset includes details such as:
- **Patient ID** and **Appointment ID**
- **Gender**
- **Scheduled Day** and **Appointment Day**
- **Age**
- **Neighbourhood**
- **Scholarship**, **Hypertension**, **Diabetes**, **Alcoholism**, **Handicap**
- **SMS Received**
- **No-show** status

---

## 🧹 Data Cleaning and Preprocessing Tasks
The following steps were performed to ensure data quality and consistency:

1. **Identified and handled missing values**  
   - Checked for null or empty entries and handled them appropriately.  

2. **Removed duplicate rows**  
   - Eliminated repeated records to avoid bias and redundancy.  

3. **Standardized text values**  
   - Made text entries consistent (e.g., gender or ‘no_show’ column values).  

4. **Converted date formats to `DD-MM-YYYY`**  
   - Ensured uniform date representation for better readability and sorting.  

5. **Converted column headers**  
   - Changed all column names to lowercase and replaced spaces with underscores.  

6. **Fixed data types**  
   - Converted columns like `PatientID`, `ScheduledDay`, and `AppointmentDay` to appropriate data types (`int`, `datetime`, etc.).

---

## 🧠 Tools & Libraries Used
- **Python**
- **Pandas**
- **NumPy**
- **Jupyter Notebook / VS Code**

---

## 📈 Outcome
After cleaning:
- The dataset is **free from duplicates and missing values**.  
- All columns follow a **consistent naming convention and correct data types**.  
- The cleaned dataset is **ready for analysis or model building**.

---

## 📊 Next Steps
- Perform **Exploratory Data Analysis (EDA)** to uncover patterns and insights.  
- Build **predictive models** to understand the factors affecting no-shows.

---

## 👩‍💻 Author
**Avdesh Arya**  
B.Tech (CSE) | Data Analyst Intern  
📍 GBU University  

---

## 🏷️ Repository Tags
`data-cleaning` `data-preprocessing` `medical-dataset` `pandas` `python` `machine-learning` `healthcare`

