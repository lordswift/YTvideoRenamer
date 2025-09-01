# TubeArchivist Video Renamer

This script renames YouTube video files in a local folder based on their titles fetched from the YouTube Data API v3. It scans the folder for `.mp4` files, extracts the YouTube video ID from the filename, retrieves the corresponding video title, and renames the file with a sanitized version of the title.

---

A Python script to restore original YouTube video titles to files downloaded by TubeArchivist, especially after the application or its database has been removed.

## The Problem: Lost Video Titles from TubeArchivist

[TubeArchivist](https://www.tubearchivist.com/) is a fantastic self-hosted media server for archiving YouTube videos. Internally, it downloads and saves videos using YouTube's unique 11-character **Video ID** as the filename.

For example, a video with the URL `https://www.youtube.com/watch?v=dQw4w9WgXcQ` will be saved as `dQw4w9WgXcQ.mp4`.

TubeArchivist uses its internal database to map these IDs to their proper titles, descriptions, and other metadata, presenting them in a clean web interface.

However, if you ever decide to uninstall TubeArchivist or if its database gets corrupted, you are left with the raw video files. Your folders will be full of cryptically named files like:

- `0GTZ-12hYtU.mp4`
- `3J8P7_S0HEU.mp4`
- `b0tCQhpP2P7LM.mp4`

Without the TubeArchivist database, it's impossible to know which video is which.

## The Solution

This script solves this problem by automating the recovery of the video titles. It works by:

1.  Scanning a specified folder for all `.mp4` video files.
2.  Treating each filename (without the extension) as a YouTube Video ID.
3.  Using the official **YouTube Data API v3** to query YouTube and fetch the video's official title.
4.  Sanitizing the title to create a valid filename (removing illegal characters like `\`, `/`, `:`, `*`, `?`, `"`, `<`, `>`, `|`).
5.  Renaming the file from its Video ID to its proper, human-readable title.

**Before:** `0GTZ-12hYtU.mp4`
**After:** `The Actual Video Title From YouTube.mp4`

## Features
- Automatically renames `.mp4` files based on YouTube video titles.
- Validates YouTube video IDs and skips invalid or inaccessible videos.
- Handles errors like invalid API keys, missing folder paths, or deleted/private videos.
- Sanitizes filenames to ensure compatibility with Windows.

---

## Prerequisites
1. **Python 3.7+**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Google API Client Library**: Install the required library using pip:
   ```bash
   pip install google-api-python-client
   ```
3. **YouTube Data API v3 Key**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or use an existing one.
   - Enable the **YouTube Data API v3** for your project.
   - Generate an API key and copy it.

---

## Setup
1. Clone or download this repository to your local machine.
2. Open the script file YTvid_renamer.py in a text editor.
3. Replace the placeholder `API_KEY` with your actual YouTube Data API v3 key:
   ```python
   API_KEY = "PASTE_YOUR_API_KEY_HERE"
   ```
4. Set the `VIDEO_FOLDER_PATH` to the full path of the folder containing your `.mp4` files:
   ```python
   VIDEO_FOLDER_PATH = r"C:\path\to\your\videos"
   ```
5. Save the file.

---

## Usage
1. **Backup Your Files**: Before running the script, make a backup of your video folder to avoid accidental data loss.
2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the folder containing the script:
     ```bash
     cd path\to\script
     ```
   - Run the script:
     ```bash
     python YTvid_renamer.py
     ```
3. **Output**:
   - The script will scan the folder, fetch video titles, and rename the files.
   - Logs will be printed to the console, indicating the renaming status for each file.

---

## Example
### Before Running:
```
Folder: C:\path\to\your\videos
Files:
- dQw4w9WgXcQ.mp4
- 3JZ_D3ELwOQ.mp4
```

### After Running:
```
Folder: C:\path\to\your\videos
Files:
- Rick Astley - Never Gonna Give You Up.mp4
- Mark Ronson - Uptown Funk ft. Bruno Mars.mp4
```

---

## Notes
- Only `.mp4` files are processed.
- The script assumes filenames are YouTube video IDs (11 characters long).
- Videos that are deleted, private, or inaccessible will be skipped.
- Ensure your API key has sufficient quota to process all files.

---

## Troubleshooting
- **Invalid API Key**: Ensure the API key is correct and has access to the YouTube Data API v3.
- **Folder Not Found**: Verify the `VIDEO_FOLDER_PATH` is correct and accessible.
- **Quota Exceeded**: The YouTube Data API has a daily quota. Wait for it to reset or request a higher quota.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
