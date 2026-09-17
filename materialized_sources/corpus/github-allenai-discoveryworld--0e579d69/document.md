# Repository semantic capsule: allenai/discoveryworld

- Commit: `fd591323920be0d3786ef350955de1945aa571e5`
- Default branch: `main`
- Description: allenai/discoveryworld
- Selected evidence files: 1 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# DiscoveryWorld: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents
NeurIPS Datasets and Benchmarks 2024 (Spotlight)

![discoveryworld](doc/discoveryworld-logo.png)

## Example Agent Video
Below is a short 60 second clip of one of the baseline agents *(Hypothesizer)* attempting a task (Proteomics, Normal Difficulty, Seed 0).  For comparison, a narrated walkthrough of a human playing this same scenario is available on [Youtube](https://www.youtube.com/watch?v=hKWd-pwF0_E).

![discoveryworld-video](doc/output_hypothesizer_agent.Proteomics-Normal-s0-imagesTrue-modelgpt-4o-thread2007.20240525-142057-first60sec.gif)

## 1. Quick Start

### 1.1. I want to read about DiscoveryWorld
The DiscoveryWorld paper (NeurIPS 2024, Spotlight) is available here: [https://openreview.net/forum?id=cDYqckEt6d](https://openreview.net/forum?id=cDYqckEt6d)

A short summary is also available on the [project website](https://allenai.github.io/discoveryworld/).

### 1.2. I want to play DiscoveryWorld using the graphical user interface intended for humans
Installing and running DiscoveryWorld is easy, and generally takes just a few minutes.  To run as a human, please follow the installation instructions in `Section 2` below.

*NOTE: The paper contains spoilers for the DiscoveryWorld tasks.  If you'd like to complete them as the human scientist participants did, without prior knowledge, we would recommend trying the tasks before reading the paper in detail.*

### 1.3. I want to make my own DiscoveryWorld agent, or examine the baseline agents.
The baseline agents are provided in `/agents`, with a special README intended to help you get started quickly, and callout helpful portions of the code that you might be interested in viewing or reusing:
https://github.com/allenai/discoveryworld/tree/main/agents

API documentation is provided below in `Section 3`.

### 1.4. I want to examine the raw data from the agent runs or human runs described in the paper, or see videos of agents playing DiscoveryWorld.
Links to full data releases, including instructions for downloading, as well as their format and other datacard information, is provided in `/data`:
https://github.com/allenai/discoveryworld/tree/main/data

A direct link to a limited archive containing only videos of the baseline agents playing DiscoveryWorld is [available here](https://drive.google.com/file/d/1I34EMVRUIIOppQFX3RueG4Nl75n8_zlJ/view?usp=drive_link).

### 1.5. I want to view the instructions provided to the human scientists when they played DiscoveryWorld.
Please find the instructions provided to the human scientists in `README-USERSTUDY.md`.

### 1.6. I want to see a human scientist playthrough of a DiscoveryWorld task.

Please find a narrated human playthrough of one of the shortest tasks, Proteomics (on Normal difficulty), [available on Youtube](https://www.youtube.com/watch?v=hKWd-pwF0_E).

## 2. Installation and Running

### 2.1. Installation

Clone this repository:
```
git clone https://github.com/allenai/discoveryworld.git
cd discoveryworld
```

Create a conda environment:
```
conda create --name discoveryworld python=3.9
conda activate discoveryworld
```

Install the dependencies:
```
pip install -r requirements.txt
pip install -e .
```


### 2.2. Running the Graphical User Interface

The graphical interface can be run with the following command from the `discoveryworld` root:
```
python scripts/userstudy.py
```

You should see a menu that allows you to select a given scenario theme, difficulty, and parametric seed, followed by the user interface:

![discoveryworld](doc/screenshot.png)


### 2.3. Controls

The following controls are supported:
* **Arrow keys for movement:** `left/right` keys rotate the agent, `up/down` move forward/backward
* **Arguments:** The objects the agent interacts with are specified by the argument boxes, at the bottom. Use number keys to select specific inventory item of the top argument box, hold shift + number keys for the bottom argument box. Alternatively, `[` and `]` cycle the selection through the top argument box, and `;` and `'` for the bottom argument box.
* **TAB:** View the current task information.
* **Pick up object:** `Space` will attempt to pick up the object in `arg1`
* **Drop object:** `d` will drop the object in `arg1`
* **Put object in container:** `p` will attempt to put the object in `arg1` in the container in `arg2`
* **Give object to another character:** `p` will attempt to give the object in `arg1` to the character in `arg2`
* **Open/Close:** `o` and `c` will attempt to open/close `arg1`
* **Activate/Deactivate:** `a` and *`s`* will attempt to activate/deactivate `arg1`
* **Use:** `u` will attempt to use `arg1` on `arg2` (e.g. use shovel on soil)
* **Talk:** `t` will attempt to talk to the agent in `arg1`
* **Read:** `r` will read the object in `arg1`
* **Eat:** `e` will eat `arg1`
* **Wait:** `w` will do nothing.
* **DiscoveryFeed:** `v` will view the most recent posts on the Discovery Feed.
* **Help:** `?` or `F1` to display help message.
* **Quit:** `ESC` will exit.


### 2.4. Logging

The `userstudy.py` user interface saves extensive logs after each run, including the full game state at each step, the user actions, and frame captures of the game at each step (to assemble a video).  These are stored in the `logs` subdirectory.


## 3. API Documentation

### 3.1 Philosophy

The API is intended to closely resemble the `OpenAI Gym` API used by many virtual environments, including `TextWorld` and `ScienceWorld`.  The underlying philosophy and workflow of those APIs is:
1. Initialize the API and instantiate an environment
2. Have the agent get an `Observation` (i.e. what it sees at the current time step) from the environment
3. Have the agent provide it's current `Action` (i.e. what it chooses to do, like `eat apple`) at the current timestep
4. Continually repeat steps 3+4 until some exit condition is met, like completing the task, or reaching a maximum number of steps.

The API is described first through minimal agent examples, then through documentation for specific functions.

### 3.2. Minimal Example (Random Agent)

The *Random Baseline Agent*, which randomly selects an action to take at each time step in the environment, is provided as a minimal end-to-end example in the `/agents` folder.

### 3.3. Initializing the API and instantiating a specific world.

Initializing a scenario is performed using the `loadScenario()` function:

```
    api = DiscoveryWorldAPI(threadID=1)
    success = api.loadScenario(scenarioName = scenarioName, difficultyStr = difficultyStr, randomSeed = seed, numUserAgents = 1)
    if (success == False):
        print("Error: Could not load scenario '" + scenarioName + "' with difficulty '" + difficultyStr + "'.")
        return None
```

Note that while DiscoveryWorld was designed to support multiple user agents in a given scenario, this feature is currently untested, and as such `numUserAgents` is set to 1 above.

#### 3.3.1 Scenarios (Task Themes)

A list of recognized task themes can be found here:
```
from discoveryworld.ScenarioMaker import SCENARIO_NAMES
```

#### 3.3.2 Difficulties

A list of recognized difficulties is nominally `Easy`, `Normal`, and `Challenge`, though these can be imported programmatically here:
```
from discoveryworld.ScenarioMaker import SCENARIO_DIFFICULTY_OPTIONS
```

#### 3.3.3 Parametric Variation Seed

The seed is nominally a value between 0 and 4 (i.e. `0, 1, 2, 3, 4`).  Other higher values are possible, and should generate additional parametric variations of a given `{task theme, difficulty}` combination, but are officially outside of the benchmark and unsupported.

#### 3.3.4 Thread ID and Uniqueness

It's important that each concurrently running DiscoveryWorld be given it's own unique `threadID` during initialization.

Internally, the `threadID` is used to create unique output directories for storing the frames of each run.  If you don't wish to have the frames from one run overwritten by another, then your **threadID should be unique across all runs**.

### 3.4. Observation

Observations are provided from the `getAgentObservation()` function, for example:
```
observation = api.getAgentObservation(agentIdx=0)
```

Observations contain the following keys within the `ui` dictionary (in alphabetical order), which can typically be provided directly to an LLM that's able to read JSON-formatted input:
- `accessibleEnvironmentObjects`: A list of objects (and their UUIDs and descriptions) that are close enough to the agent to interact with.
- `agentLocation`: The agent's current world location, the direction it's facing, directions it can move to, and directions that are blocked (nominally, by big objects, like walls).
- `dialog_box`: Information about whether the agent is currently in dialog or not
- `discoveryFeed`: Information about the most recent DiscoveryFeed posts (a Twitter-like environment internal to DiscoveryWorld, and used for some scenarios)
- `extended_action_message`: (Rarely used) This may contain information from text boxes that are provided to the user.
- `inventoryObjects`: A list of objects in the agent's inventory
- `lastActionMessage`: The plain text result of the last action (e.g. `You successfull moved to (16, 5)`).  This is generally identical to the text that the user would see at the bottom of the screen after performing an action.
- `nearbyAgents`: This section lists the recent action history (i.e. within the last few steps) of any agents that are nearby. This can help you understand what other agents are doing, and what they might be planning to do.
- `nearbyObjects`: This section lists objects that are near the agent (i.e. within 3 tiles), including their names, UUIDs, descriptions, and distances.  They are sorted into directions (`north, east, south, west, north-east, north-west, south-east, south-west`) as well as those on the same tile that the agent is standing (`same_location`).  This tends to be, by a wide margin, the largest part of the observation.
- `taskProgress`: Contains the current task description, and whether or not it has been completed.  Critically, no other fine-grained score information (such as the score or subtasks from the scorecard) is available to the agent.
- `world_steps`: The step counter from the environment

For models that can make use of visual information, two images are provided under the `vision` key, encoded in `base64` (that models such as e.g. GPT-4o can use):
- `base64_no_grid`: The 16x24 tile observation of the environment, typically identical to what would be shown in the user interface.
- `base64_with_grid`: As above, but with the grid outline provided.

In addition, an `errors` key is provided in the dictionary, which is empty in normal operation.  If errors are encountered, this may provide helpful additional information.

An example observation return can be found here, for the Dialog unit test:
https://github.com/allenai/discoveryworld/blob/main/doc/example-observation.json


### 3.5. Actions

Actions are performed with the `performAgentAction()` function, which is similar to the `step()` function in the OpenAI Gym API.
```
# Assemble an action packet
actionName = "USE"
actionCommand = {
   "action": actionName,
   "arg1": None,
   "arg2": None
}

# Arguments are the UUIDs of specific objects.  These typically come from the `uuid` field of an object found in the observation
# Here we'll just assume `accessibleObjects` is a list of nearby and accessible objects, taken from the observation, and
# randomly pick two objects from it to serve as arguments.
obj1 = r.choice(accessibleObjects)
actionCommand[arg1] = obj1["uuid"]
obj2 = r.choice(accessibleObjects)
actionCommand[arg1] = obj2["uuid"]

# Perform the action
result = api.performAgentAction(agentIdx=0, actionJSON=actionCommand)
```

#### 3.5.1. What actions are available?

A list of available actions (and, what arguments they expect) is provided through the `listKnownActions()` function.  These actions are specifically formatted such that they can be provided directly in the prompt to LLMs that can read JSON, such as GPT4:
```
actionDescriptions = {
    ActionType.PICKUP.name:         {"args": ["arg1"], "desc": "pick up an object (arg1)"},
    ActionType.DROP.name:           {"args": ["arg1"], "desc": "drop an object (arg1)"},
    ActionType.PUT.name:            {"args": ["arg1", "arg2"], "desc": "put an object (arg1) in/on another object (arg2), or give an object (arg1) to another agent (arg2)"},
    ActionType.OPEN.name:           {"args": ["arg1"], "desc": "open an object (arg1)"},
