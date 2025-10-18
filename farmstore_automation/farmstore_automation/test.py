from playwright.sync_api import sync_playwright, TimeoutError
import re

def run_order_test():
    try:
        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch()
            context = browser.new_context()
            page = context.new_page()

            try: 
                # Direct to cpp farm order site
                page.goto("https://www.orderfarmstore.com/")

                # Select Farm Store Bag
                page.locator("a").filter(has_text="Farm Store Bag $").click()

                # Clarify order details (carryout and time)
                # Still in the process of ordering Farm Store Bag...
                page.get_by_text("Carryout", exact=True).click()

                # Select first available order time that is not the placeholder text
                try:
                    page.get_by_label("Pick an Order Time (All times").select_option(index=1)
                except Exception as e:
                    return {
                        "message": "Could not select a valid order time",
                        "error": f"{str(e)}"
                    }
                
                page.get_by_role("button", name="Update").click()

                # Add an additional Farm Store Bag (2 total in cart)
                page.get_by_role("button", name="+").click()
                page.get_by_role("button", name="Add to Cart $").click()

                # Add Cal Poly Orange Juice 64 oz to cart (3 total in cart)
                page.locator("a").filter(has_text="Cal Poly Orange Juice 64 oz").click()
                page.get_by_role("button", name="+").click()
                page.get_by_role("button", name="+").click()
                page.get_by_role("button", name="Add to Cart $").click()

                # Proceed to checkout in order to see the total price
                page.get_by_role("button", name="Checkout $").click()

                # Extract the total price from the checkout page (use regex to find price pattern)
                summary_html = page.locator("#summary-total").inner_html()
                match = re.search(r"\$([\d.,]+)", summary_html)
                if not match:
                    raise ValueError("Could not extract price from checkout page.")
                price = float(match.group(1).replace(",", "")) if match else None
                
                return { "total_price": price }

            except TimeoutError as e:
                return { 
                    "message": "Page loading took too long or specific elements could not be found",
                    "error": f"TimeoutError: {str(e)}"
                }
            
            except ValueError as e:
                return { 
                    "message": "Could not extract price from checkout page",
                    "error": f"ValueError: {str(e)}"
                }
            
            except Exception as e:
                return { 
                    "message": "An unexpected error occurred during the order process",
                    "error": f"{str(e)}"
                }
        
    except Exception as e:
        return { 
            "message": "An error occurred launching the browser.", 
            "error": f"{str(e)}"
        }