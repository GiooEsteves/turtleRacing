import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['vermelho', 'verde', 'azul', 'laranja', 'amarelo', 'preto', 'roxo', 'rosa', 'marrom', 'ciano']
COLOR_MAP = {
    'vermelho': 'red',
    'verde': 'green',
    'azul': 'blue',
    'laranja': 'orange',
    'amarelo': 'yellow',
    'preto': 'black',
    'roxo': 'purple',
    'rosa': 'pink',
    'marrom': 'brown',
    'ciano': 'cyan'
}

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Digite o número de corredores (Entre 2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('A entrada não é numérica... Tente novamente!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('O número não está no intervalo de 2-10. Tente novamente!')

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(COLOR_MAP[color])
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Corrida de Tartarugas!')

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("O vencedor é a tartaruga de cor:", winner)
time.sleep(5)
