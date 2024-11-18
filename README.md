# **AI Data Extractor**

## **Project Description**
The **AI Data Extractor** is a user-friendly web application that automates data retrieval and processing from online sources.  
Users can:
- Upload a CSV file.
- Define a custom search prompt.
- Retrieve structured information by leveraging **SerpApi** and an AI-powered search mechanism.  

The extracted data is displayed in a table format and can be downloaded as a CSV file for further use.

---

## **Features**
1. **File Upload & Data Preview**:  
   - Upload CSV files and preview the data before processing.  

2. **Dynamic Query Input**:  
   - Create custom prompts using placeholders like `{entity}` for dynamic queries.  

3. **Automated Web Search**:  
   - Retrieve relevant search results for each entity using **SerpApi**.  

4. **Data Extraction & Display**:  
   - Parse and display structured information in a table format.  

5. **Download Results**:  
   - Download the extracted data as a CSV file for offline usage.

---
## **Usage Guide**

1. **Open the Application**:  
   Once the app starts, open the Streamlit link displayed in the terminal.

2. **Upload a File**:  
   Upload a CSV file containing the data you want to process. A preview of the data will be displayed.

3. **Select a Column**:  
   Choose the column containing entities (e.g., company names).

4. **Define a Custom Query**:  
   Input a custom prompt such as:  
   `"What is the website of {entity}?"`  
   Replace `{entity}` with each value from the selected column dynamically.

5. **Run the Search**:  
   Click **"Run Search and Extract"** to process the data.

6. **View and Download Results**:  
   - Extracted results will be displayed in a table.  
   - Use the **"Download CSV"** button to download the results.

---

## **Technologies Used**

- **Backend**: Python  
- **Frontend**: Streamlit  
- **Search API**: SerpApi  
- **Data Handling**: pandas  
- **Environment Management**: dotenv  

---

## **Notable Implementations**

1. **Retry Logic**:  
   Handles API rate limits and timeouts with automatic retries.  

2. **Dynamic Prompt Replacement**:  
   Enables flexible search templates using `{entity}` as a placeholder.  

3. **Data Parsing**:  
   Extracts URLs or snippets from search results efficiently.

---

## **Video Walkthrough**

Check out the 2-minute video demonstration: [https://drive.google.com/file/d/1AK06jXGv579um29NOrzMMX0miLUv9OTD/view?usp=drive_link](#)
