# Giá nhà = b0 + b1 * diện tích + b2 * số phòng

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv('priceHouse.txt', header=None, names=["DienTich", "SoPhong", "Gia"])

X = data[["DienTich", "SoPhong"]] # đầu vào
y = data["Gia"] # đầu ra

# Chia dữ liệu thành 80% huyến luyện va 20% kiem tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo và huấn luyện mô hình để huấn luyện ra bo b1 b2
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)  # Sai số trung bình tuyệt đối
mse = mean_squared_error(y_test, y_pred)  # Sai số trung bình bình phương


print("MAE (Sai số trung bình tuyệt đối):", mae)
print("MSE (Sai số trung bình bình phương):", mse)

print("\nCác hệ số hồi quy:")
print("b0 (Hệ số chặn):", model.intercept_)
print("b1 (Hệ số diện tích):", model.coef_[0])
print("b2 (Hệ số số phòng):", model.coef_[1])

new_data = pd.DataFrame({"DienTich": [100, 150], "SoPhong": [3, 4]})
predictions = model.predict(new_data)

print("\nDự đoán giá nhà cho diện tích và số phòng mới:")
for i, prediction in enumerate(predictions):
    print(f"Nhà {i+1} - Diện tích: {new_data['DienTich'][i]}m², Số phòng: {new_data['SoPhong'][i]}, Giá nhà dự đoán: {prediction:.2f}")