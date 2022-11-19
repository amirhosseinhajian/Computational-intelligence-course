import random
import time

start = time.time()
current_population = []
fitness_value = []
parrent = []
ofspring = []
next_population = []

def initial_population():
    global current_population
    global fitness_value
    for i in range(20):
        buffer_list = [random.randint(0,7),
                       random.randint(0,7),
                       random.randint(0,7),
                       random.randint(0,7),
                       random.randint(0,7),
                       random.randint(0,7),
                       random.randint(0,7),
                       random.randint(0,7),]
        current_population.append(buffer_list)
        fitness_value.append(28)

def fitness_function(key):
    if key == 1:
        global current_population
        global fitness_value
        for k in range(20):
            for i in range(8):
                for j in range(i + 1, 8):
                    if current_population[k][i] == current_population[k][j]:
                        fitness_value[k] -= 1
                    if current_population[k][j] == current_population[k][i] - (j - i):
                        fitness_value[k] -= 1
                    if current_population[k][j] == current_population[k][i] + (j - i):
                        fitness_value[k] -= 1

    elif key == 2:
        global ofspring
        children_value = [28, 28, 28, 28, 28]
        for k in range(5):
            for i in range(8):
                for j in range(i + 1, 8):
                    if ofspring[k][i] == ofspring[k][j]:
                        children_value[k] -= 1
                    if ofspring[k][j] == ofspring[k][i] - (j - i):
                        children_value[k] -= 1
                    if ofspring[k][j] == ofspring[k][i] + (j - i):
                        children_value[k] -= 1
        return children_value


def natural_selection_for_reproduction():
    global current_population
    global fitness_value
    global parrent
    parrent = []
    for i in range(10):
        max = -1
        index = 0
        for j in range(0, 20):
            if fitness_value[j] > max and current_population[j] not in parrent:
                max = fitness_value[j]
                index = j
        parrent.append(current_population[index])



def crossover():
    global parrent
    global ofspring
    ofspring = []
    for i in range(0, 10, 2):
        ofspring_buffer = []
        crossover_point = random.randint(1, 6)
        random_parrent_choice = random.randint(i, i+1)
        if random_parrent_choice == i:
            for j in range(0, crossover_point):
                ofspring_buffer.append(parrent[i][j])
            for k in range(crossover_point, 8):
                ofspring_buffer.append(parrent[i+1][k])
        else:
            for j in range(0, crossover_point):
                ofspring_buffer.append(parrent[i+1][j])
            for k in range(crossover_point, 8):
                ofspring_buffer.append(parrent[i][k])

        ofspring.append(ofspring_buffer)

def mutation():
    global ofspring
    random_index = random.randint(0, 10)
    if random_index >= 0 and random_index < 5:
        random_alen_index = random.randint(0, 7)
        random_alen_value = random.randint(0, 7)
        while random_alen_value == ofspring[random_index][random_alen_index]:
            random_alen_value = random.randint(0, 7)
        ofspring[random_index][random_alen_index] = random_alen_value

def natural_selection_for_survive():
    global next_population
    global current_population
    global ofspring
    global fitness_value
    children_fitness_value = fitness_function(2)
    children_death_index = 0
    for i in range(1, 5):
        if children_fitness_value[i] < children_fitness_value[children_death_index]:
            children_death_index = i

    chance_array = []
    for i in range(20):
        for j in range(fitness_value[i], 28):
            chance_array.append(i)
    random.shuffle(chance_array)
    death_parrent_index = []
    for i in range(4):
        random_parrent = random.choice(chance_array)
        while random_parrent in death_parrent_index:
            random_parrent = random.choice(chance_array)
        death_parrent_index.append(random_parrent)

    next_population = []
    fitness_value_buffer = []
    for i in range(20):
        if i not in death_parrent_index:
            next_population.append(current_population[i])
            fitness_value_buffer.append(fitness_value[i])
    for i in range(5):
        if i != children_death_index:
            next_population.append(ofspring[i])
            fitness_value_buffer.append(children_fitness_value[i])
    current_population = next_population
    fitness_value = fitness_value_buffer


initial_population()
fitness_function(1)
epochs = 0
while 28 not in fitness_value:
    natural_selection_for_reproduction()
    crossover()
    mutation()
    natural_selection_for_survive()
    epochs += 1

print("Result:")
print(current_population[fitness_value.index(28)])
print("--- %s seconds ---" % (time.time() - start))
print("epochs:" + str(epochs))