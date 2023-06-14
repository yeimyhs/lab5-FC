import sympy


# Configuración de impresión con LaTeX
sympy.init_printing(use_latex="mathjax")


# Definición de variables simbólicas
x, y, z, u = sympy.symbols("x y z u")
p, rho, g, h = sympy.symbols("p rho g h")
p0, z0, u0 = sympy.symbols("p0 z0 u0")  # Se agregan las variables faltantes p0, z0, u0


# Ecuación de Bernoulli
eq = sympy.Eq(p/rho + g*z + 0.5*rho*u**2, p0/rho + g*z0 + 0.5*rho*u0**2 + h)  # Se corrige la ecuación de Bernoulli


# Solución de la ecuación de Bernoulli
sol = sympy.solve(eq, u)


# Impresión de la solución
print("Solución de la ecuación de Bernoulli:")
sympy.pprint(sol)
