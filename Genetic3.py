import random

POPULATION_SIZE = 6      
MUTATION_RATE = 0.05      
SIZE = 8                      

class Chromosome:
    def __init__(self, g=[]):
        if g:
            self.genes = g.copy()    
        else:
            self.genes = [random.choice([0, 1]) for _ in range(SIZE)]
        self.fitness = 0         
    
    def cal_fitness(self):          
        self.fitness = sum([self.genes[i] * (2 ** (SIZE - 1 - i)) for i in range(SIZE)])
        return self.fitness

    def __str__(self):
        return str(self.genes)


def print_p(pop):
    for i, x in enumerate(pop):
        print(f"염색체 #{i} = {x} 적합도 = {x.cal_fitness()}")
    print("")


def select(pop):
    max_value = sum(c.cal_fitness() for c in pop)
    pick = random.uniform(0, max_value)
    current = 0
    
    for c in pop:
        current += c.cal_fitness()
        if current > pick:
            return c


def crossover(pop):
    father = select(pop)
    mother = select(pop)
    index = random.randint(1, SIZE - 1)
    child1 = father.genes[:index] + mother.genes[index:]
    child2 = mother.genes[:index] + father.genes[index:]
    return (Chromosome(child1), Chromosome(child2))
    

def mutate(c):
    for i in range(SIZE):
        if random.random() < MUTATION_RATE:
            c.genes[i] = 1 - c.genes[i]  

######################
population = [Chromosome() for _ in range(POPULATION_SIZE)]

count = 0
population.sort(key=lambda x: x.cal_fitness(), reverse=True)
print("세대 번호 =", count)
print_p(population)
count = 1

while population[0].cal_fitness() < (2 ** SIZE - 1):
    new_pop = []


    for _ in range(POPULATION_SIZE // 2):
        c1, c2 = crossover(population)
        new_pop.append(c1)
        new_pop.append(c2)


    population = new_pop.copy()    
    

    for c in population: 
        mutate(c)


    population.sort(key=lambda x: x.cal_fitness(), reverse=True)
    print("세대 번호 =", count)
    print_p(population)
    count += 1
    if count > 100: 
        break

