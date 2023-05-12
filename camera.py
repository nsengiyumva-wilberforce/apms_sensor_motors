from picamera import PiCamera
import io
from time import sleep
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# Initialize the camera
camera = PiCamera()

# Set the resolution and framerate of the camera
camera.resolution = (1000, 800)
camera.framerate = 30

# Start the camera preview
camera.start_preview()

# Wait for the camera to warm up
sleep(2)

# Capture a picture and load it as a PIL Image object
stream = io.BytesIO()
camera.capture(stream, format='jpeg')
stream.seek(0)
pil_image = Image.open(stream)

# Add a timestamp watermark to the image
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
draw = ImageDraw.Draw(pil_image)
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 36)
text_width, text_height = draw.textsize(timestamp, font)
x = pil_image.width - text_width - 10
y = pil_image.height - text_height - 10
draw.text((x, y), timestamp, font=font, fill=(255, 255, 255, 128))

# Save the watermarked image
filename = 'image.jpg'
pil_image.save(filename)

# Stop the camera preview
camera.stop_preview()
