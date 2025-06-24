import numpy as np
import yaml
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from mpl_toolkits.mplot3d import Axes3D

G = 1  # 万有引力常数

class NBodySystem:
    def __init__(self, masses, positions, velocities):
        self.N = len(masses)
        self.masses = np.array(masses)
        self.y0 = np.concatenate((positions.flatten(), velocities.flatten()))
    
    def derivatives(self, t, y):
        N = self.N
        positions = y[:3*N].reshape((N, 3))
        velocities = y[3*N:].reshape((N, 3))
        accelerations = np.zeros_like(positions)

        for i in range(N):
            for j in range(N):
                if i != j:
                    diff = positions[j] - positions[i]
                    distance = np.linalg.norm(diff) + 1e-5
                    accelerations[i] += G * self.masses[j] * diff / distance**3

        dydt = np.concatenate((velocities.flatten(), accelerations.flatten()))
        return dydt

    def energy(self, y):
        N = self.N
        positions = y[:3*N].reshape((N, 3))
        velocities = y[3*N:].reshape((N, 3))
        kinetic = 0.5 * np.sum(self.masses[:, None] * velocities**2)
        potential = 0
        for i in range(N):
            for j in range(i+1, N):
                r = np.linalg.norm(positions[i] - positions[j]) + 1e-5
                potential -= G * self.masses[i] * self.masses[j] / r
        return kinetic + potential

    def integrate(self, t_span, t_eval):
        sol = solve_ivp(self.derivatives, t_span, self.y0, t_eval=t_eval, rtol=1e-9, atol=1e-9)
        return sol

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    bodies = config['bodies']
    masses = [body['mass'] for body in bodies]
    positions = np.array([body['position'] for body in bodies])
    velocities = np.array([body['velocity'] for body in bodies])

    t_start = config['simulation']['t_start']
    t_end = config['simulation']['t_end']
    steps = config['simulation']['steps']

    output_cfg = config['output']

    return masses, positions, velocities, t_start, t_end, steps, output_cfg

def visualize(system, sol, output_cfg):
    N = system.N
    positions = sol.y[:3*N].reshape((N, 3, -1))

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    lim = np.max(np.abs(positions))
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_title(f"{N}-Body Simulation")

    lines = []
    points = []
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    for i in range(N):
        line, = ax.plot([], [], [], color=colors[i % len(colors)], label=f'Body {i+1}')
        point, = ax.plot([], [], [], color=colors[i % len(colors)] + 'o')
        lines.append(line)
        points.append(point)
    ax.legend()

    def update(frame):
        for i in range(N):
            lines[i].set_data(positions[i, 0, :frame], positions[i, 1, :frame])
            lines[i].set_3d_properties(positions[i, 2, :frame])
            points[i].set_data(positions[i, 0, frame], positions[i, 1, frame])
            points[i].set_3d_properties(positions[i, 2, frame])
        return lines + points

    ani = FuncAnimation(fig, update, frames=positions.shape[2], interval=20, blit=False)

    if output_cfg['save_animation']:
        filename = output_cfg['filename']
        writer = FFMpegWriter(fps=30)
        ani.save(filename, writer=writer)
        print(f"动画已保存为 {filename}")

    plt.show()

def main():
    masses, positions, velocities, t_start, t_end, steps, output_cfg = load_config('config.yaml')

    system = NBodySystem(masses, positions, velocities)

    t_eval = np.linspace(t_start, t_end, steps)
    sol = system.integrate((t_start, t_end), t_eval)

    # 能量守恒曲线
    energies = [system.energy(sol.y[:, i]) for i in range(sol.y.shape[1])]
    plt.figure()
    plt.plot(t_eval, energies)
    plt.title("Energy Conservation")
    plt.xlabel("Time")
    plt.ylabel("Total Energy")
    plt.grid()
    plt.show()

    visualize(system, sol, output_cfg)

if __name__ == "__main__":
    main()
