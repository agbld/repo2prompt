# repo2prompt

`repo2prompt` is a simple Python tool designed to convert an entire code repository into a text file that can be used as input (prompt/context) for large language models (LLMs) in context-based question-answering tasks. It recursively traverses a repository, collects file contents, and formats them for easier comprehension by an LLM.

## Features

- Recursively scans all files in a code repository.
- Allows you to specify which file extensions to include (e.g., `.py`, `.js`, `.java`).
- Excludes version control directories (e.g., `.git`, `.svn`) and can exclude other directories as needed.
- Outputs a single text file containing file paths and their contents.
- Ideal for preparing code repositories for context-based QA tasks with LLMs.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/repo2prompt.git
cd repo2prompt
```

2. Ensure you have Python 3 installed. You can install it from [here](https://www.python.org/downloads/) if necessary.

3. No external dependencies are required. The script runs with Python’s standard library.

## Usage

You can run the script from the command line by providing the path to the repository you want to process, and optionally specifying the output file name and file extensions to include.

```bash
python dump_repo.py /path/to/your/repo -o repo_context.txt -e .py .js .java
```

### Arguments:

- **repo_path**: (Required) The path to the repository you want to process.
- `-o`, `--output`: (Optional) Specify the output file name. Defaults to `repo_context.txt`.
- `-e`, `--extensions`: (Optional) A space-separated list of file extensions to include (e.g., `.py .js .java`). If omitted, the script processes all files.
- `--exclude_dirs`: (Optional) Directories to exclude from processing. Defaults to excluding `.git`, `.svn`, `.hg`, and `__pycache__`.

### Example:

```bash
# Convert all Python and JavaScript files from a repo to an LLM-friendly context file
python dump_repo.py /path/to/your/repo -o output.txt -e .py .js
```

## Example Output

The generated output file will look like this:

```
### File: /path/to/your/repo/script.py
# Content of script.py

### File: /path/to/your/repo/module/utils.js
// Content of utils.js

...
```

Each file is prefixed with its relative path, followed by its content.

## Limitations

- The script concatenates files into a single text file. Be mindful of the LLM's maximum context length when working with large repositories.
- No file summarization or chunking is performed by default. Consider adding custom logic if your repo is too large for a single LLM prompt.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

---

Feel free to adjust any sections based on your repository's structure or additional features you might add!