import os
import sys
import shutil
import pathlib
import hashlib

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def main():
    script_dir = pathlib.Path(__file__).resolve().parent
    src_path = script_dir / "entry.png"
    
    if not src_path.is_file():
        print(f"Error: entry.png not found at expected path: {src_path}", file=sys.stderr)
        sys.exit(1)
        
    out_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir = pathlib.Path(out_dir_env)
    
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Error creating output directory {out_dir}: {e}", file=sys.stderr)
        sys.exit(1)
        
    dest_path = out_dir / "entry.png"
    
    try:
        shutil.copyfile(src_path, dest_path)
    except Exception as e:
        print(f"Error copying entry.png: {e}", file=sys.stderr)
        sys.exit(1)
        
    # Verify file integrity (size and sha256)
    src_size = src_path.stat().st_size
    dest_size = dest_path.stat().st_size
    
    if src_size != dest_size:
        print(f"Error: Size mismatch between source ({src_size}) and destination ({dest_size})", file=sys.stderr)
        sys.exit(1)
        
    src_sha = calculate_sha256(src_path)
    dest_sha = calculate_sha256(dest_path)
    
    if src_sha != dest_sha:
        print(f"Error: SHA256 mismatch between source ({src_sha}) and destination ({dest_sha})", file=sys.stderr)
        sys.exit(1)
        
    print(f"Successfully copied entry.png to {dest_path}")
    print(f"Size: {dest_size} bytes, SHA256: {dest_sha}")

if __name__ == "__main__":
    main()
