# Shopify Bot

A very simple Shopify Bot to self checkout using Python and Selenium.

## Installation

Download [chromedriver](https://chromedriver.chromium.org/) and save in the `checkout-shopify` folder.

## Usage

- Add your `user information` for the checkout.
- Change `domain` and `handle` details.

```
➜  checkout-shopify git:(master) ✗ python checkout-shopify.py
1. Added to the cart...
2. Selecting Shipping...
3. Filling up Payment...
4. Credit Card details ready...
5. Processing payment...

            Order #1026
          
('Checkout total: ', 26.51839303970337, 'seconds.')
```

## Information
I made changes to this to work with Unifi in order to get a doorbell a while back. It worked then, not maintained. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
