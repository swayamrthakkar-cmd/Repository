import yfinance as yf
data = yf.download("AAPL", period="24mo", interval="1d")

print(data)

ago0 = data["Close"].iloc[-1]
ago1 = data["Close"].iloc[-30]
ago2 = data["Close"].iloc[-60]
ago3 = data["Close"].iloc[-90]
ago4 = data["Close"].iloc[-120]
ago5 = data["Close"].iloc[-150]
ago6 = data["Close"].iloc[-180]
ago7 = data["Close"].iloc[-210]
ago8 = data["Close"].iloc[-240]
ago9 = data["Close"].iloc[-270]
ago10 = data["Close"].iloc[-300]
ago11 = data["Close"].iloc[-330]
ago12 = data["Close"].iloc[-360]

ago0_vol = data["Volume"].iloc[-1]
ago1_vol = data["Volume"].iloc[-30]
ago2_vol = data["Volume"].iloc[-60]
ago3_vol = data["Volume"].iloc[-90]
ago4_vol = data["Volume"].iloc[-120]
ago5_vol = data["Volume"].iloc[-150]
ago6_vol = data["Volume"].iloc[-180]
ago7_vol = data["Volume"].iloc[-210]
ago8_vol = data["Volume"].iloc[-240]
ago9_vol = data["Volume"].iloc[-270]
ago10_vol = data["Volume"].iloc[-300]
ago11_vol = data["Volume"].iloc[-330]
ago12_vol = data["Volume"].iloc[-360]

array_vol = [ago0_vol, ago1_vol, ago2_vol, ago3_vol, ago4_vol, ago5_vol, ago6_vol, ago7_vol, ago8_vol, ago9_vol, ago10_vol, ago11_vol, ago12_vol]

array = [ago0, ago1, ago2, ago3, ago4, ago5, ago6, ago7, ago8, ago9, ago10, ago11, ago12]

def longTermMomentum(array):
    positive = 0
    gains = []
    for i in range(len(array)-1):
        gains.append(array[i] - array[i+1])

    for g in gains:
        if g > 0:
            positive += 1
        
    score = (positive / len(gains)) * 100
    return score

def longTermVolume(array):
    ...