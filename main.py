from instagrapi import Client
import moviepy.editor as mp
import os
from PIL import Image

INSTAGRAM_USERNAME = os.environ["instagram_username"]
INSTAGRAM_PW = os.environ["instagram_pw"]

cl = Client()

def resize_for_story(input_path, output_path="resized_story.jpg"):
    with Image.open(input_path) as img:
        img = img.convert("RGB")  # Ensure JPEG compatible
        img = img.resize((1080, 1920))  # Instagram story size
        img.save(output_path, quality=95)
    return output_path

cl.photo_upload_to_story(resize_for_story('image.jpg'))
