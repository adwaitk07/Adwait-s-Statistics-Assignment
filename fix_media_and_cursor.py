"""
Update HTML to use <img> tags for WebP animations and fix cursor CSS
"""

import re

# 1. Update HTML
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace video tags with img tags
# Pattern matches: <div class="video-solution">\s*<video controls><source src="(.*?)" type="video/webm">.*?</video>\s*</div>
pattern = r'<div class="video-solution">\s*<video controls><source src="(.*?)" type="video/webm">.*?</video>\s*</div>'

def replace_video(match):
    video_path = match.group(1).replace('.webm', '.webp')
    return f'<div class="video-solution"><img src="{video_path}" alt="Video Solution" style="width: 100%; border-radius: 0.5rem;"></div>'

content = re.sub(pattern, replace_video, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[SUCCESS] Replaced <video> tags with <img> tags in index.html")

# 2. Update CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Remove the block that forces cursor: pointer
# We'll replace it with a rule that ensures custom cursor is used everywhere
# except maybe links where we might want a custom pointer, but user asked to fix "cursor turning back to normal"
# so we will enforce custom cursor more strictly.

pointer_rule = r'/\* Allow normal cursor for video controls and interactive elements \*/.*?cursor: pointer !important;\s*}'
css_content = re.sub(pointer_rule, '', css_content, flags=re.DOTALL)

# Ensure * { cursor: none !important; } is still there (it is)
# But we need to make sure the custom cursor is applied.
# The custom cursor is usually applied via JS or a specific class.
# Let's check how it's implemented.
# Assuming there's a custom cursor element.

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("[SUCCESS] Removed cursor override from style.css")
