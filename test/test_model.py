# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

from lindbladmpo.LindbladMPOSolver import LindbladMPOSolver
import unittest
import numpy as np

s_output_path = "./"
s_cygwin_path = None
s_solver_path = None


class LindbladMPOSolverModel(unittest.TestCase):
	def test_All_zero(self):
		solver_params = {'tau': 1, 't_final': 1, 'N': 1, 'g_1': 0,
						 'output_files_prefix': s_output_path}
		solver = LindbladMPOSolver(solver_params, s_cygwin_path, s_solver_path)
		solver.solve()
		expected_XY = 0
		expected_Z = 1
		self.assertEqual(solver.result['1q'][(1, 'X', 1)], expected_XY)
		self.assertEqual(solver.result['1q'][(1, 'Y', 1)], expected_XY)
		self.assertEqual(solver.result['1q'][(1, 'Z', 1)], expected_Z)

	def test_hz_not_zero(self):
		solver_params = {'tau': 1, 't_final': 1, 'N': 1, 'g_1': 0, 'l_x': 0, 'h_z': 5,
						 'output_files_prefix': s_output_path}
		solver = LindbladMPOSolver(solver_params, s_cygwin_path, s_solver_path)
		solver.solve()
		expected_XY = 0
		expected_Z = 1
		self.assertEqual(solver.result['1q'][(1, 'X', 1)], expected_XY)
		self.assertEqual(solver.result['1q'][(1, 'Y', 1)], expected_XY)
		self.assertEqual(solver.result['1q'][(1, 'Z', 1)], expected_Z)

	def test_steady_state(self):
		solver_params = {'tau': 1, 't_final': 1, 'N': 1, 'g_1': 5, 'l_x': 0, 'h_z': 5,
						 'output_files_prefix': s_output_path}
		solver = LindbladMPOSolver(solver_params, s_cygwin_path, s_solver_path)
		solver.solve()
		expected_XY = 0
		expected_Z = 1
		self.assertEqual(solver.result['1q'][(1, 'X', 1)], expected_XY)
		self.assertEqual(solver.result['1q'][(1, 'Y', 1)], expected_XY)
		self.assertEqual(solver.result['1q'][(1, 'Z', 1)], expected_Z)

	def test_steady_state_2(self):
		solver_params = {'tau': 1, 't_final': 10, 'N': 1, 'g_1': 5, 'g_0': 1, 'l_x': 0, 'h_z': 5,
						 'output_files_prefix': s_output_path}
		solver = LindbladMPOSolver(solver_params, s_cygwin_path, s_solver_path)
		solver.solve()
		expected_XY = 0
		expected_Z = 4/6
		self.assertEqual(solver.result['1q'][(1, 'X', 1)], expected_XY)
		self.assertEqual(solver.result['1q'][(1, 'Y', 1)], expected_XY)
		self.assertEqual(solver.result['1q'][(1, 'Z', 1)], expected_Z)


if __name__ == '__main__':
	unittest.main()
