import numpy as np

class VortexEngine:
    def __init__(self, N=256, L=40.0, dt=0.001):
        self.N, self.L, self.dt = N, L, dt
        self.x = np.linspace(-L/2, L/2, N)
        self.y = np.linspace(-L/2, L/2, N)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        self.dx = self.x[1] - self.x[0]
        
        # Operador Cinético
        k = 2 * np.pi * np.fft.fftfreq(N, d=self.dx)
        KX, KY = np.meshgrid(k, k)
        self.K2 = KX**2 + KY**2
        self.exp_kinetic = np.exp(-1j * 0.5 * self.K2 * dt)
        
    def create_single_vortex(self):
        """Estado inicial: um único vórtice centralizado"""
        psi = np.ones((self.N, self.N), dtype=complex)
        r = np.sqrt(self.X**2 + self.Y**2)
        theta = np.arctan2(self.Y, self.X)
        
        # Perfil de densidade e fase topológica
        psi *= np.tanh(r / 1.5) * np.exp(1j * theta)
        
        # Filtro de borda para evitar o efeito 'xadrez'
        mask = np.exp(-(self.X**4 + self.Y**4) / (2 * 18**4))
        psi *= mask
        
        return psi / np.sqrt(np.sum(np.abs(psi)**2) * self.dx**2)

    def step(self, psi, V_ext, current_g):
        """Evolução temporal Split-Step"""
        # Passo de potencial e interação
        psi *= np.exp(-1j * (V_ext + current_g * np.abs(psi)**2) * self.dt / 2)
        # Passo cinético (Fourier)
        psi_k = np.fft.fft2(psi)
        psi_k *= self.exp_kinetic
        psi = np.fft.ifft2(psi_k)
        # Meio passo final
        psi *= np.exp(-1j * (V_ext + current_g * np.abs(psi)**2) * self.dt / 2)
        return psi / np.sqrt(np.sum(np.abs(psi)**2) * self.dx**2)
