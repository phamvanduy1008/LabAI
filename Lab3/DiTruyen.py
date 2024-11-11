import random

# Tính tổng quãng đường của lộ trình
def calculate_distance(route, distance_matrix):
    distance = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    return distance + distance_matrix[route[-1]][route[0]]  # Quay lại điểm đầu

# Khởi tạo quần thể ban đầu với các lộ trình ngẫu nhiên
def create_population(pop_size, cities):
    return [random.sample(cities, len(cities)) for _ in range(pop_size)]

# Chọn hai lộ trình ngẫu nhiên dựa trên độ tốt của chúng
def select_parents(population, distance_matrix):
    population.sort(key=lambda route: calculate_distance(route, distance_matrix))
    return random.choices(population[:len(population)//2], k=2)

# Lai ghép hai lộ trình bằng cách giữ một đoạn của cha mẹ đầu và thêm thành phố còn lại từ cha mẹ thứ hai
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = parent1[start:end]
    child += [city for city in parent2 if city not in child]
    return child

# Thực hiện đột biến bằng cách đổi chỗ hai thành phố ngẫu nhiên
def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

# Tìm lộ trình ngắn nhất trong quần thể
def get_best_route(population, distance_matrix):
    return min(population, key=lambda route: calculate_distance(route, distance_matrix))

# Hàm chính giải thuật di truyền cho bài toán TSP
def genetic_algorithm_tsp(distance_matrix, cities, pop_size=100, generations=200, mutation_rate=0.05):
    population = create_population(pop_size, cities)
    for _ in range(generations):
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = select_parents(population, distance_matrix)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
    best_route = get_best_route(population, distance_matrix)
    return best_route, calculate_distance(best_route, distance_matrix)

# Ma trận khoảng cách giữa các thành phố
distance_matrix = [
    [0, 10, 15, 20],
    [0, 0, 35, 25],
    [5, 35, 0, 30],
    [0, 25, 30, 0]
]
cities = [0, 1, 2, 3]  # Các thành phố

# Chạy thuật toán di truyền
best_route, best_distance = genetic_algorithm_tsp(distance_matrix, cities)
print("Lộ trình tốt nhất:", best_route)
print("Tổng khoảng cách:", best_distance)
