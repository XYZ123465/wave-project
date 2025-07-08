from .wave_solver_base import WaveSolverBase

class ImplicitSolver(WaveSolverBase):
    def __init__(self, c: float, dx: float, dt: float):
        """
        隐式格式求解器
        :param c: 波速
        :param dx: 空间步长
        :param dt: 时间步长
        """
        super().__init__(c, dx, dt)
        pass
    
    def build_matrix(self, n_points: int):
        """
        构建系数矩阵
        :param n_points: 网格点数
        """
        pass
    
    def solve_step(self):
        """
        实现隐式差分格式
        """
        pass
