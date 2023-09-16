# -*- coding: utf-8 -*-
"""USI_ML_22_Assignment_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uFPawpotuO2M75xx-KkuxGjfVUWbs0XD

# Machine Learning 2022/2023
## Assignment 5
Deadline: 23:59 on the 23th of December, 2022

First name: Ariola

Last name: Leka

## About this assignment

In this assignment you will further deepen your understanding of Reinforcement Learning (RL).

## Submission instructions

Please write your answers, equations, and code directly in this python notebook and print the final result to pdf (File > Print). Make sure that code has appropriate line breaks such that all code is visible in the final pdf. If necessary, select A3 for the PDF size to prevent content from being clipped.

The final pdf must be named name.lastname.pdf and uploaded to the iCorsi website before the deadline expires. Late submissions will result in 0 points.

**Also share this notebook (top right corner 'Share') with teaching.idsia@gmail.com during submission.**

**Keep your answers brief and respect the sentence limits in each question (answers exceeding the limit are not taken into account)**.

Note that there are a total of **50 points in this assignment**.

Learn more about python notebooks and formatting here: https://colab.research.google.com/notebooks/welcome.ipynb

## How to get help

We encourage you to ask questions or to discuss exercises with other students. However, do not look at any code written by others or share your code with others. Violation of that rule is considered plagiarism and can result in various penalties, most commonly a grade of 0 for the course.

For questions on this assignment, you can contact the responsible TA at dylan.ashley@idsia.ch

### Question 1 (20p)

Consider a 4x4 gridworld depicted in the following table:

![Grid world](https://i.ibb.co/HdSdKJB/image.png)

The non-terminal states are $S = \{1, 2, \ldots, 14\}$ and the terminal states are $0, 15$. There are four available actions for each state, that is $A = \{\text{up}, \text{down}, \text{left}, \text{right}\}$. Assume the state transitions are deterministic and all transitions result in a negative reward −1. If the agent hits the boundary, then its state will remain unchanged, e.g. $p(s=8, r=−1|s=8, a=\text{left}) = 1$.

Implement the environment as described in the code skeleton below.
Come up with your own solution and do not copy the code from a third party source.

Then test your implementation of GridWorld using the implementation of policy iteration provided below. Run the code multiple times. Do you always end up with the same policy? Why? (max 4 sentences)

---

**ANSWER HERE**

The answer is yes I end up having the same policy each time we run the code. The reason why this happens according to my oppinion is that the model ends up converging to the best(optimal) policy. So, every time we run it the model is learning and returning the same optimal policy and running multiple time would not change it.

#### Imports
"""

import numpy as np
import itertools

np.set_printoptions(precision=3, linewidth=180)

"""#### Defining the problem"""

class GridWorld:

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, side=4):
        self.side = side
        # -------------------------
        # Define integer states, actions, and final states as specified
        # in the problem description

        # TODO insert code here
        self.actions = [self.UP, self.DOWN, self.LEFT, self.RIGHT]
        self.states = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # we have a 4x4 grid so 16 states from 0-15

        self.finals = [0,15] #the two states where we terminate as stated in the description

        # -------------------------
        self.actions_repr = np.array(['↑', '↓', '←', '→'])

    def _is_terminal(self, s):
        # -------------------------
        # Return True if s is a terminal state and False otherwise

        # TODO insert code here

        if s in self.finals:
          return True
        else:
          return False

        # -------------------------

    def _next_state(self, s, a):
        # -------------------------
        # Deterministically returns the next state of the environment if action a were
        # taken while in state

        # TODO insert code here
        if s in self.finals: #is you are in one of the final states you just return the state
          return s
        elif a == self.UP:
          return s if s - 4 < 0 else s - 4 # if we are higher that 4 we can go up
        elif a == self.DOWN:
          return s if s + 4 > 15 else s + 4 # if we are at a state smaller than 12 we can go down
        elif a == self.LEFT:
          return s if s in [0, 4, 8, 12] else s - 1 #unless we are at states 4,8,12 we can go left since htese are in the border
        elif a == self.RIGHT:
          return s if s in [3, 7, 11, 15] else s + 1 #unless we are at states 3,7,11 we can go right since these are in the border

        # -------------------------

    def _reward(self, s, s_next, a):
        # -------------------------
        # Return the reward for the given transition as specified
        # in the problem description

        # TODO insert code here
        if s_next in self.finals: #if the state we are is one of the final states we return 0 otherwise we give a reward of 1
          return 0
        return -1

        # -------------------------

    def reset(self):
        # -------------------------
        # Set the internal state of the environment to be sampled uniformly
        # at random from the set of non-terminal states and return the state

        # TODO insert code here
        non_terminal_states = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]# all the states that are not terminal (internal)
        self.s = np.random.choice(non_terminal_states) #randomly chose between the internal states
        return self.s
        # -------------------------

    def step(self, a):
        # -------------------------
        # Advances the environment one step using action a and returns s, r, T
        # where s is the next state, r is the reward, and T is a boolean saying
        # whether the episode is done or not

        # TODO insert code here
        state_next = self._next_state(self.s, a) # put the next state as the next state of state s when you take action a
        r = self._reward(self.s, state_next, a) # set the reward you take for moving from state s to state next after taking action a
        T = self._is_terminal(state_next) #check if the state we finish in is a terminal state
        self.s = state_next #update the state
        return state_next, r, T
        # -------------------------

    def print_policy(self, policy):
        P = np.array(policy).reshape(self.side, self.side)
        print(self.actions_repr[P])

    def print_values(self, values):
        V = np.array(values).reshape(self.side, self.side)
        print(V)

