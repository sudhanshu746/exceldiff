# Excel Sheet Comparator

Excel Sheet Comparator is a Streamlit application designed to allow users to compare two Excel sheets in real time through an interactive user interface. It highlights the differences between corresponding cells from two sheets, making it easier to identify discrepancies.

## Features

- Upload two separate Excel files (.xlsx) for comparison.
- Select specific sheets within these files to compare.
- Choose unique common column(s) that will serve as the identifier for row comparisons.
- Instantly view differences highlighted directly in the user interface.
- Differences are displayed with content either separated by `|` for mismatches or shown side by side for matches.
- Download the results in Excel format directly from the app.

## Installation

To run this Streamlit app, you must have Python installed on your computer. Additionally, please ensure you have the following packages installed:

```bash
pip install streamlit pandas openpyxl
```

Clone the repository or download the app's code to your local machine. Once you have all the necessary files and requirements, run the application using Streamlit:

```bash
streamlit run checkdiff.py
```

Replace `your_app_name.py` with the path to the script if it's located in a different directory.

## Usage

The application has a simple workflow:

1. **Upload Excel Files**: Use the provided file uploaders to select your first and second Excel files respectively.
   
2. **Select Sheets**: After uploading each file, choose the sheet you wish to compare by selecting it from the dropdown menu that appears.

3. **Select Unique Identifier**: Pick one or more columns that uniquely identify each row across the sheets. This will be used for alignment during the comparison.

4. **Compare Sheets**: Click on the 'Compare Sheets' button to initiate the comparison. If both files and sheet names are correctly selected, the app will proceed to show you the differences.

5. **Review & Download**: Observe highlighted discrepancies on the screen and use the 'Download Comparison Excel' button to save the results locally.

## Contributing

Feel free to fork the repository and submit pull requests. You can also report bugs or request features by opening issues on the GitHub page of this project.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

**Note**: The above contact information (email/Slack) is fictitious; replace it with your actual contact details.

---

Good luck with your comparisons, and feel free to contribute to the project!