import piexif
from PIL import Image, PngImagePlugin, TiffImagePlugin
import hashlib
import io


def get_sha256_hash(file_bytes: bytes) -> str:
    """Generate a SHA-256 hash for the provided file bytes."""
    return hashlib.sha256(file_bytes).hexdigest()


def extract_exif(image: Image.Image) -> dict:
    """
    Extract EXIF metadata from supported image formats (JPEG, PNG).
    """
    try:
        exif_data = image.info.get("exif")
        if exif_data:
            return piexif.load(exif_data)
        elif "png" in image.format.lower():
            return {"PNG Info": image.info}
        else:
            return {"Info": "No EXIF data found or unsupported format."}

    except Exception as e:
        return {"Error": str(e)}


def format_metadata(raw_exif: dict) -> dict:
    """
    Format raw EXIF data with readable tag names.
    """
    formatted = {}
    for ifd_name in raw_exif:
        if isinstance(raw_exif[ifd_name], dict):
            formatted[ifd_name] = {}
            for tag in raw_exif[ifd_name]:
                try:
                    tag_name = piexif.TAGS[ifd_name][tag]["name"]
                    value = raw_exif[ifd_name][tag]
                    if isinstance(value, bytes):
                        value = value.decode(errors="ignore")
                    formatted[ifd_name][tag_name] = value
                except:
                    pass
        else:
            formatted[ifd_name] = raw_exif[ifd_name]
    return formatted


def strip_exif(image: Image.Image) -> io.BytesIO:
    """
    Strip EXIF metadata from an image and return cleaned image buffer.
    """
    clean_buffer = io.BytesIO()
    format_to_use = image.format.upper() if image.format else "JPEG"

    # Force fallback for unknown formats
    if format_to_use not in ["JPEG", "PNG", "TIFF", "BMP", "WEBP"]:
        format_to_use = "JPEG"

    # Strip logic
    save_kwargs = {}

    if format_to_use == "JPEG":
        save_kwargs["exif"] = b""
    elif format_to_use == "PNG":
        save_kwargs["pnginfo"] = PngImagePlugin.PngInfo()
    elif format_to_use == "TIFF":
        save_kwargs["tiffinfo"] = TiffImagePlugin.ImageFileDirectory_v2()

    try:
        image.save(clean_buffer, format=format_to_use, **save_kwargs)
        clean_buffer.seek(0)
        return clean_buffer
    except Exception as e:
        raise RuntimeError(f"Failed to clean image: {str(e)}")
