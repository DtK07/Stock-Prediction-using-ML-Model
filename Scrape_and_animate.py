from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import datetime
import pandas as pd

def realtime_stock_prices(code):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    url = f"https://finance.yahoo.com/quote/{code}"
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
    return price

stock_codes = ["AAPL", "GOOGL", "MSFT", 'META']

# Initialize an empty list to store data from each iteration
data_list = []

for step in range(1, 10):
    price = []
    col = []

    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for code in stock_codes:
        price.append(realtime_stock_prices(code))

    col = [time_stamp]
    col.extend(price)
    #print(col)
    # Append the current iteration's data to the list
    data_list.append(col)

# Create a DataFrame from the accumulated data
columns = ['Timestamp'] + stock_codes
df = pd.DataFrame(data_list, columns=columns)

# Display or use the final DataFrame 'df'
#print(df)

price1 = df['AAPL']
price2 = df['GOOGL']
price3 = df['MSFT']
price4 = df['META']

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex= True)
fig.suptitle('Big 4 - Stock price fluctuations', fontsize=12, y=1)
fig.text(0.06, 0.5, 'Price', ha='center', va='center', rotation='vertical')
x_values = []
y_values = []
for p in range(len(price1)):
    x_values.append(p)
    y_values.append(price1[p])
    ax1.set_title('Apple')
    ax1.plot(x_values,y_values, color='blue', linestyle='--', marker='o')
    plt.pause(2)

x_values = []
y_values = []
for p in range(len(price2)):
    x_values.append(p)
    y_values.append(price2[p])
    ax2.set_title('Google')
    ax2.plot(x_values, y_values, color='green', linestyle='-', marker='s')
    plt.pause(2)

x_values = []
y_values = []
for p in range(len(price3)):
    x_values.append(p)
    y_values.append(price3[p])
    ax3.set_title('Microsoft')
    ax3.plot(x_values, y_values, color='red', linestyle=':', marker='^')
    plt.pause(2)

x_values = []
y_values = []
for p in range(len(price4)):
    x_values.append(p)
    y_values.append(price4[p])
    ax4.set_title('Meta')
    ax4.plot(x_values, y_values, color='purple', linestyle='-.', marker='d')
    plt.pause(2)
plt.show()





