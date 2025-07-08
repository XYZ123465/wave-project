from src.solver_factory import SolverFactory
from src.boundary_condition import BoundaryCondition

def main():
    # 创建边界条件
    bc = BoundaryCondition(bc_type='dirichlet')
    bc.set_params({'left_value': 0.0, 'right_value': 0.0})
    
    # 使用工厂创建隐式求解器
    implicit_solver = SolverFactory.create_solver(
        method='implicit',
        c=1.0,
        dx=0.01,
        dt=0.005
    )
    
    # 初始化解
    implicit_solver.initialize(
        u0=[...],  # 初始位移场
        v0=[...]   # 初始速度场
    )
    
    # 求解偏微分方程
    solution = implicit_solver.solve(t_steps=1000)
    
    # 结果可视化
    visualizer = Visualizer()
    visualizer.animate_solution(solution)

if __name__ == "__main__":
    main()
