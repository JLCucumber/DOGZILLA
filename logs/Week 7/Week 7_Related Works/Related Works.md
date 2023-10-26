# RL List

**Useful Links**

1. https://github.com/curieuxjy/Awesome_Quadrupedal_Robots

   

> **RL-based quadrupedal robots**
>
> 1. Learning quadrupedal locomotion over challenging terrain
> 2. Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild
>
> **Model-Free RL Methods**
>
> 1. Learning to Walk in Minutes Using Massively Parallel DRL. CoRL 2022
>
>    利用NVIDIA设计的并行仿真环境，可以支持数千个机器人同时的在线训练，从而在很短的时间内学习到稳定的策略，并通过sim-to-real将策略迁移到真实的环境中。
>
> 2. Walk These Ways: Gait-conditioned Policies Yield Diversified Quadrupedal Agility. CoRL 2022
>
> **Model-based RL Methods**
>
> 1. DayDreamer: World Models for Physical Robot Learning. CoRL 2022
>
> **Vision-based RL Methods**
>
> 1. Legged Locomotion in Challenging Terrains using Egocentric Vision. CoRL 2022 Oral
> 2. Coupling Vision and Proprioception for Navigation of Legged Robots. CVPR 2022
> 3. Visual-Locomotion: Learning to Walk on Complex Terrains with Vision. CoRL 2021
>
> **Sim-to-Real / Generalizations / Imitations**
>
> 1. GenLoco: Generalized Locomotion Controllers for Quadrupedal Robots. CoRL 2022
>
>    该文章研究四足机器人策略在不同机型之间的泛化问题，其目的是训练单个策略，使其能够同时适用于多种不同的机型，具体包括Unitree’s A1, Go1, Aliengo, Laikago, MIT’s Mini Cheetah, CUHK’s Sirius, and Boston Dynamics’ Spot 等。文章的 motivation 包括：
>
>    - 现有的基于强化学习的四足机器人策略需要在特定的机型上面进行训练，随后迁移到该机型。当四足机器人的种类改变时，策略就无法直接进行适用。
>    - 然而，我们需要一个通用的策略，使其能够在不同的机型上面进行使用，同时应该能够泛化到一些具有相似形态学的四足机器人上，如下图所示。
>
> 2. Learning Semantics-Aware Locomotion Skills from Human Demonstration. CoRL 2022
>
> 
>



