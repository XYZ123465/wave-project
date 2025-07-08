# src/__init__.py
"""
波动方程求解器 - 核心模块
此包包含偏微分方程求解所需的所有类实现
"""

# 显式导入关键类和函数
from .wave_solver_base import WaveSolverBase
from .explicit_solver import ExplicitSolver
from .implicit_solver import ImplicitSolver
from .boundary_condition import BoundaryCondition
from .file_manager import FileManager
from .visualizer import Visualizer
from .solver_factory import SolverFactory

# 简化导入语句
__all__ = [
    'WaveSolverBase',
    'ExplicitSolver',
    'ImplicitSolver',
    'BoundaryCondition',
    'FileManager',
    'Visualizer',
    'SolverFactory'
]
