import os
import time
import requests
import streamlit as st
import pandas as pd
import json  # For JSON serialization

# Define your SerpApi key directly or set via environment variables
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")  

# Function to perform a web search using SerpApi with retry logic
def perform_web_search(query, retries=3, delay=5):
    url = "https://serpapi.com/search"
    params = {
        "q": query,  # The search query
        "api_key": SERPAPI_API_KEY,  # Your SerpApi API key
        "engine": "google",  # You can use different engines here (e.g., google, bing)
    }
    
    for attempt in range(retries):
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            return response.json()  # Successful response
        elif response.status_code == 429:  # Too many requests error
            st.warning(f"Rate limit exceeded, retrying in {delay} seconds...")
            time.sleep(delay)  # Wait before retrying
        else:
            st.error(f"Error retrieving search results. Status code: {response.status_code}, Response: {response.text}")
            break
    return None

# Function to extract relevant data from the search results
def extract_relevant_info(search_results):
    extracted_data = []
    
    if search_results and 'organic_results' in search_results:
        for result in search_results['organic_results']:
            link = result.get("link", "")
            
            # If the result contains a link, add it directly
            if link:
                extracted_data.append(link)
                break  # Stop after the first valid link

            # If no link, extract a brief snippet
            snippet = result.get("snippet", "")
            if snippet:
                extracted_data.append(snippet)
                break  # Stop after the first relevant snippet

    return extracted_data

# Streamlit UI
st.title("AI Data Extractor")
st.write("Upload a CSV or Google Sheet, specify your query, and retrieve and parse data.")

# File upload section
uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

if uploaded_file is not None:
    # Read uploaded CSV
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data Preview:")
    st.dataframe(df.head())

    # Select column for entity
    selected_column = st.selectbox("Select the column to search for entities", df.columns)

    # Input for custom prompt
    prompt_template = st.text_input("Enter your custom prompt (e.g., 'What is the website of {entity}')")

    if st.button("Run Search and Extract"):
        if prompt_template and selected_column:
            results = []
            for entity in df[selected_column]:
                st.write(f"Processing: {entity}")
                search_query = prompt_template.replace("{entity}", entity)

                # Get web search results using SerpApi
                search_results = perform_web_search(search_query)
                if search_results:
                    # Extract relevant data from the search results
                    parsed_data = extract_relevant_info(search_results)
                    
                    # Convert the extracted data into a simple, plain text format
                    parsed_data_str = "\n".join(parsed_data)  # Join as plain text
                    results.append({"Entity": entity, "Extracted Data": parsed_data_str})
            
            # Display results
            results_df = pd.DataFrame(results)
            st.write("Extracted Results:")
            st.dataframe(results_df)

            # Download option
            csv_download = results_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", csv_download, "extracted_results.csv", "text/csv")
        else:
            st.warning("Please ensure a prompt template and column are selected.")
