import streamlit as st
from PIL import Image, UnidentifiedImageError
import io
import os

from utils.metadata_tools import (
    get_sha256_hash,
    extract_exif,
    format_metadata,
    strip_exif
)

st.set_page_config(
    page_title="MetaWiper | Metadata Viewer & Shredder",
    page_icon="assests/favicon.ico",
    layout="centered"
)

# Use theme-based colors instead of hardcoded
st.markdown("""
    <style>
        .stApp {
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, h4 {
            color: var(--text-color);
            text-align: center;
        }
        .upload-box {
            border: 2px dashed var(--text-color);
            padding: 24px;
            border-radius: 12px;
            background-color: var(--block-background-color);
            transition: all 0.3s ease-in-out;
        }
        .metadata-section {
            padding: 20px;
            border-radius: 12px;
            background-color: var(--block-background-color);
            box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
            margin-bottom: 24px;
        }
        .btn-primary {
            background-color: var(--primary-color);
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
        }
        .btn-primary:hover {
            opacity: 0.9;
        }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("## MetaWiper – Metadata Viewer & Shredder")
st.markdown("<p style='text-align:center;'>Protect your privacy by removing hidden metadata (Exif) from images before sharing.</p>", unsafe_allow_html=True)

# --- File Upload UI ---
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "📤 Drag & drop or click to upload an image (JPEG, PNG, WebP, TIFF, BMP)",
    type=["jpg", "jpeg", "png", "webp", "tiff", "bmp"]
)
st.markdown('</div>', unsafe_allow_html=True)

# --- Image Processing ---
if uploaded_file is not None:
    try:
        file_bytes = uploaded_file.read()
        image = Image.open(io.BytesIO(file_bytes))

        st.image(image, caption="🖼️ Uploaded Image", use_container_width=True)

        # File Hash
        st.markdown('<div class="metadata-section">', unsafe_allow_html=True)
        st.markdown("### 🔐 File Hash (SHA-256)")
        st.code(get_sha256_hash(file_bytes), language="bash")
        st.markdown('</div>', unsafe_allow_html=True)

        # Metadata View
        st.markdown('<div class="metadata-section">', unsafe_allow_html=True)
        st.markdown("### 📋 Image Metadata (Exif)")
        raw_exif = extract_exif(image)
        if raw_exif:
            formatted = format_metadata(raw_exif)
            has_data = False
            for section, tags in formatted.items():
                if tags:
                    has_data = True
                    with st.expander(f"📂 {section}"):
                        if isinstance(tags, dict):
                            for k, v in tags.items():
                                st.markdown(f"- **{k}**: {v}")
                        else:
                            st.markdown(f"- {tags}")
            if not has_data:
                st.info("No visible metadata found in this image.")
        else:
            st.warning("No Exif metadata available.")
        st.markdown('</div>', unsafe_allow_html=True)

        # Metadata Strip
        st.markdown('<div class="metadata-section">', unsafe_allow_html=True)
        st.markdown("### 🧹 Remove Metadata")
        if st.button("Strip Metadata & Prepare Clean Image"):
            clean_image = strip_exif(image)
            st.success("✅ Metadata removed successfully!")

            original_filename = os.path.splitext(uploaded_file.name)[0]
            cleaned_ext = image.format.lower() or "jpg"
            cleaned_filename = f"{original_filename}_cleaned.{cleaned_ext}"

            st.download_button(
                label="📥 Download Clean Image",
                data=clean_image,
                file_name=cleaned_filename,
                mime=f"image/{cleaned_ext}"
            )
        st.markdown('</div>', unsafe_allow_html=True)

    except UnidentifiedImageError:
        st.error("❌ Uploaded file is not a valid image.")
else:
    st.info("🧭 Please upload a supported image to begin.")