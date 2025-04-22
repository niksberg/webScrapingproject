import requests
from bs4 import BeautifulSoup
products_to_track = [
    {
        "product_url": "https://www.amazon.in/Renewed-Samsung-Galaxy-Ocean-Storage/dp/B08DY3GFPJ/",
        "name": "Samsung M31"
    },

    {
        "product_url": "https://www.amazon.com/Sony-Unlocked-Smartphone-Official-Warranty/dp/B0C3WN5JZM",
        "name": "Sony Xperia 1V"
    },
    {
        "product_url": "https://www.amazon.in/Motorola-Edge-Magenta-256GB-Storage/dp/B0CFJF8M7N",
        "name": "Motorola Edge40"
    },
    {
        "product_url": "https://amzn.in/d/7xXXw16",
        "name": "Nokia 105"
    },
    {
        "product_url": "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY/",
        "name": "iPhone 15"
    },
    {
        "product_url": "https://www.amazon.in/Samsung-Thunder-Storage-Corning-Gorilla/dp/B0D7Z8CJP8/",
        "name": "Samsung M35"
    },
    {
        "product_url": "https://www.amazon.in/iPhone-16-128-GB-Control/dp/B0DGJHBX5Y/ref=sr_1_1_sspa?crid=1WO9IZIM6A1IU&dib=eyJ2IjoiMSJ9.wa1Mduoi5z5GFkGrEynB8Th3GOSXlDQ0G7VxioICMKZtFRNOPqmw4ggNnOLjMJRNHvBtXkChqUZxqh8HDWPgIy-0sXvsRIrqUwWksB2W6ukggSGVG7IcYnpHsGPrJSKHdzTfvmf-XZMwINe-HcAL3TNW12Hco8jEzRGVytJVJxKGbh4MPfssAuEOtkFlEkrbaTMXgAJQR8D73aINweOAkujlMemedQGmn85NA-5BEC0.QrnwqDdSYpPZ1IlOyk2UzxIIX57lqLgpIyiSkK8FM4A&dib_tag=se&keywords=iphone+16&qid=1741338347&sprefix=iphone+16%2Caps%2C433&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "name": "iPhone 16"
    },
    {
        "product_url": "https://www.amazon.in/Vivo-V50-Storage-Additional-Exchange/dp/B0DTHVHZC5/ref=sr_1_1?crid=OHPBKURBT9OJ&dib=eyJ2IjoiMSJ9.sQDvwgXOTwGt18eeJl3OaQ6x7WlQ1YViQOkYzxKzRXb9-Wew-qaX752-NYNFGUwG7jy2lM20-YxhOqYB8dSeX9xYN1kpVHe6yaPj8vwKmaOB9XdZSdBsTbZOE9OeKrZpyxqhX13Y1CjnFrqTZTZTnLAuWZFrPR7vfK8VOn9u0KcJNkffiOULOBD8l91UFFRWIGbRWIay6tocTXVLjXQ-340-SQEu0XYakEzFvhoMgNU.B6Mt_55uT_UgWVZCbdWyGcH2rD2cCJr0AM97LsyZWBc&dib_tag=se&keywords=vivo%2Bv%2B50&nsdOptOutParam=true&qid=1741340105&sprefix=vivo%2Caps%2C421&sr=8-1&th=1",
        "name": "vivo v50"
    }
]
def give_product_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find the whole part of the price
    price_whole = soup.find('span', class_='a-price-whole')
    # Find the fractional part of the price
    price_fraction = soup.find('span', class_='a-price-fraction')
    # Check if both parts are found
    if price_whole and price_fraction:
        # Combine the whole and fractional parts
        price_text = f"{price_whole.text}{price_fraction.text}".replace(',', '').strip()
        try:
            # Convert the price to a float and then to an integer
            product_price = int(float(price_text))
            return product_price
        except ValueError:
            print(f"Could not convert price '{price_text}' to an integer.")
            return None
    else:
        print("Price not found on the page.")
        return None


# Desired price thresholds for each product
desired_prices = {
    "Samsung M31": 8990,
    "Sony Xperia 1V": 60000,
    "Motorola Edge40": 30000,
    "Nokia 105": 1000,
    "iPhone 15": 62500,
    "Samsung M35": 17000,
    "iPhone 16": 74000,
    "vivo v50": 37000,
}

# Open the result file with utf-8 encoding
with open('my_result_file.txt', 'w', encoding='utf-8') as result_file:
    for product in products_to_track:
        print(f"Checking price for: {product['name']}")
        current_price = give_product_price(product['product_url'])
        if current_price is not None:
            print(f"Current Price: ₹{current_price}")
            desired_price = desired_prices.get(product['name'])
            if desired_price and current_price <= desired_price:
                print(f"{product['name']} is available at your desired price or lower.")
                result_file.write(
                    f"{product['name']} is available at your desired price or lower. Current price: ₹{current_price}\n")
            else:
                print(f"{product['name']} is still above your desired price.")
        print()
