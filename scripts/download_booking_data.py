import pandas as pd

BOOKING_DATA_URL = (
    "https://raw.githubusercontent.com/"
    "rfordatascience/tidytuesday/master/"
    "data/2020/2020-02-11/hotels.csv"
)

OUTPUT_PATH = "data/raw/hotel_bookings_raw.csv"


def download_booking_data():
    """
    Download hotel booking dataset and save raw copy.
    """

    print("Downloading dataset...")

    df = pd.read_csv(BOOKING_DATA_URL)

    print(f"Dataset shape: {df.shape}")

    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Dataset saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    download_booking_data()