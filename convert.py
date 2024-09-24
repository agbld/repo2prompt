import os
import sys
import argparse

def process_repo(repo_path, output_file, extensions, exclude_dirs):
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for root, dirs, files in os.walk(repo_path, topdown=True):
            # Exclude specified directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file_name in files:
                # Include only specified file extensions
                if extensions:
                    if not any(file_name.endswith(ext) for ext in extensions):
                        continue
                
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Write file name as a header
                        out_f.write(f"### File: {file_path}\n")
                        out_f.write(content)
                        out_f.write("\n\n")
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description='Dump and convert a code repository into LLM prompt/context.')
    parser.add_argument('repo_path', help='Path to the code repository.')
    parser.add_argument('-o', '--output', default='repo_context.txt', help='Output file name.')
    parser.add_argument('-e', '--extensions', nargs='*', help='File extensions to include, e.g., .py .js .java')
    parser.add_argument('--exclude_dirs', nargs='*', default=['.git', '.svn', '.hg', '__pycache__'], help='Directories to exclude.')
    args = parser.parse_args()
    
    process_repo(args.repo_path, args.output, args.extensions, args.exclude_dirs)

if __name__ == '__main__':
    main()
