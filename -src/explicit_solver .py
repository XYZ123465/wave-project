from .wave_solver_base import WaveSolverBase

class ExplicitSolver(WaveSolverBase):
    def __init__(self, c: float, dx: float, dt: float):
        """
        显式格式求解器
        :param c: 波速
        :param dx: 空间步长
        :param dt: 时间步长
        """
        super().__init__(c, dx, dt)
    
    def solve_step(self):
        """
        实现显式差分格式
        """
        pass
