```markdown
# PhishMe API CSV Downloader

This Python script interfaces with the PhishMe API to download CSV results from the previous month's phishing scenarios.

## Features

- Automatically retrieves scenarios from the previous month
- Downloads full CSV results for each scenario
- Handles API rate limiting with built-in delays
- Error handling for API requests and file operations

## Prerequisites

- Python 3.6 or higher
- PhishMe API token

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/phishme-api-downloader.git
   cd phishme-api-downloader
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Before running the script, you need to set up your API token and output directory:

1. Open the script in a text editor.
2. Replace `"PUT API TOKEN HERE"` with your actual PhishMe API token.
3. (Optional) Modify the `OUTPUT_DIR` variable to change where CSV files are saved.

## Usage

Run the script with:

```
python phishme_downloader.py
```

The script will:
1. Fetch scenarios from the previous month
2. Download CSV results for each scenario
3. Save CSV files in the specified output directory

## Output

CSV files will be saved in the format:
```
/home/user/phishmefailures_<scenario_id>.csv
```

## Error Handling

The script includes basic error handling for API requests and file operations. Check the console output for any error messages.

## Rate Limiting

To prevent hitting API rate limits, the script waits 5 seconds between each CSV download.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/phishme-api-downloader/issues) if you want to contribute.

## License

[MIT]

## Acknowledgments

- Original script by @M1ckeysofine


## Contact

If you have any questions or comments, please open an issue in this repository.
```
