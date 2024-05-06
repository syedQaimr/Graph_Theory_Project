import requests
from bs4 import BeautifulSoup

def scrape_fashion_beauty_data(url, output_file):
   

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Identify the HTML elements (classes, tags, attributes) that contain the desired data
    items = soup.find_all('div',class_="jsx-32f40a79a91143c8 article")  # Replace with relevant selectors

    scraped_data = []
    for item in items:
        titles=item.find_all('p')
        for p_tag in titles:
            scraped_data.append(p_tag.text.strip())


    with open(output_file, 'w', encoding='utf-8') as f:
        # Write data to the text file in a user-friendly format (adjust as needed)
        # f.write(scraped_data)
        for item in scraped_data:
            f.write(item)

    return scraped_data
# Example usage (replace with the actual URL you want to scrape)
url = "https://www.onlymyhealth.com/list-of-necessary-fertility-tests-for-men-1712660410"  # Replace with the target website URL
output_file = "Diseases_Symptoms14.txt"  # Adjust the output file name
data = scrape_fashion_beauty_data(url, output_file)

if data:
    print(f"Scraped data saved to: {output_file}")
else:
    print("No data found on the website.")
