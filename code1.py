import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("/content/KaggleV2-May-2016[1].csv")

# Quick peek
print(df.shape)
print(df.head(3))

# Identifying and handling missing values

# Count missing per column
missing_counts = df.isnull().sum()
print("Missing values per column:\n", missing_counts)

# Remove rows with missing value
df_dropped = df.dropna().copy()
print("After dropna:", df_dropped.shape)

# Remove duplicate rows
df = df.drop_duplicates(subset=['PatientId', 'ScheduledDay', 'AppointmentDay'])
print(df.shape)

#Standardize text values

# Standardize Gender column
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].astype(str).str.strip().str.upper()  # remove spaces & make uppercase
    df['Gender'] = df['Gender'].replace({
        'FEMALE': 'F',
        'F': 'F',
        'MALE': 'M',
        'M': 'M'
    })

print(df['Gender'].value_counts())

# Standardize Neighbourhood column
if 'Neighbourhood' in df.columns:
    df['Neighbourhood'] = df['Neighbourhood'].astype(str).str.strip().str.title()

print(df['Neighbourhood'].head())

# Convert date formats to (dd-mm-yyyy)

date_columns = ['ScheduledDay', 'AppointmentDay']

for col in date_columns:
    if col in df.columns:
        # Convert to datetime (automatically detects format)
        df[col] = pd.to_datetime(df[col], errors='coerce')

        # Format as dd-mm-yyyy (string format)
        df[col] = df[col].dt.strftime('%d-%m-%Y')

# Check result
print(df[date_columns].head(3))

# Convert column headers to lowercase and replace spaces with underscores
df.columns = (
    df.columns
      .str.strip()             # remove extra spaces
      .str.lower()             # make lowercase
      .str.replace(' ', '_')   # replace spaces with underscore
      .str.replace('-', '_')   # replace hyphens with underscore
)

print(df.columns)

# Check data types
print(df.dtypes)

# Fix data types

# Convert 'patientid' to integer
df['patientid'] = pd.to_numeric(df['patientid'], errors='coerce')  # convert invalid values to NaN
df['patientid'] = df['patientid'].fillna(0).round(0).astype(int)   # fill NaN, round, then convert to int

# Convert date columns to datetime
df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')
df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')

# Standardize and convert text columns
df['gender'] = df['gender'].astype(str).str.strip().str.upper().replace({'FEMALE': 'F', 'MALE': 'M'})
df['neighbourhood'] = df['neighbourhood'].astype(str).str.strip().str.title()
df['no_show'] = df['no_show'].astype(str).str.strip().str.title()

# Convert categorical columns to category type
df['gender'] = df['gender'].astype('category')
df['neighbourhood'] = df['neighbourhood'].astype('category')
df['no_show'] = df['no_show'].astype('category')

# Convert numeric 0/1 columns to boolean
bool_cols = ['scholarship', 'hipertension', 'diabetes', 'alcoholism', 'handcap', 'sms_received']
for col in bool_cols:
    df[col] = df[col].astype(bool)

# Final check of data types
print("\n Data types after fixing:\n")
print(df.dtypes)