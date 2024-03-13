import numpy as np
import matplotlib.pyplot as plt
import PSO

# testitron
# this code is from the matlab version converted into python
def ackley(xx):
    a = 20
    b = 0.2
    c = 2*np.pi
    d = len(xx)
    
    sum1 = np.sum(xx**2, axis=0)
    sum2 = np.sum(np.cos(c * xx), axis=0)
    
    term1 = -a * np.exp(-b * np.sqrt(sum1 / d))
    term2 = -np.exp(sum2 / d)
    
    return term1 + term2 + a + np.exp(1)

# got some help online for plotting this https://stackoverflow.com/questions/53041175/add-contour-plot-to-surface-plot-in-r
# Generate data for plotting
x = np.linspace(-32.768, 32.768, 100)
y = np.linspace(-32.768, 32.768, 100)
X, Y = np.meshgrid(x, y)
Z = ackley(np.array([X, Y]))

# Plotting Ackley function
fig = plt.figure(figsize=(12, 6))

# Plotting the 3D surface plot of Ackley function
ax1 = fig.add_subplot(111, projection='3d')
# https://matplotlib.org/stable/users/explain/colors/colormaps.html
surf = ax1.plot_surface(X, Y, Z, cmap='twilight', alpha = 0.6)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Ackley Function')

# Particle Swarm Optimization
S = 20
particles = []

# create all the particles
for s in range(S):
    x = np.random.uniform(-32.768, 32.768, 2)  # Ensure particles are within the range of the function
    v = np.random.uniform(-np.abs(-32.768-0), np.abs(-32.768-0), 2)
    # call the particle constructor and append the list
    particles.append(PSO.Particle(x, v, 0.8, 0.1, 0.1))  # values for phi and w are given

particle = PSO.Particle
g = particles[0].x.copy()

positionVals = []
n = 0
while n < 20:
    for particle in particles:
        particle.updateVelocity(g)
        particle.updatePosition()
        particle.updateValue()
        if particle.value < PSO.f(g):
            g = particle.x.copy()
            positionVals.append(g)

    # Plotting particles' positions at each iteration
    for particle in particles:
        ax1.plot([particle.x[0]], [particle.x[1]], [PSO.f(particle.x)], "k*")
    n += 1

plt.show()

print("The PSO flocked towards", positionVals[-1])
print("The PSO started at", positionVals[0])
print("This finds the minimum point and from the graph it is centered around (0,0).")
