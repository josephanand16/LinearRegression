# Linear Regression
A simple code to explain regression

## Terms and their meanings:
### Covariance : 
#### Covariance is a measure of the joint variability of two random variables
### Variance : 
#### Variance is the expectation of the squared deviation of a random variable from its mean
### Mean :
#### The mean is the average of all numbers
### Slope :
#### The slope or gradient of a line is a number that describes both the direction and the steepness of the line
### Intercept :
#### The point where the line touches the 'Y' axis.

### The problem to be solved: Probabilistic data to be represented as a deterministic equation.
#### Linear regression addresses the above problem. We can represent probabilitic data as a deterministic equation. The output is based on the statistical information of the dependent and Independent variables.

### How do you determine the function.
#### 1. First find the mean of dependent and Independent variables.
#### 2. Calculate the error function
Q = sum(intercept + slope*xcap(i))
#### 3. For the most optimal solution. partial derivative of Q with respect to slope and intercept should be close to zero.
#### 4. Solving for slope, it can be observed that slope = Covariance(X,Y)/Variance(X^2)
#### 5. Also from the solution, the mean passes through the line.
#### 6. Therefore substituting the mean values along with slope gives the intercept value.

### The output of a Linear regression function which will be printed by the python script when run.
![A regression Equation](regression.jpg)
