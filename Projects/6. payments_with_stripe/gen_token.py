import stripe


def gen_token():
    stripe.api_key = "sk_test_51LAv4mBBC9GFSnA6hbnV7iU7jB651dreqGLIxyjhnYVrXllfZDu3VrA4BfJv5b5yOXcJCFIOwQ2Ji7txq7YsOzPn00Iryjdprf"
    
    token = stripe.Token.create(
    card={
        "number": "4242424242424242",
        "exp_month": 11,
        "exp_year": 2022,
        "cvc": "314",
    },
    )

    print(token)

if __name__ == "__main__":
    gen_token()