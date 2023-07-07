from googleapiclient.discovery import build

def get_channel_link(channel_id, api_key):
    # Create a YouTube Data API client
    youtube = build("youtube", "v3", developerKey=api_key)

    # Get the channel resource
    channels_response = youtube.channels().list(
        part="snippet",
        id=channel_id
    ).execute()

    # Extract the channel link from the response
    if "items" in channels_response:
        channel_link = f"https://www.youtube.com/channel/{channel_id}"
        return channel_link

    return None

# Example usage
channel_id = "CHANNEL_ID"  # Replace with the actual YouTube Channel ID
api_key = "YOUR_API_KEY"  # Replace with your YouTube Data API key

channel_link = get_channel_link(channel_id, api_key)
if channel_link:
    print(f"Channel Link: {channel_link}")
else:
    print("Failed to retrieve channel link.")
