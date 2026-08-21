import os
import sys
import subprocess

def check_dependencies():
    import yt_dlp
    return yt_dlp

def download_videos(url, output_dir):
    yt_dlp = check_dependencies()
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\n--- Downloading videos from: {url} ---")
    print(f"Saving to: {output_dir}")
    
    # We choose format 'best' to ensure we download a merged video/audio stream without needing external ffmpeg dependencies if they aren't on the system
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(upload_date)s_%(title)s_%(id)s.%(ext)s'),
        'format': 'best',
        'ignoreerrors': True,
        'no_warnings': False,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Error downloading from {url}: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Create the base download directory
    base_dir = "downloaded_videos"
    os.makedirs(base_dir, exist_ok=True)
    
    # Facebook Videos
    fb_url = "https://www.facebook.com/wiredvibeapp"
    download_videos(fb_url, os.path.join(base_dir, "facebook"))
    
    # TikTok Videos
    tiktok_url = "https://www.tiktok.com/@wiredvibe"
    download_videos(tiktok_url, os.path.join(base_dir, "tiktok"))
    
    print("\nProcess finished! Please check the 'downloaded_videos' directory.")
