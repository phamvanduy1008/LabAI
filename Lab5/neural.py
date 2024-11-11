import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical


# Bước 1: Nạp dữ liệu từ file mnist.npz
with np.load('mnist.npz') as data:
    X_train = data['x_train']
    y_train = data['y_train']
    X_test = data['x_test']
    y_test = data['y_test']

# Bước 2: Chuẩn hóa dữ liệu
X_train = X_train / 255.0  #đưa giá trị pixel từ [0, 255] về khoảng [0, 1].
X_test = X_test / 255.0

# Chuyển đổi nhãn sang dạng one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Bước 3: Xây dựng mô hình mạng neural
model = Sequential([
    Flatten(input_shape=(28, 28)),       # Chuyển ma trận 28x28 thành vector 784
    Dense(128, activation='relu'),       # Lớp ẩn với 128 neuron và hàm kích hoạt ReLU
    Dense(64, activation='relu'),        # Lớp ẩn thứ hai với 64 neuron và hàm kích hoạt ReLU
    Dense(10, activation='softmax')      # Lớp đầu ra với 10 neuron (cho 10 chữ số), dùng softmax
])

# Bước 4: Biên dịch mô hình
model.compile(optimizer='adam',              # Sử dụng thuật toán tối ưu Adam
              loss='categorical_crossentropy',  # Hàm mất mát cho bài toán phân loại nhiều lớp
              metrics=['accuracy'])           # Đo lường độ chính xác

# Bước 5: Huấn luyện mô hình
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))  # Huấn luyện trong 10 epochs

# Bước 6: Đánh giá mô hình trên tập kiểm tra
loss, accuracy = model.evaluate(X_test, y_test)
print("Độ chính xác trên tập kiểm tra:", accuracy)

# Bước 7: Dự đoán trên một số mẫu
predictions = model.predict(X_test[:5])  # Dự đoán chữ số cho 5 mẫu đầu tiên trong tập kiểm tra
print("Dự đoán:", np.argmax(predictions, axis=1))  # In ra nhãn dự đoán
print("Giá trị thực:", np.argmax(y_test[:5], axis=1))  # In ra nhãn thực tế
