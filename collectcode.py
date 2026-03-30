import os

def collect_code(output_file="project_code.txt"):
    # Directories and files to ignore
    ignore_dirs = {
        '.git', 'node_modules', '__pycache__', 'venv', 'env', 
        '.vscode', 'dist', 'build', '.idea'
    }
    
    ignore_exts = {
        '.pyc', '.exe', '.dll', '.png', '.jpg', '.jpeg', '.gif', 
        '.ico', '.pkl', '.db', '.sqlite3', '.pdf', '.zip', '.tar', '.gz',
        '.mp3', '.mp4', '.wav'
    }
    
    # Exclude the output file and this script itself
    ignore_files = {output_file, 'collectcode.py'}
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk('.'):
            # Modify dirs in-place to skip ignored directories
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            
            for file in files:
                if file in ignore_files:
                    continue
                    
                ext = os.path.splitext(file)[1].lower()
                if ext in ignore_exts:
                    continue
                    
                filepath = os.path.join(root, file)
                
                # Write file header
                outfile.write("="*80 + "\n")
                outfile.write(f"File: {filepath}\n")
                outfile.write("="*80 + "\n\n")
                
                # Try reading and writing the file content
                try:
                    with open(filepath, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        outfile.write("\n\n")
                except UnicodeDecodeError:
                    outfile.write(f"[Binary or non-UTF-8 file ignored]\n\n")
                except Exception as e:
                    outfile.write(f"[Error reading file: {e}]\n\n")

if __name__ == "__main__":
    out_file = "project_code.txt"
    collect_code(output_file=out_file)
    print(f"Code collection complete. Output saved to {out_file}")
