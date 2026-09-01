import io
from PIL import Image, ImageDraw, ImageEnhance
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from ml_image import image_analyzer

# Create Photo A: Base Zebra Stripe Pattern
img_a = Image.new('RGB', (400, 300), color=(240, 240, 240))
draw_a = ImageDraw.Draw(img_a)
for x in range(10, 390, 30):
    draw_a.rectangle([x, 10, x+15, 290], fill=(10, 10, 10))

buf_a = io.BytesIO()
img_a.save(buf_a, format='JPEG')

# Create Photo B: Same Animal under Different Lighting & Brightness (Altered Exposure)
enhancer = ImageEnhance.Brightness(img_a)
img_b = enhancer.enhance(1.4) # 40% brighter sunlight exposure

buf_b = io.BytesIO()
img_b.save(buf_b, format='JPEG')

# Run deep PyTorch feature vector extraction & re-ID matching
res_a = image_analyzer.analyze(buf_a.getvalue(), "zebra_morning.jpg")
res_b = image_analyzer.analyze(buf_b.getvalue(), "zebra_afternoon_bright.jpg")

print(f"Photo A (Morning Light)  Re-ID: {res_a['individual_id']}")
print(f"Photo B (Altered Light) Re-ID: {res_b['individual_id']}")

assert res_a['individual_id'] == res_b['individual_id'], f"Re-ID Mismatch: {res_a['individual_id']} != {res_b['individual_id']}"
print("\n[SUCCESS] Deep PyTorch Feature Vector Re-ID Verified! Same individual correctly identified across lighting & photo variations.")
