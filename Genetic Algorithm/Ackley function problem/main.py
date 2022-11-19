import random
import math
import time

POPULATION = 750
start = time.time()
current_population = []
fitness_value = []
parrent = []
ofspring = []
next_population = []


def initial_population():
    global current_population
    for i in range(POPULATION):
        buffer = [random.randint(-32, 32), random.randint(-32, 32)]
        current_population.append(buffer)

def fitness_function(key):
    if key == 1:
        global fitness_value
        for i in range(len(current_population)):
            first_sum = 0.0
            second_sum = 0.0
            for c in current_population[i]:
                first_sum += c ** 2
                second_sum += math.cos(2.0 * math.pi * c)
            fitness_value.append(1 / (-20.0 * (math.exp(-0.2 * math.sqrt(first_sum / 2))) - math.exp(second_sum / 2) + 20 + math.e))

    elif key == 2:
        global ofspring
        children_fitness_value = []
        for i in range(len(ofspring)):
            first_sum = 0.0
            second_sum = 0.0
            for c in ofspring[i]:
                first_sum += c ** 2
                second_sum += math.cos(2.0 * math.pi * c)
            children_fitness_value.append(1 / (-20.0 * (math.exp(-0.2 * math.sqrt(first_sum / 2))) - math.exp(second_sum / 2) + 20 + math.e))
        return children_fitness_value

def natural_selection_for_reproduction():
    global current_population
    global fitness_value
    global parrent
    parrent = []
    for i in range(488):
        parrent.append(random.choice(current_population))

def crossover():
    global parrent
    global ofspring
    ofspring = []
    for i in range(0, 488, 2):
        ofspring_buffer = []
        random_parrent_choice = random.randint(i, i+1)
        if random_parrent_choice == i:
            ofspring_buffer.append(parrent[i][0])
            ofspring_buffer.append(parrent[i+1][1])
        else:
            ofspring_buffer.append(parrent[i+1][0])
            ofspring_buffer.append(parrent[i][1])

        ofspring.append(ofspring_buffer)

def mutation():
    global ofspring
    random_index = random.randint(0, 250)
    if random_index >= 0 and random_index < 244:
        random_alen_index = random.randint(0, 1)
        random_alen_value = random.randint(-32, 32)
        while random_alen_value == ofspring[random_index][random_alen_index]:
            random_alen_value = random.randint(-32, 32)
        ofspring[random_index][random_alen_index] = random_alen_value

def natural_selection_for_survive():
    global next_population
    global current_population
    global ofspring
    global fitness_value
    children_fitness_value = fitness_function(2)
    children_death_indexes = []
    for i in range(57):
        cmp = max(children_fitness_value)
        index = children_fitness_value.index(cmp)
        for j in range(244):
            if children_fitness_value[j] < cmp and j not in children_death_indexes:
                cmp = children_fitness_value[j]
                index = j
        children_death_indexes.append(index)

    parrent_death_indexes = []
    for i in range(187):
        cmp = max(fitness_value)
        index = fitness_value.index(cmp)
        for j in range(750):
            if fitness_value[j] < cmp and j not in parrent_death_indexes:
                cmp = fitness_value[j]
                index = j
        parrent_death_indexes.append(index)

    next_population = []
    fitness_value_buffer = []
    for i in range(750):
        if i not in parrent_death_indexes:
            next_population.append(current_population[i])
            fitness_value_buffer.append(fitness_value[i])
    for i in range(244):
        if i not in children_death_indexes:
            next_population.append(ofspring[i])
            fitness_value_buffer.append(children_fitness_value[i])
    current_population = next_population
    fitness_value = fitness_value_buffer


initial_population()
fitness_function(1)
best_fitness = max(fitness_value)
counter = 0
epochs = 0
while counter < 6:
    natural_selection_for_reproduction()
    crossover()
    mutation()
    natural_selection_for_survive()
    if max(fitness_value) > best_fitness:
        best_fitness = max(fitness_value)
        counter = 0
    else:
        counter += 1
    epochs += 1
index = fitness_value.index(best_fitness)
print("The minimum of the function is at point " + str(current_population[index]))
print("--- %s seconds ---" % (time.time() - start))
print("epochs:" + str(epochs))