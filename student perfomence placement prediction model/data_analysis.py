def analyze_dataset(df):

    print("\n--- First 5 Students ---")
    print(df.head())

    print("\n--- Dataset Shape ---")
    print("Rows and Columns:", df.shape)

    print("\n--- Column Names ---")
    print(df.columns.tolist())

    print("\n--- Dataset Information ---")
    df.info()

    print("\n--- Statistical Summary ---")
    print(df.describe())

    print("\n--- Missing Values ---")
    print(df.isnull().sum())
    
    print("\n--- Duplicate Rows ---")
    print("Number of duplicate rows:", df.duplicated().sum())
