import piexif
from PIL import Image
import hashlib
import io

def get_sha256_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

def extract_exif(image: Image.Image) -> dict:
    """
    Extract Exif metadata (JPEG) or info (PNG).
    """
    try:
        exif_data = image.info.get("exif")
        if exif_data:
            return piexif.load(exif_data)
        elif "png" in image.format.lower():
            return {"PNG Info": image.info}
        else:
            return {}
    except Exception as e:
        return {"Error": str(e)}

def format_metadata(raw_exif: dict) -> dict:
    formatted = {}
    for ifd_name, tags in raw_exif.items():
        if not isinstance(tags, dict):
            # If for some reason, tags are not a dict, we can't iterate .items()
            # Let's create a placeholder to avoid crashing.
            formatted[ifd_name] = {"Error": "Could not read metadata section."}
            continue

        formatted_tags = {}
        for tag, value in tags.items():
            try:
                tag_name = piexif.TAGS[ifd_name][tag]["name"]
            except KeyError:
                tag_name = str(tag)  # Use the tag itself if not found

            if isinstance(value, bytes):
                value = value.decode(errors='ignore')

            formatted_tags[tag_name] = value

        formatted[ifd_name] = formatted_tags
    return formatted

def strip_exif(image: Image.Image) -> io.BytesIO:
    """
    Return an image with metadata stripped (clean version).
    """
    clean_buffer = io.BytesIO()
    format_to_use = image.format if image.format in ["JPEG", "PNG", "TIFF", "BMP", "WEBP"] else "JPEG"
    image.save(clean_buffer, format=format_to_use, exif=b'' if format_to_use == "JPEG" else None)
    clean_buffer.seek(0)
    return clean_buffer