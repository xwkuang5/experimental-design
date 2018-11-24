# Experimental Design

A simple tool to calculate the number of conditions, the minimum number of participants and the arrangement of conditions in a controlled experiment.

## Getting started

Clone the repository to your local machine and start using!
```
git clone https://github.com/xwkuang5/experimental-design
```

## Usage

The program takes as input a configuration file (explained later) and optionally an output filename for exporting the parsed experimental design.

```
python app.py <input_config> --out <output_filename>
```

### Input Configuration (JSON)

The input configuration file has the following format:
```
{
  "independentVariables": {
    "<VariableName>": {
      "levels": [<level1>, <level2>, ..., <levelN>],
      "design": <design_type>,
      "order": <order_type>
    },
    ...
  },
  "availableTasks": {
    <TaskName>: {
      "repeatable": <boolean>
    }
  }
}
```

#### Design Type

The design of a variable can take on one of the following two types:

1. `between_subject`: each participant only goes through one of the levels of the variable
2. `within_subject`: each participant goes through all the levels of the variable

#### Order Type

The order of a variable determines how it will be counterbalanced in the experiment. The following values are possible

1. `sequential`: the variable will not be counterbalanced.
2. `latin_square`: the variable will be counterbalanced using a latin square.
3. `balanced_latin_square`: the variable will be countebalanced using a balanced latin square
4. `fully_counter_balanced`: the variable will be counterbalanced using all possible permutations of the levels.

#### Available tasks
Each task is associated with an attribute `repeatable`, if a task is repeatable, then it will be used repeatedly for all conditions. On the other hand, if a task is not repeatable, then it will only be used once in all the conditions for one participant.

### Example
Suppose we have the following input configuration file `input_config.json`
```json
{
    "independentVariables": {
        "phone": {
            "levels": ["iphone", "huawei", "samsung"],
            "design": "between_subject"
        },
        "browser": {
            "levels": ["safari", "chrome", "IE"],
            "design": "within_subject",
            "order": "latin_square"
        }
    },
    "availableTasks": {
        "findPresidentOfUS": {
            "repeatable": true
        }
    }
}
```

Running the command 
```
python app.py input_config.json --out output_config.json
```
produces the output configuration `output_config.json` with the following content
```json
{
  "minimumNumberOfParticipants": 9, 
  "numberOfConditionsPerParticipant": 3, 
  "arrangements": [
      ["phone::iphone", [["browser::safari"], ["browser::chrome"], ["browser::IE"]]], 
      ["phone::iphone", [["browser::chrome"], ["browser::IE"], ["browser::safari"]]], 
      ["phone::iphone", [["browser::IE"], ["browser::safari"], ["browser::chrome"]]], 
      ["phone::huawei", [["browser::safari"], ["browser::chrome"], ["browser::IE"]]], 
      ["phone::huawei", [["browser::chrome"], ["browser::IE"], ["browser::safari"]]], 
      ["phone::huawei", [["browser::IE"], ["browser::safari"], ["browser::chrome"]]], 
      ["phone::samsung", [["browser::safari"], ["browser::chrome"], ["browser::IE"]]], 
      ["phone::samsung", [["browser::chrome"], ["browser::IE"], ["browser::safari"]]], 
      ["phone::samsung", [["browser::IE"], ["browser::safari"], ["browser::chrome"]]]
  ]
}
```

For more examples, look at the test cases in `root/tests`

## Todo
* Add implementation for non-repeatable tasks (should tasks also be counter-balanced then?)
* Add visualization of arrangements (tree, etc)