import tkinter as tk

from simulation import Simulation


class App:

    def __init__(self, root):

        self.root = root

        self.root.title("Simulación Cola de Impresión")

        self.root.geometry("500x400")

        tk.Label(
            root,
            text="Duración"
        ).pack()

        self.duration_entry = tk.Entry(root)
        self.duration_entry.pack()

        self.duration_entry.insert(0, "300")

        tk.Label(
            root,
            text="Páginas por minuto"
        ).pack()

        self.ppm_entry = tk.Entry(root)
        self.ppm_entry.pack()

        self.ppm_entry.insert(0, "10")

        boton = tk.Button(
            root,
            text="Iniciar Simulación",
            command=self.run_simulation
        )

        boton.pack(pady=10)

        self.resultado = tk.Text(
            root,
            width=50,
            height=12
        )

        self.resultado.pack()

    def run_simulation(self):

        duration = int(self.duration_entry.get())

        ppm = int(self.ppm_entry.get())

        simulacion = Simulation(duration, ppm)

        datos = simulacion.run()

        self.resultado.delete("1.0", tk.END)

        self.resultado.insert(
            tk.END,
            f"Trabajos procesados: {datos['total']}\n"
        )

        self.resultado.insert(
            tk.END,
            f"Promedio espera: "
            f"{datos['average_wait']:.2f}\n"
        )

        self.resultado.insert(
            tk.END,
            f"Máximo cola: "
            f"{datos['max_queue_size']}\n"
        )