import random

THETA = 0

def computing_weights(smp):
    # convert to bipolar
    vector = []
    for i in range(len(smp)):
        if smp[i] == 0:
            vector.append(-1)
        else:
            vector.append(1)
    weight = []
    for i in range(len(vector)):
        buffer = []
        for j in range(len(vector)):
            if i == j:
                buffer.append(0)
            else:
                buffer.append(vector[i] * vector[j])
        weight.append(buffer)
    return weight

def make_noise(smp):
    noisy_indexes = []
    buffer = []
    for i in range(50):
        while True:
            random_index = random.randint(0, 99)
            if random_index not in noisy_indexes:
                noisy_indexes.append(random_index)
                break
    for i in range(len(smp)):
        if i in noisy_indexes:
            if smp[i] == 1:
                buffer.append(0)
            else:
                buffer.append(1)
        else:
            buffer.append(smp[i])
    return buffer

def hopfield(sample, target):
    weight = computing_weights(sample)
    for counter in range(10):
        x = make_noise(sample)
        y = x
        random_index = []
        for i in range(100):
            random_index.append(i)
        random.shuffle(random_index)
        i = 0
        while True:
            y_in = x[random_index[i]]
            for j in range(len(y)):
                y_in += y[j] * weight[j][random_index[i]]
            if y_in > THETA:
                y[random_index[i]] = 1
            elif y_in < THETA:
                y[random_index[i]] = 0
            i += 1
            if y == target[0]:
                print(f"Characters identified in Experiment {counter+1}: A")
                break
            elif y == target[1]:
                print(f"Characters identified in Experiment {counter+1}: B")
                break
            elif y == target[2]:
                print(f"Characters identified in Experiment {counter+1}: C")
                break
            elif y == target[3]:
                print(f"Characters identified in Experiment {counter+1}: D")
                break
            if i == 100:
                i = 0
                random.shuffle(y)

#################### MAIN ########################
fonts = [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
          0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0,
          1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1,
          1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0,
          0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1,
          1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1,
          1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0,
          0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1,
          1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
          1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
          0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
          0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
          1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1,
          1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
          0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,
          0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1,
          1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]]

print("-----------------------------------")
print("A font has entered the network...")
print("-----------------------------------")
hopfield(fonts[0], fonts)
print("-----------------------------------")
print("B font has entered the network...")
print("-----------------------------------")
hopfield(fonts[1], fonts)
print("-----------------------------------")
print("C font has entered the network...")
print("-----------------------------------")
hopfield(fonts[2], fonts)
print("-----------------------------------")
print("D font has entered the network...")
print("-----------------------------------")
hopfield(fonts[3], fonts)
print("-----------------------------------")
print("-----------------------------------")