"""#### Policy iteration"""

def transition_prob(s, s_next, a):
    return 1 if problem._next_state(s, a) == s_next else 0


def eval_policy(problem, policy, value, gamma=0.9, theta=0.01):
    p = transition_prob
    r = problem._reward

    while True:
        delta = 0
        for s in problem.states:
            v = value[s]
            value[s] = np.sum(
                [
                    p(s, next_s, policy[s])
                    * (r(s, next_s, policy[s]) + gamma * value[next_s])
                    for next_s in problem.states
                ]
            )
            delta = max(delta, abs(v - value[s]))

        if delta < theta:
            return value


def improve_policy(problem, policy, value, gamma=0.9):
    p = transition_prob
    r = problem._reward

    stable = True
    for s in problem.states:
        actions = problem.actions

        b = policy[s]
        policy[s] = actions[
            np.argmax(
                [
                    np.sum(
                        [
                            p(s, next_s, a) * (r(s, next_s, a) + gamma * value[next_s])
                            for next_s in problem.states
                        ]
                    )
                    for a in actions
                ]
            )
        ]
        if b != policy[s]:
            stable = False

    return stable


def policy_iteration(problem, gamma=0.9, theta=0.01):
    # Initialize a random policy
    policy = np.array([np.random.choice(problem.actions) for s in problem.states])
    print("Initial policy")
    problem.print_policy(policy)
    # Initialize values to zero
    values = np.zeros_like(problem.states, dtype=np.float32)

    # Run policy iteration
    stable = False
    for i in itertools.count():
        print(f"Iteration {i}")
        values = eval_policy(problem, policy, values, gamma, theta)
        problem.print_values(values)
        stable = improve_policy(problem, policy, values, gamma)
        problem.print_policy(policy)
        if stable:
            break

    return policy, values

# Run the below code, please include the output in your submission
problem = GridWorld()
policy_iteration(problem, gamma=0.5)

"""### Question 2 (10p)

Let's run policy iteration with $\gamma = 1$. Describe what is happening. Why is this the case? Give an example. What is $\gamma$ trading off and how does it affect policy iteration? (max 8 sentences)

---

**ANSWER HERE**

If we run with a γ = 1 we und up on running infinitely in iteration 0. After taking information on internet what γ does is it decides how much weight goes to the future rewaards. And if this γ = 1 this mean all future rewards are given a weight of 1. At this point the algorithm might not want to risk and tek a step that send him to finish state, consequentively it runs forever. On the other side when γ is smaller than 1 the algorithm is willing to take a risk and continue exploring to find the final state.  

The knowledge for this answer were taken in the following page:
https://towardsdatascience.com/practical-reinforcement-learning-02-getting-started-with-q-learning-582f63e4acd9#:~:text=gamma%20is%20the%20discount%20factor,to%20consider%20only%20immediate%20rewards.

"""

# policy_iteration(problem, gamma=1.0) I am commenting this because each time i was running it it was stopping my code.

"""### Question 3 (20p)

Implement Q-learning using the code skeleton below. Come up with your own solution and do not copy the code from a third party source. Then execute the block to show that your solution reached when $\gamma = 0.5$ is optimal.
"""

problem = GridWorld()
GAMMA = 0.5
sa_values = np.zeros((len(problem.states), len(problem.actions)), dtype=float)
#print(sa_values.shape)

def epsilon_greedy(a_values, epsilon):
    # -------------------------
    # This function takes a list a_values where each index i corresponds
    # to an estimate of the value of action i and then performs
    # epsilon-greedy action selection to sample and return an action
    # https://www.geeksforgeeks.org/epsilon-greedy-algorithm-in-reinforcement-learning/ this page helped me understand better epsilon-greegy action

    # TODO insert code here

    possible_actions = list(range(len(a_values))) #is a list of the possible actions beeing [0,1,2,3]

    if np.random.random() < epsilon:    # Epsilon-Greedy is a simple method to balance exploration and exploitation by choosing between exploration and exploitation randomly.
      action = np.random.choice(possible_actions)
    else:
      action = np.argmax(a_values)
    return action



for i in range(10000): #the range was too high end it was never ending the loop that is why i decreased it
    s = problem.reset()
    done = False
    while not done:

        # Perform one step of Q-learning here using sa_values to store
        # the action-value estimates and epsilon_greedy to perform the
        # action selection
        #
        # Play around to find a good step size

        # TODO insert code here
        s = problem.s

        epsilon = 0.6 #with epsilon = 0.1 always explores never exploites
        action = epsilon_greedy(sa_values[s], epsilon) # the action-value estimates and epsilon_greedy to perform the action selection
        s_next, r, done = problem.step(action)
        sa_values[s][action] = sa_values[s][action] + 0.1 * (r + GAMMA * np.max(sa_values[s_next]) - sa_values[s][action]) #Bellman Equation for Q-learning
        #s=s_next
        problem.s = s_next # we update the state with the next state



optimal_policy_state_values = policy_iteration(problem, gamma=0.5)[1]
learned_policy_state_values = np.max(sa_values, axis=1)

print('Optimal Policy State Values:')
print(optimal_policy_state_values)
print('Learned Policy State Values:')
print(learned_policy_state_values)
print('Root Mean Squared Value Error: {0:.18f}'.format(
    np.sqrt(np.mean(np.square(optimal_policy_state_values - learned_policy_state_values)))))