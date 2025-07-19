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
        if "exif" in image.info:
            exif_data = image.info["exif"]
            loaded_exif = piexif.load(exif_data)
            return loaded_exif if isinstance(loaded_exif, dict) else {"Error": "Invalid EXIF format."}

        elif image.format == "PNG":
            return {"PNG Info": {k: v for k, v in image.info.items() if isinstance(v, str)}}

        elif image.format == "TIFF":
            return {"TIFF Info": dict(image.tag.items()) if hasattr(image, "tag") else {}}

        else:
            return {"Info": "No EXIF data found or unsupported format."}

    except Exception as e:
        return {"Error": str(e)}


def format_metadata(raw_exif: dict) -> dict:
    """
    Format raw EXIF data with readable tag names.
    """
    formatted = {}

    for ifd_name, tags in raw_exif.items():
        if not isinstance(tags, dict):
            formatted[ifd_name] = {"Error": "Could not parse metadata section."}
            continue

        formatted_tags = {}
        for tag, value in tags.items():
            try:
                tag_name = piexif.TAGS[ifd_name][tag]["name"]
            except KeyError:
                tag_name = f"Unknown-{tag}"

            if isinstance(value, bytes):
                value = value.decode(errors='ignore')

            formatted_tags[tag_name] = value

        formatted[ifd_name] = formatted_tags

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
