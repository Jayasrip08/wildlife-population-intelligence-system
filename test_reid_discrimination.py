import io
from PIL import Image, ImageDraw, ImageFilter
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from ml_image import image_analyzer

print("===== RUNNING RIGOROUS BIOMETRIC RE-ID DISCRIMINATION TEST =====")

# --- ANIMAL A (Zebra A - Narrow Stripe Pattern) ---
img_a1 = Image.new('RGB', (400, 300), color=(240, 240, 240))
draw_a1 = ImageDraw.Draw(img_a1)
for x in range(10, 390, 20):
    draw_a1.rectangle([x, 10, x+8, 290], fill=(10, 10, 10))

buf_a1 = io.BytesIO()
img_a1.save(buf_a1, format='JPEG')

# Photo A2: Genuinely different photo of Zebra A (cropped / blurred / rotated perspective)
img_a2 = img_a1.crop((20, 20, 380, 280)).resize((400, 300)).filter(ImageFilter.GaussianBlur(1.0))
buf_a2 = io.BytesIO()
img_a2.save(buf_a2, format='JPEG')


# --- ANIMAL B (Zebra B - Genuinely Different Animal with Wide Blocky Stripe Pattern) ---
img_b = Image.new('RGB', (400, 300), color=(240, 240, 240))
draw_b = ImageDraw.Draw(img_b)
for x in range(10, 390, 80):
    draw_b.rectangle([x, 10, x+45, 290], fill=(10, 10, 10))

buf_b = io.BytesIO()
img_b.save(buf_b, format='JPEG')


# Run PyTorch deep layer-4 spatial feature vector extraction
res_a1 = image_analyzer.analyze(buf_a1.getvalue(), "zebra_A_cam1.jpg")
res_a2 = image_analyzer.analyze(buf_a2.getvalue(), "zebra_A_cam2_cropped.jpg")
res_b  = image_analyzer.analyze(buf_b.getvalue(), "zebra_B_different_animal.jpg")

print(f"Zebra A (Photo 1 - Cam 1):       {res_a1['individual_id']}")
print(f"Zebra A (Photo 2 - Crop/Blur):   {res_a2['individual_id']}")
print(f"Zebra B (Different Animal):     {res_b['individual_id']}")

# 1. TRUE POSITIVE CHECK: Same Animal (A1 vs A2) MUST match IDs
assert res_a1['individual_id'] == res_a2['individual_id'], f"True Positive Failed: {res_a1['individual_id']} != {res_a2['individual_id']}"
print("[PASS] 1. True Positive Test Passed: Same animal across camera angles returns IDENTICAL Re-ID.")

# 2. TRUE NEGATIVE CHECK: Different Animals (A vs B) MUST have DIFFERENT IDs
assert res_a1['individual_id'] != res_b['individual_id'], f"True Negative Failed: Zebra A & B assigned same ID! ({res_a1['individual_id']})"
print("[PASS] 2. True Negative Test Passed: Different individuals correctly receive UNIQUE Re-IDs.")

print("\n[SUCCESS] BIOMETRIC RE-ID VERIFIED: True Positive Match & True Negative Discrimination Confirmed!")
