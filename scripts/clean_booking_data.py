import pandas as pd

RAW_DATA_PATH = "data/raw/hotel_bookings_raw.csv"
CLEAN_DATA_PATH = "data/processed/hotel_bookings_clean.csv"


def clean_booking_data():
    """
    Clean hotel booking dataset.
    """

    print("Loading raw dataset...")

    df = pd.read_csv(RAW_DATA_PATH)

    print(f"Original shape: {df.shape}")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert reservation status date into datetime
    df["reservation_status_date"] = pd.to_datetime(
        df["reservation_status_date"]
    )

    # Fill missing children values with 0
    df["children"] = df["children"].fillna(0)

    print(f"Cleaned shape: {df.shape}")

    df.to_csv(CLEAN_DATA_PATH, index=False)

    print(f"Clean dataset saved to: {CLEAN_DATA_PATH}")


if __name__ == "__main__":
    clean_booking_data()