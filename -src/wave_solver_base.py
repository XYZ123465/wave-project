class WaveSolverBase:
    def __init__(self, c: float, dx: float, dt: float):
        """
        偏微分方程求解器基类
        :param c: 波速
        :param dx: 空间步长
        :param dt: 时间步长
        """
        pass
    
    def initialize(self, u0: 'ndarray', v0: 'ndarray'):
        """
        初始化位移场和速度场
        :param u0: 初始位移场
        :param v0: 初始速度场
        """
        pass
    
    def solve_step(self):
        """
        求解单个时间步
        """
        pass
    
    def solve(self, t_steps: int) -> list:
        """
        求解多个时间步
        :param t_steps: 时间步数
        :return: 解序列
        """
        pass
    
    def apply_boundary_conditions(self):
        """
        应用边界条件
        """
        pass

