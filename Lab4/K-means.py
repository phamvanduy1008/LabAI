import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.read_csv('Cust_Segmentation.csv')
X = data[['Age', 'Income', 'Card Debt', 'Other Debt', 'DebtIncomeRatio']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Dữ liệu sau khi chuẩn hóa

 # Xác định số cụm k bằng phương pháp Elbow
inertia = []
K = range(1, 10)  # Thử nghiệm với các giá trị k từ 1 đến 10

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)  # Độ biến thiên bên trong cụm

# Vẽ biểu đồ Elbow để chọn k
plt.plot(K, inertia, 'bo-')
plt.xlabel('Số cụm k')
plt.ylabel('Inertia')
plt.title('Phương pháp Elbow để xác định số cụm k')
plt.show()

# Bước 4: Áp dụng K-means với số cụm đã chọn (giả sử chọn k=3 từ biểu đồ Elbow)
kmeans = KMeans(n_clusters=3, random_state=42)  # Tạo mô hình K-means để huấn luyện
kmeans.fit(X_scaled)
data['Cluster'] = kmeans.labels_  # Gán nhãn cụm cho từng khách hàng

# Bước 5: Xem kết quả phân cụm
print(data[['Customer Id', 'Cluster']].head())  # Hiển thị ID khách hàng và cụm tương ứng

# Bước 6: Trực quan hóa (tuỳ chọn)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=data['Cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Phân cụm khách hàng với K-means')
plt.show()
