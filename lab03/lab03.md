# Prompt Engineering Process

### Step 1
#### Intention
>What is the improvement that you intend to make?\
I wanted to make the agent greet the user rather than just saying "Lets Begin". I will try to do this by prompting the agent at the begining to "Kindly greet the user to open the conversation".

#### Action/Change
>Why do you think this action/change will improve the agent?\
I think this will improve the agent because it forces it to make opening message a greeting instead of making the user begin the interaction. 

#### Result
>What was the result?\
This worked well, the agent opened the conversation with "Hello! Welcome to the conversation. I'm here to listen and help you express yourself. What's on your mind today?"

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?\
I think it worked because the system prompt was read by the agent before it first responsed, so it knew to greet the user on the first message. 


### Step 2
#### Intention
>What is the improvement that you intend to make?\
I want to make the agent more personable. For example, in the last chat the agent started with "welcome to the conversation," which I don't think a human would normally say when opening a conversation. To make this improvement I will increase the temperature to 0.65.

#### Action/Change
>Why do you think this action/change will improve the agent?\
I think this action will improve the agent beacause it will allow the agent to be more creative with its answers. 

#### Result
>What was the result?\
I feel like this worked well, the agent opened the conversation with "Hello! How can I help you today?" which definitly has more personality. I did have to modify the prompt to the system to make sure that the agent doesn't respond with emojis because it was causing an error.

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?\
This works because increasing the temperature because it increases the randomness of the tokens, which allows for more outcomes.


### Step 3
#### Intention
>What is the improvement that you intend to make?\
Sometimes the agent wouldn't continue the conversation and just respond to questions I had. I want to make sure that the agent always continues the conversation. Also, I want to add clearer instructions to make sure that it knew that it was not supposed to respond with emojis. 

#### Action/Change
>Why do you think this action/change will improve the agent?\
I think this action will improve the agent beacause it makes sure that the conversation doesn't stop until /exit is typed. 

#### Result
>What was the result?\
This worked well because it made sure that the agent either asked a question or made a comment about what they typed, so the conversation would continue no matter what the user says.

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?\
This worked because it gives specific instructions to ask a question or comment. However, the agent sometimes still responds with emojis.

### Step 4
#### Intention
>What is the improvement that you intend to make?\
I want to add clearer instructions to make sure that it knows that it isn't supposed to respond with emojis. Also, I will decrease the temperature to 0.60

#### Action/Change
>Why do you think this action/change will improve the agent?\
I think this change will improve the agent beacause it will make the instructions more simple, so the agent will have an easier time trying to understand them. 

#### Result
>What was the result?\
It works because now it doesn't use emojis.

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?\
I think making the instructions less verbose helped because it makes sure the agent focuses on the important parts of the instructions.