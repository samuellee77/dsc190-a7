import pandas as pd

VALID_EVENT_TYPES = {"click", "view", "purchase"}

def parse_timestamp(ts):
    """Try multiple formats, return ISO 8601 string or None."""
    formats = [
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%m/%d/%Y %H:%M:%S",
    ]
    for fmt in formats:
        try:
            return pd.Timestamp(ts).strftime("%Y-%m-%dT%H:%M:%S")
        except Exception:
            pass
    return None

def main():
    df = pd.read_csv("data/raw/events.csv")

    # Drop rows with any missing fields
    df = df.dropna()

    # Drop rows with invalid event_type
    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    # Drop rows with non-positive duration_seconds
    df = df[df["duration_seconds"] > 0]

    # Normalize timestamps — parse flexibly, output ISO 8601
    df["timestamp"] = pd.to_datetime(df["timestamp"], format='mixed')
    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    # Drop any rows where timestamp couldn't be parsed
    df = df.dropna(subset=["timestamp"])

    df.to_csv("data/clean/events.csv", index=False)
    print(f"Clean: {len(df)} rows written.")

if __name__ == "__main__":
    main()