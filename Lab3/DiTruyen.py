import random

# Tính tổng quãng đường của một lộ trình
def calculate_distance(route, distance_matrix):
    distance = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    return distance + distance_matrix[route[-1]][route[0]]

# Tạo quần thể ban đầu ngẫu nhiên
def create_population(pop_size, cities):
    return [random.sample(cities, len(cities)) for _ in range(pop_size)]

# Chọn hai cha mẹ từ nửa tốt nhất của quần thể
def select_parents(population, distance_matrix):
    population.sort(key=lambda route: calculate_distance(route, distance_matrix))  # sắp xếp tăng dần quảng đường -> ngăns sẽ đươc ưu tiên
    return random.sample(population[:len(population)//2], 2)  #lấy nửa đầu tiên rồi chọn 2

# Lai ghép đơn giản giữ nửa đầu của cha mẹ đầu và nửa sau của cha mẹ thứ hai
def crossover(parent1, parent2):
    child = parent1[:len(parent1)//2]
    child += [city for city in parent2 if city not in child]
    return child

# đổi chỗ ngẫu nhiên hai thành phố
def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

# Tìm lộ trình ngắn nhất
def get_best_route(population, distance_matrix):
    return min(population, key=lambda route: calculate_distance(route, distance_matrix))


# Giải thuật di truyền đơn : Tạo quẩn thể -> lặp qua các thế hệ (Chọn cha mẹ, Lai ghép để tạo lộ trình con, Đột biến, Tạo quần thể mới) -> Chọn lộ trình tốt nhất
def genetic_algorithm_tsp(distance_matrix, cities, pop_size=100, generations=200, mutation_rate=0.05):
    population = create_population(pop_size, cities)
    for _ in range(generations):# Lặp qua các thế hệ
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = select_parents(population, distance_matrix)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2]) # Thêm con vào quần thể mới
        population = new_population
    best_route = get_best_route(population, distance_matrix)
    return best_route, calculate_distance(best_route, distance_matrix)


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
cities = [0, 1, 2, 3]

best_route, best_distance = genetic_algorithm_tsp(distance_matrix, cities)
print("Lộ trình tốt nhất:", best_route)
print("Tổng khoảng cách:", best_distance)
