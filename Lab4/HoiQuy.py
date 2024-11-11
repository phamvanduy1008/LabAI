# Giá nhà = b0 + b1 * diện tích + b2 * số phòng

#Bước 1: Nạp dữ liệu từ file priceHouse.txt.
#Bước 2: Xác định biến đầu vào X (diện tích, số phòng) và biến đầu ra y (giá nhà).
#Bước 3: Chia dữ liệu thành 2 phần: tập huấn luyện và tập kiểm tra.
#Bước 4: Tạo mô hình hồi quy tuyến tính và huấn luyện với tập huấn luyện.
#Bước 5: Dự đoán giá nhà từ tập kiểm tra.
#Bước 6: Tính và in ra các chỉ số đánh giá: MAE, MSE, và R-squared.


# Import các thư viện cần thiết
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Bước 1: Nạp dữ liệu từ file
data = pd.read_csv('priceHouse.txt', header=None, names=["DienTich", "SoPhong", "Gia"])

# Bước 2: Chuẩn bị dữ liệu (X: đầu vào, y: đầu ra)
X = data[["DienTich", "SoPhong"]]
y = data["Gia"]

# Bước 3: Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Bước 4: Tạo và huấn luyện mô hình dùng LinearRegression để huấn luyện ra bo b1 b2
model = LinearRegression()
model.fit(X_train, y_train)

# Bước 5: Dự đoán trên tập kiểm tra y_pred tương ứng với mỗi giá nhà của từng X_test
y_pred = model.predict(X_test)

# Bước 6: Đánh giá mô hình
mae = mean_absolute_error(y_test, y_pred)  # Sai số trung bình tuyệt đối
mse = mean_squared_error(y_test, y_pred)  # Sai số trung bình bình phương
r2 = r2_score(y_test, y_pred)  # Hệ số xác định

# Hiển thị kết quả
print("MAE (Sai số trung bình tuyệt đối):", mae)
print("MSE (Sai số trung bình bình phương):", mse)
print("R-squared (Hệ số xác định):", r2)
