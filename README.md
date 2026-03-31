# My First Intelligent Contract by Rokon

Beginner-friendly Intelligent Contract for GenLayer.

This is the example contract used in my tutorial **"From Zero to GenLayer: Build Your First Intelligent Contract"**.

## Contract Features
- AI generates fun topics using `create_topic()`
- On-chain XP tracking system
- Simple view functions to read data
- Uses `gl.eq_principle.strict_eq` for Optimistic Democracy consensus

## How to Use
1. Import this contract in GenLayer Studio:
   https://studio.genlayer.com/contracts?import-contract=0xb438FB85B4F1d5D928d3049AbA1a7EC760ac4D65

2. Call `create_topic()` → AI will generate a new fun topic
3. Use `add_xp(amount)` to give points
4. Check topic with `get_topic(topic_id)`
5. Check your XP with `get_my_xp()`

**Contract Address:**  
`0xb438FB85B4F1d5D928d3049AbA1a7EC760ac4D65`

**Full Tutorial:**  
https://x.com/Rokon_Islam58/status/2038659907441049655

This contract is part of my beginner tutorial to help new builders understand Intelligent Contracts on GenLayer.

Built by Rokon
