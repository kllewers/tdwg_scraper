import requests
import json
from bs4 import BeautifulSoup

def fetch_and_write_github_dwc_issues(token, repo_name="tdwg/dwc", output_filename="tdwg_dwc_issuetracker.jsonl"):
    """Fetch GitHub issues for the specified repository and write them to a .jsonl file"""
    
    # Configure the request headers with the provided authentication token
    headers = {'Authorization': f'token {token}'}
    
    # Construct the URL for fetching issues from the specified repository
    url = f"https://api.github.com/repos/{repo_name}/issues"
    
    # Make the request to get issues
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        issues = response.json()
        
        # Open a file to write the issues data
        with open(output_filename, "w") as file:
            for issue in issues:
                # Extract the title as prompt and body as completion from each issue
                prompt = issue["title"]
                completion = issue["body"]  # Consider preprocessing to remove markdown, URLs, etc.
                
                # Format the data as a JSON object (dictionary in Python)
                formatted_data = {"prompt": prompt, "completion": completion}
                
                # Convert the dictionary to a JSON string and write it to the file with a newline
                json_line = json.dumps(formatted_data)
                file.write(json_line + "\n")
    else:
        # Print an error message if the request failed
        print(f"Failed to fetch issues. Status code: {response.status_code}")
        print(f"Response body: {response.text}")

def fetch_and_write_github_ac_issues(token, repo_name="tdwg/ac", output_filename="tdwg_ac_issuetracker.jsonl"):
    """Fetch GitHub issues for the specified repository and write them to a .jsonl file"""
    
    # Configure the request headers with the provided authentication token
    headers = {'Authorization': f'token {token}'}
    
    # Construct the URL for fetching issues from the specified repository
    url = f"https://api.github.com/repos/{repo_name}/issues"
    
    # Make the request to get issues
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        issues = response.json()
        
        # Open a file to write the issues data
        with open(output_filename, "w") as file:
            for issue in issues:
                # Extract the title as prompt and body as completion from each issue
                prompt = issue["title"]
                completion = issue["body"]  # Consider preprocessing to remove markdown, URLs, etc.
                
                # Format the data as a JSON object (dictionary in Python)
                formatted_data = {"prompt": prompt, "completion": completion}
                
                # Convert the dictionary to a JSON string and write it to the file with a newline
                json_line = json.dumps(formatted_data)
                file.write(json_line + "\n")
    else:
        # Print an error message if the request failed
        print(f"Failed to fetch issues. Status code: {response.status_code}")
        print(f"Response body: {response.text}")
# URL of the page to scrape

def fetch_and_write_github_ltc_issues(token, repo_name="tdwg/ltc", output_filename="tdwg_ltc_issuetracker.jsonl"):
    """Fetch GitHub issues for the specified repository and write them to a .jsonl file"""
    
    # Configure the request headers with the provided authentication token
    headers = {'Authorization': f'token {token}'}
    
    # Construct the URL for fetching issues from the specified repository
    url = f"https://api.github.com/repos/{repo_name}/issues"
    
    # Make the request to get issues
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        issues = response.json()
        
        # Open a file to write the issues data
        with open(output_filename, "w") as file:
            for issue in issues:
                # Extract the title as prompt and body as completion from each issue
                prompt = issue["title"]
                completion = issue["body"]  # Consider preprocessing to remove markdown, URLs, etc.
                
                # Format the data as a JSON object (dictionary in Python)
                formatted_data = {"prompt": prompt, "completion": completion}
                
                # Convert the dictionary to a JSON string and write it to the file with a newline
                json_line = json.dumps(formatted_data)
                file.write(json_line + "\n")
    else:
        # Print an error message if the request failed
        print(f"Failed to fetch issues. Status code: {response.status_code}")
        print(f"Response body: {response.text}")
# URL of the page to scrape

def fetch_and_write_github_hc_issues(token, repo_name="tdwg/hc", output_filename="tdwg_hc_issuetracker.jsonl"):
    """Fetch GitHub issues for the specified repository and write them to a .jsonl file"""
    
    # Configure the request headers with the provided authentication token
    headers = {'Authorization': f'token {token}'}
    
    # Construct the URL for fetching issues from the specified repository
    url = f"https://api.github.com/repos/{repo_name}/issues"
    
    # Make the request to get issues
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        issues = response.json()
        
        # Open a file to write the issues data
        with open(output_filename, "w") as file:
            for issue in issues:
                # Extract the title as prompt and body as completion from each issue
                prompt = issue["title"]
                completion = issue["body"]  # Consider preprocessing to remove markdown, URLs, etc.
                
                # Format the data as a JSON object (dictionary in Python)
                formatted_data = {"prompt": prompt, "completion": completion}
                
                # Convert the dictionary to a JSON string and write it to the file with a newline
                json_line = json.dumps(formatted_data)
                file.write(json_line + "\n")
    else:
        # Print an error message if the request failed
        print(f"Failed to fetch issues. Status code: {response.status_code}")
        print(f"Response body: {response.text}")



