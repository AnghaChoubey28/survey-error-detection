import pandas as pd

df = pd.read_csv("data.csv")

def check_errors(row):
    errors = []

    
    if row['Age'] <= 0 or row['Age'] > 100:
        errors.append("Invalid Age")

    # Income validation
    if row['Income'] < 0:
        errors.append("Invalid Income")

    # Age-Occupation mismatch
    if row['Age'] < 18 and row['Occupation'] != "Student":
        errors.append("Age-Occupation mismatch")

    # Family size validation
    if row['FamilySize'] <= 0:
        errors.append("Invalid Family Size")

    # Logical check: electricity but no internet (optional insight)
    if row['HasElectricity'] == "No" and row['HasInternet'] == "Yes":
        errors.append("Internet without Electricity")

    return ", ".join(errors)

# Apply validation
df['Errors'] = df.apply(check_errors, axis=1)

# Save output
df.to_csv("output.csv", index=False)

print("✅ Error detection completed. Check output.csv")

# ------------------ INSIGHTS ------------------

print("\n📊 BASIC INSIGHTS")

print("Total Records:", len(df))
print("Average Income:", df['Income'].mean())

print("People with Electricity:", (df['HasElectricity'] == 'Yes').sum())
print("People with Internet:", (df['HasInternet'] == 'Yes').sum())


# ------------------ ERROR SUMMARY ------------------

print("\n❌ ERROR SUMMARY")

print("Invalid Age:", df['Errors'].str.contains("Invalid Age").sum())
print("Invalid Income:", df['Errors'].str.contains("Invalid Income").sum())
print("Mismatch:", df['Errors'].str.contains("Mismatch").sum())


# ------------------ VALID VS INVALID ------------------

valid = (df['Errors'] == "").sum()
invalid = (df['Errors'] != "").sum()

print("\n✅ Valid Records:", valid)
print("❌ Invalid Records:", invalid)


# ------------------ STATE ANALYSIS ------------------

print("\n📍 State-wise Count:")
print(df['State'].value_counts())


print("\n💰 Avg Income by State:")
print(df.groupby('State')['Income'].mean())


# ------------------ INFRASTRUCTURE ------------------

electricity = (df['HasElectricity'] == 'Yes').mean() * 100
internet = (df['HasInternet'] == 'Yes').mean() * 100

print("\n⚡ Electricity Access %:", electricity)
print("🌐 Internet Access %:", internet)


# ------------------ TOP ERRORS ------------------

print("\n🚨 Most Common Errors:")
print(df['Errors'].value_counts().head())

# ------------------ SAVE INSIGHTS TO EXCEL ------------------

summary = {
    "Total Records": [len(df)],
    "Average Income": [df['Income'].mean()],
    "People with Electricity": [(df['HasElectricity'] == 'Yes').sum()],
    "People with Internet": [(df['HasInternet'] == 'Yes').sum()],
    "Invalid Age": [df['Errors'].str.contains("Invalid Age").sum()],
    "Invalid Income": [df['Errors'].str.contains("Invalid Income").sum()],
}

summary_df = pd.DataFrame(summary)

with pd.ExcelWriter("final_output.xlsx") as writer:
    df.to_excel(writer, sheet_name="Data", index=False)
    summary_df.to_excel(writer, sheet_name="Insights", index=False)

print("✅ Excel file with insights created: final_output.xlsx")
