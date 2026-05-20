import pandas as pd

def main():
    df = pd.read_csv("data/clean/events.csv")

    # Extract date portion from ISO 8601 timestamp
    df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")

    df.to_csv("data/transformed/events.csv", index=False)
    print(f"Transform: {len(df)} rows written.")

if __name__ == "__main__":
    main()