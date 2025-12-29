import numpy as np
import pandas as pd

np.random.seed(42)
#3000 users per platform
N_USERS = 3000

def generate_platform_data(platform):
    if platform == "web":
        time_spent = np.random.normal(loc=8, scale=3, size=N_USERS)
        conversion_rate = 0.18
        checkout_time = np.random.normal(loc=180, scale=60, size=N_USERS)
        items = np.random.poisson(lam=2.2, size=N_USERS)
        satisfaction = np.random.normal(loc=3.6, scale=0.8, size=N_USERS)

    else:  # android app
        time_spent = np.random.normal(loc=10, scale=3, size=N_USERS) #Time spent is a normal distribution with most values localiized around 10 [the mean].
        conversion_rate = 0.25
        checkout_time = np.random.normal(loc=140, scale=50, size=N_USERS)
        items = np.random.poisson(lam=2.8, size=N_USERS) #
        satisfaction = np.random.normal(loc=4.1, scale=0.7, size=N_USERS)

    converted = np.random.binomial(1, conversion_rate, N_USERS)

    df = pd.DataFrame({
        "platform": platform,
        "time_spent_min": np.clip(time_spent, 1, None),
        "converted": converted,
        "cart_to_checkout_sec": np.clip(checkout_time, 30, None),
        "items_in_cart": np.clip(items, 0, None),
        "satisfaction_rating": np.clip(
            np.round(satisfaction), 1, 5
        ).astype(int)
    })

    return df


web_df = generate_platform_data("web")
app_df = generate_platform_data("android")

data = pd.concat([web_df, app_df], ignore_index=True)
data.insert(0, "user_id", range(1, len(data) + 1))

data.to_csv("ecommerce_ab_test_data.csv", index=False)

print("Dataset created:", data.shape)
print(data.head())
