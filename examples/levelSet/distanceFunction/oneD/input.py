#!/usr/bin/env python

## 
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "input.py"
 #                                    created: 11/17/03 {10:29:10 AM} 
 #                                last update: 10/6/04 {4:30:46 PM} { 1:23:41 PM}
 #  Author: Jonathan Guyer <guyer@nist.gov>
 #  Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 #  Author: James Warren   <jwarren@nist.gov>
 #    mail: NIST
 #     www: http://www.ctcms.nist.gov/fipy/
 #
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  FiPy is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  
 #  Description: 
 # 
 #  History
 # 
 #  modified   by  rev reason
 #  ---------- --- --- -----------
 #  2003-11-17 JEG 1.0 original
 # ###################################################################
 ##

"""

Here we solve the level set equation in one dimension. The level set
equation is generally to solve a variable to be a distance function
such that,

.. raw:: latex

    $$ | \\nabla \\phi | = 1 $$

with a boundary condition,
    
    $\phi = 0$ at $x = L / 2$.

The solution to this problem in FiPy will be demonstrated
Set up the parameters:

   >>> dx = 0.5
   >>> dy = 2.
   >>> nx = 10
   >>> ny = 1
   >>> L = nx * dx

Construct the mesh:

   >>> from fipy.meshes.grid2D import Grid2D
   >>> mesh = Grid2D(dx = dx, dy = dy, nx = nx, ny = ny)

Construct a 'distanceVariable' object. This object is required by the
distanceEquation in order to solve.

   >>> from fipy.models.levelSet.distanceFunction.distanceVariable import DistanceVariable
   >>> var = DistanceVariable(
   ...     name = 'level set variable',
   ...     mesh = mesh,
   ...     value = -1.)

The positive and negative parts of the domain must be set.

   >>> positiveCells = mesh.getCells(filter = lambda cell: cell.getCenter()[0] < L / 2.)
   >>> var.setValue(1.,positiveCells)

A distanceEquation is constructed.

   >>> from fipy.models.levelSet.distanceFunction.distanceEquation import DistanceEquation
   >>> eqn = DistanceEquation(var)

The problem can be executed with the following commands.

   >>> if __name__ == '__main__':
   ...     from fipy.viewers.grid2DGistViewer import Grid2DGistViewer
   ...     viewer = Grid2DGistViewer(var = var, palette = 'rainbow.gp', minVal = -5., maxVal = 5.)
   ...     viewer.plot()
   ...     eqn.solve()
   ...     viewer.plot()

The result can be tested.

   >>> eqn.solve()
   >>> import Numeric
   >>> Numeric.allclose(var, \\
   ...     Numeric.array((9. * dx / 2., 7. * dx / 2., 5. * dx / 2., 
   ...     3. * dx / 2., dx / 2., -dx / 2., -3. * dx / 2., -5. * dx / 2., 
   ...     -7. * dx / 2., -9. * dx / 2.)))
   1


"""
__docformat__ = 'restructuredtext'

if __name__ == '__main__':
    import fipy.tests.doctestPlus
    exec(fipy.tests.doctestPlus.getScript())
    raw_input("finished")
