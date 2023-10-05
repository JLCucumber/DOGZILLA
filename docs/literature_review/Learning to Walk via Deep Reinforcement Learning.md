## Learning to Walk via Deep Reinforcement Learning

https://arxiv.org/abs/1812.11103

Deep reinforcement learning (deep RL) holds the promise of automating the acquisition of complex controllers that can **map sensory inputs directly to low-level actions.** (End-to-End)

But it is really difficult to apply in the real world: **poor sample complexity** & **sensitivity to hyperparameters**

In this paper, we propose a sample-efficient deep RL algorithm based on maximum entropy RL that requires minimal per-task tuning and only a modest number of trials to learn neural network policies.

[results] Our method can acquire **a stable gait** from scratch directly in the real world in about two hours, without relying on any model or simulation, and **the resulting policy is robust to moderate variations in the environment.**
