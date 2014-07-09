spparks-demo
============

`spparks-demo` is a tutorial for getting started with using [SPPARKS](http://spparks.sandia.gov) for microstructural science.
SPPARKS is an open source Unix-style command line application developed at [SANDIA National Labs](http://www.sandia.gov) for mesoscale materials modeling. 

This demo is a part of the [2014 Materials Science workshop on methods for 3D microstuctural studies](http://www.materials.cmu.edu/news/summerworkshop.html) at Carnegie Mellon University.
The demo briefly covers the design and capabilities of SPPARKS, and focuses on how to use SPPARKS for simulating grain growth in polycrystalline materials.
This includes compiling SPPARKS from the source code, writing and running simulation scripts, grain growth kinetics, and visualizing simulation data with [pizza.py](http://pizza.sandia.gov) and [ParaView](http://www.paraview.org).

software requirements
---------------------
To follow along with all of the interactive demos, you'll need some software and a Unix-like operating system (and a terminal app).
If you use Windows, I won't be able to help you with compiling SPPARKS, but you can try using [cygwin](https://www.cygwin.com), or use linux in a VM with [virtualbox](https://www.virtualbox.org).

If you aren't familiar with using a Unix shell, don't worry: you can (mostly) copy-and-paste all the commands from the slides, so this is your chance to learn :)

Compilation of (the serial version of) SPPARKS will be covered during the demo session, but if you want to be able to run the parallel version of SPPARKS, it's recommended that you [try to install SPPARKS beforehand](http://spparks.sandia.gov/doc/Section_start.html) (configuring SPPARKS with MPI can be tricky).

### essentials
- Terminal app
- C++ compiler and GNU build tools (included in the Apple Dev. tools)
- `SPPARKS` [Kinetic Monte Carlo framework from SANDIA](http://http://www.sandia.gov/~sjplimp/download.html)

### required for parallel SPPARKS
- `MPI` message passing library (suggested: use a package manager such as Macports or Homebrew to install [MPICH](http://www.mpich.org) or [openmpi](http://www.open-mpi.org))

### required for the visualization demo
<!--- relevant pizza.py files included in demo/visualization for simplicity...
- `pizza.py` [pre/post-processing toolkit from SANDIA](http://http://www.sandia.gov/~sjplimp/download.html)
   -->
- `ParaView` [visualization software](http://www.paraview.org)

### optional
- `matplotlib` (optional) python plotting library. Excel will work too.
