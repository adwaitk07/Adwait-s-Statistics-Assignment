"""
Replace video tags with img tags for WebP animated images
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match the video divs
# Looking for: <div class="video-solution">\s*<video...>...</video>\s*</div>
pattern = r'<div class="video-solution">\s*<video[^>]*>\s*<source src="([^"]+\.webm)"[^>]*>.*?</video>\s*</div>'

def replace_video_with_img(match):
    video_path = match.group(1).replace('.webm', '.webp')
    return f'<div class="video-solution"><p><strong>Video Solution:</strong></p><img src="{video_path}" alt="Solution Animation" style="width: 100%; border-radius: 0.5rem; margin-top: 10px;"></div>'

# Replace all video tags with img tags
content = re.sub(pattern, replace_video_with_img, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[SUCCESS] Replaced all <video> tags with <img> tags for WebP animations")
