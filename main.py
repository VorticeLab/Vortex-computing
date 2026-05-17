import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from engine import VortexEngine

# Instância da física
eng = VortexEngine(N=256, dt=0.001)
psi = eng.create_single_vortex()

root = tk.Tk()
root.title("VorticeLab - Estabilização")

frame_ctrl = ttk.Frame(root, padding="10")
frame_ctrl.pack(side=tk.LEFT, fill=tk.Y)
frame_sim = ttk.Frame(root)
frame_sim.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

var_alpha = tk.DoubleVar(value=0.0)
var_g = tk.DoubleVar(value=500.0)

ttk.Label(frame_ctrl, text="Transporte:").pack()
ttk.Scale(frame_ctrl, from_=0, to=0.3, variable=var_alpha, orient="horizontal").pack()
ttk.Label(frame_ctrl, text="Interação:").pack()
ttk.Scale(frame_ctrl, from_=100, to=800, variable=var_g, orient="horizontal").pack()

txt_log = tk.Text(frame_ctrl, height=5, width=25, bg="black", fg="lime")
txt_log.pack(pady=10)

fig, ax = plt.subplots(figsize=(5, 5))
im = ax.imshow(np.abs(psi)**2, extent=[-20, 20, -20, 20], cmap='magma', origin='lower', interpolation='bilinear')
canvas = FigureCanvasTkAgg(fig, master=frame_sim)
canvas.get_tk_widget().pack()

def update(frame):
    global psi
    V = 0.06 * (eng.X**2 + eng.Y**2) - var_alpha.get() * eng.X
    psi = eng.step(psi, V, var_g.get())
    
    density = np.abs(psi)**2
    im.set_array(density)
    
    if frame % 20 == 0:
        max_d = np.max(density)
        txt_log.delete(1.0, tk.END)
        status = "Estável" if max_d < 2.5 else "Instável"
        txt_log.insert(tk.END, f"D-Max: {max_d:.3f}\nStatus: {status}")
    return [im]

ani = FuncAnimation(fig, update, interval=10, blit=True)
root.mainloop()
