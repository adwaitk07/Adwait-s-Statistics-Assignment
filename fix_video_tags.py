"""
Update HTML to use <video> tags with autoplay for WebM files
"""

import re

# Update HTML
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace img tags with video tags
# Pattern matches: <div class="video-solution"><img src="(.*?)" alt="Video Solution" style="width: 100%; border-radius: 0.5rem;"></div>
pattern = r'<div class="video-solution"><img src="(.*?)" alt="Video Solution" style="width: 100%; border-radius: 0.5rem;"></div>'

def replace_with_video(match):
    # Get path and change extension to .webm
    img_path = match.group(1)
    video_path = img_path.replace('.webp', '.webm')
    
    # Create video tag with autoplay, loop, muted, playsinline
    # We also keep 'controls' so user can scrub if they want
    return f'''<div class="video-solution">
        <video controls autoplay loop muted playsinline style="width: 100%; border-radius: 0.5rem;">
            <source src="{video_path}" type="video/webm">
            Your browser does not support the video tag.
        </video>
    </div>'''

content = re.sub(pattern, replace_with_video, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[SUCCESS] Replaced <img> tags with <video> tags (autoplay enabled) in index.html")
