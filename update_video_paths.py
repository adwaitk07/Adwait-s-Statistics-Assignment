"""
Update video paths in HTML to use local videos directory
"""

import re

# Read the current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Video file mappings - old paths to new paths
video_mappings = {
    "C:/Users/adwai/.gemini/antigravity/brain/ffbce717-9e9e-47a8-8e5b-06794be0768d/solution_q01_birthday_1763976466766.webp": "videos/solution_q01_birthday_1763976466766.webp",
    "C:/Users/adwai/.gemini/antigravity/brain/ffbce717-9e9e-47a8-8e5b-06794be0768d/solution_q02_false_positive_1763976608249.webp": "videos/solution_q02_false_positive_1763976608249.webp",
    "C:/Users/adwai/.gemini/antigravity/brain/ffbce717-9e9e-47a8-8e5b-06794be0768d/solution_q03_streaky_shooter_1763976654185.webp": "videos/solution_q03_streaky_shooter_1763976654185.webp",
    "C:/Users/adwai/.gemini/antigravity/brain/ffbce717-9e9e-47a8-8e5b-06794be0768d/solution_q04_system_reliability_1763976714779.webp": "videos/solution_q04_system_reliability_1763976714779.webp",
    "C:/Users/adwai/.gemini/antigravity/brain/ffbce717-9e9e-47a8-8e5b-06794be0768d/solution_q05_mean_median_1763976773984.webp": "videos/solution_q05_mean_median_1763976773984.webp",
    "C:/Users/adwai/.gemini/antigravity/brain/ffbce717-9e9e-47a8-8e5b-06794be0768d/solution_q06_rare_events_1763976865544.webp": "videos/solution_q06_rare_events_1763976865544.webp",
    "C:/Users/adwai/.gemini/antigravity/brain/ffbce717-9e9e-47a8-8e5b-06794be0768d/solution_q07_confidence_interval_1763976929746.webp": "videos/solution_q07_confidence_interval_1763976929746.webp",
    "C:/Users/adwai/.gemini/antigravity/brain/ffbce717-9e9e-47a8-8e5b-06794be0768d/solution_q08_sample_size_1763977002339.webp": "videos/solution_q08_sample_size_1763977002339.webp",
    "C:/Users/adwai/.gemini/antigravity/brain/ffbce717-9e9e-47a8-8e5b-06794be0768d/solution_q09_checkpoints_1763977060977.webp": "videos/solution_q09_checkpoints_1763977060977.webp",
    "C:/Users/adwai/.gemini/antigravity/brain/ffbce717-9e9e-47a8-8e5b-06794be0768d/solution_q10_power_analysis_1763977124203.webp": "videos/solution_q10_power_analysis_1763977124203.webp"
}

# Replace all video paths
for old_path, new_path in video_mappings.items():
    content = content.replace(old_path, new_path)

# Write the updated HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[SUCCESS] Updated all video paths to use local videos/ directory")
print("Videos are now accessible at:")
for new_path in video_mappings.values():
    print(f"  {new_path}")
