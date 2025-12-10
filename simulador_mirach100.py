#Rodolfo Milhomem
#https://github.com/rodolfo-space-force/

import numpy as np
import matplotlib.pyplot as plt

def simular_lancamento(massa_kg=380, #peso estimado completo
                       empuxo_boosters=13400, #newtons
                       empuxo_turbojato=1570, #newtons
                       duracao_boosters=5, #segundos
                       duracao_total=10,
                       dt=0.01): #intervalo de tempo
    g = 9.81  #gravidade
    t = np.arange(0, duracao_total, dt)
    acc = np.zeros_like(t)
    vel = np.zeros_like(t)
    pos = np.zeros_like(t)

    for i in range(1, len(t)):
        if t[i] <= duracao_boosters:
            thrust = empuxo_boosters + empuxo_turbojato
        else:
            thrust = empuxo_turbojato
        acc[i] = (thrust - massa_kg * g) / massa_kg
        vel[i] = vel[i-1] + acc[i] * dt
        pos[i] = pos[i-1] + vel[i] * dt

    return t, acc, vel, pos

def plotar_resultados(t, acc, vel, pos, duracao_boosters):
    plt.figure(figsize=(10, 6))
    plt.plot(t, acc, label="Aceleração (m/s²)")
    plt.plot(t, vel, label="Velocidade (m/s)")
    plt.plot(t, pos, label="Posição (m)")
    plt.axvline(x=duracao_boosters, color='red', linestyle='--', label="Fim do booster")
    plt.title("Simulação de Lançamento do Mirach 100/5")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Valores")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    # Executar simulação com parâmetros padrão
    t, acc, vel, pos = simular_lancamento()
    plotar_resultados(t, acc, vel, pos, duracao_boosters=5)
