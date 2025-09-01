import os
import re
from googleapiclient.discovery import build

# --- IMPORTANT: EDIT THESE TWO LINES ---
API_KEY = "PASTE_YOUR_API_KEY_HERE"  # Your YouTube Data API v3 key
VIDEO_FOLDER_PATH = r"C:\path\to\your\videos\UCu7iQE-L5gzt8aD7zuuufjw" # The full path to the folder with the videos

# This function removes characters that are illegal in Windows filenames
def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

def rename_videos():
    if API_KEY == "PASTE_YOUR_API_KEY_HERE":
        print("🛑 ERROR: Please replace 'PASTE_YOUR_API_KEY_HERE' with your actual API key.")
        return

    if not os.path.isdir(VIDEO_FOLDER_PATH):
        print(f"🛑 ERROR: The folder path '{VIDEO_FOLDER_PATH}' does not exist.")
        return
        
    print(f"🔍 Scanning folder: {VIDEO_FOLDER_PATH}\n")

    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        for filename in os.listdir(VIDEO_FOLDER_PATH):
            # Process only .mp4 files
            if filename.endswith(".mp4"):
                video_id = os.path.splitext(filename)[0]
                
                # Check if video_id is a valid YouTube ID length
                if len(video_id) == 11:
                    try:
                        request = youtube.videos().list(
                            part="snippet",
                            id=video_id
                        )
                        response = request.execute()

                        if response['items']:
                            video_title = response['items'][0]['snippet']['title']
                            safe_title = sanitize_filename(video_title)
                            new_filename = f"{safe_title}.mp4"
                            
                            old_filepath = os.path.join(VIDEO_FOLDER_PATH, filename)
                            new_filepath = os.path.join(VIDEO_FOLDER_PATH, new_filename)

                            print(f"✅ Renaming '{filename}' to '{new_filename}'")
                            os.rename(old_filepath, new_filepath)
                        else:
                            print(f"⚠️ Could not find title for video ID: {video_id} (Video might be deleted or private)")

                    except Exception as e:
                        print(f"❌ An error occurred processing {video_id}: {e}")
                else:
                    print(f"⏭️ Skipping '{filename}' (Doesn't look like a valid YouTube ID)")

    except Exception as e:
        print(f"❌ A critical error occurred. Your API key might be invalid or you've exceeded your quota.")
        print(f"   Error details: {e}")

    print("\n🎉 Renaming process complete!")

# Run the function
if __name__ == "__main__":
    # --- IMPORTANT ---
    # BEFORE RUNNING: MAKE A BACKUP OF YOUR VIDEO FOLDER!
    rename_videos()