def scrape_dwc_terms(url="https://dwc.tdwg.org/terms/", filename="dwc_terms.jsonl"):

    # Send a GET request to the page
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize an empty list to hold all terms
    terms = []

    # Find all tables and iterate over them
    for table in soup.find_all('table'):
        # Initialize an empty dictionary for the term
        term_data = {}
        
        # Extracting term name from the table's heading
        heading = table.find('th').text.strip()
        # Removing "Term Name: " prefix and updating to just "Term"
        term_name = heading.replace('Term Name: ', '')
        if term_name.startswith('Term Name '):
            term_name = term_name.replace('Term Name  ', '', 1)
        term_data['Term'] = term_name
        # Additional step to remove "Term Name " prefix if it exists

        
        # Iterate over all rows in the table body to extract term details
        for row in table.find('tbody').find_all('tr'):
            cells = row.find_all('td')
            if cells and len(cells) > 1:
                # Assuming the first cell is the key and the second is the value
                key = cells[0].text.strip()
                value = cells[1].text.strip()
                # Special handling for URLs
                if cells[1].find('a'):
                    value = cells[1].find('a')['href']
                term_data[key] = value

        # Add the populated term data to the terms list
        terms.append(term_data)

    # Specify the filename where the output should be saved
    file_name = filename

    # Write the output to a .jsonl file
    with open(file_name, 'w') as outfile:
        for term in terms:
            json_line = json.dumps(term)
            outfile.write(json_line + '\n')

    print(f"Data extracted and saved to {file_name}")

def scrape_ac_terms(url="https://ac.tdwg.org/termlist/", filename="ac_terms.jsonl"):
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize an empty list to hold all terms
    terms = []

    # Find all tables and iterate over them
    for table in soup.find_all('table'):
        # Initialize an empty dictionary for the term
        term_data = {}
        
        # Extracting term name from the table's heading
        heading = table.find('th').text.strip()
        # Removing "Term Name: " prefix and updating to just "Term"
        term_name = heading.replace('Term Name: ', '')
        term_data['Term'] = term_name
        
        # Iterate over all rows in the table body to extract term details
        for row in table.find('tbody').find_all('tr'):
            cells = row.find_all('td')
            if cells and len(cells) > 1:
                # Assuming the first cell is the key and the second is the value
                key = cells[0].text.strip()
                value = cells[1].text.strip()
                # Special handling for URLs
                if cells[1].find('a'):
                    value = cells[1].find('a')['href']
                term_data[key] = value

        # Add the populated term data to the terms list
        terms.append(term_data)

    # Specify the filename where the output should be saved
    file_name = filename

    # Write the output to a .jsonl file
    with open(file_name, 'w') as outfile:
        for term in terms:
            json_line = json.dumps(term)
            outfile.write(json_line + '\n')

    print(f"Data extracted and saved to {file_name}")

def scrape_ltc_terms(url="https://ltc.tdwg.org/terms/", filename="ltc_terms.jsonl"):
    # Send a GET request to the page
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize a list to store the scraped data
    terms_data = []

    # The given HTML seems to be a series of tables or similar structure for each term
    # Let's find each term's table and extract information
    tables = soup.find_all('table', class_='table-compact')  # Assuming class to narrow down

    for table in tables:
        term_data = {}
        # Iterate through each row in the table
        for row in table.find_all('tr'):
            # Try to extract data from both 'th' and 'td' elements
            header = row.find('th').get_text(strip=True) if row.find('th') else None
            value = row.find('td').get_text(strip=True) if row.find('td') else None

            # Check for link in 'td' and possibly override the value with the href attribute
            if row.find('td') and row.find('td').find('a'):
                value = row.find('td').find('a')['href']

            if header and value:
                if header == "Qualified Term":
                    header = "Term"
                term_data[header] = value

            

        if term_data:  # Ensure it's not empty
            terms_data.append(term_data)

    # Specify the filename where the output should be saved
    file_name = filename

    # Write the output to a .jsonl file
    with open(file_name, 'w') as outfile:
        for term in terms_data:
            json_line = json.dumps(term)
            outfile.write(json_line + '\n')

    print(f"Data extracted and saved to {file_name}")   
