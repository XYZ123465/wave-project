from .explicit_solver import ExplicitSolver
from .implicit_solver import ImplicitSolver

class SolverFactory:
    @staticmethod
    def create_solver(method: str, **kwargs) -> 'WaveSolverBase':
        """
        创建求解器实例（工厂方法）
        :param method: 求解方法 ('explicit' 或 'implicit')
        :param kwargs: 求解器参数
        :return: 求解器实例
        """
        pass
